import argparse
import sys
import tomllib
from pathlib import Path


REQUIRED_P_STEPS = [
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

REQUIRED_I_STEPS = [
    "I1_construction_equivalence",
]

REQUIRED_F_STEPS = [
    "F1_vocab_table",
    "F2a_derivation_table",
    "F2b_constructions_table",
    "F3_semantic_groups_table",
    "F4_construction_table",
    "F5_opposition_table",
    "F6_naturalness_table",
]


def check_language(lang_code: str, data_root: Path, skip_format: bool = False):
    lang_dir = data_root / lang_code
    print(f"\n=== Checking language: {lang_code} ===")

    if not lang_dir.exists():
        print(f"❌ MISSING: data/{lang_code}/ (directory not found)")
        return False

    ok = True

    # Check P files
    for step in REQUIRED_P_STEPS:
        fp = lang_dir / f"{step}.content.txt"
        if not fp.exists():
            print(f"❌ Missing P-step: {fp}")
            ok = False
        else:
            print(f"✔ Found {fp.name}")

    # Check I files
    for step in REQUIRED_I_STEPS:
        fp = lang_dir / f"{step}.interpret.txt"
        if not fp.exists():
            print(f"❌ Missing I-step: {fp}")
            ok = False
        else:
            print(f"✔ Found {fp.name}")

    # Check F files
    if not skip_format:
        for step in REQUIRED_F_STEPS:
            fp = lang_dir / f"{step}.format.txt"
            if not fp.exists():
                print(f"❌ Missing F-step: {fp}")
                ok = False
            else:
                print(f"✔ Found {fp.name}")

    # Context log
    context_file = lang_dir / "context.jsonl"
    if not context_file.exists():
        print(f"❌ Missing context: {context_file}")
        ok = False
    else:
        print(f"✔ Found context.jsonl")

    return ok


def main():
    parser = argparse.ArgumentParser(description="Verify CLCA language completeness.")
    parser.add_argument("config", help="Path to language config TOML file")
    parser.add_argument("--data-dir", default="data", help="Root data directory (default: data)")
    args = parser.parse_args()

    config_path = Path(args.config)

    if not config_path.exists():
        print(f"Configuration file not found: {config_path}")
        sys.exit(1)

    with config_path.open("rb") as fh:
        config = tomllib.load(fh)

    languages = config.get("languages", [])
    skip_format = config.get("skip_format", False)

    if not languages:
        print("No languages listed under [languages] in TOML file.")
        sys.exit(1)

    data_root = Path(args.data_dir)

    print("\n============================================")
    print("  CLCA 3.1 LANGUAGE COMPLETENESS VERIFIER")
    print("============================================\n")

    all_ok = True
    for lang in languages:
        if not check_language(lang, data_root, skip_format):
            all_ok = False

    print("\n============================================")
    if all_ok:
        print("  ✔ All languages are complete.")
        print("============================================\n")
        sys.exit(0)
    else:
        print("  ❌ Missing files found.")
        print("============================================\n")
        sys.exit(2)


if __name__ == "__main__":
    main()
