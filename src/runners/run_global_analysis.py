from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

from src.config import Settings
from src.backends import get_backend
from src.pipeline.prompt_renderer import PromptRenderer
from src.pipeline.context_manager import ContextManager
from src.global_analysis.cross_language_index import build_global_context_block


def _json_default(obj):
    """
    JSON serializer for objects not serializable by default json code.
    Mirrors run_language's behavior.
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


def load_g_steps(prompt_dir: Path) -> list[dict]:
    """
    Load G* steps in lexicographic order from prompts/G.

    Returns:
        [
          {"file": Path, "code": "G1_summary", "kind": "global"},
          ...
        ]
    """
    g_dir = prompt_dir / "G"
    if not g_dir.exists():
        raise FileNotFoundError(f"Global prompts directory not found: {g_dir}")

    g_steps = sorted(g_dir.glob("G*.j2"))

    steps: list[dict] = []
    for file in g_steps:
        steps.append(
            {
                "file": file,
                "code": file.stem,  # e.g., "G1_summary"
                "kind": "global",
            }
        )

    return steps


def main():
    parser = argparse.ArgumentParser(description="Run CLCA G-phase global analysis.")
    parser.add_argument(
        "--languages",
        nargs="+",
        required=True,
        help="List of language codes to include (e.g., ka yo fi).",
    )
    parser.add_argument(
        "--backend",
        default=None,
        help="dummy | openai | anthropic | local (default: from config)",
    )
    parser.add_argument(
        "--config",
        default=None,
        help="Path to settings TOML file (default: src/config/settings.toml)",
    )
    parser.add_argument(
        "--data-dir",
        default="data",
        help="Root data directory for input/output (default: data)",
    )
    parser.add_argument(
        "--model-name",
        default=None,
        help="Optional override for backend model name.",
    )
    parser.add_argument(
        "--max-tokens",
        type=int,
        default=None,
        help="Override max tokens for G-phase (default: 64000).",
    )
    parser.add_argument(
        "--request-timeout",
        type=float,
        default=None,
        help="Override Anthropic/OpenAI request timeout in seconds (default: 300s for G-phase).",
    )
    parser.add_argument(
        "--steps",
        nargs="+",
        default=None,
        help="Optional list of G-phase step codes to run (e.g., G5_construction_comparison G7b_compare_to_AOML). "
        "If omitted, runs all G* prompts.",
    )
    parser.add_argument(
        "--output-code",
        default="global",
        help='Output subdirectory name under data/ (default: "global").',
    )
    parser.add_argument(
        "--aoml-matrix",
        default=None,
        help="Optional path to an AOML constraint matrix (JSON or text) for G7b.",
    )
    args = parser.parse_args()

    # Settings: load from config file, then apply CLI overrides
    config_path = Path(args.config) if args.config else None
    settings = Settings.from_file(config_path)
    if args.backend:
        settings.backend = args.backend
    settings.phase = "G"

    # Long-context prompts need much higher generation limits
    default_g_max = 16384
    settings.max_tokens = args.max_tokens or max(settings.max_tokens, default_g_max)
    default_timeout = 300.0
    settings.request_timeout = args.request_timeout or settings.request_timeout or default_timeout

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

    language_codes = args.languages

    # "Global" output directory
    base_output = Path(args.data_dir) / args.output_code
    base_output.mkdir(parents=True, exist_ok=True)

    # Build static cross-language context block from F-phase tables
    global_lang_context = build_global_context_block(language_codes, data_root=Path(args.data_dir))

    # Dummy "language" info used by PromptRenderer
    lang_info = {
        "name": "GLOBAL_ANALYSIS",
        "code": args.output_code,
        "script": "multi",
        "languages": language_codes,
    }

    backend = get_backend(settings)
    renderer = PromptRenderer(settings, lang_info, base_output)
    context_mgr = ContextManager(base_output)
    prompt_dir = Path("prompts")

    steps = load_g_steps(prompt_dir)

    if args.steps:
        requested = {code.strip() for code in args.steps if code.strip()}
        filtered = [step for step in steps if step["code"] in requested]
        missing = requested - {step["code"] for step in filtered}
        if missing:
            print(f"⚠️  Requested G-phase steps not found: {', '.join(sorted(missing))}")
        if not filtered:
            raise ValueError("No valid G-phase steps matched --steps selection.")
        steps = filtered

    aoml_text = None
    aoml_path = None

    # Prefer CLI-provided matrix; otherwise fall back to bundled default
    if args.aoml_matrix:
        aoml_path = Path(args.aoml_matrix)
    else:
        default_path = Path('aoml') / 'aoml_constraint_matrix.json'
        if default_path.is_file():
            aoml_path = default_path

    if aoml_path:
        if aoml_path.is_file():
            try:
                if aoml_path.suffix.lower() == '.json':
                    data = json.loads(aoml_path.read_text(encoding='utf-8'))
                    aoml_text = json.dumps(data, indent=2, ensure_ascii=False)
                else:
                    aoml_text = aoml_path.read_text(encoding='utf-8')
            except Exception as exc:
                print(f"??  Failed to load AOML matrix at {aoml_path}: {exc}")
        else:
            print(f"??  AOML matrix path not found: {aoml_path}")

    print(f"🌐 Running CLCA G-phase global analysis for languages: {', '.join(language_codes)}\n")

    for step in steps:
        template_text = step["file"].read_text(encoding="utf-8")

        # G-phase context = static cross-language data + incremental G-history
        history_context = context_mgr.gather_context()
        combined_context = (
            "### CROSS-LANGUAGE DATA FROM F-PHASE ###\n"
            + global_lang_context
            + "\n\n### PRIOR G-PHASE STEPS ###\n"
            + history_context
        )

        if step["code"] == "G7b_compare_to_AOML" and aoml_text:
            combined_context += (
                "\n\n### AOML CONSTRAINT MATRIX ###\n"
                + aoml_text
                + "\n"
            )
        elif step["code"] == "G7b_compare_to_AOML" and not aoml_text:
            print("⚠️  G7b requires an AOML matrix, but none was provided. Output may note missing data.")

        rendered_prompt = renderer.render(
            template_text=template_text,
            context=combined_context,
        )

        print(f"➡️  Running step {step['code']} ...")

        # Support both .complete() and .generate()
        if hasattr(backend, "complete"):
            response = backend.complete(rendered_prompt)
        else:
            response = backend.generate(rendered_prompt)

        output_text = getattr(response, "output", None) or getattr(response, "text", "")

        # Write output files
        out_path = base_output / f"{step['code']}.{step['kind']}.txt"
        out_path.write_text(output_text, encoding="utf-8")

        meta_path = base_output / f"{step['code']}.{step['kind']}.meta.json"
        write_metadata(meta_path, response, rendered_prompt)

        # Append to G-phase context log
        context_mgr.append_step_output(step["code"], rendered_prompt, output_text)

        print(f"   ✔ Saved: {out_path.name}")

    print("\n✅ Finished CLCA G-phase global analysis.\n")


if __name__ == "__main__":
    main()
