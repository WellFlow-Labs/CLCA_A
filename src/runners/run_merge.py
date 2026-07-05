"""M-phase: LLM-based merge of K independent P-phase probes into one
consolidated P-phase output per language.

Reads K probe directories at ``<root>/<lang>/probes/run_<k>/`` and writes
one merged ``<root>/<lang>/<layer>.content.txt`` per P-phase layer. The
output files are named to match the downstream F-phase reader, so
``run_language.py --resume`` will skip P/I and run only F-phase on the
merged inputs.

Layers merged (matches ``prompts/P/`` inventory):

  P1_vocab, P1b_root_expansion, P2a_derivational_system,
  P2b_light_verb_constructions, P3_semantic_groups, P4a_CONSTRUCTIONS,
  P4b_construction_behavior, P5_oppositions, P6_naturalness

Usage::

    python -m src.runners.run_merge \
        --root data_union --langs en zh ka qu yo fi ... \
        --backend anthropic --model-name claude-sonnet-4-6

Writes ``<root>/<lang>/<layer>.content.txt`` (merged content) and
``<root>/<lang>/<layer>.content.meta.json`` (stub metadata so resume
sees the step as complete).
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from jinja2 import Template

# Reuse the existing backend abstraction so this runner picks up the same
# rate-limiting, key handling, and model-quirk handling (e.g. Opus 4.8
# temperature drop) as run_language.py.
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from src.backends.anthropic_backend import AnthropicBackend  # noqa: E402


P_LAYERS = [
    "P1_vocab",
    "P1b_root_expansion",
    "P2a_derivational_system",
    "P2b_light_verb_constructions",
    "P3_semantic_groups",
    "P4a_CONSTRUCTIONS",
    "P4b_construction_behavior",
    "P5_oppositions",
    "P6_naturalness",
]

LANG_TABLE = {
    "en": ("English", "Latin"),
    "zh": ("Chinese", "Han"),
    "ka": ("Georgian", "Georgian"),
    "qu": ("Quechua", "Latin"),
    "fi": ("Finnish", "Latin"),
    "yo": ("Yoruba", "Latin"),
    "eu": ("Basque", "Latin"),
    "ta": ("Tamil", "Tamil"),
    "ko": ("Korean", "Hangul"),
    "he": ("Hebrew", "Hebrew"),
    "sa": ("Sanskrit", "Devanagari"),
    "el": ("Greek", "Greek"),
    "tl": ("Tagalog", "Latin"),
    "sw": ("Swahili", "Latin"),
    "id": ("Indonesian", "Latin"),
    "tr": ("Turkish", "Latin"),
}


def load_probes(probes_dir: Path, layer: str) -> list[str]:
    """Return the text of layer.content.txt for each run_<k> subdir, in order."""
    if not probes_dir.is_dir():
        return []
    out: list[str] = []
    for run_dir in sorted(
        probes_dir.iterdir(),
        key=lambda p: int(p.name.split("_")[1]) if p.name.startswith("run_") else 0,
    ):
        if not run_dir.is_dir() or not run_dir.name.startswith("run_"):
            continue
        f = run_dir / f"{layer}.content.txt"
        if f.is_file():
            out.append(f.read_text(encoding="utf-8"))
    return out


def render_prompt(template_text: str, lang_code: str, layer: str, probes: list[str]) -> str:
    name, script = LANG_TABLE[lang_code]
    tmpl = Template(template_text, keep_trailing_newline=True)
    return tmpl.render(
        lang={"name": name, "code": lang_code, "script": script},
        layer_name=layer,
        k=len(probes),
        probes=probes,
    )


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--root", default="data_union",
                   help="Output root containing <lang>/probes/run_<k>/ and "
                        "where merged outputs land at <lang>/<layer>.content.txt")
    p.add_argument("--langs", nargs="+", required=True)
    p.add_argument("--layers", nargs="+", default=P_LAYERS,
                   help="Restrict to a subset of P-phase layers (default: all 9).")
    p.add_argument("--backend", default="anthropic")
    p.add_argument("--model-name", default="claude-sonnet-4-6")
    p.add_argument("--prompt", default="prompts/M/M_merge.j2",
                   help="Path to the merge prompt template.")
    p.add_argument("--max-tokens", type=int, default=8000,
                   help="Higher than the per-step default; merged outputs are "
                        "larger because they union K probes.")
    p.add_argument("--request-timeout", type=float, default=900.0,
                   help="Per-request HTTP timeout in seconds. Default is 900 "
                        "(15 min) — much higher than the 120s P-phase default, "
                        "because merge calls generate ~6-8k tokens of "
                        "structured output and routinely take 3-10 minutes.")
    p.add_argument("--force", action="store_true",
                   help="Overwrite existing merged outputs instead of skipping them.")
    args = p.parse_args()

    root = Path(args.root)
    template_text = Path(args.prompt).read_text(encoding="utf-8")

    # Only Anthropic backend is implemented for this runner. Other backends
    # could be plugged in by reusing src.runners.run_language's get_backend.
    if args.backend != "anthropic":
        raise SystemExit(f"backend {args.backend!r} not supported by run_merge yet")
    backend = AnthropicBackend(
        model=args.model_name,
        max_tokens=args.max_tokens,
        request_timeout=args.request_timeout,
        phase="P",
    )

    n_calls = 0
    n_skipped = 0
    for lang in args.langs:
        if lang not in LANG_TABLE:
            print(f"⚠️  unknown language code {lang!r} — skipping", flush=True)
            continue
        lang_dir = root / lang
        probes_dir = lang_dir / "probes"
        lang_dir.mkdir(parents=True, exist_ok=True)
        for layer in args.layers:
            out_path = lang_dir / f"{layer}.content.txt"
            meta_path = lang_dir / f"{layer}.content.meta.json"
            if out_path.exists() and not args.force:
                print(f"   ⏭  {lang}/{layer}: merged output exists, skipping "
                      f"(use --force to overwrite)", flush=True)
                n_skipped += 1
                continue
            probes = load_probes(probes_dir, layer)
            if not probes:
                print(f"   ✗  {lang}/{layer}: no probes found at "
                      f"{probes_dir}/run_*/{layer}.content.txt", flush=True)
                continue
            print(f"   →  {lang}/{layer}: merging {len(probes)} probes...",
                  flush=True)
            prompt = render_prompt(template_text, lang, layer, probes)
            response = backend.generate(prompt)
            out_path.write_text(response.output, encoding="utf-8")
            meta = {
                "step": layer,
                "phase": "M",
                "merged_from": len(probes),
                "backend": args.backend,
                "model": args.model_name,
                "raw_metadata": response.metadata,
            }
            meta_path.write_text(json.dumps(meta, indent=2, ensure_ascii=False),
                                 encoding="utf-8")
            n_calls += 1

    print(f"\nMerge complete: {n_calls} merges performed, {n_skipped} skipped.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
