from __future__ import annotations

from pathlib import Path
from typing import Dict, List


DEFAULT_F_STEPS = [
    "F1_vocab_table",
    "F2a_derivation_table",
    "F2b_constructions_table",
    "F3_semantic_groups_table",
    "F4_construction_table",
    "F5_opposition_table",
    "F6_naturalness_table",
]


def load_language_tables(
    language_codes: List[str],
    data_root: Path | None = None,
    f_steps: List[str] | None = None,
) -> Dict[str, Dict[str, str]]:
    """
    Load F-phase formatted outputs for each language.

    Returns:
        {
          "ka": {
              "F1_vocab_table": "...",
              "F2_derivation_table": "...",
              ...
          },
          "yo": {
              ...
          },
          ...
        }

    Only *.format.txt files are loaded. Missing files are skipped.
    """

    if data_root is None:
        data_root = Path("data")

    if f_steps is None:
        f_steps = DEFAULT_F_STEPS

    result: Dict[str, Dict[str, str]] = {}

    for code in language_codes:
        lang_dir = data_root / code
        tables: Dict[str, str] = {}
        if not lang_dir.exists():
            # Skip silently; caller can decide how to handle missing languages
            result[code] = tables
            continue

        for step in f_steps:
            fname = lang_dir / f"{step}.format.txt"
            if fname.exists():
                tables[step] = fname.read_text(encoding="utf-8")

        result[code] = tables

    return result


def build_global_context_block(
    language_codes: List[str],
    data_root: Path | None = None,
    f_steps: List[str] | None = None,
) -> str:
    """
    Create a single text block that concatenates all F-phase tables for all
    requested languages in a clearly delimited format suitable for prompting.

    The format is:

        ### LANGUAGE <code>
        #### <F-step>
        <content>

    """
    tables_by_lang = load_language_tables(language_codes, data_root=data_root, f_steps=f_steps)

    blocks: list[str] = []

    for lang_code in language_codes:
        blocks.append(f"\n\n============================\n### LANGUAGE {lang_code}\n============================\n")
        tables = tables_by_lang.get(lang_code, {})

        if not tables:
            blocks.append(f"(No F-phase tables found for language code: {lang_code})\n")
            continue

        # Preserve a stable order of steps where possible
        step_keys = sorted(tables.keys())

        for step in step_keys:
            blocks.append(f"\n#### {step}\n")
            blocks.append(tables[step].strip())
            blocks.append("\n")

    return "".join(blocks)
