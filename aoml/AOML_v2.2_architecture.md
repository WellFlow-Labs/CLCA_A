# AOML v2.2 — Semantic Constraint Architecture

**Status:** Stage 2 consolidation. This is the human-readable reference for AOML v2.2, built from v2.1 plus the 16-language union-pipeline delta (`data_union/aoml_v2.2_delta_from_union.md`). The machine-readable companion is `aoml/aoml_constraint_matrix_v2.2.json`. The v2.1 JSON and the read-only `Aoml_v2.1_constraint_architecture.html` remain the frozen baseline. `Aoml_v2.2_constraint_architecture.html` is the rendered HTML companion of this document — regenerated from it, not an independent input (it replaced an earlier abandoned "causal-fabrication" v2.2 draft); this Markdown remains the source of truth.

**Evidence base:** All empirical claims are tagged by source:
- **[CLCA-BOTH]** — attested in both independent language sets (Set A: ka yo fi eu ta id tr ko; Set B: zh he sa el en tl sw qu), no shared languages. Strongest tier.
- **[CLCA-A] / [CLCA-B]** — single set.
- **[FALLACY]** — supported by the fallacy map / oAOML rather than cross-linguistic lexicalization (legitimate, but a different instrument — as with TEMP).

---

## What changed from v2.1

1. **LIFE primary axis → LIKE meta-axis.** Verisimilitude was misclassified as a primary axis. It is the grammaticalized **similative** ("resembles A without being A"), a modulator of any host axis. Verisimilitude is now `LIKE[VER]`; lifelikeness is its aesthetic subset. Primary axes: 7 → **6**.
2. **EVID meta-axis added.** Evidentiality (source-of-knowledge marking). Meta-axes: 2 → **4** (DEG, TEMP, LIKE, EVID).
3. **Three new structural rules.** R7 (agentive polarity asymmetry), R8 (LIKE substitution), R9 (EVID substitution).
4. **R1 refined** to distinguish direct causation (blocked) from indirect facilitation (attested).
5. **Empirical ratification** of the v2.1 core by the union pipeline (R1, R3, R4, REVEAL, ATTR/CONTR/ABSTR universals, DEG, target-type ontology — all [CLCA-BOTH]).
6. **CONTR / FRAME split.** What earlier formulations called "CONTR" conflated two layers — the **CONTR operator** (negative/contrastive attribution, CF2; an attested universal operator) and the **opposition FRAME** (the binary-by-default value-space each axis carves; the Type-5 precondition, Paper III). They are now distinguished (§1C, §1E); *mithyā* is a question about the FRAME's bivalence on ESS, not about a core operator (§6.6).

**Seven** proposed refinements were examined against the data (§6). **Six dissolved into existing structure** rather than new axes/values — SINC split → TEMP[host] (§6.1); NORM split → NORM's SINC rider under R1 (§6.2); AUTH neutral intermediate → LIKE[AUTH] + R8 (§6.3); VER/NORM gradient → a cross-axis conformity predicate (§6.4); partial-truth rule + deontic interaction → the deception principle and NORM-over-conduct (§6.5). The **seventh** — *mithyā* / the opposition FRAME — is the single genuine open conflict (§6.6, §7): it challenges the **bivalence of the FRAME** on the ESS axis (a Type-5 precondition question), not an operator or an axis. The 6-and-1 asymmetry is the architecture's honesty check (§5).

---

## Layer 1 — Claim structure

### 1A. Primary axes (6) — *what kind of truth is claimed?*

| Axis | Gloss | Default habitat | Union ratification |
|---|---|---|---|
| **VER** | Veridical — correspondence of a statement to fact | OBSERVATION / EXPERIMENT | core dimension, all langs |
| **AUTH** | Authenticity — genuineness of provenance | PROVENANCE | core; R3 confirmed [CLCA-BOTH] |
| **SINC** | Sincerity — inner alignment of person | TESTIMONY | core; R1 confirmed [CLCA-BOTH] |
| **NORM** | Normative — moral/legal/procedural rightness | PRINCIPLE / CONSENSUS | core, all langs |
| **ESS** | Essence — inherent/definitional nature | LOGIC | partial (R2 untested) |
| **VERIF** | Verification — evidential establishment | EXPERIMENT / STATISTICS / LOGIC | core, all langs |

*(LIFE removed — see §1B LIKE.)*

### 1B. Meta-axes (4) — *the grammatical modulations of a truth claim*

Meta-axes do not constitute independent claim types; they modulate a host primary axis, inherit its operator licensing, and **cannot substitute for it** (the substitution prohibitions R5/R6/R8/R9). The four correspond to four cross-linguistically robust grammatical categories:

| Meta-axis | Category | M[A] = | Substitution rule | Evidence |
|---|---|---|---|---|
| **DEG** | degree / intensity | how-much-A (very/half true) | R5 | [CLCA-BOTH] + [FALLACY] |
| **TEMP** | tense / aspect / persistence | when-A; sustained-A | R6 | **[CLCA-BOTH]** (via reliability, §6.1) + [FALLACY] |
| **LIKE** | similative | resembles-A (like-true) | R8 | [CLCA-BOTH] + [FALLACY] |
| **EVID** | evidentiality | on-what-basis-A (heard/inferred/seen) | R9 | [CLCA-BOTH] dimension; grammaticalized in qu |

**LIKE[A] — the similative.** "Resembles A without being A." Host-dependent valence: positive for `LIKE[VER]`-aesthetic (lifelikeness, the goal of art), negative elsewhere — `LIKE[AUTH]` = forgery, `LIKE[SINC]` = hypocrisy, `LIKE[VERIF]` = sophistry, `LIKE[NORM]` = demagoguery, `LIKE[ESS]` = illusion. Verisimilitude = `LIKE[VER]`. Grammaticalized via a truth-stem + similative compound in six unrelated traditions (Latin *vēri-similis*, Tagalog *parang totoo*, Quechua *cheqa hina*, Chinese 逼真, Greek αληθοφανής, Sanskrit *-ābhāsa*). Distinct from DEG: DEG is how-much (on A's scale); LIKE is resemblance (off A's scale). Full treatment: `data_union/aoml_LIKE_revision_draft.md`.

**EVID[A] — evidentiality.** Marks the source of knowledge: DIRECT (witnessed, qu *-m/-mi*), REPORTED (hearsay, qu *-s/-si*), CONJECTURAL (inferred, qu *-chá*). Grammaticalized three-way in Quechua; lexical across the sample. Distinct from DEG (magnitude vs. source-kind) and from the validation-habitat layer (normative admissibility vs. descriptive marking). Carries a noted overlap with TESTIMONY/OBSERVATION habitats and DEG — see `data_union/aoml_EVID_revision_draft.md` §4. Full treatment there.

### 1C. Operators (7 + 1 provisional)

ATTR, CAUSE, BECOME, RESULT, ABSTR, STRAT, CONTR — selectively licensed across axes. **CONTR** here is **negative/contrastive attribution** (CF2: morphological/syntactic negation of a truth-predicate — *not-true*, *unreliable*, *invalid*; the negative-pole partner of ATTR), universally licensed [CLCA-BOTH]; its operator-level misuse maps to **UFA Type 2**. CONTR is *not* the opposition FRAME (§1E) — earlier formulations conflated the two under one label. **REVEAL** (provisional primitive): disclosure of a latent pre-existing host-axis truth-state. The former "LIFE blocks REVEAL" diagnostic is retired — `LIKE[A]` is resemblance with no latent A to disclose, so the restriction follows from the meta-axis structure, not a separate diagnostic. REVEAL's primitive status rests on the intransitive truth-revelation construction attested in all 16 languages [CLCA-BOTH], pending cross-architectural validation.

### 1D. Levels (4)

EMPIRICAL, CONVENTIONAL, FORMAL, ULTIMATE — govern permissible inference across strata. Level-crossing without justification = UFA Type 4.

### 1E. The opposition FRAME — the precondition the matrix presupposes

Distinct from the CONTR operator (§1C): the **FRAME** is the *opposition topology* — the value-space each axis carves between a claim and its negation. It is **binary by default** (the foundational truth/falsehood antonym pair is universal — CU-10, [CLCA-BOTH]). The FRAME is the **precondition** that the Axis / Operator / Method / Level distinctions presuppose (Paper III's argument from distinction), not a coordinate operator. Misconfiguring it — imposing a binary where the space is N-ary (false dilemma), or collapsing a real distinction (false equivalence) — is **UFA Type 5 (Contrast Frame Collapse)**. *Why two layers, not one:* the union pipeline attests CF2 negation as a universal **operator** (it composes with every axis), while bivalence is a property of the per-axis **FRAME** (binary for every axis attested; challenged only on ESS — §6.6). Conflating them produced the old "is CONTR an operator or a precondition?" tension; the answer is *both*, because they are different things.

---

## Layer 2 — Subregions

Axis-internal lexical territories (e.g. AUTH: genuineness / forgery / provenance / imitation). Meta-axes have no subregions (they inherit from host).

---

## Layer 3 — Validation & structural rules

### 3A. Validation habitats

Each primary axis admits specific methods (VER: OBSERVATION/EXPERIMENT; SINC: TESTIMONY; ESS: LOGIC; …). Using an inadmissible method = **UFA Type 3**. Note the descriptive overlap with EVID: TESTIMONY ≈ EVID-REPORTED, OBSERVATION ≈ EVID-DIRECT (habitats are normative-admissibility; EVID is the speaker's source-marking).

### 3B. Target-type ontology

FACTUAL (VER, AUTH), EPISTEMIC (VERIF, VER-as-belief), DISPOSITIONAL (SINC). Governs differential CAUSE licensing — confirmed [CLCA-BOTH]: CAUSE licensed for factual targets, restricted for epistemic, blocked for dispositional.

### 3C. Structural rules R1–R9

| Rule | Statement | Status |
|---|---|---|
| **R1** | CAUSE × dispositional (SINC) → universally blocked | **confirmed [CLCA-BOTH]**, strongest single alignment. *v2.2 refinement:* blocks direct causation of the state, not indirect facilitation of conditions (eu *zintzotu eragin*, ko *진정성을 높이다*) nor BECOME (character development). |
| **R2** | CAUSE × ESS, BECOME × ESS → blocked | not tested by union pipeline (ESS-adjacent dims only in zh/sa) |
| **R3** | CAUSE(+) × AUTH blocked; CAUSE(−) × AUTH licensed | **confirmed [CLCA-BOTH]** — cannot manufacture authenticity; can forge |
| **R4** | Positive emergence bias: BECOME(+) natural, BECOME(−) marked | **confirmed [CLCA-BOTH]** |
| **R5** | DEG[A] ↛ A | confirmed; Appeal to Probability/Emotion/Populum |
| **R6** | TEMP[A] ↛ A; internal level-crossing → Type 4 | [FALLACY]; Sunk Cost, Appeal to Novelty, Presentism |
| **R7** | **Agentive polarity asymmetry** — ABSTR(agentive)×positive-pole blocked, ×negative-pole licensed | **confirmed [CLCA-BOTH]** (liar lexicalizes, truth-teller doesn't). Mechanism open. *New in v2.2.* |
| **R8** | **LIKE[A] ↛ A** | confirmed; unifies forgery (AUTH), sophistry (VERIF), hypocrisy (SINC), demagoguery (NORM), truthiness (VER), illusion (ESS). *New in v2.2.* |
| **R9** | **EVID[A] ↛ A** | confirmed [CLCA-BOTH] dimension; Appeal to Authority/hearsay-as-proof, inference-as-proof. *New in v2.2.* |

---

## 4. The meta-axis substitution family — the central result

R5, R6, R8, R9 are one structural pattern — **M[A] ↛ A** — instantiated on each of the four meta-axes. Each maps to **UFA Type 2** (Operator Overextension, meta-axis substitution subtype) and each unifies a class of fallacies:

| Rule | Meta-axis | "X[A] passed as A" yields |
|---|---|---|
| R5 | DEG | Appeal to Probability, Appeal to Emotion, Argumentum ad Populum |
| R6 | TEMP | Appeal to Novelty, Sunk Cost, Presentism |
| R8 | LIKE | Forgery, Sophistry, Hypocrisy, Demagoguery, Truthiness, Illusion |
| R9 | EVID | Appeal to Authority, Hearsay-as-proof, Inference-as-proof |

This is the central theoretical result of v2.2: **a single substitution schema over four grammatical modulations generates a large, principled family of classical fallacies.**

---

## 5. The stability principle

The six primary axes are load-bearing primitives. When the union pipeline surfaces an apparent need to *split* an axis or *add* a value, the refinement almost always resolves into an **existing orthogonal layer** — a meta-axis modulation (DEG/TEMP/LIKE/EVID), a level stratification, a subregion, or a cross-axis predicate — rather than a new axis. The working rule:

> **Prefer an orthogonal-layer resolution before enlarging the axis set.**

§6 applies this to all seven proposed refinements; §6.6 reports the single genuine residual that tests — and thereby vindicates — the principle.

---

## 6. Resolved refinements — the proposal arc

## 6.1 Reliability = TEMP[host] — resolves the SINC-split question, and grounds TEMP

The proposed SINC split is **withdrawn**. Reliability/dependability-over-time is not a SINC sub-axis; it is **TEMP applied to a host trust-axis** — the temporal-persistence (integral) modulation of sincerity (is the source honest, sustained?) and/or veridicality (are its outputs accurate, sustained?). Tested against the union vocabulary and confirmed on four predictions:

1. **Temporal-persistence semantics.** English separates them in its own lexicon: *credible* = "believability **rather than consistent performance**" (present-state); *reliable* = "**consistently** trusted to perform correctly over repeated use" (sustained-over-time). Reliability *is* the temporal reading.
2. **Integral behaviour.** Trust is *built, earned, lost, eroded, shaken, established* ([CORE] across he, tl, en, …) — accumulation and depletion over time, exactly v2.1's definition of TEMP as "the integral of the primary-axis claim over time."
3. **SINC+VER blend.** Reliability glosses fuse honesty (SINC) and accuracy (VER): "consistently trusted to perform correctly **or provide accurate information**." This is **why Set A and Set B cut the region along different seams** (A → content-credibility/VER; B → source-honesty/SINC): a TEMP-modulation over a blend gets carved differently by different samples. The cross-set instability that argued *against* splitting SINC is positive evidence *for* the TEMP reading.
4. **R1 is preserved, not relaxed.** No language lexicalizes a direct "make someone reliable" causative; reliability is *accumulated* (TEMP integral), not *caused*. The apparent "R1 relaxation" that motivated the split was TEMP integration all along.

**Consequences:** (a) SINC stays a single primary axis (R1 intact); reliability/faithfulness remain SINC subregions, now understood as the host of a TEMP modulation. (b) **TEMP gains its missing CLCA footing.** TEMP was the one meta-axis resting on fallacy evidence alone; reliability — robustly lexicalized in *both* sets with [CORE] build/erode constructions — gives it cross-linguistic [CLCA-BOTH] support. All four meta-axes (DEG, TEMP, LIKE, EVID) are now CLCA-attested. (c) Generative prediction (weakly confirmed, worth following up): the same sustained-over-time modulation should appear on other axes — attested as "reliably valid" (TEMP[VERIF/NORM]), "consistently correct" (TEMP[VER]).

---

## 6.2 NORM's SINC rider governs CAUSE — resolves the NORM-split question

The proposed NORM split (NORM-DEONTIC / NORM-INSTITUTIONAL) is **withdrawn**. NORM stays a single primary axis. The CAUSE-licensing asymmetry is governed by **NORM's SINC rider** — its substantive/moral pole carries a sincerity-like *constitutive* component, and the existing **R1** (CAUSE × constitutive/dispositional → blocked) acts on it. v2.1's flat "CAUSE × NORM: restricted" was unconditioned; the right account is the rider, not a freestanding new rule.

**The rider (as stated in the documents).** NORM's substantive pole is constitutive, not merely correspondence-tracking. Paper IV: *"NORM requires integrity of distinction (a normative claim whose constitutive distinction between right and wrong has collapsed is incoherent)."* GrokDiscussion poses it directly — *"What should we do about NORM? Isn't this like sincerity?"* — and answers yes: normative truths are *"partly constituted by reflective endorsement … (Korsgaard, Street)."* So substantive moral NORM carries a SINC rider; this is the same constitutive structure that Paper III identifies as "R1's structural source."

- **Substantive / moral NORM** (rider engaged): **CAUSE blocked via R1.** You cannot make something genuinely just any more than you can make someone sincere — external causation would collapse the constitutive distinction that defines the truth-condition. No language lexicalizes "make something just"; moral causatives touch *persons* (he *hitsdiq* "vindicated"), never ultimate rightness by decree.
- **Institutional / procedural NORM** (no rider — a *constituted status*, Searle's status functions): **CAUSE licensed, both polarities.** Validity is conferred and revoked by the proper institutional act: validate/invalidate, legitimize, ratify, annul are [CORE] across 7/8 languages (el *ακυρώνω* "annul a contract", tr *meşrulaştırmak* "legitimize", id *mengesahkan* "validate", sw *kuhalalisha*, he *letaqqef*).

The rider/no-rider distinction **correlates with level** (substantive-moral ≈ FORMAL/ULTIMATE; institutional ≈ CONVENTIONAL), but the *operative* mechanism is the SINC rider + R1, not level per se — which is why this resolution grounds in the framework's strongest existing rule rather than positing new level-conditioned CAUSE behaviour.

Set B's G7b reached the surface pattern independently: *"the restriction may apply primarily to the deontic sub-domain (causing someone to be morally right) rather than to the institutional sub-domain."* **[CLCA-BOTH]** — Set A also marks it (D5 "Legal/Procedural Validity vs. Moral/Substantive Legitimacy").

**Refinement adopted:** `CAUSE × NORM` is governed by **NORM's SINC rider** — blocked for the constitutive/moral pole (via R1), licensed for the institutional/constituted-status pole (no rider). Not a freestanding level rule; the rider does the work, and level only correlates. No axis split.

---

## 6.3 The AUTH neutral-copy is LIKE[AUTH]-acknowledged — resolves the AUTH-intermediate question

The proposed AUTH neutral intermediate is **withdrawn**. AUTH stays binary at the axis level (genuine / not-genuine); the empirically robust **three-way** genuine / copy / fake is AUTH plus the **LIKE meta-axis under R8** — no new axis value.

The data shows the three-way in ≥6 unrelated languages, with the diagnostic property that **the copy is neutral while the fake is negative**: ta *acal* (original) / *nakal* (copy — "neutral, a certified copy is a *nakal* without negative implication") / *pōli* (fake — "always negative"); fi *kopio* / *jäljitelmä* (imitation, lesser status) / *väärennös* (forgery, fraudulent); also eu *kopiakoa*/*faltsua*, id *tiruan*/*palsu*, tr *taklit*/*sahte*, ko *모조품*/*위조품*. That neutral-vs-negative asymmetry is precisely the acknowledged-vs-passed-off distinction already built into LIKE's valence (§1B):

- **genuine** = AUTH (the real thing)
- **neutral copy** = **LIKE[AUTH] acknowledged** — resembles genuine, openly presented as a copy. No R8 substitution → **neutral** (a labelled replica is harmless).
- **fraudulent fake** = **LIKE[AUTH] passed off as AUTH** — the **R8 violation** = forgery → **negative**.

This also resolves the CAUSE half of the proposal ("distinguish CAUSE(−) with vs. without fraudulent intent"). R3's `CAUSE(−) × AUTH: licensed` already covers *both* making a copy and making a forgery; the difference between them is **not** in the causation (R3) but in whether the product is then passed off as genuine (R8/LIKE). "Fraudulent intent" lives in the R8 substitution layer, not in a CAUSE refinement.

**Bonus:** this is direct cross-linguistic lexical evidence (6+ languages) for the acknowledged-vs-substituted distinction that R8 and LIKE's host-valence depend on — the copy/fake lexical split *is* the grammaticalization of "LIKE acknowledged vs LIKE passed off."

---

## 6.4 The VER/NORM "gradient" is a conformity predicate, not an axis merge — resolved

The proposed VER/NORM gradient (from the D1/D11 merger in yo and ta) is **withdrawn**. VER and NORM stay distinct primary axes. The "merger" is not a collapse of the axes; it is a **cross-axis conformity predicate** lexicalized by one root.

**The axes do not merge — the data confirms they stay distinct.** Both "merging" languages keep separate truth-vs-justice vocabulary: yo *òtítọ́* (factual truth) vs *òdodo* (moral rightness, glossed "distinct from *òtítọ́*"); ta *uṇmai* (truth) vs *niyāyam* (justice). What is shared is a single **correctness** root — yo *tọ́* ("conforms to a standard of correctness or propriety," used for "both factual correctness and moral rightness"), ta *cari* ("both epistemic [factual error] and moral [wrongdoing] registers").

**Correctness = conformity-to-standard, and the standard sets the axis.** Set B's D3 defines it exactly: "whether an answer, procedure, or action **meets a relevant standard**." A factual standard → conformity is on VER (correct answer); a normative standard → conformity is on NORM (correct conduct). The predicate is **axis-neutral**; it takes its axis from its standard argument. Languages that lexicalize the bare conformity relation (*tọ́*, *cari*, en *correct*) apply it across both, which *looks* like a VER/NORM merge but is the predicate's axis-neutrality, not a boundary instability. The axes remain distinct (different habitats, different CAUSE behaviour) — and yo/ta prove it by retaining separate truth and justice lexemes.

This is structurally the same kind of cross-axis predicate as **D12 deception** (= VER-falsity + SINC-intent) and the **deontic** constructions (NORM × {VER, SINC}, §6.5): a single lexicalized concept that ranges over more than one axis without collapsing them. No gradient, no axis restructuring; if anything the finding *strengthens* the VER/NORM distinction.

---

## 6.5 The deception principle resolves partial-truth and deontic (and clarifies D12)

Two pending proposals — the partial-truth rule and the deontic cross-axis interaction — both resolve through one observation about how SINC interacts with the rest of the framework.

**Partial-truth = R5 violation + SINC-intent.** A half-truth (*半真半假*, *ḥatsi ʾemet*, *half-truth*, *nusu ukweli*; 7/8 langs) is genuinely DEG[VER] — partly true on the degree scale. Deploying it *as if* it were the whole truth is exactly the **R5** substitution (DEG[VER] ↛ VER). What makes it *deception* rather than a mere inference error is that it is done deliberately to mislead — engaging **SINC**. The data confirms the moralization: partial truth is "actively evaluated as a form of dishonesty," not a weaker truth. No new rule: it is R5 + SINC-intent.

**The deception principle (general).** This generalizes across the whole framework:

> A structural violation — a false claim, or any meta-axis substitution M[A] ↛ A (R5/R6/R8/R9) — committed **knowingly, to mislead**, is a **SINC violation** (a lie). The *same* violation committed by mistake is an **innocent error**.

This is precisely Set A's **D12 (Deliberate Deception vs. Innocent Error)**, which the G7b had to map onto "two axes (VER-falsity + SINC-intent)." The principle states it cleanly: deception = (structural violation) + (SINC-intent); error = the violation without it. It unifies D12, partial-truth, forgery-vs-replica (§6.3, LIKE[AUTH] passed off *knowingly*), and sophistry-vs-honest-mistake under one account. No new axis; it names how SINC-intent converts any structural error into a lie.

**Deontic dissolves into NORM-over-conduct.** "One ought to tell the truth / ought not to lie" (*satyaṃ brūyāt*, *ama llullakuychu*, *usipige uongo*; F-J, all 8 langs) is a **NORM** claim whose object is a *truth-related act* (truth-telling, not-lying). NORM's domain is precisely the normative evaluation of conduct; truth-telling is conduct. So deontic is NORM operating on its normal domain, with a truth-act as the evaluated object — not a new operator-interaction layer. (If one later wants to model the obligation→target-axis link explicitly, it would be a "cross-axis predicate," the same shape as the deception family; but the data does not force it.)

---

## 6.6 *mithyā*: mostly LIKE[ESS] + level-relativity; one genuine residual

The proposed multi-valued-opposition refinement (a third value in the **opposition FRAME**, §1E) is the **one case that does not fully dissolve** — and after six that did, treating it honestly matters. Most of the Sanskrit ontological apparatus is absorbed by existing structure; a strong residual is not, and is correctly *not* a reason to relax the FRAME's binary default.

**What dissolves:**
- **Appearance → LIKE[ESS].** *pratibhāsa* / *ābhāsa* ("mere appearance, semblance") are the *similative* (F-M) expressions for D11 — i.e. LIKE[ESS], the apparent resembling the real without being it (the rope-snake). Consistent with §1B/§6.3.
- **Level-indexed reality → the LEVEL layer.** Advaita indexes being by level — *vyāvahārika* (empirical), *paramārtha* (ultimate): *paramārthataḥ na vidyate* ("it does not exist at the ultimate level"). "Real at the empirical level, unreal at the ultimate level" is the **binary opposition FRAME evaluated per level**; collapsing the levels (treating empirical-real as ultimate-real) is a **Type 4** level-crossing. The FRAME stays binary.

**What does not dissolve (the residual):** Advaita's strong *anirvacanīya* — *mithyā* as genuinely *indeterminable* as either *sat* or *asat*, a stable third ontological category resistant to bivalence even within a single level. A binary FRAME plus levels does not capture this. The data is emphatic: it "conflicts with AOML's binary CONTR assumption" and **"has no parallel in any other language in the corpus."**

**Verdict — recorded, not adopted.** The opposition FRAME remains binary by default (the truth/falsehood binary is a CU-10 universal). The strong *anirvacanīya* three-valued ontology is the **single genuine residual** the union pipeline surfaced. It is **not** adopted into the core: relaxing the FRAME's bivalence on the evidence of one language and one philosophical tradition would be unwarranted, and the data itself holds the question open (G8 OQ-11: "Does the *mithyā* three-valued system have parallels in other traditions not in the corpus?"). It is recorded as a genuine, scoped open conflict pending cross-traditional confirmation.

### Closing the proposal arc — and the honesty check

Seven proposed refinements, examined against the data:

| # | Proposal | Outcome |
|---|---|---|
| 1 | SINC split | dissolved → TEMP[SINC] (reliability) |
| 2 | NORM split | dissolved → R1 on NORM's SINC rider |
| 3 | AUTH neutral intermediate | dissolved → LIKE[AUTH] + R8 (copy vs forgery) |
| 4 | VER/NORM gradient | dissolved → axis-neutral conformity predicate |
| 5 | partial-truth rule | dissolved → R5 + the deception principle |
| 6 | deontic interaction | dissolved → NORM over truth-related conduct |
| 7 | FRAME multi-valued (*mithyā*) | **mostly** dissolved (LIKE[ESS] + levels); strong *anirvacanīya* residual recorded, not adopted |

Six dissolved cleanly into existing structure; the seventh mostly dissolved with one well-scoped residual that is *not* swept in. **That asymmetry is the architecture's honesty check.** If every proposal had dissolved, the stability principle would look like motivated reasoning — force-fitting all evidence into the existing six axes. The fact that the union pipeline surfaced exactly one thing the architecture does not absorb (single-language, single-tradition, held open by the data itself) is what makes the other six dissolutions credible: the principle has real discriminating power. **The six primary axes were not enlarged; one genuine open conflict stands recorded.**

---

## 7. The single open conflict

**FRAME bivalence vs. Advaita *anirvacanīya* (§6.6).** The only refinement not resolved into existing structure. Sanskrit's *mithyā* (genuinely indeterminable, neither *sat* nor *asat*) is a stable third ontological value resisting the opposition FRAME's binary assumption — [CLCA-B], single-tradition, no cross-corpus parallel, held open by the data's own OQ-11. The FRAME remains binary by default; the three-valued ontology is recorded as a scoped open question pending evidence that other traditions independently lexicalize a third ontological value. **Decision deferred — and appropriately so: it should not be resolved on one tradition's evidence.**

---

## 8. Not tested by the union pipeline

R2 (CAUSE/BECOME × ESS), R6 substitution prohibition (only construction-availability tested), STRAT × AUTH/SINC restrictions, ESS-distinctive predictions. (TEMP itself is no longer untested — see §6.1, reliability.) These are coverage gaps, not refutations — marked "not tested" rather than "confirmed."

---

## 9. Provenance & artifacts

- `aoml/aoml_constraint_matrix_v2.2.json` — machine-readable v2.2 (this document's companion)
- `aoml/aoml_constraint_matrix.json` + `Aoml_v2.1_constraint_architecture.html` — frozen v2.1 baseline
- `data_union/aoml_v2.2_delta_from_union.md` — Stage 1 discovery inventory
- `data_union/aoml_LIKE_revision_draft.md`, `aoml_EVID_revision_draft.md` — meta-axis treatments
- `data_union/meta_axis_candidates_assessment.md` — why PROB/MOD/CAUS-STR/INT/SPAT were not added
- `data_union/global_set_{A,B}/G7a,G7b,G8` — the empirical matrices behind every [CLCA-*] tag
