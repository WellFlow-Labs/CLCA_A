# Comprehensive Universal Map of Logical Fallacies
## 100 Classical and Contemporary Fallacies Mapped to Five Structural Error Types
### Companion Document to Paper II: The Universal Fallacy Architecture
### Brent Alan Seeley · WellFlow Labs · April 2026, revised July 2026 (entries 95–98 added)

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
#101. The document therefore has 101 numbered entries and 100 distinct fallacies.

**Reading an entry.** The AOML Violation column names the constraint breached and,
in parentheses, which AOML component it belongs to (Axis, Operator, Method, Level,
or Contrast). An arrow marks a substitution, source to target. So entry 1,
Ad Hominem, reads `SINC → VER (Axis)`: evidence about a speaker's sincerity is
substituted for evidence about the veridical truth of a claim, and the component
violated is the Axis condition. Named rules (R1, R3, R4, R5, R6, R7, R8, R9) are
the structural rules defined in Paper II and AOML v2.2.

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
| 19 | Appeal to Ideal | Using a normative ideal as evidence for veridical truth | NORM → VER (Axis) | Distinct from Nirvana (Type 4 level); this is axis transfer |
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
| 29 | Affirming the Consequent | If P then Q; Q therefore P | CAUSE reversed (Operator) | Illicit CAUSE direction reversal |
| 30 | Denying the Antecedent | If P then Q; not P therefore not Q | NEGATION/conditional misused (Operator) | Illicit conditional negation |
| 31 | Non Sequitur | Conclusion doesn't follow | INFERENCE invalid (Operator) | Illicit inferential connection |
| 32 | Argument from Fallacy | Fallacious argument means false conclusion | STRUCTURE → CONTENT (Operator) | Illicit RESULT from structure |
| 33 | Affirming a Disjunct | A or B; A, so not B | DISJUNCTION misused (Operator) | Exclusive disjunction assumed |
| 34 | Appeal to Probability | Likely, so true | DEG meta-axis substitution (R5) | Probability treated as veridical certainty |
| 35 | Appeal to Novelty | Better because new | TEMP meta-axis substitution (R6) | Recency treated as normative validity |
| 36 | Modal Fallacy | Necessity/sufficiency confusion | MODAL misused (Operator) | Modal operator misuse |
| 37 | Modal Scope Fallacy | Misplaced necessity | SCOPE violated (Operator) | Modal scope violation |
| 38 | Undistributed Middle | Middle term undistributed | DISTRIBUTION violated (Operator) | Classic syllogistic error |
| 39 | Existential Fallacy | Universal to particular | QUANTIFICATION misused (Operator) | Universal → Existential jump |
| 40 | Affirmative from Negative | Positive conclusion from negative premises | POLARITY misused (Operator) | Polarity operator mismatch |
| 41 | Exclusive Premises | Both premises negative | PREMISE combination (Operator) | Invalid premise operator |
| 42 | Four Terms | Syllogism with four terms | TERM overextended (Operator) | Term count violation |
| 43 | Illicit Major / Illicit Minor | Major/minor term undistributed | DISTRIBUTION violated (Operator) | Distribution boundary error |
| 44 | Negative from Affirmative | Negative from positive premises | POLARITY misused (Operator) | Polarity operator error |
| 45 | Amphiboly | Grammatical ambiguity leads to false conclusion | STRUCTURE ambiguity (Operator) | Syntactic scope; distinct from Equivocation (lexical) |
| 46 | Kafkatrap | Denial of accusation as evidence of guilt | CAUSE/RESULT reversed (Operator) | Self-sealing argument structure |
| 99 | Appeal to Emotion (intensity substitution) | Strength of feeling treated as establishing the claim | DEG[A] ↛ A (R5) | Meta-axis substitution: the degree of conviction or affect is substituted for the truth of what is felt. The reading Paper II lists under R5; distinguish from #2, the axis-transfer reading |
| 100 | Appeal to Authority (evidential substitution) | The fact that a claim is authoritatively asserted treated as establishing it | EVID[A] ↛ A (R9) | Meta-axis substitution: the source-marking of a claim (authoritatively asserted, reported) treated as itself establishing it. The reading Paper II lists under R9; distinguish from #48, the habitat-mismatch reading |
| 101 | Argumentum ad Populum (intensity substitution) | Widespread or intense belief treated as establishing truth | DEG[VER] ↛ VER (R5) | Meta-axis substitution: the prevalence or intensity of belief treated as constituting truth. The reading Paper II lists under R5; distinguish from #47, the consensus-as-method reading |
| 72 | Conjunction Fallacy | Specific more probable than general | LIKE[VER] ↛ VER (R8) | Representativeness: resemblance to a stereotype substituted for probability; the composition violates P(A∧B) ≤ P(A). Reclassified from Type 4 |
| 73 | Double Counting | Overcounting probability | Unlicensed composition (Operator) | Non-independent evidence composed as though independent. Reclassified from Type 4 |

**Type 2 count: 27** (includes #72 Conjunction Fallacy and #73 Double Counting, reclassified from Type 4 under the operator-licensing reading, and the meta-axis substitution readings #99 Appeal to Emotion (R5), #100 Appeal to Authority (R9), and #101 Argumentum ad Populum (R5); original sequence IDs are retained)

---

## Type 3: Verification Habitat Mismatch (Validation Condition)
*The axis is correctly identified, but the validation method is inappropriate. Wrong kind of evidence for the kind of claim being made.*

| # | Fallacy | Brief Description | AOML Violation | Notes |
|---|---------|------------------|----------------|-------|
| 47 | Bandwagon (consensus as method) | The agreement of many offered as verification of a claim | CONSENSUS → VER (Method) | Consensus offered as a validation method for a claim whose axis requires observation. Distinguish from #101, where the sheer prevalence or intensity of belief is treated as itself establishing truth |
| 48 | Appeal to Authority (habitat mismatch) | Expert testimony used outside the expert's axis of competence | AUTH/TESTIMONY misapplied (Method) | Expertise misapplied across domains. Distinguish from #100, where the mere fact of authoritative assertion is treated as establishing the claim |
| 49 | Appeal to Tradition | Right because traditional | AUTH → NORM (Method) | Custom as evidence |
| 50 | Argument from Silence | Absence of evidence as evidence | NULL → VER (Method) | Null as positive evidence |
| 51 | Appeal to Ignorance | Truth from absence of disproof | NULL → VER (Method) | Absence of counter-evidence as validation; distinct from Arg. from Silence |
| 52 | Confirmation Bias | Seeking only supporting evidence | SELECTIVE method (Method) + possible 2/4 | Biased verification; often compounds with pattern overextension |
| 53 | Cherry Picking | Selective supporting data | SELECTIVE method (Method) + possible 2/4 | Biased method; variant of selective + operator imposition |
| 54 | Nut-Picking | Selective negative data | SELECTIVE method (Method) + possible 2/4 | Biased negative method |
| 55 | Survivorship Bias | Ignoring failures | SELECTIVE method (Method) + possible 4 | Selective survival evidence (level variant) |
| 56 | Appeal to Purity | Purer form is better | PURITY → NORM (Method) | Purity as validation |
| 57 | Burden of Proof | Shifting evidential responsibility | METHOD inversion (Method) | Method responsibility shifted |
| 58 | Proof by Assertion | Repetition as proof | FREQUENCY → VER (Method) | Repetition as verification |
| 59 | Gish Gallop | Overwhelming with quantity of weak arguments | VOLUME → VER (Method) | Quantity of arguments as validation method |

**Type 3 count: 13**

---

## Type 2+3 Compound
*Operator overextension combined with method mismatch.*

| # | Fallacy | Brief Description | AOML Violation | Notes |
|---|---------|------------------|----------------|-------|
| 60 | Texas Sharpshooter | Retrofitting patterns | SELECTIVE/POST-HOC method + CAUSE/PATTERN (Operator) | Composite: selective method + illicit pattern imposition |

**Type 2+3 count: 1**

---

## Type 2+4 Compound
*Operator overextension combined with stratification misalignment.*

| # | Fallacy | Brief Description | AOML Violation | Notes |
|---|---------|------------------|----------------|-------|
| 61 | Chronological Snobbery | Old, so wrong | TEMP meta-axis + TEMPORAL levels (Operator + Level) | Temporal position misused across levels |
| 62 | Gambler's Fallacy | Independent events as dependent | INDEPENDENCE violated + statistical levels (Operator + Level) | Illicit causal connection across probability levels |
| 63 | Hot Hand Fallacy | Random streaks as meaningful | PATTERN overextended + statistical levels (Operator + Level) | Pattern overinterpretation across levels |
| 64 | Regression Fallacy | Mistaking regression to mean | STATISTICAL CAUSE + levels (Operator + Level) | Statistical CAUSE error across levels |
| 65 | Sunk Cost Fallacy | Continuing due to prior investment | TEMP meta-axis + PAST → FUTURE (Operator + Level) | Past level misaligned with future (R6) |
| 95 | Fallacy of Accident | A general rule applied to an exceptional case outside its licensing conditions | RULE overextension + contextual levels (Operator + Level) | Rule overextension across contextual levels; classical mirror of hasty generalization (instance→rule vs. rule→exception) |

**Type 2+4 count: 6**

---

## Type 2+5 Compound
*Operator overextension combined with contrast frame collapse.*

| # | Fallacy | Brief Description | AOML Violation | Notes |
|---|---------|------------------|----------------|-------|
| 96 | Fallacy of Relative Privation | A problem dismissed because a worse problem exists | DEG[A] < DEG[B] → ¬NORM[attend(A)] (Operator, R5 family) + exclusive-admissibility frame (Contrast) | Meta-axis substitution (M[A] ↛ A family): priority ordering collapsed into exclusive admissibility. Distinct from whataboutism (no counter-accusation) and the Nirvana fallacy (real-vs-real, not real-vs-ideal) |
| 97 | Fallacy of the Single Cause | A contributing cause presented as the exhaustive explanation of a multicausal outcome | CAUSE scope amplification (Operator) + causal-field foreclosure (Contrast) | Partial causal license inflated to exhaustive scope. Distinct from post hoc: the causal link may be genuine; the exhaustiveness is not |

**Type 2+5 count: 2**

---

## Type 4: Stratification Misalignment (Stratification Condition)
*Inference crosses levels of abstraction, probability, or temporal position without justification.*

| # | Fallacy | Brief Description | AOML Violation | Notes |
|---|---------|------------------|----------------|-------|
| 66 | Hasty Generalization | Broad conclusions from small samples | INSTANCE → CATEGORY (Level) | Instance → Category jump |
| 67 | Ecological Fallacy | Inferring individual from group data | GROUP → INDIVIDUAL (Level) | Group level → Individual level |
| 68 | Composition Fallacy | Whole has parts' properties | PARTS → WHOLE (Level) | Parts → Whole attribution |
| 69 | Division Fallacy | Parts have whole's properties | WHOLE → PARTS (Level) | Whole → Parts attribution |
| 70 | Argument from Anecdote | Anecdote as general evidence | INSTANCE → GENERAL (Level) | Single story → Universal rule |
| 71 | Base Rate Fallacy | Ignoring base rates | INDIVIDUAL vs GROUP probabilities (Level) | Individual-level conclusion requires class-level information to license it; the level bridge is dropped |
| 74 | Nirvana Fallacy | Compare to unattainable ideal | IDEAL vs ACTUAL (Level) | Ideal vs. actual level confusion |
| 75 | Historian's Fallacy | Anachronistic judgment | TEMPORAL levels (Level) | Temporal level confusion |
| 76 | Presentism | Current standards on past | TEMPORAL levels (Level) | Temporal stratification error |

**Type 4 count: 9**

---

## Type 5: Contrast Frame Collapse (Opposition Topology, the Precondition)
*False or inverted opposition imposed. A multidimensional space is forced into a binary, or contrast boundaries are manipulated. Also includes relevance failures (off-question diversion) and identity-persistence failures (meaning drift), which mis-specify or fail to maintain the opposition frame over a discourse; see Paper III §6.*

| # | Fallacy | Brief Description | AOML Violation | Notes |
|---|---------|------------------|----------------|-------|
| 77 | False Dilemma | Limited options as exhaustive | BINARY imposed (Contrast) | False binary opposition |
| 78 | False Equivalence | Treating unequal things as equal | SIMILARITY → IDENTITY (Contrast) | Superficial similarity as identity |
| 79 | Straw Man | Misrepresenting argument to refute it | OPPOSITION distorted (Contrast) | False opposition via distortion |
| 80 | No True Scotsman | Redefining to exclude counterexamples | BOUNDARY moved (Contrast) | Inverted opposition boundary |
| 81 | Loaded Question | Question assuming unproven premise | BINARY imposed (Contrast) | Imposes false binary choice |
| 82 | Argument to Moderation | Middle ground always correct | MIDDLE assumed (Contrast) | False middle binary |
| 83 | Continuum Fallacy | Rejecting imprecise claims | DISCRETE imposed (Contrast) | Imposes discrete opposition |
| 84 | Suppressed Correlative | Redefining to exclude | OPPOSITION collapsed (Contrast) | Collapses natural opposition |
| 85 | Perfect Solution Fallacy | Imperfect, so reject | PERFECTION binary (Contrast) | Binary perfection standard |
| 86 | Special Pleading | Exception without justification | BOUNDARY ad hoc (Contrast) | Ad hoc boundary manipulation |
| 87 | Moving the Goalposts | Changing success criteria | CRITERIA dynamic (Contrast) | Dynamic opposition frame |
| 88 | Middle Ground Fallacy | Truth between extremes | CENTER assumed (Contrast) | Assumed central validity |
| 89 | Incomplete Comparison | Comparison without basis | COMPARISON incomplete (Contrast) | Incomplete opposition frame |
| 90 | Thought-Terminating Cliché | Cliché ends discussion | CLOSURE artificial (Contrast) | Artificial discussion closure |
| 91 | Motte and Bailey | Defending strong claim by retreating to weaker one | BOUNDARY dynamic (Contrast) | Two claims of different strength treated as equivalent |
| 23 | Equivocation | Ambiguous terms to mislead | FRAME drift over occurrences (temporal) | A term's distinction drifts mid-argument, an identity-persistence failure = maintenance of the opposition frame over time (Paper III §6) |
| 93 | Red Herring | Irrelevant distraction | FRAME, off-question claim (Contrast) | Presents an off-question claim as occupying the position at issue; a same-axis diversion is a pure FRAME failure (Paper III §6). +Type 1 only when an axis-shift is also present |

**Type 5 count: 17** *(includes #23 Equivocation and #93 Red Herring, reclassified under the FRAME / opposition-topology reading of Paper III §6; their original sequence IDs are retained)*

---

## Type 1+5 Compound
*Axis transfer combined with contrast frame corruption.*

| # | Fallacy | Brief Description | AOML Violation | Notes |
|---|---------|------------------|----------------|-------|
| 92 | Whataboutism | Diverting with counter-accusations | SINC → VER (Axis) + CONTRAST | Axis diversion + false equivalence |

**Type 1+5 count: 1**

---

## Type 3+4 Compound
*Verification habitat mismatch combined with stratification misalignment.*

| # | Fallacy | Brief Description | AOML Violation | Notes |
|---|---------|------------------|----------------|-------|
| 94 | Appeal to Tradition (compound analysis) | Right because traditional | AUTH → NORM (Method) + TEMP levels (Level) | Custom as evidence + temporal level crossing |

**Note:** Appeal to Tradition appears at #49 as a primary Type 3 violation and here as a compound analysis showing its Type 4 component. It is counted once in the total.

---

## Type 5+4 Compound
*Contrast frame collapse combined with stratification misalignment.*

| # | Fallacy | Brief Description | AOML Violation | Notes |
|---|---------|------------------|----------------|-------|
| 98 | Package-Deal Fallacy | Separable claims or commitments fused into one indivisible object of acceptance or rejection | False fusion of the option space (Contrast) + component/package evaluation transfer (Level) | The inverse topology of false dilemma. Distinct from guilt by association (relational transfer) and composition (property inference after fusion) |

**Type 5+4 count: 1**

---

## Summary Statistics

| UFA Type | Name | Condition Violated | Count | Description |
|----------|------|--------------------|-------|-------------|
| Type 1 | Axis Transfer Error | Category | 23 | One kind of truth substituted for another |
| Type 2 | Operator Overextension | Composition licensing | 27 | Illicit compositional rule applied (includes R3, R5, R6, R7, R8, R9 subtypes) |
| Type 3 | Verification Habitat Mismatch | Validation | 13 | Wrong evidence type for the claim |
| Type 2+3 | Operator + Method compound | Composition + Validation | 1 | Operator overextension combined with method mismatch |
| Type 2+4 | Operator + Level compound | Composition + Stratification | 6 | Operator overextension combined with level misalignment |
| Type 4 | Stratification Misalignment | Stratification | 9 | Illegitimate level jump |
| Type 5 | Contrast Frame Collapse | Opposition topology *(precondition)* | 17 | False or inverted opposition (includes relevance/identity-persistence failures, Paper III §6) |
| Type 1+5 | Axis + Contrast compound | Category + Opposition topology | 1 | Axis transfer combined with contrast frame corruption |
| Type 2+5 | Operator + Contrast compound | Composition + Opposition topology | 2 | Operator overextension combined with contrast frame collapse |
| Type 5+4 | Contrast + Level compound | Opposition topology + Stratification | 1 | Contrast frame collapse combined with level misalignment |
| | **Total unique entries** | | **100** | |

*Note: Appeal to Tradition (#49/#94) is counted once. Several Type 3 entries (Confirmation Bias, Cherry Picking, Nut-Picking, Survivorship Bias) note possible compound components in their AOML Violation column but are primarily classified as Type 3. Entries #95–#98 were added in the July 2026 revision. Entries #99–#101 split names that each cover two structurally distinct errors (Appeal to Emotion #2/#99; Appeal to Authority #48/#100; Bandwagon/Argumentum ad Populum #47/#101), giving 101 numbered entries and 100 distinct fallacies. The total represents 100 unique fallacies with primary and compound classifications.*

---

## Key Structural Properties

1. **Empirical completeness**: Every classical and contemporary fallacy tested reduces to one of five boundary violation patterns, with compound violations decomposing into identified components. No sixth primitive type was required.

2. **Compound transparency**: Fallacies that combine multiple violation types are analyzed as compounds rather than forced into single categories. The compound nature explains why certain fallacies are more rhetorically effective: they exploit multiple failure modes simultaneously.

3. **AOML component mapping**: Each entry now explicitly identifies which AOML component is violated (Axis, Operator, Method, Level, Contrast), connecting the fallacy map directly to the constraint geometry and the argument from distinction (Paper III).

4. **Extensibility without negation**: If a sixth type were discovered, it would mean a fifth condition for coherent distinction-making exists beyond category, composition, validation, stratification, and opposition topology. The five existing types would remain valid.

5. **Cross-substrate applicability**: The same five violation types appear in human language (CLCA), engineering systems (oAOML), and 2,400 years of independent philosophical investigation, supporting the structural argument that these are conditions for coherent distinction-making rather than artifacts of any particular analytical tradition.

---

## Connection to AOML v2.2 and the Argument from Distinction

Each fallacy type corresponds to a violation of one condition for coherent distinction-making (Paper III):

- **Type 1 (Axis)** → Category condition: the system must track what kind of distinction it is making
- **Type 2 (Operator)** → Composition licensing condition: compositions must be licensed (includes R1–R4 and R7 structural rules; R5, R6, R8, R9 meta-axis substitution: the M[A] ↛ A family)
- **Type 3 (Method)** → Validation condition: evidence must match the claim type
- **Type 4 (Level)** → Stratification condition: level boundaries must be preserved across inference
- **Type 5 (Contrast)** → Opposition topology precondition: the space of possible distinctions must be correctly configured

The first four conditions correspond to the four AOML tuple components (A, O, M, L). Type 5 corresponds to the opposition-topology precondition (tokened the FRAME in the AOML v2.2 reference) that makes the other four possible. Four independent philosophical traditions each identified one of these conditions independently over 2,400 years.

---

## Related Documents

This map is one artifact in a series; several questions it raises are answered elsewhere.

- **Paper II, The Universal Fallacy Architecture.** Defines the AOML tuple, the structural rules R1 through R9 including the meta-axis substitution family M[A] does not yield A, and the derivation of the five types. The place to go for anything this map references but does not define.
- **Paper III, Given Distinction.** The closure argument: why there are exactly five types, why the opposition topology is a precondition rather than a fifth coordinate condition, and the historical convergence across independent traditions.
- **Terminology Correspondence** (companion). Maps every term used here to its nearest counterpart in linguistics, philosophy and epistemology, formal logic, and computer science, including a section that places the five violation types against argumentation theory, philosophy of logic, cognitive science, and AI vocabulary.
- **Paper I, Cross-Linguistic Compositional Analysis.** The cross-linguistic evidence the axes rest on. https://doi.org/10.5281/zenodo.21709636

On the exhaustiveness claim specifically: Paper II section 6.7 reports a pre-registered inter-rater study in which independent raters classified this inventory using only the five type definitions, with a *fallacy but fits no type* option available on every item and salted distractor items included. That study, not this map, is where the claim that no sixth type is required is put at risk.

---

*Companion document to: Seeley, B.A. (2026). The Universal Fallacy Architecture. Paper II, Foundations of the Convergent Semantic Architecture.*
*Structural foundation: Seeley, B.A. (2026). Given Distinction. Paper III, Foundations of the Convergent Semantic Architecture.*
*Empirical foundation: Seeley, B.A. (2026). Cross-Linguistic Compositional Analysis (CLCA). Paper I, Foundations of the Convergent Semantic Architecture. https://doi.org/10.5281/zenodo.21709636*
