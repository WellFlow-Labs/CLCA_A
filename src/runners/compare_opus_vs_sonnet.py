"""Compare Opus single-probe P1 coverage against Sonnet baseline + K=5 union.

Headline question: does Claude Opus 4.8 recover more vocabulary per probe
than Claude Sonnet, and does its K=1 coverage approach the K=5 Sonnet
saturation union?

Three quantities per language, per layer (P1 / P5 / P6):

* ``|Opus|``             — Opus single-probe set size
* ``|Sonnet K=1|``       — Sonnet single-probe set size (baseline ``data/``)
* ``|Sonnet K=5 union|`` — union over the 5 Sonnet probes in
                            ``data_saturation/<lang>/run_1..5/``

And three coverage ratios:

* ``Opus ⊂ K=5 union``      — fraction of Opus's set that Sonnet K=5 also finds
                              (does Sonnet's multi-probe sampling subsume Opus?)
* ``K=1 ⊂ Opus``            — fraction of Sonnet baseline that Opus also finds
                              (does Opus subsume one Sonnet probe?)
* ``Opus / K=5 union``      — Opus single-probe coverage as a fraction of the
                              K=5 union size (Opus's saturation rate at K=1)

The third number is the most informative: if Opus K=1 ≈ Sonnet K=5 union,
capability replaces quantity.

Usage::

    python -m src.runners.compare_opus_vs_sonnet \
        --opus data_opus --sonnet data --saturation data_saturation \
        --langs en zh ka qu --output data_opus/opus_vs_sonnet.md
"""
from __future__ import annotations

import argparse
from pathlib import Path

from src.runners.compare_runs import (
    extract_p1_core_forms,
    extract_p5_core_oppositions,
    extract_p6_script_tokens,
)


EXTRACTORS = {
    "P1": (extract_p1_core_forms, "P1_vocab.content.txt"),
    "P5": (extract_p5_core_oppositions, "P5_oppositions.content.txt"),
    "P6": (extract_p6_script_tokens, "P6_naturalness.content.txt"),
}


def _read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except OSError:
        return ""


def _extract(directory: Path, layer: str) -> set:
    extractor, filename = EXTRACTORS[layer]
    return extractor(_read(directory / filename))


def _sonnet_k5_union(saturation_root: Path, lang: str, layer: str) -> set:
    union: set = set()
    lang_dir = saturation_root / lang
    if not lang_dir.is_dir():
        return union
    for run_dir in sorted(lang_dir.iterdir()):
        if run_dir.is_dir() and run_dir.name.startswith("run_"):
            union |= _extract(run_dir, layer)
    return union


def _format_pct(num: int, den: int) -> str:
    if den == 0:
        return "—"
    return f"{100 * num / den:.1f}%"


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--opus", default="data_opus")
    p.add_argument("--sonnet", default="data",
                   help="Sonnet baseline single-probe root (default: data)")
    p.add_argument("--saturation", default="data_saturation",
                   help="Sonnet K-runs saturation root (default: data_saturation)")
    p.add_argument("--langs", nargs="+", required=True)
    p.add_argument("--output", default="-")
    args = p.parse_args()

    opus_root = Path(args.opus)
    sonnet_root = Path(args.sonnet)
    sat_root = Path(args.saturation)

    out: list[str] = [
        "# Opus single-probe vs. Sonnet baseline + Sonnet K=5 union",
        f"# Opus root:        {opus_root}",
        f"# Sonnet baseline:  {sonnet_root}",
        f"# Sonnet K=5 root:  {sat_root}",
        f"# Languages:        {', '.join(args.langs)}",
        "",
        "For each (lang, layer):",
        "  |Opus|             — Opus single-probe set size",
        "  |Sonnet K=1|       — Sonnet single-probe set size (baseline)",
        "  |Sonnet K=5 union| — union over the 5 Sonnet probes in saturation",
        "  Opus ∩ K=5 / Opus  — fraction of Opus's set that K=5 union also finds",
        "  Opus ∩ K=5 / K=5   — Opus's saturation rate at K=1 (most informative)",
    ]

    summary_rows: list[tuple] = []

    for lang in args.langs:
        out.append(f"\n## {lang}")
        for layer in ("P1", "P5", "P6"):
            opus = _extract(opus_root / lang, layer)
            sonnet1 = _extract(sonnet_root / lang, layer)
            sonnet5 = _sonnet_k5_union(sat_root, lang, layer)
            in_both = opus & sonnet5
            opus_subset = len(in_both)
            opus_size = len(opus)
            son5_size = len(sonnet5)
            out.append(f"\n### {lang} — {layer}")
            out.append(f"  |Opus|             = {opus_size}")
            out.append(f"  |Sonnet K=1|       = {len(sonnet1)}")
            out.append(f"  |Sonnet K=5 union| = {son5_size}")
            out.append(
                f"  Opus ∩ K=5 union   = {opus_subset}  "
                f"({_format_pct(opus_subset, opus_size)} of Opus, "
                f"{_format_pct(opus_subset, son5_size)} of K=5)"
            )
            opus_only = opus - sonnet5
            k5_only = sonnet5 - opus
            out.append(f"  Opus-only          = {len(opus_only)}")
            out.append(f"  K=5-union-only     = {len(k5_only)}")
            summary_rows.append((lang, layer, opus_size, len(sonnet1), son5_size,
                                 opus_subset, len(opus_only), len(k5_only)))

    out.append("\n## Summary")
    out.append("")
    out.append("| Lang | Layer | Opus | K=1 | K=5 union | Opus∩K=5 | Opus / K=5 | K=1 / K=5 |")
    out.append("|---|---|---:|---:|---:|---:|---:|---:|")
    for lang, layer, o, s1, s5, both, _oo, _k5o in summary_rows:
        out.append(
            f"| {lang} | {layer} | {o} | {s1} | {s5} | {both} "
            f"| {_format_pct(o, s5)} | {_format_pct(s1, s5)} |"
        )

    body = "\n".join(out) + "\n"
    if args.output == "-":
        print(body, end="")
    else:
        Path(args.output).write_text(body, encoding="utf-8")
        print(f"wrote {args.output}")


if __name__ == "__main__":
    main()
