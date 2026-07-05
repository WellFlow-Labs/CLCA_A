"""P-phase saturation analysis for CLCA-Revision pipeline.

Loads K independent P-phase runs per language (output of
``run_p_phase_saturation.sh``) and computes the cumulative-union growth
curve for each measured P-phase set: core vocabulary (P1), core
oppositions (P5), and script-token content (P6).

The headline metric is the **saturation ratio** R(k) = |union(runs 1..k)|
/ |union(runs 1..K)| — the fraction of the K-run union that K' < K probes
already capture. If R(k) flattens quickly (e.g., R(3) ≥ 0.9), the pipeline
saturates and a single P-phase run captures most of the recoverable
material; if it grows linearly, the elephant is bigger than any single
probe.

For order-independence, the curve is averaged over a random sample of
run-orderings (default: 100 permutations) — otherwise the order of
``run_1, run_2, ...`` would bias the curve.

Usage::

    python -m src.runners.compute_saturation \
        --root data_saturation \
        --langs en zh ka qu \
        --output data_saturation/saturation_curve.md
"""
from __future__ import annotations

import argparse
import random
from itertools import permutations
from pathlib import Path

from src.runners.compare_runs import (
    extract_p1_core_forms,
    extract_p5_core_oppositions,
    extract_p6_script_tokens,
)


# ---------------------------------------------------------------------------
# Per-language loading
# ---------------------------------------------------------------------------

def load_runs(root: Path, lang: str) -> dict[str, list[set]]:
    """Return ``{layer: [run_1_set, run_2_set, ...]}`` for one language.

    Each run subdir is expected at ``<root>/<lang>/run_<k>/`` and to contain
    P1/P5/P6 outputs. Missing files yield an empty set for that run.
    """
    lang_dir = root / lang
    run_dirs = sorted(
        (d for d in lang_dir.iterdir() if d.is_dir() and d.name.startswith("run_")),
        key=lambda d: int(d.name.split("_")[1]),
    )
    p1: list[set[str]] = []
    p5: list[set[frozenset[str]]] = []
    p6: list[set[str]] = []
    for d in run_dirs:
        p1_path = d / "P1_vocab.content.txt"
        p5_path = d / "P5_oppositions.content.txt"
        p6_path = d / "P6_naturalness.content.txt"
        p1.append(extract_p1_core_forms(_read(p1_path)) if p1_path.exists() else set())
        p5.append(extract_p5_core_oppositions(_read(p5_path)) if p5_path.exists() else set())
        p6.append(extract_p6_script_tokens(_read(p6_path)) if p6_path.exists() else set())
    return {"P1": p1, "P5": p5, "P6": p6}


def _read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except OSError:
        return ""


# ---------------------------------------------------------------------------
# Saturation curve
# ---------------------------------------------------------------------------

def saturation_curve(
    runs: list[set], n_permutations: int = 100, rng: random.Random | None = None,
) -> list[tuple[float, float, float]]:
    """Return ``[(mean_cumulative, mean_marginal, mean_ratio), ...]`` per k.

    Averaged over ``n_permutations`` random orderings of the run list (or
    all orderings if K! is small). Index 0 is k=1.
    """
    K = len(runs)
    if K == 0:
        return []
    if K <= 6 and n_permutations >= 720:  # exhaust if practical
        orderings = list(permutations(range(K)))
    else:
        rng = rng or random.Random(0)
        orderings = [tuple(rng.sample(range(K), K)) for _ in range(n_permutations)]

    # Per-k aggregates across orderings.
    cum_sum = [0.0] * K
    marg_sum = [0.0] * K
    for order in orderings:
        union: set = set()
        for k, idx in enumerate(order):
            prev_size = len(union)
            union = union | runs[idx]
            cum_sum[k] += len(union)
            marg_sum[k] += len(union) - prev_size
    n = len(orderings)
    mean_cum = [s / n for s in cum_sum]
    mean_marg = [s / n for s in marg_sum]
    final_union = mean_cum[-1] if mean_cum[-1] else 1.0
    mean_ratio = [c / final_union for c in mean_cum]
    return list(zip(mean_cum, mean_marg, mean_ratio))


# ---------------------------------------------------------------------------
# Reporting
# ---------------------------------------------------------------------------

def format_curve(
    lang: str, layer: str, runs: list[set], curve: list[tuple[float, float, float]],
) -> str:
    sizes = [len(r) for r in runs]
    out = [f"\n### {lang} — {layer}"]
    out.append(f"  Per-run sizes: {sizes} (mean {sum(sizes)/len(sizes):.1f})")
    out.append(f"  Full K-run union: {curve[-1][0]:.0f} items")
    out.append(f"  {'k':>3s}  {'cumulative':>10s}  {'marginal':>9s}  {'R(k)':>6s}")
    for k, (cum, marg, ratio) in enumerate(curve, start=1):
        out.append(f"  {k:>3d}  {cum:>10.1f}  {marg:>9.2f}  {ratio:>6.1%}")
    return "\n".join(out)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default="data_saturation")
    parser.add_argument(
        "--langs", nargs="+", required=True,
        help="Language codes to analyze (subdirs of --root)."
    )
    parser.add_argument(
        "--permutations", type=int, default=100,
        help="Number of run-order permutations to average over (default: 100).",
    )
    parser.add_argument("--output", default="-", help="Output file or '-' for stdout.")
    args = parser.parse_args()

    root = Path(args.root)
    lines: list[str] = [
        "# CLCA P-phase saturation curve",
        f"# Root: {root}",
        f"# Languages: {', '.join(args.langs)}",
        f"# Permutations per curve: {args.permutations}",
        "",
        "Each language was run K times through the P-phase pipeline; below,",
        "the cumulative-union growth across the K probes is averaged over",
        f"{args.permutations} random run-orderings. R(k) is the fraction of",
        "the full K-run union captured by the first k probes.",
        "",
        "If R(k) flattens quickly (e.g. R(3) ≥ 0.9), a single P-phase run",
        "captures most of the recoverable material and the pipeline saturates.",
        "If R(k) grows roughly linearly, the underlying structure is bigger",
        "than any single probe and more runs uncover meaningfully more.",
    ]

    summary_rows: list[tuple[str, str, float, float, float]] = []
    for lang in args.langs:
        runs_by_layer = load_runs(root, lang)
        lines.append(f"\n## {lang}")
        for layer in ("P1", "P5", "P6"):
            runs = runs_by_layer[layer]
            if not runs:
                lines.append(f"\n### {lang} — {layer}\n  (no runs found)")
                continue
            curve = saturation_curve(runs, n_permutations=args.permutations)
            lines.append(format_curve(lang, layer, runs, curve))
            # Capture summary stats for the bottom table. R(K) is always
            # 100% by definition (the union of K runs equals itself), so
            # the headline numbers are R(1) — what fraction does a single
            # probe see — and intermediate R(2), R(3).
            r1 = curve[0][2] if len(curve) >= 1 else float("nan")
            r2 = curve[1][2] if len(curve) >= 2 else float("nan")
            r3 = curve[2][2] if len(curve) >= 3 else float("nan")
            summary_rows.append((lang, layer, r1, r2, r3, len(curve)))

    # Summary table at the end.
    lines.append("\n## Summary — R(k) across all (lang, layer) pairs")
    lines.append("")
    lines.append("R(k) is the fraction of the full K-run union captured by")
    lines.append("the first k probes (averaged over random run-orderings).")
    lines.append("R(K) is omitted because it is 100% by definition.")
    lines.append("")
    lines.append("| Lang | Layer | K | R(1) | R(2) | R(3) |")
    lines.append("|---|---|---:|---:|---:|---:|")
    for lang, layer, r1, r2, r3, K in summary_rows:
        def f(x: float) -> str:
            return "—" if x != x else f"{x:.1%}"  # NaN check
        lines.append(f"| {lang} | {layer} | {K} | {f(r1)} | {f(r2)} | {f(r3)} |")

    body = "\n".join(lines) + "\n"
    if args.output == "-":
        print(body, end="")
    else:
        Path(args.output).write_text(body, encoding="utf-8")
        print(f"wrote {args.output}")


if __name__ == "__main__":
    main()
