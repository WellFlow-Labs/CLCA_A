# Terminology Correspondence Table
## Mapping CLCA/AOML/UFA Vocabulary to Standard Disciplinary Terms
### Companion Document to the Foundations of the Convergent Semantic Architecture (Papers I–III)
### Brent Alan Seeley · Independent Researcher · April 2026

---

## Purpose

The Convergent Semantic Architecture spans multiple disciplines: linguistic typology, epistemology, formal logic, argumentation theory, philosophy of language, and artificial intelligence. Because no single discipline's vocabulary covers the full framework, the papers use internally consistent terminology that may not match the standard terms in any one field. This document maps the framework's terms to their nearest equivalents in each relevant discipline, notes where the mapping is approximate, and explains the principled reasons for terminological choices.

This table is intended for specialists reading the papers from within a particular tradition. It does not claim that the framework's terms are synonymous with their disciplinary counterparts; it identifies the functional correspondence so that readers can locate the framework's concepts within their own analytical vocabulary. Mappings are functional correspondences, not strict equivalences. Where no close match exists, the cell indicates the nearest conceptual overlap or notes the absence.

---

## Core Framework Terms

### Structural Components (AOML)

| CLCA/AOML Term | Linguistics | Philosophy / Epistemology | Formal Logic | Computer Science / AI |
|---|---|---|---|---|
| **Axis** (e.g., VER, AUTH, SINC, NORM, ESS, VERIF) | Semantic field, conceptual domain, lexical field | Truth-kind, alethic dimension, epistemic category | Propositional domain, universe of discourse | State type, variable category, data domain |
| **Operator** (e.g., CAUSE, BECOME, ATTR, RESULT, REVEAL, ABSTR, STRAT, CONTR) | Compositional operator, semantic function; for specific operators: valence alternation, argument structure operation | Compositional relation, epistemic operation | Inference rule, logical connective, derivation step | State transition function, transformation rule |
| **Method** (e.g., OBSERVATION, EXPERIMENT, TESTIMONY, LOGIC, CONSENSUS) | No direct equivalent; closest: evidential marking, epistemic stance markers | Epistemic justification type, warrant type, evidential basis | No direct equivalent; closest: proof method, decision procedure | Verification procedure, validation method, test oracle |
| **Level** (e.g., EMPIRICAL, CONVENTIONAL, FORMAL, ULTIMATE) | No direct equivalent; closest: register, pragmatic level | Ontological stratum, epistemic level, degree of abstraction | Quantifier scope, metalanguage level, type hierarchy | Abstraction layer, data type level, scope boundary |
| **Meta-axis: DEG** (Degree) | Scalar modifier, degree word, intensifier | Epistemic strength, credence, degree of belief | Probability value, confidence level | Confidence score, logit, probability weight |
| **Meta-axis: TEMP** (Temporal) | Tense/aspect marking, temporal adverbial | Temporal indexicality, historical context | Temporal logic operator (past, future, since, until) | Timestamp, temporal state, version |
| **Meta-axis: LIKE** (Likeness / Similative) | Similative marking ("like / as-if"), comparative resemblance | Verisimilitude, semblance, appearance vs. reality | No direct equivalent; closest: model/interpretation resemblance | Simulation fidelity, synthetic data, deepfake / spoofing |

### Specific Axes

| CLCA/AOML Term | Linguistics | Philosophy / Epistemology | Formal Logic | AI / Safety |
|---|---|---|---|---|
| **VER** (Veridical) | Truth-conditional semantics, propositional content | Correspondence truth, alethic truth | Truth value, T/F assignment | Factual accuracy, groundedness |
| **AUTH** (Authenticity) | No direct equivalent; closest: provenance marking | Authenticity (Heidegger, Trilling, Taylor); genuineness; autographic vs. allographic (Goodman) | No direct equivalent | Provenance verification, chain of custody |
| **SINC** (Sincerity) | Expressive meaning, speaker attitude | Sincerity conditions (Searle); Gricean Quality maxim; inner alignment; good faith | No direct equivalent | Intent alignment, honest reporting |
| **NORM** (Normative) | Deontic modality, evaluative predication | Normative truth, deontic/evaluative domain, moral realism/anti-realism, ought-claims | Deontic logic operators (obligatory, permitted, forbidden) | Value alignment, normative constraint |
| **ESS** (Essence) | Definitional semantics, necessary predication | Essential vs. accidental properties (Aristotle, Kripke); analytic truth | Logical necessity, definitional axiom | Schema definition, type identity |
| **VERIF** (Verification) | Evidential morphology, epistemic modality | Verification, confirmation, epistemic access | Proof, decidability, verification procedure | Testing, validation pipeline, evidence checking |
| **LIKE** (Likeness / Similative) — *meta-axis, not a primary axis* | Similative marking; mimesis, iconicity | Verisimilitude = LIKE[VER] (aesthetic subset: lifelikeness); semblance, appearance vs. reality | No direct equivalent | Simulation fidelity; deepfake/spoofing = LIKE[AUTH] |

### Specific Operators

| CLCA/AOML Term | Linguistics | Philosophy / Epistemology | Formal Logic | AI / Safety |
|---|---|---|---|---|
| **CAUSE** | Causative morphology, causative alternation | Causal relation, efficient cause (Aristotle) | Material conditional (loosely), causal operator | Causal inference, intervention |
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
| **Mode-Condition Collapse** | No direct equivalent; describes the mechanism underlying all fallacies | Illicit analogical transfer; presupposition failure in mapping | Analogical transfer error, mapping failure | Hallucination mechanism, structural error |
| **Type 1: Axis Transfer Error** | Ignoratio elenchi (partially), irrelevant conclusion | Category mistake (Ryle), categorical confusion | Cross-domain mapping error | Domain confusion, type error |
| **Type 2: Operator Overextension** | Non sequitur, formal fallacy, invalid syllogism | Invalid inference, scope error, rule misapplication | Reasoning error, rule overgeneralization | Invalid state transition, illegal operation |
| **Type 3: Verification Habitat Mismatch** | Irrelevant appeal (ad populum, ad verecundiam, ad ignorantiam) | Epistemic mismatch, warrant failure, evidential error | Source monitoring error, evidence confusion | Wrong metric, validation mismatch |
| **Type 4: Stratification Misalignment** | Fallacy of composition/division, hasty generalization, accident | Level confusion, mereological fallacy; two-truths collapse (Buddhist) | Abstraction error, base-rate neglect | Type-level confusion, abstraction leak |
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

## Terminological Choices: Rationale

The framework uses its own vocabulary rather than adopting any single discipline's terms for three reasons:

**Cross-disciplinary scope.** No single discipline's vocabulary covers the full framework. Linguistic terms cover the axes and operators but have no equivalent for methods or levels as used here. Epistemological terms cover methods and levels but handle operators differently. Formal logic terms cover operator licensing but have no equivalent for axes as semantic domains. Using one discipline's vocabulary would make the framework legible to that discipline while obscuring it for others.

**Functional precision.** The framework's terms are defined by their structural role in the constraint geometry, not by their historical associations. "Axis" was chosen over "semantic field" because the framework treats axes as dimensions of a geometric space with licensing constraints, not as collections of related words. "Operator" was chosen over "valence alternation" because the framework treats operators as compositional functions that may be licensed or blocked, not as morphosyntactic processes. Each term carries its AOML definition rather than the associations of its nearest disciplinary equivalent.

**Internal consistency.** The AOML tuple (Axis, Operator, Method, Level) is designed as a coherent system where the four components play structurally parallel roles. Borrowing terms from four different disciplines would obscure this parallelism. The uniform terminology makes the structural relationships visible: each component can be violated, each violation produces a distinct failure type, and the four components plus the contrast precondition exhaust the conditions for coherent distinction-making.

Where the framework's terms do correspond closely to existing disciplinary terms (e.g., "causative" for CAUSE, "inchoative" for BECOME, "sincerity conditions" for SINC), the correspondence is noted in the relevant paper and in the tables above. Where the correspondence is approximate, the tables note the approximation. Where no disciplinary equivalent exists (e.g., "verification habitat," "Mode-Condition Collapse"), the term is novel to this framework. Readers who prefer their home discipline's terminology are encouraged to use this table as a translation tool; the framework's vocabulary is offered as a unifying layer across disciplines, not as a replacement for any discipline's established terms.

---

*Companion document to: Seeley, B.A. (2026). Papers I–III, Foundations of the Convergent Semantic Architecture.*
