"""AOML JSON patch: LIFE (primary axis) → LIKE (meta-axis) + Rule R8.

Reads ``aoml/aoml_constraint_matrix.json``, applies the meta-axis revision
from ``data_union/aoml_LIKE_revision_draft.md``, and writes the result to
``aoml/aoml_constraint_matrix.LIKE_patch.json`` for review.

The original file is NOT overwritten. After review, adopt by:

    mv aoml/aoml_constraint_matrix.LIKE_patch.json aoml/aoml_constraint_matrix.json

Architecture change: the former LIFE primary axis is removed and replaced
by the LIKE meta-axis (the grammaticalized similative — "resembles A
without being A"), joining DEG and TEMP. Primary axes return to 6 (VER,
AUTH, SINC, NORM, ESS, VERIF). VERISIMILITUDE is now LIKE[VER]; lifelikeness
is the aesthetic subset of LIKE[VER]. A new substitution-prohibition rule
R8 (LIKE[A] cannot substitute for A) is added, parallel to R5 (DEG) and
R6 (TEMP).

Notation: the token is always written LIKE[host] in brackets; bare
lowercase "like" is the ordinary English word.

Idempotent: re-running on an already-patched file is a no-op.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

SRC = Path("aoml/aoml_constraint_matrix.json")
DST = Path("aoml/aoml_constraint_matrix.LIKE_patch.json")


LIKE_META_AXIS_ENTRY = {
    "name": "LIKENESS / SIMILATIVE",
    "prior_name": "LIFE / LIFELIKENESS (was a primary axis in v2.1)",
    "description": (
        "Similative modifier. The appearance of a primary-axis property "
        "without the actual property: LIKE[A] = 'resembles A without being "
        "A'. The grammaticalized similative — every cross-linguistic "
        "lexicalization uses a truth-stem + similative compound (Latin "
        "vēri-similis, Tagalog parang totoo 'like-true', Quechua cheqa hina "
        "'like-genuine', Sanskrit -ābhāsa, Chinese 逼真, Greek αληθοφανής). "
        "Host-dependent valence: positive for VER in the aesthetic register "
        "(lifelikeness, the goal of representational art), negative for AUTH "
        "(forgery), SINC (hypocrisy), VERIF (sophistry), NORM (sham "
        "legitimacy), ESS (illusion). The VER instance, LIKE[VER], is "
        "verisimilitude (the case Latin named); lifelikeness is its "
        "aesthetic subset. Distinct from DEG: DEG[A] is how-much-A on A's "
        "scale; LIKE[A] is resembles-A off A's scale."
    ),
    "instances": {
        "LIKE[VER]": "verisimilitude (aesthetic subset: lifelikeness; epistemic subset: plausibility/truthiness)",
        "LIKE[AUTH]": "forgery / counterfeit",
        "LIKE[SINC]": "feigned sincerity / hypocrisy",
        "LIKE[VERIF]": "pseudo-proof / sophistry (sa pramāṇābhāsa, hetvābhāsa)",
        "LIKE[NORM]": "sham legitimacy / demagoguery",
        "LIKE[ESS]": "mere appearance / illusion (sa ābhāsa)",
    },
    "inherits_operators_from": "host primary axis",
    "substitution_constraint": (
        "LIKE[A] cannot substitute for A in any inference step. See "
        "Structural Rule R8. The R8 violation per host axis is a named "
        "deception: forgery (AUTH), sophistry (VERIF), hypocrisy (SINC), "
        "demagoguery (NORM), truthiness (VER), illusion (ESS)."
    ),
    "distinct_from_DEG": (
        "DEG[A] = how-much-A, on A's own scale (half-true, more accurate). "
        "LIKE[A] = resembles-A, off A's scale (plausible-but-false, "
        "lifelike-but-fake). A half-truth (DEG[VER]) and a plausible "
        "falsehood (LIKE[VER]) are different objects."
    ),
    "empirical_status": (
        "Confirmed by the 16-language union pipeline. Lexicalized at [CORE] "
        "in ~12 of 16 languages; the truth-stem+similative template is "
        "morphologically transparent in 6 unrelated traditions. Set B G7b "
        "independently recommended meta-axis (not primary-axis) status."
    ),
}

R8_RULE = {
    "name": "LIKE Meta-Axis Substitution Prohibition",
    "formal": "LIKE[A] cannot substitute for A in any inference step",
    "description": (
        "Resembling an A-property cannot establish the A-property. Likeness "
        "is not the host property. This single rule unifies a class of "
        "classical deceptions: each is LIKE[host] passed off as host."
    ),
    "examples": [
        "A forgery (LIKE[AUTH]) passed as genuine (AUTH) — Forgery / counterfeiting",
        "A specious argument (LIKE[VERIF]) passed as valid (VERIF) — Sophistry",
        "Performed sincerity (LIKE[SINC]) passed as genuine (SINC) — Hypocrisy",
        "The appearance of legitimacy (LIKE[NORM]) passed as legitimacy (NORM) — Demagoguery",
        "A claim that looks true (LIKE[VER]) passed as true (VER) — Truthiness",
    ],
    "empirical_status": (
        "Confirmed by the 16-language union pipeline. Sanskrit lexicalizes "
        "the prohibition directly: 'hetvābhāsaḥ na hetuḥ' — a pseudo-reason "
        "is not a reason."
    ),
    "ufa_type": "Type 2 — Operator Overextension (Meta-Axis Substitution subtype)",
}

REVEAL_KEY_DIAGNOSTIC = (
    "REVEAL operates on a latent host-axis truth-state. The former "
    "'LIFE blocks REVEAL' diagnostic is superseded by the reclassification "
    "of likeness as a meta-axis: LIKE[A] is resemblance with no latent A to "
    "disclose, so REVEAL has no host truth-state to operate on — this "
    "follows from the meta-axis structure, not a separate primitive "
    "diagnostic. REVEAL's primitive-vs-derived status should be evaluated on "
    "its own evidence (the intransitive truth-revelation construction "
    "attested in all 16 languages), not via the likeness diagnostic."
)

PROVISIONAL_OPERATOR_NOTE = (
    "REVEAL is provisionally licensed for VER, AUTH, SINC, NORM, ESS, "
    "VERIF. Likeness is now a meta-axis (LIKE); REVEAL has no latent host "
    "truth-state to disclose for LIKE[A], so the former LIFE block is moot. "
    "Excluded from core matrix pending cross-architectural validation."
)


def _rename_key(d: dict, old: str, new: str, new_value=None) -> bool:
    if old not in d:
        return False
    items = []
    for k, v in d.items():
        items.append((new, new_value if new_value is not None else v) if k == old else (k, v))
    d.clear()
    d.update(items)
    return True


def main() -> int:
    if not SRC.exists():
        print(f"ERROR: {SRC} not found", file=sys.stderr)
        return 1

    data = json.loads(SRC.read_text(encoding="utf-8"))
    primary_axes = data["layer_1"]["primary_axes"]["axes"]
    meta_axes = data["layer_1"]["meta_axes"]["axes"]

    if "LIKE" in meta_axes and "LIFE" not in primary_axes:
        print(f"{SRC} already patched (LIKE in meta_axes, no LIFE). Nothing to do.")
        return 0

    changes: list[str] = []

    if "LIFE" in primary_axes:
        del primary_axes["LIFE"]
        changes.append("primary_axes: removed LIFE (now 6: VER, AUTH, SINC, NORM, ESS, VERIF)")

    if "LIKE" not in meta_axes:
        meta_axes["LIKE"] = LIKE_META_AXIS_ENTRY
        changes.append("meta_axes: added LIKE (joins DEG, TEMP — 3 meta-axes)")

    rules = data["layer_3"]["structural_rules"]["rules"]
    if "R8" not in rules:
        rules["R8"] = R8_RULE
        changes.append("structural_rules: added R8 (LIKE[A] cannot substitute for A)")

    empirical = data["layer_1"].get("levels", {}).get("EMPIRICAL", {})
    if "LIFE" in empirical.get("default_axes", []):
        empirical["default_axes"].remove("LIFE")
        changes.append("levels.EMPIRICAL.default_axes: removed LIFE")

    subregions = data["layer_2"]["subregions"]
    if "LIFE" in subregions:
        del subregions["LIFE"]
        changes.append("layer_2.subregions: removed LIFE (meta-axes have no subregions)")

    habitats = data["layer_3"]["validation_habitats"]["habitats"]
    if "LIFE" in habitats:
        del habitats["LIFE"]
        changes.append("validation_habitats: removed LIFE (LIKE inherits host habitat)")

    classes = data["layer_3"]["target_type_classes"]["classes"]
    for cls_name, cls in classes.items():
        axes = cls.get("primary_axes", [])
        if "LIFE" in axes:
            axes.remove("LIFE")
            changes.append(f"target_type_classes.{cls_name}: removed LIFE (LIKE is not a target type)")

    matrix = data["core_legality_matrix"]["axes_x_operators"]
    if "LIFE" in matrix:
        del matrix["LIFE"]
        changes.append("core_legality_matrix.axes_x_operators: removed LIFE row (meta-axes inherit, no own row)")

    abstr = data["layer_1"]["core_operators"]["operators"].get("ABSTR", {})
    exceptions = abstr.get("exceptions", {})
    if "LIFE" in exceptions:
        del exceptions["LIFE"]
        changes.append("ABSTR.exceptions: removed LIFE (LIKE inherits ABSTR from host; old block moot)")

    reveal = data["layer_1"]["provisional_operator"]["REVEAL"]
    if "key_diagnostic" in reveal:
        reveal["key_diagnostic"] = REVEAL_KEY_DIAGNOSTIC
        changes.append("REVEAL.key_diagnostic: reframed (meta-axis consequence, not separate diagnostic)")
    prov = reveal.get("provisional_licensing", {})
    if "LIFE" in prov:
        del prov["LIFE"]
        changes.append("REVEAL.provisional_licensing: removed LIFE (no latent host truth-state for LIKE)")

    core = data["core_legality_matrix"]
    if "provisional_operator_note" in core:
        core["provisional_operator_note"] = PROVISIONAL_OPERATOR_NOTE
        changes.append("provisional_operator_note: reframed for LIKE meta-axis")

    DST.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {DST}")
    print()
    print(f"Applied {len(changes)} changes:")
    for c in changes:
        print(f"  - {c}")
    print()
    print("Sanity:")
    print(f"  primary axes: {list(primary_axes.keys())}")
    print(f"  meta axes:    {list(meta_axes.keys())}")
    print(f"  rules:        {list(rules.keys())}")
    print()
    print("To diff:  diff aoml/aoml_constraint_matrix.json " + str(DST))
    print("To adopt: mv " + str(DST) + " aoml/aoml_constraint_matrix.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
