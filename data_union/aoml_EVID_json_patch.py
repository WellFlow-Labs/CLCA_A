"""AOML JSON patch: add EVID meta-axis + Rule R9 (Option A).

Chains on the LIKE patch. Reads ``aoml/aoml_constraint_matrix.LIKE_patch.json``
(the LIKE-patched proposed state) and writes
``aoml/aoml_constraint_matrix.LIKE_EVID_patch.json`` with EVID added.

If the LIKE patch hasn't been generated yet, run aoml_LIKE_json_patch.py
first (this script will error with a clear message otherwise).

Adds EVID as a fourth meta-axis (DEG, TEMP, LIKE, EVID) — the
grammaticalized source-of-knowledge modulation — and R9 (EVID[A] cannot
substitute for A). See aoml_EVID_revision_draft.md, including §4 (the
meta-axis-vs-habitat-correlate design fork).

Idempotent: re-running on an already-EVID-patched file is a no-op.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

SRC = Path("aoml/aoml_constraint_matrix.LIKE_patch.json")
DST = Path("aoml/aoml_constraint_matrix.LIKE_EVID_patch.json")


EVID_META_AXIS_ENTRY = {
    "name": "EVIDENTIALITY",
    "description": (
        "Source-of-knowledge modifier. EVID[A] marks how the claimant knows "
        "A — direct (witnessed/perceived), reported (hearsay/testimony), or "
        "conjectural (inferred). A grammatical category (one of the most "
        "robustly attested cross-linguistically); grammaticalized as an "
        "obligatory three-way enclitic system in Quechua (-m/-mi direct, "
        "-s/-si reported, -chá conjectural), lexical in all attested "
        "languages. Distinct from DEG: DEG[A] is how-much-A (confidence "
        "magnitude); EVID[A] is on-what-basis-A (source kind). Distinct from "
        "the validation-habitat layer: habitats state which method is "
        "admissible for an axis (normative); EVID is the speaker's "
        "grammatical marking of source on the claim (descriptive). The "
        "conjectural value's magnitude face is DEG; its source face is EVID."
    ),
    "values": {
        "DIRECT": "witnessed / perceived firsthand (qu -m/-mi; ~ OBSERVATION habitat)",
        "REPORTED": "hearsay / testimony / 'it is said' (qu -s/-si; ~ TESTIMONY habitat)",
        "CONJECTURAL": "inferred / 'probably' (qu -chá; absorbs the source face of the proposed PROB)",
    },
    "inherits_operators_from": "host primary axis",
    "substitution_constraint": (
        "EVID[A] cannot substitute for A in any inference step. See "
        "Structural Rule R9. REPORTED[A] passed as A is Appeal to Authority "
        "/ hearsay-as-proof (also a Type 3 habitat mismatch where the axis "
        "excludes testimony); CONJECTURAL[A] passed as A is inference-as-proof."
    ),
    "empirical_status": (
        "Confirmed. The evidential/source dimension is cross-set: Set A D9 "
        "(Evidential Grounding and Proof) + D3 (source trustworthiness); Set "
        "B D8 (epistemic certainty and source of knowledge) + F-L (evidential "
        "constructional function). The grammaticalized three-way system is "
        "Quechua; the source distinction is lexical across the sample."
    ),
    "design_note": (
        "Overlaps the validation-habitat layer (REPORTED~TESTIMONY, "
        "DIRECT~OBSERVATION) and DEG (conjectural magnitude). Adopted as a "
        "distinct meta-axis to give the four grammatical modulations (DEG, "
        "TEMP, LIKE, EVID) a parallel treatment and to unify source-laundering "
        "under R9. See aoml_EVID_revision_draft.md §4 for the "
        "meta-axis-vs-habitat-correlate fork."
    ),
}

R9_RULE = {
    "name": "Evidentiality Meta-Axis Substitution Prohibition",
    "formal": "EVID[A] cannot substitute for A in any inference step",
    "description": (
        "The source from which a claim is known cannot establish the claim "
        "itself. That something is reported, or inferred, is not that it is "
        "the case. Unifies source-laundering: the evidential marking treated "
        "as the host-axis verdict."
    ),
    "examples": [
        "REPORTED[VER] passed as VER ('it is said to be true, therefore true') — Appeal to Authority / hearsay-as-proof",
        "CONJECTURAL[VER] passed as VER ('it can be inferred, therefore established') — inference-as-proof",
        "A reported-evidential claim used where the axis requires direct OBSERVATION — Type 3 habitat mismatch",
    ],
    "empirical_status": (
        "Confirmed by the union pipeline. The Quechua evidential enclitics "
        "grammaticalize the source distinction obligatorily; every language's "
        "hedging vocabulary (he savir, qu cheqachá) guards the substitution."
    ),
    "ufa_type": "Type 2 — Operator Overextension (Meta-Axis Substitution subtype); evidential/habitat mismatches also surface as Type 3",
}


def main() -> int:
    if not SRC.exists():
        print(
            f"ERROR: {SRC} not found. Run aoml_LIKE_json_patch.py first "
            "(EVID chains on the LIKE patch).",
            file=sys.stderr,
        )
        return 1

    data = json.loads(SRC.read_text(encoding="utf-8"))
    meta_axes = data["layer_1"]["meta_axes"]["axes"]
    rules = data["layer_3"]["structural_rules"]["rules"]

    if "EVID" in meta_axes and "R9" in rules:
        print(f"{SRC} already EVID-patched. Nothing to do.")
        return 0

    changes = []
    if "EVID" not in meta_axes:
        meta_axes["EVID"] = EVID_META_AXIS_ENTRY
        changes.append("meta_axes: added EVID (DEG, TEMP, LIKE, EVID — 4 meta-axes)")
    if "R9" not in rules:
        rules["R9"] = R9_RULE
        changes.append("structural_rules: added R9 (EVID[A] cannot substitute for A)")

    DST.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {DST}")
    print()
    print(f"Applied {len(changes)} changes:")
    for c in changes:
        print(f"  - {c}")
    print()
    print("Sanity:")
    print(f"  primary axes: {list(data['layer_1']['primary_axes']['axes'].keys())}")
    print(f"  meta axes:    {list(meta_axes.keys())}")
    print(f"  rules:        {list(rules.keys())}")
    print()
    print("To diff (shows just the EVID addition):")
    print(f"  diff aoml/aoml_constraint_matrix.LIKE_patch.json {DST}")
    print("To adopt the full LIKE+EVID state:")
    print(f"  mv {DST} aoml/aoml_constraint_matrix.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
