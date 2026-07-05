import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List

from src.config import Settings
from src.backends import get_backend
from src.pipeline.prompt_renderer import PromptRenderer
from src.pipeline.context_manager import ContextManager

# For dependencies.toml parsing
try:
    import tomllib  # Python 3.11+
except ImportError:  # Fall back to 'toml' package if installed
    try:
        import toml as tomllib  # type: ignore
    except ImportError:
        tomllib = None  # We'll handle this gracefully below


# ------------------------------------------------------------
# Step loading (P* then I* then F*), from prompts/P, prompts/I, prompts/F
# ------------------------------------------------------------
def load_steps(prompt_dir: Path):
    """
    Load P*, I*, and F* templates in lexicographic order.

    P-prompts run first (content), then I-prompts (single-language
    interpretation), then F-prompts (formatting).
    All prompts must be .j2 Jinja templates.
    """
    p_steps = sorted(prompt_dir.joinpath("P").glob("P*.j2"))
    i_steps = sorted(prompt_dir.joinpath("I").glob("I*.j2"))
    f_steps = sorted(prompt_dir.joinpath("F").glob("F*.j2"))

    steps = []

    for file in p_steps:
        steps.append({
            "file": file,
            "code": file.stem,   # e.g. "P1_vocab"
            "kind": "content",
            "phase": "P",
        })

    for file in i_steps:
        steps.append({
            "file": file,
            "code": file.stem,   # e.g. "I1_construction_equivalence"
            "kind": "interpret",
            "phase": "I",
        })

    for file in f_steps:
        steps.append({
            "file": file,
            "code": file.stem,   # e.g. "F1_vocab_table"
            "kind": "format",
            "phase": "F",
        })

    return steps


# ------------------------------------------------------------
# Dependency loading
# ------------------------------------------------------------
def load_dependencies(dep_path: Path) -> Dict[str, List[str]]:
    """
    Load dependencies.toml into a dict:
        { "P2_derivations": ["P1_vocab"], ... }

    If the file is missing or tomllib is unavailable, we just
    return an empty dict and steps will get no prior context.
    """
    if not dep_path.exists():
        return {}

    if tomllib is None:
        print("⚠️  dependencies.toml found but no TOML parser available. "
              "Install 'toml' or use Python 3.11+ for tomllib.")
        return {}

    with dep_path.open("rb") as fh:
        data = tomllib.load(fh)

    deps: Dict[str, List[str]] = {}
    for step_code, spec in data.items():
        if isinstance(spec, dict):
            lst = spec.get("depends_on", [])
            if isinstance(lst, list):
                deps[step_code] = [str(x) for x in lst]
    return deps


# ------------------------------------------------------------
# Metadata writer (now using timezone-aware UTC)
# ------------------------------------------------------------
def _json_default(obj):
    """
    Convert SDK-specific objects (e.g., usage structs) into JSON-friendly values.
    """
    for attr in ("model_dump", "dict", "to_dict"):
        if hasattr(obj, attr):
            method = getattr(obj, attr)
            try:
                return method()
            except TypeError:
                return method(obj)

    if hasattr(obj, "__dict__"):
        return {
            key: value
            for key, value in vars(obj).items()
            if not key.startswith("_")
        }

    return str(obj)


def write_metadata(meta_path: Path, backend_response, prompt_text: str):
    metadata = backend_response.metadata or {}
    meta = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "prompt": prompt_text,
        "model": metadata.get("model"),
        "backend": metadata.get("backend"),
        "temperature": metadata.get("temperature"),
        "usage": metadata.get("usage"),
        "raw_metadata": metadata,
    }
    meta_path.write_text(json.dumps(meta, indent=2, default=_json_default))


# ------------------------------------------------------------
# Main runner
# ------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--language-name", required=True)
    parser.add_argument("--language-code", required=True)
    parser.add_argument("--script", required=True)
    parser.add_argument(
        "--backend",
        default=None,
        help="dummy | openai | anthropic | local (default: from config)"
    )
    parser.add_argument(
        "--config",
        default=None,
        help="Path to settings TOML file (default: src/config/settings.toml)"
    )
    parser.add_argument(
        "--data-dir",
        default="data",
        help="Root data directory for output (default: data)"
    )
    parser.add_argument(
        "--no-formatting",
        action="store_true",
        help="Skip F* formatting prompts; run only P* prompts."
    )
    parser.add_argument(
        "--model-name",
        default=None,
        help="Optional override for the backend model name."
    )
    parser.add_argument(
        "--resume",
        action="store_true",
        help="Skip steps whose output files already exist."
    )
    args = parser.parse_args()

    # Settings: load from config file, then apply CLI overrides
    config_path = Path(args.config) if args.config else None
    settings = Settings.from_file(config_path)
    if args.backend:
        settings.backend = args.backend
    settings.phase = "P"

    backend_lower = settings.backend.lower()
    if backend_lower == "anthropic":
        settings.api_key_env = "ANTHROPIC_API_KEY"
        settings.model_name = args.model_name or "claude-sonnet-4-5"
    elif backend_lower == "openai":
        settings.api_key_env = "OPENAI_API_KEY"
        settings.model_name = args.model_name or settings.model_name
    else:
        if args.model_name:
            settings.model_name = args.model_name

    lang_info = {
        "name": args.language_name,
        "code": args.language_code,
        "script": args.script,
    }

    base_output = Path(args.data_dir) / args.language_code
    base_output.mkdir(parents=True, exist_ok=True)

    # Persist per-language metadata for later cross-language analysis (G-phase)
    lang_meta_path = base_output / "language.json"
    lang_info = {
        "name": args.language_name,
        "code": args.language_code,
        "script": args.script,
    }

    prompt_dir = Path("prompts")
    dep_path = prompt_dir / "dependencies.toml"
    if not dep_path.exists():
        # Fallback to repo-root dependencies if someone relocated the file
        alt_dep = Path("dependencies.toml")
        if alt_dep.exists():
            dep_path = alt_dep

    backend = get_backend(settings)
    renderer = PromptRenderer(settings, lang_info, base_output)
    context_mgr = ContextManager(base_output)

    steps = load_steps(prompt_dir)
    dependencies = load_dependencies(dep_path)

    # Optionally skip formatting prompts (F*)
    if args.no_formatting:
        steps = [s for s in steps if s["kind"] != "format"]

    # On resume, figure out which steps already have outputs in context
    completed_in_context = set()
    if args.resume:
        existing_history = context_mgr.load_history()
        completed_in_context = {entry.get("step") for entry in existing_history}

    print(f"🔎 Running CLCA pipeline for {args.language_name} ({args.language_code})...\n")

    for step in steps:
        code = step["code"]
        kind = step["kind"]
        phase = step["phase"]

        out_path = base_output / f"{code}.{kind}.txt"

        # Resume: skip steps with existing output
        if args.resume and out_path.exists():
            if code in completed_in_context:
                print(f"   ⏭ Skipping {code} (already completed)")
                continue
            else:
                # Output file exists but not in context — re-sync
                existing_output = out_path.read_text(encoding="utf-8")
                context_mgr.append_step_output(code, "", existing_output)
                print(f"   ⏭ Skipping {code} (output exists, re-synced context)")
                continue

        template_text = step["file"].read_text(encoding="utf-8")

        # Look up which prior steps this step depends on
        required_steps = dependencies.get(code, [])

        # Build context from *outputs only* of required steps
        cumulative_context = context_mgr.gather_subset(required_steps)

        # Render the actual prompt
        rendered_prompt = renderer.render(
            template_text=template_text,
            context=cumulative_context,
        )

        settings.phase = phase
        if hasattr(backend, "phase"):
            backend.phase = phase

        print(f"➡️  Running step {code} ...")

        # Call backend (supports both .complete() or .generate())
        if hasattr(backend, "complete"):
            response = backend.complete(rendered_prompt)
        else:
            response = backend.generate(rendered_prompt)

        output_text = response.output

        # Write output files
        out_path.write_text(output_text, encoding="utf-8")

        meta_path = base_output / f"{code}.{kind}.meta.json"
        write_metadata(meta_path, response, rendered_prompt)

        # Log this step in context.jsonl (prompt + output)
        context_mgr.append_step_output(code, rendered_prompt, output_text)

        print(f"   ✔ Saved: {out_path.name}")

    print("\n🎉 Finished CLCA pipeline.\n")


if __name__ == "__main__":
    main()

