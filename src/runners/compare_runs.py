"""Within-protocol reproducibility comparison for CLCA-Revision pipeline.

Compares two complete CLCA pipeline output directories (e.g. ``data`` vs.
``data_reproducibility``) on the metrics referenced in Paper I §4.2:

* **P1 core vocab overlap** — Jaccard similarity over items marked ``[CORE]``
  in each language's ``P1_vocab.content.txt``.
* **P5 core oppositions match** — match rate over oppositions marked
  ``[CORE]`` in ``P5_oppositions.content.txt``, treating each opposition as an
  unordered pair of lexical terms.
* **P6 content overlap** — Jaccard similarity over the *script-character
  tokens* (non-Latin script forms) cited in each run's
  ``P6_naturalness.content.txt``. Used in place of structural overlap
  because the P6 prompt evolved (v3.3 → v3.4) between runs, reorganising
  section headers; the token-level metric is robust to that formatting
  drift while still capturing which morphological constructions the run
  cites as natural / marginal / blocked.

Usage::

    python -m src.runners.compare_runs \\
        --baseline data \\
        --rerun data_reproducibility \\
        --set all \\
        --output data_reproducibility/comparison_report.txt

Both pipeline runs must use the same languages and the same prompt set; this
script does not verify that, only that the per-language P1/P5/P6 outputs
exist in both directories.
"""
from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

SET_A = ["ka", "yo", "fi", "eu", "ta", "id", "tr", "ko"]
SET_B = ["zh", "he", "sa", "el", "en", "tl", "sw", "qu"]


# ---------------------------------------------------------------------------
# Extractors
# ---------------------------------------------------------------------------

def _normalize_form(s: str) -> str:
    """Strip parenthetical transliterations and surrounding whitespace.

    The two pipeline runs sometimes embed a parenthetical romanization after
    the script form (e.g. ``ჭეშმარიტი (ch'eshmarit'i)``) and the romanization
    can drift between runs (``ṭq'uili`` vs ``t'q'uili``) even when the script
    form is identical. Stripping parentheticals lets us compare the lexeme
    itself rather than the formatting around it.
    """
    s = re.sub(r"\s*\([^)]*\)\s*$", "", s.strip())
    s = re.sub(r"\s+", " ", s)
    return s.strip()


def extract_p1_core_forms(text: str) -> set[str]:
    """Return the set of [CORE] lexical forms.

    The pipeline runs use at least three markdown styles for P1 items, so
    the extractor accepts all of them:

    - **Format A** (e.g. baseline ka, eu): ``### N`` header followed by
      ``**Form:** X`` line.
    - **Format B** (e.g. rerun ka, yo, fi, qu): ``### N. X (translit)``
      header — form is embedded in the header.
    - **Format C** (e.g. rerun tr, eu, ko, zh, en, sw): top-level numbered
      list item ``N. **X**`` with bullet sub-fields.

    Items in any format are detected by a boundary regex that matches either
    a ``###`` numbered header or a top-level ``N.`` numbered list line.
    """
    forms: set[str] = set()
    # Item boundary — accepts the styles seen across runs to date:
    #   ``## N`` / ``### N``                  heading style (baseline)
    #   ``N. **X**``                          numbered list, bold value
    #   ``**N. X**``                          number-and-name in single bold
    #   ``**N.**`` followed by ``**Form:** X`` number-only bold + Form line
    # The last two are emitted by the K-runs saturation experiment.
    boundary = re.compile(
        r"(?m)^(?:"
        r"#{2,}\s+\d+"
        r"|\d+\.\s+(?=\*\*)"
        r"|\*\*\d+\.\s+(?=[^*])"
        r"|\*\*\d+\.\*\*"
        r")"
    )
    boundaries = list(boundary.finditer(text))
    for i, mb in enumerate(boundaries):
        item_start = mb.start()
        item_end = boundaries[i + 1].start() if i + 1 < len(boundaries) else len(text)
        item = text[item_start:item_end]
        if "[CORE]" not in item:
            continue
        form: str | None = None
        # Format A: explicit ``**Form:** X`` line. Tolerates the Opus
        # single-line variant where the number prefix is folded into the
        # same bold span (``**1. Form:** X``).
        m = re.search(r"\*\*(?:\d+\.\s+)?Form:\*\*\s+([^\n]+)", item)
        if m:
            form = m.group(1)
        else:
            # Other formats: read the first line of the item and strip the
            # boundary prefix, then take the next token as the form.
            first_line = item.split("\n", 1)[0]
            after_head = re.sub(
                r"^(?:#{2,}\s+\d+[.)]?\s*|\d+\.\s+|\*\*\d+\.\s+)",
                "",
                first_line,
            )
            if after_head:
                m2 = re.match(r"\*\*([^*]+)\*\*", after_head.strip())
                if m2:
                    form = m2.group(1)
                else:
                    # If the boundary was ``**N. X**`` and we stripped the
                    # ``**N. `` prefix, the remainder still has a trailing
                    # ``**``. Strip it before taking the form.
                    trimmed = after_head.strip()
                    if trimmed.endswith("**"):
                        form = trimmed[:-2].strip()
                    else:
                        form = trimmed
        if form:
            forms.add(_normalize_form(form))
    return forms


def extract_p5_core_oppositions(text: str) -> set[frozenset[str]]:
    """Return the set of ``frozenset({term_a, term_b})`` for [CORE] oppositions.

    Accepts opposition items headed by ``## OPPOSITION N`` or
    ``### OPPOSITION N`` or ``## OPPOSITION N: <inline header text>``.
    Parenthetical romanizations are stripped from each term so the same
    script-level opposition matches across romanization drift.
    """
    opps: set[frozenset[str]] = set()
    # Any number of leading '#' marks, then OPPOSITION + number, then optional
    # rest. Case-insensitive — some runs emit ``## Opposition 1`` (mixed case)
    # rather than ``## OPPOSITION 1`` (all caps).
    items = re.split(r"(?im)^#+\s+OPPOSITION\s+\d+[^\n]*", text)
    # Allow the colon to be inside *or* outside the closing ``**``: some runs
    # produce ``**Term A:** X`` and others produce ``**Term A**: X``.
    term_a_re = re.compile(r"\*\*Term A:?\*\*:?\s+([^\n]+)")
    term_b_re = re.compile(r"\*\*Term B:?\*\*:?\s+([^\n]+)")
    for item in items[1:]:
        if "[CORE]" not in item:
            continue
        a = term_a_re.search(item)
        b = term_b_re.search(item)
        if a and b:
            opps.add(frozenset([_normalize_form(a.group(1)),
                                _normalize_form(b.group(1))]))
    return opps


# Script-character ranges: any code point above U+00FF (i.e. outside Latin-1
# basic + Latin-1 Supplement) is treated as part of a non-Latin script token.
# This lets us capture Georgian, Hebrew, Devanagari, Han, Hangul, Greek, etc.
# while ignoring English / transliteration text.
_SCRIPT_TOKEN_RE = re.compile(r"[^\x00-\xff]+")


def extract_p6_script_tokens(text: str) -> set[str]:
    """Return the set of non-Latin script tokens appearing in P6.

    P6 protocol version drifted (v3.3 → v3.4) between the two runs, producing
    radically different section structures, so structural overlap is not a
    useful reproducibility measure. The semantic content of P6 — which actual
    morphological/lexical constructions the run identifies as natural,
    marginal, or blocked — is carried by the non-Latin tokens (Georgian,
    Chinese, etc.) it cites. Comparing those token sets across runs gives a
    content-level reproducibility signal that is robust to formatting drift.
    """
    tokens: set[str] = set()
    for m in _SCRIPT_TOKEN_RE.finditer(text):
        tok = m.group(0).strip()
        if len(tok) >= 1:
            tokens.add(tok)
    return tokens


def detect_protocol_version(text: str) -> str | None:
    """Extract the ``CLCA Protocol vX.Y`` tag from a file header, if present."""
    m = re.search(r"CLCA Protocol\s+v?(\d+(?:\.\d+)*)", text)
    return m.group(1) if m else None


# ---------------------------------------------------------------------------
# Per-language comparison
# ---------------------------------------------------------------------------

@dataclass
class PhaseResult:
    baseline_count: int
    rerun_count: int
    intersection: int
    union: int

    @property
    def jaccard(self) -> float:
        return self.intersection / self.union if self.union else 1.0


def _glob_one(folder: Path, prefix: str) -> Path | None:
    """Find the first ``<prefix>*.content.txt`` file in ``folder`` (or None)."""
    for path in sorted(folder.glob(f"{prefix}_*.content.txt")):
        if path.is_file():
            return path
    return None


def compare_phase(
    baseline_dir: Path,
    rerun_dir: Path,
    lang: str,
    prefix: str,
    extractor,
) -> PhaseResult | None:
    base_file = _glob_one(baseline_dir / lang, prefix)
    rerun_file = _glob_one(rerun_dir / lang, prefix)
    if base_file is None or rerun_file is None:
        return None
    b = extractor(base_file.read_text(encoding="utf-8"))
    r = extractor(rerun_file.read_text(encoding="utf-8"))
    return PhaseResult(
        baseline_count=len(b),
        rerun_count=len(r),
        intersection=len(b & r),
        union=len(b | r),
    )


def compare_p6_script_content(
    baseline_dir: Path, rerun_dir: Path, lang: str
) -> tuple[PhaseResult, str | None, str | None] | None:
    """Compare P6 script-token overlap (formatting-agnostic content match)."""
    base_file = _glob_one(baseline_dir / lang, "P6")
    rerun_file = _glob_one(rerun_dir / lang, "P6")
    if base_file is None or rerun_file is None:
        return None
    base_text = base_file.read_text(encoding="utf-8")
    rerun_text = rerun_file.read_text(encoding="utf-8")
    b = extract_p6_script_tokens(base_text)
    r = extract_p6_script_tokens(rerun_text)
    pr = PhaseResult(len(b), len(r), len(b & r), len(b | r))
    return pr, detect_protocol_version(base_text), detect_protocol_version(rerun_text)


# ---------------------------------------------------------------------------
# Reporting
# ---------------------------------------------------------------------------

def emit(out, line: str = "") -> None:
    out.write(line + "\n")


def report(baseline_dir: Path, rerun_dir: Path, langs: Iterable[str], out) -> None:
    emit(out, f"# CLCA within-protocol reproducibility comparison")
    emit(out, f"# baseline: {baseline_dir}")
    emit(out, f"# rerun:    {rerun_dir}")
    emit(out, f"# languages: {', '.join(langs)}")
    emit(out)
    emit(out, f"{'Lang':<6} {'P1 core Jaccard':<22} {'P5 core match':<22} {'P6 content Jaccard':<22}")
    emit(out, "-" * 76)

    p1_jaccards: list[float] = []
    p5_jaccards: list[float] = []
    p5_perfect = 0
    p6_jaccards: list[float] = []
    p6_version_mismatch: list[tuple[str, str | None, str | None]] = []
    missing: list[str] = []

    for lang in langs:
        p1 = compare_phase(baseline_dir, rerun_dir, lang, "P1", extract_p1_core_forms)
        p5 = compare_phase(baseline_dir, rerun_dir, lang, "P5", extract_p5_core_oppositions)
        p6 = compare_p6_script_content(baseline_dir, rerun_dir, lang)

        def fmt(r: PhaseResult | None) -> str:
            if r is None:
                return "N/A"
            return f"{r.jaccard*100:5.1f}% ({r.intersection}/{r.union})"

        if p6 is None:
            p6_str = "N/A"
            p6_result = None
        else:
            p6_result, base_ver, rerun_ver = p6
            p6_str = fmt(p6_result)
            if base_ver and rerun_ver and base_ver != rerun_ver:
                p6_version_mismatch.append((lang, base_ver, rerun_ver))

        if p1 is None or p5 is None or p6 is None:
            missing.append(lang)

        emit(out, f"{lang:<6} {fmt(p1):<22} {fmt(p5):<22} {p6_str:<22}")

        if p1 is not None:
            p1_jaccards.append(p1.jaccard)
        if p5 is not None:
            p5_jaccards.append(p5.jaccard)
            if p5.jaccard == 1.0:
                p5_perfect += 1
        if p6_result is not None:
            p6_jaccards.append(p6_result.jaccard)

    emit(out)
    emit(out, "=== Summary ===")
    if p1_jaccards:
        lo, hi = min(p1_jaccards), max(p1_jaccards)
        mean = sum(p1_jaccards) / len(p1_jaccards)
        emit(out, f"P1 core vocab Jaccard:    range {lo*100:.0f}–{hi*100:.0f}%, mean {mean*100:.0f}% across {len(p1_jaccards)} languages")
    if p5_jaccards:
        lo, hi = min(p5_jaccards), max(p5_jaccards)
        mean = sum(p5_jaccards) / len(p5_jaccards)
        emit(out, f"P5 core oppositions:      {p5_perfect}/{len(p5_jaccards)} perfect match — range {lo*100:.0f}–{hi*100:.0f}%, mean {mean*100:.0f}%")
    if p6_jaccards:
        lo, hi = min(p6_jaccards), max(p6_jaccards)
        mean = sum(p6_jaccards) / len(p6_jaccards)
        emit(out, f"P6 content (script-token) Jaccard: range {lo*100:.0f}–{hi*100:.0f}%, mean {mean*100:.0f}%")
    if p6_version_mismatch:
        emit(out)
        emit(out, "Protocol-version mismatch on P6 (baseline vs rerun):")
        for lang, b, r in p6_version_mismatch:
            emit(out, f"  {lang}: v{b} → v{r}")
        emit(out, "(P6 comparison uses script-token overlap because the v3.3 → v3.4 prompt change reorganised section headers; the token-level content metric is robust to formatting drift.)")
    if missing:
        emit(out)
        emit(out, f"Note: missing P1/P5/P6 output for: {', '.join(missing)}")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(
        description="Compare two CLCA-Revision pipeline runs for within-protocol reproducibility.",
    )
    parser.add_argument("--baseline", type=Path, default=Path("data"),
                        help="Baseline data root (default: data)")
    parser.add_argument("--rerun", type=Path, default=Path("data_reproducibility"),
                        help="Rerun data root (default: data_reproducibility)")
    parser.add_argument("--set", choices=["A", "B", "all"], default="all",
                        help="Which language set to compare (default: all)")
    parser.add_argument("--output", type=Path, default=None,
                        help="Optional output file for the report (default: stdout)")
    args = parser.parse_args()

    if not args.baseline.is_dir():
        print(f"!! baseline directory not found: {args.baseline}", file=sys.stderr)
        return 2
    if not args.rerun.is_dir():
        print(f"!! rerun directory not found: {args.rerun}", file=sys.stderr)
        return 2

    if args.set == "A":
        langs = SET_A
    elif args.set == "B":
        langs = SET_B
    else:
        langs = SET_A + SET_B

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        with args.output.open("w", encoding="utf-8") as out:
            report(args.baseline, args.rerun, langs, out)
            # Also mirror to stdout for convenience
        print(args.output.read_text(encoding="utf-8"))
    else:
        report(args.baseline, args.rerun, langs, sys.stdout)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
