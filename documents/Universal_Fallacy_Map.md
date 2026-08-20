# The Universal Fallacy Map
## Classical and Contemporary Fallacies Mapped to Five Structural Error Types
### Companion Document to Paper II: The Universal Fallacy Architecture
### Brent Alan Seeley · WellFlow Labs · April 2026, revised July–August 2026; Second Edition, August 2026
### DOI: https://doi.org/10.5281/zenodo.21880635 (Second Edition; First Edition: https://doi.org/10.5281/zenodo.21766167)

---

## How to Read This Map

This is a companion to Paper II, but it is written to be readable on its own.
Each entry names a fallacy, gives a brief description, and records which AOML
constraint it violates.

**The six semantic axes** (the kinds of truth a claim can be about):

| Axis | Tracks | Settled by |
|---|---|---|
| **VER** | Veridical truth: is it so, in the world? | observation, measurement, experiment |
| **AUTH** | Authenticity: is it the genuine item? | provenance, chain of custody |
| **SINC** | Sincerity: is the speaker's inner state as presented? | behavioral consistency, testimony |
| **NORM** | Normative correctness: is it right, proper, just? | principle, consequence, consensus |
| **ESS** | Essence: what is it by definition or nature? | formal logic, definition, proof |
| **VERIF** | Verification: has it been established or tested? | experiment, statistics, formal proof |

**The four meta-axes** modify a claim on a host axis without being that axis:
**DEG** (degree or intensity), **TEMP** (temporal position), **LIKE** (resemblance
to the host property without being it), **EVID** (source-marking: reported,
inferred, firsthand). Treating a meta-axis modification as if it established the
underlying claim is the substitution family M[A] does not yield A, formalized as
rules R5, R6, R8, and R9 in Paper II.

**Numbering.** Entry numbers are stable identifiers, not a running tally. When an
entry is reclassified its original number travels with it (so #23 Equivocation and
#93 Red Herring sit in Type 5, #72 and #73 in Type 2), which is why the numbers are
not contiguous within a section. Later additions are appended rather than
interleaved. A fallacy analyzed two ways appears twice and is counted once (Appeal
to Tradition at #49 and #94). Where one name covers two structurally distinct
errors, both are listed and both are counted: Appeal to Emotion at #2 and #99,
Appeal to Authority at #48 and #100, Bandwagon/Argumentum ad Populum at #47 and
#101. Where two entries prove to be one fallacy, they merge onto a single row that
retains both numbers and is counted once (Argument to Moderation / Middle Ground
at #82/#88). Entries #102 and #103 were added in the Second Edition, unbundled
from #67 and #71 respectively. The document therefore has 102 entry rows carrying
103 numbered identifiers and describing 101 distinct fallacies.

**Reading an entry.** The AOML Violation column names the constraint breached and,
in parentheses, which AOML component it belongs to (Axis, Operator, Method, Level,
or Contrast). An arrow marks a substitution, source to target. So entry 1,
Ad Hominem, reads `SINC → VER (Axis)`: evidence about a speaker's sincerity is
substituted for evidence about the veridical truth of a claim, and the component
violated is the Axis condition. Named rules (R1, R3, R4, R5, R6, R7, R8, R9) are
the structural rules defined in Paper II and AOML v2.2.

**Root and locus.** Where an entry involves two AOML components, the Second
Edition distinguishes their contributions. A component is the **root** if
repairing its side condition, with the judgment held fixed, licenses the
inference; it is the **locus** if removing it does not repair anything but
destroys the judgment under examination, leaving nothing to evaluate. A compound
whose two violations are each independently reparative (each survives repair of
the other) is marked **co-roots**; a compound where one component carries the
violation the other causes is marked **root/locus**.

---

## Second Edition Revision Note

The Second Edition applies a classification criterion, frozen before the pass,
to every entry of the July–August 2026 edition:

1. **Judgment form vs. side condition.** Write the entry's judgment form (the
   shape of the inferential claim) and list its licensing side conditions
   separately.
2. **Three-outcome intervention.** Repair each side condition with the judgment
   held fixed: if the inference becomes licensed, that condition is the root; if
   the failure persists, it is not the root; if the judgment itself disappears,
   the component is the locus, not the root.
3. **Regimentation stability.** Classify only when the verdict is stable across
   admissible regimentations (those preserving inferential content). Genuine
   instability is a finding: the traditional label covers more than one
   structural error and splits.
4. **Type 4 root reserved for unassignability.** A Type 4 root requires that no
   legal stratification assignment can make the judgment form well-formed, not
   merely that a level boundary is crossed.
5. **Method identity.** A Type 3 classification requires a method that is
   independently specifiable apart from the inference under audit, with an
   established warrant it is being used outside of.
6. **Dual intervention for compounds.** Where two candidate violations are
   present, repair each while holding the other fixed; violations that each
   survive repair of the other are co-roots.

The principal results: Type 3 contracts to nine entries, each an identifiable
epistemic practice used outside its warrant (#56 moves to a new 1+2 compound
row, #57 and #59 to Type 5, #58 to Type 2). The former Type 4 roster moves to
the compound sections: eight entries to 2+4, uniformly Type 2 root with Type 4
locus, and #74 to 5+4, contrast root with level locus. No numbered entry
survives as a Type 4 root, and the type's exhibited cases are three unnumbered
witnesses (paradoxes, not fallacies). #82 and #88 merge as one
fallacy. Two bundled errors receive their own entries: #102 Aggregation
Reversal (from #67) and #103 Confusion of the Inverse (from #71). Several of
these moves had been made independently in the July–August revision before the
criterion was applied; the convergence of the two passes is itself evidence
that the classification is tracking structure rather than editorial taste.
The Second Edition also renames the type: Stratification Failure (First
Edition: Stratification Misalignment), with unassignability as its primary
form, since misalignment names precisely the reparable class that now sits in
the 2+4 section as locus.

---

## Type 1: Axis Transfer Error (Category Condition)
*One kind of truth substituted for another. The pattern holds across domains, but the axis of the claim changes without justification.*

| # | Fallacy | Brief Description | AOML Violation | Notes |
|---|---------|------------------|----------------|-------|
| 1 | Ad Hominem | Attacking the person instead of the argument | SINC → VER (Axis) | Character/intent as empirical disproof |
| 2 | Appeal to Emotion (affective substitution) | An emotional consideration is offered where the claim's own axis requires evidence | SINC → VER (Axis) | The classic axis transfer: sympathy, fear, or indignation supplied in place of veridical support. Distinguish from #99, where it is the *intensity* of feeling rather than its content that is treated as probative |
| 3 | Appeal to Pity | Sympathy to persuade | SINC → VER (Axis) | Emotional vulnerability replaces proof |
| 4 | Appeal to Fear | Fear to persuade | SINC → VER (Axis) | Emotional → Veridical |
| 5 | Appeal to Flattery | Praise to persuade | SINC → VER (Axis) | Affective → Veridical |
| 6 | Appeal to Spite | Resentment to persuade | SINC → VER (Axis) | Emotional → Veridical |
| 7 | Appeal to Ridicule | Mockery as refutation | SINC → VER (Axis) | Social performance → Veridical |
| 8 | Tu Quoque | Dismissing due to hypocrisy | SINC → VER (Axis) | Sincerity as veridical evidence |
| 9 | Wishful Thinking | Desire as evidence | SINC/PREFERENCE → VER (Axis) | Preference → Veridical |
| 10 | Poisoning the Well | Preemptively discrediting a source | SINC → VER (Axis) | Preemptive sincerity attack; anticipatory, not reactive |
| 11 | Argument from Incredulity | Can't imagine, so false | SINC/personal belief → VER (Axis) | Personal epistemic state → veridical evidence |
| 12 | Genetic Fallacy | Judging something based on its origin | AUTH → VER (Axis) | Provenance as truth-value |
| 13 | Guilt by Association | Invalid because associated with despised group | AUTH → VER (Axis) | Association treated as truth-value |
| 14 | Naturalistic Fallacy | Deriving "ought" from "is" | VER → NORM (Axis) | Descriptive → Normative |
| 15 | Appeal to Nature | Natural, so good | VER → NORM (Axis) | Descriptive → Normative |
| 16 | Is-Ought Gap | Descriptive implies prescriptive | VER → NORM (Axis) | Factual → Normative |
| 17 | Appeal to Consequences | Claim must be false because of its consequences | NORM → VER (Axis) | Normative desirability substituted for truth |
| 18 | Moralistic Fallacy | Ought, so is | NORM → VER (Axis) | Normative → Descriptive |
| 19 | Appeal to Ideal | Using a normative ideal as evidence for veridical truth | NORM → VER (Axis) | Distinct from Nirvana (#74, contrast frame with level locus); this is axis transfer |
| 20 | Divine Fallacy | Amazing, so divine | VER → ESS (Axis) | Phenomenal → Supernatural/essential |
| 21 | False Analogy | Poor analogy | Various axes mismatch (Axis) | Axis mismatch in analogical transfer |
| 22 | Masked-Man Fallacy | Identity substitution error | ESS confusion (Axis) | Identity axis confusion |
| 24 | Category Error | Misapplying concepts across categories | Multiple axes (Axis) | Pure category/axis violation (prototypical) |

**Type 1 count: 23**

---

## Type 2: Operator Overextension (Composition Licensing Condition)
*A compositional operator is applied beyond its licensed semantic scope. Includes meta-axis substitution subtypes (R5, R6, R8, R9) and polarity conditioning (R3, R7).*

| # | Fallacy | Brief Description | AOML Violation | Notes |
|---|---------|------------------|----------------|-------|
| 25 | Post Hoc Ergo Propter Hoc | Assuming correlation implies causation | CAUSE misapplied (Operator) | Illegitimate CAUSE from sequence |
| 26 | Slippery Slope | One event leads to extreme consequences | BECOME misapplied (Operator) | Unsupported BECOME chain |
| 27 | Begging the Question | Assuming conclusion in premises | RESULT misused (Operator) | Illicit RESULT as premise |
| 28 | Circular Reasoning | Premise as conclusion | IDENTITY misused as inference (Operator) | Identity treated as derivation |
| 29 | Affirming the Consequent | If P then Q; Q therefore P | CONDITIONAL converse assumed (Operator) | Converse assumed for a conditional; licensed only under the stronger biconditional (P ↔ Q). The conditional need not be causal |
| 30 | Denying the Antecedent | If P then Q; not P therefore not Q | CONDITIONAL inverse assumed (Operator) | Inverse assumed for a conditional; licensed only under the biconditional (P ↔ Q) |
| 31 | Non Sequitur | Conclusion doesn't follow | INFERENCE invalid (Operator) | Illicit inferential connection |
| 32 | Argument from Fallacy | Fallacious argument means false conclusion | STRUCTURE → CONTENT (Operator) | Illicit RESULT from structure |
| 33 | Affirming a Disjunct | A or B; A, so not B | DISJUNCTION misused (Operator) | Exclusive disjunction assumed |
| 34 | Appeal to Probability | Likely, so true | DEG meta-axis substitution (R5) | Probability treated as veridical certainty |
| 35 | Appeal to Novelty | Better because new | TEMP meta-axis substitution (R6) | Recency treated as normative validity |
| 36 | Modal Fallacy | Necessity/sufficiency confusion | MODAL misused (Operator) | Modal operator misuse |
| 37 | Modal Scope Fallacy | Misplaced necessity | SCOPE violated (Operator) | Modal scope violation |
| 38 | Undistributed Middle | Middle term undistributed | DISTRIBUTION violated (Operator) | Classic syllogistic error |
| 39 | Existential Fallacy | Universal to particular | QUANTIFICATION misused (Operator) | Universal → Existential jump under modern first-order semantics; licensed with an existence premise. Traditional treatments with existential import declare a different habitat, so the licensing is habitat-relative |
| 40 | Affirmative from Negative | Positive conclusion from negative premises | POLARITY misused (Operator) | Polarity operator mismatch |
| 41 | Exclusive Premises | Both premises negative | PREMISE combination (Operator) | Invalid premise operator |
| 42 | Four Terms | Syllogism with four terms | TERM overextended (Operator) | Term count violation |
| 43 | Illicit Major / Illicit Minor | Major/minor term undistributed | DISTRIBUTION violated (Operator) | Distribution boundary error |
| 44 | Negative from Affirmative | Negative from positive premises | POLARITY misused (Operator) | Polarity operator error |
| 45 | Amphiboly | Grammatical ambiguity leads to false conclusion | STRUCTURE ambiguity (Operator) | Syntactic scope; distinct from Equivocation (lexical) |
| 46 | Kafkatrap | Denial of accusation as evidence of guilt | CAUSE/RESULT reversed (Operator) | Self-sealing argument structure |
| 58 | Proof by Assertion | Repetition as proof | Iterated EVID[A] ↛ A (R9 family) | Second Edition reclassification from Type 3: repetition is not an independently specifiable method with an established warrant; the error is evidential substitution, iterated |
| 99 | Appeal to Emotion (intensity substitution) | Strength of feeling treated as establishing the claim | DEG[A] ↛ A (R5) | Meta-axis substitution: the degree of conviction or affect is substituted for the truth of what is felt. The reading Paper II lists under R5; distinguish from #2, the axis-transfer reading |
| 100 | Appeal to Authority (evidential substitution) | The fact that a claim is authoritatively asserted treated as establishing it | EVID[A] ↛ A (R9) | Meta-axis substitution: the source-marking of a claim (authoritatively asserted, reported) treated as itself establishing it. The reading Paper II lists under R9; distinguish from #48, the habitat-mismatch reading |
| 101 | Argumentum ad Populum (intensity substitution) | Widespread or intense belief treated as establishing truth | DEG[VER] ↛ VER (R5) | Meta-axis substitution: the prevalence or intensity of belief treated as constituting truth. The reading Paper II lists under R5; distinguish from #47, the consensus-as-method reading |
| 72 | Conjunction Fallacy | Specific more probable than general | Inclusion-order direction error (Operator) | The composition violates P(A∧B) ≤ P(A): adding a conjunct moves downward in the inclusion order, and probability preserves that order. LIKE[VER] ↛ VER (R8, representativeness) names the mechanism that makes the error attractive. Reclassified from Type 4; column harmonized with #103 in the Second Edition (structural condition in the column, mechanism in the notes) |
| 73 | Double Counting | Overcounting probability | Unlicensed composition (Operator) | Non-independent evidence composed as though independent. Reclassified from Type 4 |
| 103 | Confusion of the Inverse | P(E given H) read as P(H given E) | Inverse-conditional substitution (Operator) | New in the Second Edition, unbundled from #71: the direction error in conditionalization (the prosecutor's fallacy); the reverse conditional can be derived only when the requisite prior and base-rate terms are supplied through Bayes' theorem; it cannot be obtained by simply reversing the conditional. Distinguish #71, the suppressed-prior shortcut |

**Type 2 count: 29** (includes #72 Conjunction Fallacy and #73 Double Counting, reclassified from Type 4 under the operator-licensing reading; the meta-axis substitution readings #99, #100, and #101; #58 Proof by Assertion, reclassified from Type 3 in the Second Edition; and #103 Confusion of the Inverse, added in the Second Edition; original sequence IDs are retained)

---

## Type 3: Verification Habitat Mismatch (Validation Condition)
*The axis is correctly identified, but the validation method is inappropriate. Wrong kind of evidence for the kind of claim being made. Second Edition: every entry here names an independently specifiable epistemic practice (polling, testimony, continuity assessment, search, sampling) with an established warrant, used outside it; entries that failed that method-identity test moved out (#56 to the 1+2 compound, #57 and #59 to Type 5, #58 to Type 2).*

| # | Fallacy | Brief Description | AOML Violation | Notes |
|---|---------|------------------|----------------|-------|
| 47 | Bandwagon (consensus as method) | The agreement of many offered as verification of a claim | CONSENSUS → VER (Method) | Consensus polling has an established warrant for conventional-level facts; here it is offered for a claim whose axis requires observation. Distinguish from #101, where the sheer prevalence or intensity of belief is treated as itself establishing truth |
| 48 | Appeal to Authority (habitat mismatch) | Expert testimony used outside the expert's axis of competence | AUTH/TESTIMONY misapplied (Method) | Expertise misapplied across domains. Distinguish from #100, where the mere fact of authoritative assertion is treated as establishing the claim |
| 49 | Appeal to Tradition | Right because traditional | AUTH → NORM (Method) | Continuity-of-practice assessment warrants claims about custom, not normative validity |
| 50 | Argument from Silence | Absence of evidence as evidence | NULL → VER (Method) | A search or detection procedure warrants a null conclusion only with a detection-expectation premise (if it existed, this search would have found it); without that premise the null carries no weight |
| 51 | Appeal to Ignorance | Truth from absence of disproof | NULL → VER (Method) | Absence of counter-evidence as validation; distinct from Arg. from Silence. Second Edition: also absorbs the evidential reading of Burden of Proof (#57), where absence of disproof is offered as proof |
| 52 | Confirmation Bias | Seeking only supporting evidence | SELECTIVE method (Method) | The warrant of an evidence search assumes an unbiased search; the selective search violates it. Second Edition: the earlier possible-compound hedge is retired; the warrant violation is the whole analysis |
| 53 | Cherry Picking | Selective supporting data | SELECTIVE method (Method) | As #52, at the presentation stage; hedge retired in the Second Edition |
| 54 | Nut-Picking | Selective negative data | SELECTIVE method (Method) | As #52, negative selection; hedge retired in the Second Edition |
| 55 | Survivorship Bias | Ignoring failures | SELECTIVE method (Method) | Sampling warrant violated where the sampling frame excludes the failures; the frame is the locus of the error, the sampling warrant its root |

**Type 3 count: 9**

---

## Type 1+2 Compound
*Axis transfer combined with operator overextension.*

| # | Fallacy | Brief Description | AOML Violation | Notes |
|---|---------|------------------|----------------|-------|
| 56 | Appeal to Purity | Purer form is better | ESS → NORM (Axis) + DEG[ESS] ↛ ESS (Operator, R5 family) | Second Edition reclassification from Type 3 by dual intervention: supplying genuine essential status independently leaves the degree substitution standing; repairing the substitution leaves the axis transfer standing. Co-roots |

**Type 1+2 count: 1**

---

## Type 2+3 Compound
*Operator overextension combined with method mismatch.*

| # | Fallacy | Brief Description | AOML Violation | Notes |
|---|---------|------------------|----------------|-------|
| 60 | Texas Sharpshooter | Retrofitting patterns | SELECTIVE/POST-HOC method + CAUSE/PATTERN (Operator) | Composite: selective method + illicit pattern imposition. Co-roots (each violation survives repair of the other) |

**Type 2+3 count: 1**

---

## Type 2+4 Compound
*Operator overextension combined with stratification misalignment. Second Edition: uniformly Type 2 root with Type 4 locus. The level transition is where the inference operates; the failed operator license is why it is illicit. Repairing the license (with the level transition intact) licenses the inference; deleting the transition leaves nothing to evaluate.*

| # | Fallacy | Brief Description | AOML Violation | Notes |
|---|---------|------------------|----------------|-------|
| 61 | Chronological Snobbery | Old, so wrong | TEMP meta-axis + TEMPORAL levels (Operator + Level) | Temporal position misused across levels |
| 62 | Gambler's Fallacy | Independent events as dependent | INDEPENDENCE violated + statistical levels (Operator + Level) | Illicit causal connection across probability levels |
| 63 | Hot Hand Fallacy | Random streaks as meaningful | PATTERN overextended + statistical levels (Operator + Level) | Pattern overinterpretation across levels |
| 64 | Regression Fallacy | Mistaking regression to mean | STATISTICAL CAUSE + levels (Operator + Level) | Statistical CAUSE error across levels |
| 65 | Sunk Cost Fallacy | Continuing due to prior investment | TEMP meta-axis + PAST → FUTURE (Operator + Level) | Past level misaligned with future (R6) |
| 95 | Fallacy of Accident | A general rule applied to an exceptional case outside its licensing conditions | RULE overextension + contextual levels (Operator + Level) | Rule overextension across contextual levels; classical mirror of hasty generalization (instance→rule vs. rule→exception) |
| 66 | Hasty Generalization | Broad conclusions from small samples | ABSTR/inductive license (Operator) + INSTANCE → CATEGORY (Level) | Second Edition reclassification from Type 4: repairing the inductive license (an adequate sampling warrant) licenses the inference with the instance-to-category judgment intact |
| 67 | Ecological Fallacy | Inferring individual traits from group statistics | Down-projection without distributional license (Operator) + GROUP → INDIVIDUAL (Level) | Narrowed in the Second Edition: the Simpson-type association reversal formerly bundled here is a structurally distinct error, now #102 |
| 68 | Composition Fallacy | Whole assumed to have parts' properties | Predicate not established as preserved under composition (Operator) + PARTS → WHOLE (Level) | Second Edition reclassification from Type 4: the failed condition is preservation of the predicate under the composition operation, not the level transition itself. Not the mirror image of #69: for threshold predicates over additive quantities, exactly one of the two directions fails. The classical universal premise is also misdrawn: for up-closed predicates a single qualifying part suffices, and for down-closed predicates no quantifier strength rescues the composition |
| 69 | Division Fallacy | Parts assumed to have whole's properties | Predicate not established as preserved under division (Operator) + WHOLE → PARTS (Level) | Dual of #68; same Second Edition analysis |
| 70 | Argument from Anecdote | Anecdote as general evidence | ABSTR/inductive license (Operator) + INSTANCE → GENERAL (Level) | Second Edition reclassification from Type 4; companion to #66. Where the anecdote is also report-status evidence, an R9 compound reading applies |
| 71 | Base Rate Fallacy | Ignoring base rates | Suppressed class-level premise (Operator) + INDIVIDUAL vs GROUP probabilities (Level) | Narrowed in the Second Edition: the licensed composition requires the prior, and the shortcut omits it. The inverse-conditional confusion formerly bundled here is a structurally distinct error, now #103 |
| 75 | Historian's Fallacy | Anachronistic judgment | R6/TEMP scope (Operator) + TEMPORAL levels (Level) | Second Edition reclassification from Type 4; joins #61 and #65 in the R6 family |
| 76 | Presentism | Current standards on past | R6/TEMP scope (Operator) + TEMPORAL levels (Level) | Second Edition reclassification from Type 4: a consistently applied temporal scope licenses evaluation, so the root is the operator's scope, not the levels |
| 102 | Aggregation Reversal | A per-stratum association asserted of the aggregate, or conversely | Aggregation homomorphism not established (Operator) + STRATA vs AGGREGATE (Level) | New in the Second Edition, unbundled from #67: the Simpson-type reversal. The preservation conditions in Simpson's own analysis are precisely the missing license |

**Type 2+4 count: 15**

---

## Type 2+5 Compound
*Operator overextension combined with contrast frame collapse.*

| # | Fallacy | Brief Description | AOML Violation | Notes |
|---|---------|------------------|----------------|-------|
| 96 | Fallacy of Relative Privation | A problem dismissed because a worse problem exists | DEG[A] < DEG[B] → ¬NORM[attend(A)] (Operator, R5 family) + exclusive-admissibility frame (Contrast) | Meta-axis substitution (M[A] ↛ A family): priority ordering collapsed into exclusive admissibility. Co-roots. Distinct from whataboutism (no counter-accusation) and the Nirvana fallacy (real-vs-real, not real-vs-ideal) |
| 97 | Fallacy of the Single Cause | A contributing cause presented as the exhaustive explanation of a multicausal outcome | CAUSE scope amplification (Operator) + causal-field foreclosure (Contrast) | Partial causal license inflated to exhaustive scope. Co-roots. Distinct from post hoc: the causal link may be genuine; the exhaustiveness is not |

**Type 2+5 count: 2**

---

## Type 4: Stratification Failure (Stratification Condition)
*Second Edition: a Type 4 root violation occurs when no legal stratification assignment can make the judgment form well-formed. Stratification unassignability, not incidental level-crossing. Level-crossing whose license can be repaired is Type 2 root with Type 4 locus and sits in the 2+4 section above.*

No numbered entry survives as a Type 4 root under the revision criterion. This
is not a gap but a finding about what the type is. A fallacy presupposes a
well-formed judgment whose license can fail; a pure Type 4 violation destroys
the possibility of the required judgment itself. The type's exhibited cases are
therefore paradoxes, listed as unnumbered witnesses: they resist every
side-condition repair, and they do not enter the fallacy count.

| Witness | Case | Structure | Status |
|---|---|---|---|
| W1 | Liar cycle | Self-referential truth predication: under the declared well-founded object/meta stratification, no legal level assignment exists (Tarski) | Type 4 root: unassignability |
| W2 | Yablo regress | An infinite sequence with no self-reference; no well-founded assignment satisfying the declared dependency-order constraints exists | Type 4 root: unassignability |
| W3 | Two-Truth Collapse | The conventional/ultimate stratification erased; restoration requires habitat revision, not premise repair | Type 4 root: unassignability |

The stratification condition's everyday work is done as the locus of the
fifteen 2+4 entries; its root violations are exhibited by the configurations
the scholastic, Mādhyamaka, Kantian, and Tarskian traditions each converged on.
These structure-level configurations are violations of the existing conditions
read globally over an argument's dependency structure, not a sixth type
(Paper III §6).

**Type 4 count: 0 numbered entries; 3 exhibited witnesses**

---

## Type 5: Contrast Frame Collapse (Opposition Topology, the Precondition)
*False or inverted opposition imposed. A multidimensional space is forced into a binary, or contrast boundaries are manipulated. Also includes relevance failures (off-question diversion), identity-persistence failures (meaning drift), and temporal frame failures (boundaries shifted over a discourse), which mis-specify or fail to maintain the opposition frame; see Paper III §6.*

| # | Fallacy | Brief Description | AOML Violation | Notes |
|---|---------|------------------|----------------|-------|
| 77 | False Dilemma | Limited options as exhaustive | BINARY imposed (Contrast) | False binary opposition |
| 78 | False Equivalence | Treating unequal things as equal | SIMILARITY → IDENTITY (Contrast) | Superficial similarity as identity. Second Edition adversarial check against the R8 reading (LIKE ↛ identity): the dual intervention shows the two candidate violations are one condition. Supplying genuine equivalence does not repair a separate similarity inference; it redraws the equivalence partition itself, since equivalence classes are frame structure, and the canonical instances assert positional sameness rather than a host-axis property, leaving no host axis for an R8 substitution. Type 5 stands |
| 79 | Straw Man | Misrepresenting argument to refute it | OPPOSITION distorted (Contrast) | False opposition via distortion |
| 80 | No True Scotsman | Redefining to exclude counterexamples | BOUNDARY moved (Contrast) | Inverted opposition boundary |
| 81 | Loaded Question | Question assuming unproven premise | BINARY imposed (Contrast) | Imposes false binary choice |
| 82/88 | Argument to Moderation / Middle Ground Fallacy | The middle position selected merely because it lies between opposed positions | MIDDLE assumed (Contrast) | Second Edition merge: two First-Edition entries (#82, #88) describe one fallacy; both numbers are retained on this row and it is counted once |
| 83 | Continuum Fallacy | Rejecting imprecise claims | DISCRETE imposed (Contrast) | Imposes discrete opposition on graded structure. Second Edition annotation: where the argument trades on oscillation between essential and veridical readings of the vague predicate, a Type 1 root is also present (Paper IV) |
| 84 | Suppressed Correlative | Redefining to exclude | OPPOSITION collapsed (Contrast) | Collapses natural opposition |
| 85 | Perfect Solution Fallacy | Imperfect, so reject | PERFECTION binary (Contrast) | The acceptance boundary is set at accept-only-if-perfect: no ideal is represented in the comparison at all, and a real proposal is rejected merely for having a flaw. Distinguish #74, where an unattainable ideal is admitted into the comparison set |
| 86 | Special Pleading | Exception without justification | BOUNDARY ad hoc (Contrast) | Ad hoc boundary manipulation |
| 87 | Moving the Goalposts | Changing success criteria | CRITERIA dynamic (Contrast) | Dynamic opposition frame (temporal) |
| 89 | Incomplete Comparison | Comparison without basis | COMPARISON incomplete (Contrast) | Incomplete opposition frame |
| 90 | Thought-Terminating Cliché | Cliché ends discussion | CLOSURE artificial (Contrast) | Artificial discussion closure (temporal frame) |
| 91 | Motte and Bailey | Defending strong claim by retreating to weaker one | BOUNDARY dynamic (Contrast) | Two claims of different strength treated as equivalent; kinship with #23 |
| 23 | Equivocation | Ambiguous terms to mislead | FRAME drift over occurrences (temporal) | A term's distinction drifts mid-argument, an identity-persistence failure = maintenance of the opposition frame over time (Paper III §6) |
| 93 | Red Herring | Irrelevant distraction | FRAME, off-question claim (Contrast) | Presents an off-question claim as occupying the position at issue; a same-axis diversion is a pure FRAME failure (Paper III §6). +Type 1 only when an axis-shift is also present |
| 57 | Burden of Proof | Shifting evidential responsibility | FRAME obligation boundary shifted (temporal) | Second Edition reclassification from Type 3: the procedural reading. The obligation boundary is part of the opposition frame, and shifting it over a discourse is a temporal frame failure (Paper III §6). The evidential reading (absence of disproof offered as proof) is #51 |
| 59 | Gish Gallop | Overwhelming with quantity of weak arguments | FRAME evaluation capacity attack (temporal) | Second Edition reclassification from Type 3: quantity is not a method with an established warrant; the attack prevents the opposition frame from being evaluated at all (Paper III §6) |

**Type 5 count: 18** *(includes #23 Equivocation and #93 Red Herring, reclassified under the FRAME / opposition-topology reading of Paper III §6; #57 Burden of Proof and #59 Gish Gallop, reclassified from Type 3 in the Second Edition; and the merged #82/#88, counted once; original sequence IDs are retained)*

---

## Type 1+5 Compound
*Axis transfer combined with contrast frame corruption.*

| # | Fallacy | Brief Description | AOML Violation | Notes |
|---|---------|------------------|----------------|-------|
| 92 | Whataboutism | Diverting with counter-accusations | SINC → VER (Axis) + CONTRAST | Axis diversion + false equivalence. Co-roots (each violation survives repair of the other) |

**Type 1+5 count: 1**

---

## Type 3+4 Compound
*Verification habitat mismatch combined with stratification misalignment.*

| # | Fallacy | Brief Description | AOML Violation | Notes |
|---|---------|------------------|----------------|-------|
| 94 | Appeal to Tradition (compound analysis) | Right because traditional | AUTH → NORM (Method) + TEMP levels (Level) | Custom as evidence + temporal level crossing. Root/locus: the method-warrant violation is the root; the temporal levels carry it |

**Note:** Appeal to Tradition appears at #49 as a primary Type 3 violation and here as a compound analysis showing its Type 4 component. It is counted once in the total.

---

## Type 5+4 Compound
*Contrast frame collapse combined with stratification misalignment.*

| # | Fallacy | Brief Description | AOML Violation | Notes |
|---|---------|------------------|----------------|-------|
| 98 | Package-Deal Fallacy | Separable claims or commitments fused into one indivisible object of acceptance or rejection | False fusion of the option space (Contrast) + component/package evaluation transfer (Level) | The inverse topology of false dilemma. Root/locus: the fusion is the root; the component/package levels carry it. Distinct from guilt by association (relational transfer) and composition (property inference after fusion, #68) |
| 74 | Nirvana Fallacy | Rejecting the actual because an unattainable ideal is admitted into the comparison | Candidate-set corruption (Contrast) + IDEAL vs ACTUAL levels (Level) | Second Edition reclassification from Type 4: the root is the corrupted option space, an unattainable ideal admitted into the comparison set as though available; the ideal/actual levels carry the violation (root/locus). Distinguish #85, where no ideal is represented and the acceptance boundary itself is corrupted |

**Type 5+4 count: 2**

---

## Summary Statistics

| UFA Type | Name | Condition Violated | Count | Description |
|----------|------|--------------------|-------|-------------|
| Type 1 | Axis Transfer Error | Category | 23 | One kind of truth substituted for another |
| Type 2 | Operator Overextension | Composition licensing | 29 | Illicit compositional rule applied (includes R3, R5, R6, R7, R8, R9 subtypes) |
| Type 3 | Verification Habitat Mismatch | Validation | 9 | An identifiable epistemic practice used outside its established warrant |
| Type 1+2 | Axis + Operator compound | Category + Composition | 1 | Axis transfer combined with operator overextension (co-roots) |
| Type 2+3 | Operator + Method compound | Composition + Validation | 1 | Operator overextension combined with method mismatch |
| Type 2+4 | Operator + Level compound | Composition + Stratification | 15 | Type 2 root with Type 4 locus: a level transition whose operator license failed |
| Type 4 | Stratification Failure | Stratification | 0 numbered (3 witnesses) | Stratification unassignability; exhibited by paradoxes, populated as locus throughout 2+4 |
| Type 5 | Contrast Frame Collapse | Opposition topology *(precondition)* | 18 | False or inverted opposition (includes relevance, identity-persistence, and temporal frame failures, Paper III §6) |
| Type 1+5 | Axis + Contrast compound | Category + Opposition topology | 1 | Axis transfer combined with contrast frame corruption |
| Type 2+5 | Operator + Contrast compound | Composition + Opposition topology | 2 | Operator overextension combined with contrast frame collapse |
| Type 5+4 | Contrast + Level compound | Opposition topology + Stratification | 2 | Contrast frame collapse with level locus |
| Type 3+4 | Method + Level compound | Validation + Stratification | (counted at #49) | Dual analysis of Appeal to Tradition |
| | **Total distinct fallacies** | | **101** | |

*Note: Appeal to Tradition (#49/#94) is counted once, as is the merged Argument to Moderation / Middle Ground (#82/#88). Entries #95–#98 were added in the July 2026 revision. Entries #99–#101 split names that each cover two structurally distinct errors (Appeal to Emotion #2/#99; Appeal to Authority #48/#100; Bandwagon/Argumentum ad Populum #47/#101). Entries #102–#103 were added in the Second Edition, unbundled from #67 and #71. The document has 102 entry rows carrying 103 numbered identifiers and describing 101 distinct fallacies.*

---

## Key Structural Properties

1. **Empirical completeness**: Every classical and contemporary fallacy tested reduces to one of five boundary violation patterns, with compound violations decomposing into identified components. No sixth primitive type was required, including under the Second Edition's frozen revision criterion.

2. **Compound transparency**: Fallacies that combine multiple violation types are analyzed as compounds rather than forced into single categories. The compound nature explains why certain fallacies are more rhetorically effective: they exploit multiple failure modes simultaneously.

3. **Root/locus discipline** (Second Edition): where an entry involves two components, the classification records which condition's repair licenses the inference (the root) and which merely situates it (the locus); compounds with two independently reparative violations are co-roots. This prevents a level transition that carries an error from being mistaken for the condition that caused it.

4. **AOML component mapping**: Each entry explicitly identifies which AOML component is violated (Axis, Operator, Method, Level, Contrast), connecting the fallacy map directly to the constraint geometry and the argument from distinction (Paper III).

5. **Extensibility without negation**: If a sixth type were discovered, it would mean a fifth condition for coherent distinction-making exists beyond category, composition, validation, stratification, and opposition topology. The five existing types would remain valid.

6. **Cross-substrate applicability**: The same five violation types appear in human language (CLCA), engineering systems (oAOML), and 2,400 years of independent philosophical investigation, supporting the structural argument that these are conditions for coherent distinction-making rather than artifacts of any particular analytical tradition.

---

## Connection to AOML v2.2 and the Argument from Distinction

Each fallacy type corresponds to a violation of one condition for coherent distinction-making (Paper III):

- **Type 1 (Axis)** → Category condition: the system must track what kind of distinction it is making
- **Type 2 (Operator)** → Composition licensing condition: compositions must be licensed (includes R1–R4 and R7 structural rules; R5, R6, R8, R9 meta-axis substitution: the M[A] ↛ A family)
- **Type 3 (Method)** → Validation condition: evidence must match the claim type
- **Type 4 (Level)** → Stratification condition: level boundaries must be assignable, and preserved across inference; the root violation is unassignability
- **Type 5 (Contrast)** → Opposition topology precondition: the space of possible distinctions must be correctly configured

The first four conditions correspond to the four AOML tuple components (A, O, M, L). Type 5 corresponds to the opposition-topology precondition (tokened the FRAME in the AOML v2.2 reference) that makes the other four possible. Four independent philosophical traditions each identified one of these conditions independently over 2,400 years.

---

## Related Documents

This map is one artifact in a series; several questions it raises are answered elsewhere.

- **Paper II, The Universal Fallacy Architecture.** Defines the AOML tuple, the structural rules R1 through R9 including the meta-axis substitution family M[A] does not yield A, and the derivation of the five types. The place to go for anything this map references but does not define.
- **Paper III, Given Distinction.** The closure argument: why there are exactly five types, why the opposition topology is a precondition rather than a fifth coordinate condition, and the historical convergence across independent traditions.
- **Terminology Correspondence** (companion, https://doi.org/10.5281/zenodo.21781768). Maps every term used here to its nearest counterpart in linguistics, philosophy and epistemology, formal logic, and computer science, including a section that places the five violation types against argumentation theory, philosophy of logic, cognitive science, and AI vocabulary.
- **Paper I, Cross-Linguistic Compositional Analysis.** The cross-linguistic evidence the axes rest on. https://doi.org/10.5281/zenodo.21709636

On the exhaustiveness claim specifically: Paper II section 6.7 reports a pre-registered inter-rater study in which independent raters (three heterogeneous frontier language models in the executed first phase; a human-rater second phase is pre-declared) classified this inventory using only the five type definitions, with a *fallacy but fits no type* option available on every item and salted distractor items included. That study, not this map, is where the claim that no sixth type is required is put at risk. The study's agreement statistics were computed against the First Edition classification key (94 entries as of the study); the Second Edition's reclassifications do not retroactively alter those statistics, which stand as a First Edition result, and the exhaustiveness finding is unaffected: no entry left the five-type space in either edition. Any replication runs against the Second Edition definitions and key, since the Type 4 definition changed intensionally, not only in its assignments.

---

*Companion document to: Seeley, B.A. (2026). The Universal Fallacy Architecture. Paper II, Foundations of the Convergent Semantic Architecture.*
*Structural foundation: Seeley, B.A. (2026). Given Distinction. Paper III, Foundations of the Convergent Semantic Architecture.*
*Empirical foundation: Seeley, B.A. (2026). Cross-Linguistic Compositional Analysis (CLCA). Paper I, Foundations of the Convergent Semantic Architecture. https://doi.org/10.5281/zenodo.21709636*
