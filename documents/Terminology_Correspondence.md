# Terminology Correspondence Table
## Mapping CLCA/AOML/UFA Vocabulary to Standard Disciplinary Terms
### Companion Document to the Foundations of the Convergent Semantic Architecture (Papers I–IV)
### Brent Alan Seeley · WellFlow Labs · April 2026, revised July–August 2026
### DOI: https://doi.org/10.5281/zenodo.21781768

---

## Purpose

The Convergent Semantic Architecture spans multiple disciplines: linguistic typology, epistemology, formal logic, argumentation theory, philosophy of language, and artificial intelligence. Because no single discipline's vocabulary covers the full framework, the papers use internally consistent terminology that may not match the standard terms in any one field. This document maps the framework's terms to their nearest equivalents in each relevant discipline, notes where the mapping is approximate, and explains the principled reasons for terminological choices.

This table is intended for specialists reading the papers from within a particular tradition. It does not claim that the framework's terms are synonymous with their disciplinary counterparts; it identifies the functional correspondence so that readers can locate the framework's concepts within their own analytical vocabulary. Mappings are functional correspondences, not strict equivalences. Where no close match exists, the cell indicates the nearest conceptual overlap or notes the absence.

---

> **Methodological note (governs every cell below): mappings are functional correspondences, not strict equivalences.** Each cell locates the framework term's nearest counterpart within a tradition; it does not assert synonymy.

## How to Read the Correspondences

Correspondences come in four grades, marked in the tables where the grade is not obvious from the cell's own wording:

| Marker | Grade | Meaning |
|---|---|---|
| ≈ | Close correspondence | The established term performs substantially the same structural role. |
| ~ | Partial correspondence | The terms overlap but differ in scope, historical use, or theoretical commitments. |
| (analog.) | Analogical correspondence | The established term occupies a similar position in another disciplinary system. |
| ∅ | No direct equivalent | The framework combines functions the discipline does not name as one concept. |

Cells that read "no direct equivalent; closest: ..." are grade ∅ with an analogical pointer. Unmarked correspondences should be read as functional but approximate unless the wording or an explicit marker indicates otherwise.

## Core Framework Terms

### Structural Components (AOML)

| CLCA/AOML Term | Linguistics | Philosophy / Epistemology | Formal Logic | Computer Science / AI |
|---|---|---|---|---|
| **Axis** (e.g., VER, AUTH, SINC, NORM, ESS, VERIF) | Semantic field, conceptual domain, lexical field | Truth-kind, alethic dimension, epistemic category | Propositional domain, typed predicate family, many-sorted domain, dimension of interpretation; ~ universe of discourse | State type, variable category, data domain |
| **Operator** (e.g., CAUSE, BECOME, ATTR, RESULT, REVEAL, ABSTR, STRAT, CONTR) | Compositional operator, semantic function; for specific operators: valence alternation, argument structure operation | Compositional relation, epistemic operation | Inference rule, derivation operator, typed transformation; logical connective for a limited subset | State transition function, transformation rule |
| **Method** (e.g., OBSERVATION, EXPERIMENT, TESTIMONY, LOGIC, CONSENSUS) | No direct equivalent; closest: evidential marking, epistemic stance markers | Epistemic justification type, warrant type, evidential basis | ∅ No full equivalent; closest: proof system, derivation method, admissible evidence, semantic evaluation procedure | Verification procedure, validation method, test oracle |
| **Level** (e.g., EMPIRICAL, CONVENTIONAL, FORMAL, ULTIMATE) | No direct equivalent; closest: register, pragmatic level | Ontological stratum, epistemic level, degree of abstraction | Object language / metalanguage distinction, logical type, order of predicate, level of abstraction, theory/model distinction | Abstraction layer, architecture layer, representation level, type hierarchy |
| **Meta-axis: DEG** (Degree) | Scalar modifier, degree word, intensifier | Epistemic strength, credence, degree of belief | Probability value, confidence level | Confidence score, logit, probability weight |
| **Meta-axis: TEMP** (Temporal) | Tense/aspect marking, temporal adverbial | Temporal indexicality, historical context | Temporal logic operator (past, future, since, until) | Timestamp, temporal state, version |
| **Meta-axis: LIKE** (Likeness / Similative) | Similative marking ("like / as-if"), comparative resemblance | Verisimilitude, semblance, appearance vs. reality | No direct equivalent; closest: model/interpretation resemblance | Simulation fidelity, synthetic data, deepfake / spoofing |

### Specific Axes

| CLCA/AOML Term | Linguistics | Philosophy / Epistemology | Formal Logic | AI / Safety |
|---|---|---|---|---|
| **VER** (Veridical) | Truth-conditional semantics, propositional content | Correspondence truth, alethic truth | Truth value, T/F assignment | Factual accuracy, world correspondence; claim grounding where grounding preserves a live evidential tether |
| **AUTH** (Authenticity) | No direct equivalent; closest: provenance marking | ≈ Genuineness, authenticity of origin or authorship, provenance. Existential authenticity (Heidegger, Trilling, Taylor) is a related but distinct use; autographic vs. allographic (Goodman) concerns conditions of work identity | No direct equivalent | Provenance verification, chain of custody |
| **SINC** (Sincerity) | Expressive meaning, speaker attitude | ≈ Sincerity conditions (Searle); speaker commitment; good faith; avowal congruence. The Gricean Quality maxim overlaps but also includes evidential and veridical constraints | No direct equivalent | Faithful reporting of internal state, calibrated self-report, non-deceptive output; intent alignment applies where systems are explicitly agentic |
| **NORM** (Normative) | Deontic modality, evaluative predication | Normative truth, deontic/evaluative domain, moral realism/anti-realism, ought-claims | Deontic logic operators (obligatory, permitted, forbidden) | Value alignment, normative constraint |
| **ESS** (Essence) | Definitional semantics, necessary predication | Essential vs. accidental properties (Aristotle, Kripke); metaphysical necessity; analytic truth in some definitional cases | Logical necessity, definitional axiom | Schema definition, type identity |
| **VERIF** (Verification) | Evidential morphology, epistemic modality | Verification, confirmation, epistemic access | Proof, derivability, proof procedure; decidability where a complete decision procedure exists | Testing, validation pipeline, evidence checking |
| **LIKE** (Likeness / Similative), *meta-axis, not a primary axis* | Similative marking; mimesis, iconicity | Verisimilitude = LIKE[VER] (aesthetic subset: lifelikeness); semblance, appearance vs. reality | No direct equivalent | Simulation fidelity; deepfake/spoofing = LIKE[AUTH] |

### Specific Operators

| CLCA/AOML Term | Linguistics | Philosophy / Epistemology | Formal Logic | AI / Safety |
|---|---|---|---|---|
| **CAUSE** | Causative morphology, causative alternation | Causal relation, efficient cause (Aristotle) | ∅ No equivalent in classical propositional logic; closest in specialized systems: causal conditional, counterfactual conditional, intervention operator, structural causal relation | Causal inference, intervention |
| **BECOME** | Inchoative alternation, change-of-state predicate | Change, becoming, process | State transition | State change, update operation |
| **ATTR** (Attribution) | Predication, property assignment | Property attribution, predication | Atomic formula, predicate application | Feature assignment, label |
| **RESULT** (Resultative) | Resultative construction, telic predicate | Achieved state, outcome | Conclusion, derived proposition | Output state, end state |
| **REVEAL** | No direct equivalent; closest: evidential discovery construction | Disclosure, aletheia/unconcealment (Heidegger); manifestation | No direct equivalent | Discovery, latent variable exposure |
| **ABSTR** (Abstraction) | Nominalization, derivational morphology | Abstraction, concept formation | Lambda abstraction, type lifting | Embedding, feature extraction |
| **STRAT** (Stratification) | No direct equivalent; closest: internal classification, taxonomic structure | Internal differentiation, sub-categorization | Subtyping, partition | Hierarchical classification |
| **CONTR** (Contrast) | Antonymy, opposition, contrastive focus | Opposition, negation, dialectical contrast | Negation, complement, disjunction | Binary classification, decision boundary |

---

## UFA Terms (Paper II)

| UFA Term | Argumentation Theory | Philosophy of Logic | Cognitive Science | AI / Safety |
|---|---|---|---|---|
| **Mode-Condition Collapse** | ∅ No direct equivalent; proposed common structural mechanism underlying the UFA-classified fallacies | Illicit analogical transfer; presupposition failure in mapping | Analogical transfer error, mapping failure | Structural account of hallucinations and reasoning failures involving domain transfer, invalid composition, evidence mismatch, level confusion, or corrupted contrast framing; constraint or representation mismatch |
| **Type 1: Axis Transfer Error** | Ignoratio elenchi (partially), irrelevant conclusion | Category mistake (Ryle), categorical confusion | Cross-domain mapping error | Domain confusion, type error |
| **Type 2: Operator Overextension** | Non sequitur, formal fallacy, invalid syllogism | Invalid inference, scope error, rule misapplication | Reasoning error, rule overgeneralization | Invalid state transition, illegal operation |
| **Type 3: Verification Habitat Mismatch** | Irrelevant appeal (ad populum, ad verecundiam, ad ignorantiam) | Epistemic mismatch, warrant failure, evidential error | Source monitoring error, evidence confusion | Wrong metric, validation mismatch |
| **Type 4: Stratification Misalignment** | Fallacy of composition/division, hasty generalization, accident | Level confusion, mereological fallacy; collapse or conflation of conventional and ultimate truth levels (cf. the Buddhist two-truths distinction, which exists to prevent precisely this conflation) | Abstraction error, base-rate neglect | Type-level confusion, abstraction leak |
| **Type 5: Contrast Frame Collapse** | False dilemma, false equivalence, straw man | No unified tradition; closest: dialectical error, binary reduction | Framing effect, anchoring | Decision boundary corruption, domain misspecification |
| **Compound violation** | No standard term; "complex fallacy" used loosely | No standard term | No standard term | Multi-fault failure, cascading error |

---

## Paper III Terms

| Paper III Term | Philosophy | Logic | Systems Theory |
|---|---|---|---|
| **The argument from distinction** | Transcendental argument (Kantian tradition); constitutive condition analysis | No direct equivalent; closest: metalogical analysis | Precondition analysis, invariant derivation |
| **Conditions for coherent distinction** | Conditions of possibility (Kant); constitutive rules (Searle) | Well-formedness conditions, formation rules | System invariants, coherence constraints |
| **Opposition topology** | Dialectical structure, logical space | Negation, complementation, Boolean structure | State space topology, partition structure |
| **Precondition vs. condition** | Transcendental vs. empirical conditions | Metalevel vs. object-level distinction | Infrastructure vs. application layer |

---

## Paper IV Terms

The entries below are nearest analogues, not translations. Each row indicates where a term's closest counterpart lies in an established vocabulary and how far the correspondence extends; it does not claim that the concepts are interchangeable.

| Paper IV Term | Function within Paper IV | Nearest philosophical analogue | Formal-semantic expression | AI / epistemic-engineering analogue |
|---|---|---|---|---|
| **Distinction integrity** (the truth substrate) | Preserves the contrastive structure required for anything to count as determinately true rather than collapsed or indiscriminate | Preconditions of determinacy and intelligible predication; preservation of the true/false distinction; no standard equivalent for the substrate as such | Non-degenerate interpretation or partition; distinguishable semantic values; exclusion of models that collapse the relevant contrast | Preservation of decision-relevant distinctions in representations, labels, and outputs; avoidance of representational collapse |
| **Axis-relative truth** | Makes correctness depend upon the semantic dimension along which a claim is operating, without making truth merely subjective | Alethic pluralism and discourse-sensitive truth, especially Lynch's manifestation functionalism and Wright's domain-sensitive account; AOML axes are more explicitly dimensional | Axis-indexed satisfaction relations or evaluation functions; typed or many-sorted languages may enforce the separation of axes | Axis- or task-conditioned correctness specifications; evaluations indexed to the kind of claim rather than one undifferentiated score |
| **Two-ingredient framework** (integrity always; external correspondence on some axes) | Requires distinction integrity universally while requiring external tethering only where the governing axis calls for correspondence | A general truth role combined with domain-sensitive realization, grounding, or correspondence conditions | Non-collapsed internal semantics plus, where required, an interpretation or validation relation tied to an external target system | Representational integrity as a universal requirement; external grounding, measurement, provenance, or source tethering where correspondence is required |
| **Substrate monism, realizer pluralism** | Holds that truth has a common underlying condition while its successful realization differs by axis | Lynch's "one role, many realizers" or manifestation functionalism; AOML's substrate language may imply a stronger ontological commitment | A common satisfaction or correctness schema instantiated through axis-specific interpretations, valuations, or validation relations | A common correctness architecture with domain-specific validators, grounding channels, and evaluation mechanisms |
| **Home axis** (of a truth tradition) | Identifies the semantic axis on which a truth tradition's operator is naturally and properly licensed | The discourse or dimension in which a truth theory has its strongest explanatory fit | Intended class of models or designated semantic dimension over which a satisfaction rule is licensed | The task or claim class for which a validator, evaluator, or grounding method is properly licensed |
| **Truth-structure** | The organized conditions and validation relations through which claims on an axis can succeed as true | Domain-specific truth conditions or realization profile | Typed form of the relevant satisfaction or validation relation | Claim-specific correctness contract: required evidence, provenance, validator, and acceptance conditions |

**Note:** Paper IV §10 relates the truth traditions discussed here to the four error traditions developed in Paper III. The relation is one of structural duality, not one-to-one terminological equivalence. The error traditions map directly onto the four AOML conditions (Axis, Operator, Method, and Level) because failure can often be localized to the violation of a single condition. The truth traditions instead have their natural homes on the semantic axes VER, ESS/FORMAL, SINC/AUTH, and VERIF. Their correspondence is therefore asymmetric: successful truth typically requires an integrated truth-structure, and does not decompose into independent components as cleanly as error does.

## Terminological Choices: Rationale

The framework uses its own vocabulary rather than adopting any single discipline's terms for three reasons:

**Cross-disciplinary scope.** No single discipline's vocabulary covers the full framework. Linguistic terms cover the axes and operators but have no equivalent for methods or levels as used here. Epistemological terms cover methods and levels but handle operators differently. Formal logic terms cover operator licensing but have no equivalent for axes as semantic domains. Using one discipline's vocabulary would make the framework legible to that discipline while obscuring it for others.

**Functional precision.** The framework's terms are defined by their structural role in the constraint geometry, not by their historical associations. "Axis" was chosen over "semantic field" because the framework treats axes as dimensions of a geometric space with licensing constraints, not as collections of related words. "Operator" was chosen over "valence alternation" because the framework treats operators as compositional functions that may be licensed or blocked, not as morphosyntactic processes. Each term carries its AOML definition rather than the associations of its nearest disciplinary equivalent.

**Internal consistency.** The AOML tuple (Axis, Operator, Method, Level) is designed as a coherent system where the four components play structurally parallel roles. Borrowing terms from four different disciplines would obscure this parallelism. The uniform terminology makes the structural relationships visible: each component can be violated, and each violation produces a distinct failure type. Within the framework, the four components together with the contrast precondition are proposed as jointly exhaustive conditions for coherent distinction-making; the argument for exhaustiveness is developed in Paper III.

Where the framework's terms do correspond closely to existing disciplinary terms (e.g., "causative" for CAUSE, "inchoative" for BECOME, "sincerity conditions" for SINC), the correspondence is noted in the relevant paper and in the tables above. Where the correspondence is approximate, the tables note the approximation. Where no disciplinary equivalent exists (e.g., "verification habitat," "Mode-Condition Collapse"), the term is novel to this framework. The recurrence of these functional roles across otherwise distinct disciplines does not by itself establish the framework's completeness. It does, however, indicate that Axis, Operator, Method, and Level are not arbitrary inventions: they name recurrent structural functions that linguistic, philosophical, logical, and computational traditions have each encountered under domain-specific descriptions, distributed across their vocabularies rather than represented as one coordinated system. No single column of these tables contains the tuple in full; that distribution is itself the evidence that a unifying coordinate system was missing. The contribution of AOML is to place those functions within a common coordinate system and make their interactions explicit.

Readers who prefer their home discipline's terminology are encouraged to use this table as a translation tool; the framework's vocabulary is offered as a unifying layer across disciplines, not as a replacement for any discipline's established terms.

---

## Conclusion

The correspondences documented here show that the components of the AOML tuple recur across linguistic, philosophical, logical, and computational traditions, although no single tradition names or coordinates all four components in the same way. This recurrence does not prove that the framework is complete or uniquely formulated. It does show that its central terms identify recognizable structural functions rather than arbitrary private categories.

The framework's proposed contribution is therefore coordinative: it places category, composition, validation, and stratification within one common geometry and makes their interactions and characteristic failure modes explicit. The empirical case for that geometry is developed in Papers I and II; the argument for its structural exhaustiveness is developed in Paper III.

---

*Companion document to: Seeley, B.A. (2026). Foundations of the Convergent Semantic Architecture, Papers I–IV.*
