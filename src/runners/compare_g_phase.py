"""G-phase reproducibility comparison for CLCA-Revision pipeline.

Compares the *synthesis* layer of two complete pipeline runs — the G-phase
outputs that abstract away from the lexical noise of P-phase elicitation
and report cross-linguistic findings (semantic dimensions, candidate
universals, constraint-matrix cells).

This is the comparison Paper I §4.2 actually wants to make. P-phase
reproducibility (see ``compare_runs.py``) measures elicitation variance at
the lexical surface; G-phase reproducibility measures whether the
*scientific findings* converge across independent runs despite that
surface variance.

Comparisons performed:

* **G7a — Inferred semantic dimensions**: extract section headers of the
  form ``### Dn: NAME`` and compute Jaccard overlap on dimension names.
* **G7a — Inferred constructional functions**: extract ``### Cn: NAME``
  headers similarly.
* **G8 — Candidate universals**: extract section headers of the form
  ``### N.N HEADING`` along with their HIGH/MEDIUM/LOW confidence tag, and
  compute Jaccard on the set of HIGH-confidence universal headings.

Usage::

    python -m src.runners.compare_g_phase \\
        --baseline data \\
        --rerun data_reproducibility \\
        --set all \\
        --output data_reproducibility/g_phase_comparison_report.txt
"""
from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


# ---------------------------------------------------------------------------
# Extractors
# ---------------------------------------------------------------------------

def _normalize_heading(s: str) -> str:
    """Lower-case, collapse whitespace, strip surrounding punctuation."""
    s = re.sub(r"[\*_`]", "", s)
    s = re.sub(r"\s+", " ", s)
    return s.strip().lower().strip(".:,")


# Stopwords to drop from labels before keyword-overlap matching. Short
# function words plus generic linkers that appear in lots of labels and
# would otherwise produce spurious matches.
_LABEL_STOPWORDS = {
    "a", "an", "and", "as", "at", "but", "by", "for", "from", "in", "into",
    "of", "on", "or", "the", "to", "vs", "vs.", "with", "without", "is",
    "are", "be", "than", "between", "across", "their", "this", "that", "all",
    "across", "domain", "domains", "language", "languages", "term", "terms",
    "claim", "claims", "rating", "high", "medium", "low", "level", "levels",
    "system", "systems", "type", "types", "form", "forms", "kind", "kinds",
    "more", "less", "very", "general", "specific", "construction",
    "constructions",
}


def _label_keywords(label: str) -> set[str]:
    """Tokenise a normalised label into significant keyword stems.

    Used by the heuristic concept-matcher to recognise that e.g.
    'material authenticity' and 'authenticity of objects' name the same
    underlying concept despite different surface labels.
    """
    tokens = re.findall(r"[a-zA-Z]+", label.lower())
    return {
        t for t in tokens
        if len(t) >= 4 and t not in _LABEL_STOPWORDS
    }


def _greedy_concept_match(
    base_labels: set[str], rerun_labels: set[str], threshold: float = 0.25,
) -> tuple[list[tuple[str, str, float]], set[str], set[str]]:
    """Greedily pair baseline and rerun labels by keyword-overlap Jaccard.

    Returns ``(pairs, base_only, rerun_only)`` where ``pairs`` is a list of
    ``(baseline_label, rerun_label, jaccard)`` for matched concepts. A
    pair is created when the keyword Jaccard meets ``threshold``. Each
    label is used at most once; the greedy assignment takes the highest-
    Jaccard candidate first.
    """
    base_kw = {b: _label_keywords(b) for b in base_labels}
    rerun_kw = {r: _label_keywords(r) for r in rerun_labels}

    candidates: list[tuple[float, str, str]] = []
    for b, bk in base_kw.items():
        if not bk:
            continue
        for r, rk in rerun_kw.items():
            if not rk:
                continue
            inter = bk & rk
            if not inter:
                continue
            j = len(inter) / len(bk | rk)
            if j >= threshold:
                candidates.append((j, b, r))

    candidates.sort(reverse=True)  # highest Jaccard first
    used_b: set[str] = set()
    used_r: set[str] = set()
    pairs: list[tuple[str, str, float]] = []
    for j, b, r in candidates:
        if b in used_b or r in used_r:
            continue
        pairs.append((b, r, j))
        used_b.add(b)
        used_r.add(r)

    base_only = set(base_labels) - used_b
    rerun_only = set(rerun_labels) - used_r
    return pairs, base_only, rerun_only


def _section_body(text: str, section_header_regex: str) -> str | None:
    """Return the body of a ``## <section>`` section, or None if not found.

    The body runs from the section heading line through to the next
    ``##`` heading (or end-of-file). Section matching is case-insensitive
    to tolerate variations like ``## 2. Main recurring constructional
    functions`` vs. the title-cased ``## Constructional Function
    Inventory``.
    """
    m = re.search(
        rf"(?m)^##\s+{section_header_regex}.*?(?=^##\s|\Z)",
        text,
        re.DOTALL | re.IGNORECASE,
    )
    return m.group(0) if m else None


def _extract_table_rows_from_section(
    text: str, section_header_regex: str
) -> list[str]:
    """Pull markdown-table second-column cells from a named section.

    Handles two table schemas:

    * ``| <code> | <name> | ...``  — code in col 1, name in col 2 (the
      schema used by the matrix-style inventory rerun).
    * ``| <name> | <ALLOWED/BLOCKED/...> | ...``  — name in col 1,
      constraint values in cols 2+ (the schema GPT-5.4 used in V_5.4
      where the whole inventory only appears as the ``Semantic
      Dimension`` column of a constraint matrix).

    The function disambiguates by looking at column 2: if it's a
    constraint keyword (``ALLOWED``, ``BLOCKED``, ``VARIABLE``,
    ``INSUFFICIENT DATA``), col 1 is treated as the name. Otherwise the
    original ``code | name`` schema is assumed.
    """
    body = _section_body(text, section_header_regex)
    if body is None:
        return []
    constraint_keywords = {
        "allowed", "blocked", "variable", "insufficient data", "n/a", "—", "-",
    }
    rows: list[str] = []
    for line in body.splitlines():
        if not line.lstrip().startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 2:
            continue
        # Skip pipe-separator rows: any row whose cells are all dashes
        if all(set(c) <= {"-", " ", ":"} for c in cells):
            continue
        col1, col2 = cells[0], cells[1]
        # Skip header rows
        if col1.lower() in {"code", "id", "semantic dimension", "dimension"}:
            continue
        if not col1:
            continue
        # If col2 looks like a constraint cell, col1 is the dimension/construction name.
        if col2.lower() in constraint_keywords:
            rows.append(col1)
            continue
        # Otherwise assume ``code | name`` schema.
        if set(col1) <= {"-", " ", ":"}:
            continue
        if not col2 or set(col2) <= {"-", " ", ":"}:
            continue
        rows.append(col2)
    return rows


def _extract_table_column_headers_from_section(
    text: str, section_header_regex: str, skip_columns: int = 1,
) -> list[str]:
    """Return the column headers (excluding ``skip_columns`` leading cols)
    of the first pipe-table inside a named section.

    Used to recover construction-function names from a constraint matrix
    whose columns are constructions and whose rows are dimensions.
    """
    body = _section_body(text, section_header_regex)
    if body is None:
        return []
    for line in body.splitlines():
        if not line.lstrip().startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) <= skip_columns:
            continue
        headers = [
            c for c in cells[skip_columns:]
            if c and not set(c) <= {"-", " ", ":"}
        ]
        # If this is the dashes-separator line, keep looking
        if not headers:
            continue
        # First non-empty, non-separator row is the header row.
        return headers
    return []


def _extract_numbered_bold_from_section(
    text: str, section_header_regex: str, heading_level: int = 2,
) -> list[str]:
    """Return the bold names of numbered-list items in a named section.

    Matches list items of the form ``1. **Some Name**`` or
    ``1. **Some Name.**`` (trailing period inside the bold is tolerated).
    Used for GPT-5.4-style G7a inventories and Set B G8 universals where
    the items appear as numbered+bold under a heading like
    ``## 1. Main recurring semantic dimensions`` or
    ``## 1. Candidate Universals / Strong Tendencies``.
    """
    hashes = "#" * heading_level
    m = re.search(
        rf"(?m)^{hashes}\s+{section_header_regex}.*?(?=^{hashes}\s|\Z)",
        text,
        re.DOTALL | re.IGNORECASE,
    )
    if not m:
        return []
    body = m.group(0)
    return [
        match.group(1).strip().rstrip(".")
        for match in re.finditer(
            r"(?m)^\s*\d+\.\s+\*\*([^*]+?)\*\*", body
        )
    ]


def extract_g7a_dimensions(text: str) -> set[str]:
    """Return the set of inferred semantic dimensions named in G7a.

    Three markdown styles are accepted:

    - **Heading style** (original baseline): ``### Dn: NAME``
    - **Inline-bold style** (one rerun):     ``**Dn — Name:**``
    - **Table style** (other rerun):          ``| <code> | <name> |``
      inside a ``## Dimension Inventory`` / ``## Semantic Dimensions``
      section.

    Names are normalised (lower-cased, whitespace collapsed, surrounding
    punctuation stripped).
    """
    dims: set[str] = set()
    # ### D1: NAME       — original heading style
    for m in re.finditer(r"(?m)^###\s+D\d+\s*:\s*(.+)$", text):
        dims.add(_normalize_heading(m.group(1)))
    # **D1 — Name:** ... or **D-A: Name** ...
    # General form: **D<code><sep><name>**, where:
    #   <code> is digits and/or letters, optionally hyphen-prefixed
    #   <sep>  is colon, em-dash, en-dash, or hyphen
    for m in re.finditer(
        r"\*\*D[-\s]?[A-Za-z0-9]+\s*[:\-–—]\s*([^*\n]+?)\*\*", text
    ):
        dims.add(_normalize_heading(m.group(1)))
    dim_section_re = (
        r"(?:\d+\.\s*)?(?:Main\s+recurring\s+|Semantic\s+|Inferred\s+|Part\s+\d+:\s*)?"
        r"(?:Semantic\s+)?Dimension(?:s)?(?:\s+Inventory)?(?:\s*\(.*?\))?"
        r"(?:\s*\(rows\))?"
    )
    # Explicit dimension-inventory styles (table rows under a Dimensions
    # section, or GPT-5.4 numbered+bold list).
    for name in _extract_table_rows_from_section(text, dim_section_re):
        dims.add(_normalize_heading(name))
    for name in _extract_numbered_bold_from_section(text, dim_section_re):
        dims.add(_normalize_heading(name))
    # Fall back to the constraint-matrix row labels only if no explicit
    # inventory was found, since some pipelines duplicate the dimension
    # list as both an inventory and the row labels of the constraint matrix.
    if not dims:
        for name in _extract_table_rows_from_section(
            text, r"(?:Global\s+)?Constraint\s+Matrix"
        ):
            dims.add(_normalize_heading(name))
    return dims


def extract_g7a_constructions(text: str) -> set[str]:
    """Return the set of inferred constructional functions named in G7a.

    Same three styles as :func:`extract_g7a_dimensions`:
    ``### Cn: NAME`` / ``### CFn: NAME`` headings,
    ``**Cn — Name:**`` / ``**CFn — Name:**`` inline bold, or
    ``| CFn | Name |`` table rows under a ``## Constructional Function
    Inventory`` / ``## Constructional Functions`` section.

    The ``CF`` prefix is normalised away so ``C5`` and ``CF5`` count as
    the same concept.
    """
    cs: set[str] = set()
    # ### Cn: NAME or ### CFn: NAME — heading style
    for m in re.finditer(r"(?m)^###\s+(?:CF|C)\d+\s*:\s*(.+)$", text):
        cs.add(_normalize_heading(m.group(1)))
    # **CFn — Name:** or **CF-1: Name** — inline bold, accepting either
    # em-dash-then-colon or colon-only between code and name, and both
    # ``CF`` and ``C`` prefixes.
    for m in re.finditer(
        r"\*\*(?:CF|C)[-\s]?[A-Za-z0-9]+\s*[:\-–—]\s*([^*\n]+?)\*\*", text
    ):
        cs.add(_normalize_heading(m.group(1)))
    cs_section_re = (
        r"(?:\d+\.\s*)?(?:Main\s+recurring\s+|Inferred\s+|Part\s+\d+:\s*)?"
        r"Construction(?:al)?\s+Function(?:s)?(?:\s+Inventory)?(?:\s*\(.*?\))?"
        r"(?:\s*\(columns\))?"
    )
    # Explicit construction-function inventory (table rows or numbered+bold).
    for name in _extract_table_rows_from_section(text, cs_section_re):
        cs.add(_normalize_heading(name))
    for name in _extract_numbered_bold_from_section(text, cs_section_re):
        cs.add(_normalize_heading(name))
    # Fall back to constraint-matrix column headers only when no explicit
    # construction-function inventory was found (GPT-5.4 Set B style).
    if not cs:
        for name in _extract_table_column_headers_from_section(
            text, r"(?:Global\s+)?Constraint\s+Matrix", skip_columns=1,
        ):
            cs.add(_normalize_heading(name))
    return cs


@dataclass
class Universal:
    heading: str
    confidence: str | None  # "HIGH", "MEDIUM", "LOW", or None if not found

    def __hash__(self) -> int:
        return hash(self.heading)

    def __eq__(self, other) -> bool:
        return isinstance(other, Universal) and self.heading == other.heading


def extract_g8_universals(text: str) -> list[Universal]:
    """Return the list of candidate universals listed in G8.

    Looks for section headers ``### N.N HEADING`` (e.g.
    ``### 1.1 Core Lexical Oppositions``) and the ``**Confidence rating**:
    **HIGH/MEDIUM/LOW**`` line within each section.
    """
    out: list[Universal] = []
    # Universal-heading conventions seen across runs:
    #   ### 1.1 Heading text             (Set A baseline; flat numeric)
    #   ### CU-1. Heading text           (Set A rerun, Set B rerun; flat letter-prefix)
    #   ### CU-1: Heading text           (variant)
    #   #### CU-1: Heading text          (Set B baseline; nested under category)
    #   #### SU-1: ...                   (semantic universals)
    #   #### AU-1: ...                   (asymmetry universals)
    #   #### LU-1: ...                   (lexical universals)
    #   #### PU-1: ...                   (pragmatic universals)
    #
    # We capture universal codes only (CU/SU/AU/LU/PU) so outlier sections
    # (## 2. Major Outliers — L-OUT-*, C-OUT-*, D-OUT-*) and open-question
    # sections (## 3. — OQ-*) are excluded.
    letter_re = re.compile(
        r"(?m)^#{3,4}\s+(?:CU|SU|AU|LU|PU)\s*-?\s*\d+\s*[.:]?\s+([^\n]+)$"
    )
    # Numeric ### 1.N headings are universals only if they fall in section 1.
    # We restrict to "1.N" so we don't capture ### 2.1 (outliers) etc.
    numeric_re = re.compile(r"(?m)^###\s+1\.\d+\s+([^\n]+)$")
    # GPT-5.4 Set A style: ``## N. heading text`` under ``# 1. Candidate
    # Universals`` (single-hash section divider). Section 2 (``# 2. Major
    # Outliers``) starts subsequent ``## A.`` style outlier headings, so we
    # only collect ``## N.`` headings that fall before ``# 2.``.
    gpt54_setA_re = re.compile(r"(?m)^##\s+\d+\.\s+([^\n]+)$")

    candidates: list[tuple[int, str]] = []
    for m in letter_re.finditer(text):
        candidates.append((m.start(), m.group(1)))
    for m in numeric_re.finditer(text):
        candidates.append((m.start(), m.group(1)))
    # Only apply the GPT-5.4 ``## N.`` style if the file actually uses
    # single-hash section dividers (``# 1. Candidate Universals``,
    # ``# 2. Major Outliers``, ...). Sonnet runs use ``## N.`` for the
    # section dividers themselves, which would over-capture if we ran
    # this pattern unconditionally.
    h1_iter = list(re.finditer(r"(?m)^#\s+\d+\.\s+", text))
    if h1_iter:
        cap_end = h1_iter[1].start() if len(h1_iter) >= 2 else len(text)
        for m in gpt54_setA_re.finditer(text):
            if m.start() >= cap_end:
                break
            candidates.append((m.start(), m.group(1)))
    # GPT-5.4 Set B style: ``N. **heading.**`` numbered+bold under
    # ``## 1. Candidate Universals / Strong Tendencies``. We treat each such
    # item as one universal heading.
    setB_section_re = (
        r"(?:\d+\.\s*)?Candidate\s+Universals"
        r"(?:\s*[/\-—–]\s*Strong\s+Tendencies)?"
    )
    setB_body_match = re.search(
        rf"(?m)^##\s+{setB_section_re}.*?(?=^##\s|\Z)",
        text,
        re.DOTALL,
    )
    if setB_body_match:
        body = setB_body_match.group(0)
        body_offset = setB_body_match.start()
        for m in re.finditer(r"(?m)^\s*\d+\.\s+\*\*([^*]+?)\*\*", body):
            candidates.append((body_offset + m.start(), m.group(1).rstrip(".")))
    candidates.sort(key=lambda x: x[0])

    # Synthesise "match" objects with start positions for section-body extraction
    matches = candidates
    for i, (start_pos, heading_text) in enumerate(matches):
        heading = heading_text.strip()
        section_end = matches[i + 1][0] if i + 1 < len(matches) else len(text)
        # Body runs from end-of-this-line to start of next universal heading.
        nl = text.find("\n", start_pos)
        section_start = nl + 1 if nl >= 0 else start_pos
        body = text[section_start:section_end]
        # Strip markdown emphasis so the regex can see the actual words.
        plain = re.sub(r"[*_`]", "", body)
        # Look for "Confidence" (anywhere in the section, near the end usually)
        # followed within ~30 chars by HIGH / MEDIUM-HIGH / MEDIUM / MEDIUM-LOW / LOW.
        conf_m = re.search(
            r"Confidence[^\n]{0,40}?(MEDIUM[\s\-]?HIGH|MEDIUM[\s\-]?LOW|HIGH|MEDIUM|LOW)",
            plain,
            re.IGNORECASE,
        )
        conf = conf_m.group(1).upper().replace(" ", "-") if conf_m else None
        out.append(Universal(_normalize_heading(heading), conf))
    return out


# ---------------------------------------------------------------------------
# Comparison
# ---------------------------------------------------------------------------

@dataclass
class SetComparison:
    baseline_n: int
    rerun_n: int
    intersection: int
    union: int

    @property
    def jaccard(self) -> float:
        return self.intersection / self.union if self.union else 1.0

    def format(self) -> str:
        return f"{self.jaccard*100:5.1f}% ({self.intersection}/{self.union})"


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _find_global_file(global_dir: Path, prefix: str) -> Path | None:
    """Return the first ``<prefix>*.global.txt`` file in ``global_dir``."""
    for path in sorted(global_dir.glob(f"{prefix}_*.global.txt")):
        if path.is_file():
            return path
    return None


def compare_one_set(
    baseline_root: Path,
    rerun_root: Path,
    set_code: str,
    out,
) -> None:
    """Compare G-phase outputs for one language set (``global_set_A`` or B)."""
    base_dir = baseline_root / set_code
    rerun_dir = rerun_root / set_code

    emit(out, f"\n## {set_code}")
    if not rerun_dir.is_dir():
        emit(out, f"  (rerun directory missing: {rerun_dir})")
        return

    # Some runs put dimensions/constructions inside G7a; others factor them
    # out into G3/G5. Check G7a first, then fall back.
    base_g7a = _find_global_file(base_dir, "G7a")
    rerun_g7a = _find_global_file(rerun_dir, "G7a")

    def _report_set(label: str, bset: set[str], rset: set[str]) -> None:
        """Report both strict-label and concept-level (keyword-Jaccard) overlap."""
        # Strict (exact label match)
        strict = SetComparison(len(bset), len(rset),
                               len(bset & rset), len(bset | rset))
        # Concept (heuristic keyword-overlap match)
        pairs, base_only, rerun_only = _greedy_concept_match(bset, rset)
        matched = len(pairs)
        total = matched + len(base_only) + len(rerun_only)
        concept_jaccard = matched / total if total else 1.0
        emit(out, f"  {label}")
        emit(out, f"    strict match (exact label): {strict.format()}")
        emit(out, f"    concept match (keyword overlap, ≥0.25 Jaccard): "
                 f"{concept_jaccard*100:5.1f}% ({matched}/{total})")
        if pairs:
            emit(out, "      paired concepts:")
            for b, r, j in sorted(pairs, key=lambda x: -x[2]):
                marker = "≡" if b == r else "≈"
                emit(out, f"        {b}  {marker}  {r}  (Jaccard {j:.2f})")
        if base_only:
            emit(out, f"      baseline only: {', '.join(sorted(base_only))}")
        if rerun_only:
            emit(out, f"      rerun only:    {', '.join(sorted(rerun_only))}")

    if base_g7a and rerun_g7a:
        bdims = extract_g7a_dimensions(_read(base_g7a))
        rdims = extract_g7a_dimensions(_read(rerun_g7a))
        bcs = extract_g7a_constructions(_read(base_g7a))
        rcs = extract_g7a_constructions(_read(rerun_g7a))
        _report_set("G7a semantic dimensions:", bdims, rdims)
        _report_set("G7a constructional functions:", bcs, rcs)
    else:
        emit(out, "  G7a: missing on one or both sides")

    base_g8 = _find_global_file(base_dir, "G8")
    rerun_g8 = _find_global_file(rerun_dir, "G8")

    if base_g8 and rerun_g8:
        bu = extract_g8_universals(_read(base_g8))
        ru = extract_g8_universals(_read(rerun_g8))
        b_all = {u.heading for u in bu}
        r_all = {u.heading for u in ru}
        b_high = {u.heading for u in bu if u.confidence == "HIGH"}
        r_high = {u.heading for u in ru if u.confidence == "HIGH"}
        _report_set("G8 universals (all):", b_all, r_all)
        _report_set("G8 universals (HIGH conf.):", b_high, r_high)
    else:
        emit(out, "  G8: missing on one or both sides")


# ---------------------------------------------------------------------------
# Reporting
# ---------------------------------------------------------------------------

def emit(out, line: str = "") -> None:
    out.write(line + "\n")


def report(baseline_root: Path, rerun_root: Path, sets: Iterable[str], out) -> None:
    emit(out, "# CLCA G-phase reproducibility comparison")
    emit(out, f"# baseline: {baseline_root}")
    emit(out, f"# rerun:    {rerun_root}")
    emit(out, f"# sets: {', '.join(sets)}")
    for s in sets:
        compare_one_set(baseline_root, rerun_root, s, out)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Compare G-phase synthesis outputs across two CLCA pipeline runs.",
    )
    parser.add_argument("--baseline", type=Path, default=Path("data"),
                        help="Baseline data root (default: data)")
    parser.add_argument("--rerun", type=Path, default=Path("data_reproducibility"),
                        help="Rerun data root (default: data_reproducibility)")
    parser.add_argument("--set", choices=["A", "B", "all"], default="all",
                        help="Which set's G-phase to compare (default: all)")
    parser.add_argument("--output", type=Path, default=None,
                        help="Optional output file (default: stdout)")
    args = parser.parse_args()

    if not args.baseline.is_dir():
        print(f"!! baseline directory not found: {args.baseline}", file=sys.stderr)
        return 2
    if not args.rerun.is_dir():
        print(f"!! rerun directory not found: {args.rerun}", file=sys.stderr)
        return 2

    if args.set == "A":
        sets = ["global_set_A"]
    elif args.set == "B":
        sets = ["global_set_B"]
    else:
        sets = ["global_set_A", "global_set_B"]

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        with args.output.open("w", encoding="utf-8") as f:
            report(args.baseline, args.rerun, sets, f)
        print(args.output.read_text(encoding="utf-8"))
    else:
        report(args.baseline, args.rerun, sets, sys.stdout)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
