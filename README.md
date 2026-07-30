# Cross-Linguistic Compositional Analysis (CLCA)

Reproducible code, prompts, and data for the four-paper series **"Foundations of the Convergent Semantic Architecture."** CLCA recovers a shared semantic architecture for truth-related meaning by decompiling how sixteen unrelated languages compose it, and derives from that architecture a structural account of reasoning error (the Universal Fallacy Architecture) and of truth itself.

> **Papers:** Paper I is available at https://doi.org/10.5281/zenodo.21709636 (Papers II-IV forthcoming). This repository is the companion artifact: everything needed to inspect, run, and build on the findings.

## What's here

- **The protocol** (`src/`, `prompts/`, `configs/`) — a reproducible, LLM-assisted pipeline that elicits structured, language-specific data and synthesizes it cross-linguistically. The prompts contain no axis names and no theoretical vocabulary; the architecture is meant to emerge from the data, not be imposed on it.
- **The architecture** (`aoml/`, `Aoml_v2.2_constraint_architecture.html`) — AOML v2.2: six primary axes, four meta-axes, the operators and levels, and the structural rules. Machine-readable matrices plus a human-readable reference.
- **The data** (`data*/`) — the full outputs behind the papers (see below).
- **Reference** (`documents/`) — the Universal Fallacy Map (94 fallacies mapped to 5 error types) and a terminology-correspondence table. The four papers themselves are posted on a preprint server (see *Papers* above) and will be cross-linked here once final.

## The sixteen languages

Two independent eight-language sets that share no languages — ten genetically unrelated families plus three isolates:

- **Set A:** Georgian, Yoruba, Finnish, Basque, Tamil, Indonesian, Turkish, Korean
- **Set B:** Chinese, Hebrew, Sanskrit, Greek, English, Tagalog, Swahili, Quechua

The protocol is also run two ways (one neutral, one domain-seeded) as a mutual control, so a pattern only counts as a finding if it surfaces in both sets and both protocol variants independently.

## Reproduce

```bash
conda env create -f environment.yml
conda activate clca
export ANTHROPIC_API_KEY=...      # Anthropic backend (default)
export OPENAI_API_KEY=...         # only needed for the GPT-5.4 cross-model run
```

Single language:

```bash
python -m src.runners.run_language --language-name "Georgian" --language-code ka --script Georgian
```

A full eight-language set plus the cross-language G-phase synthesis (Windows `.bat` drivers shown; the `.sh` equivalents are alongside):

```bash
run_full_pipeline.bat        # Anthropic, Set A  -> data/
run_full_pipeline_B.bat      # Anthropic, Set B  -> data/
run_full_pipeline_gpt54.bat  # GPT-5.4,   Set A  -> data_gpt54/
```

G-phase synthesis only:

```bash
python -m src.runners.run_global_analysis \
  --languages ka yo fi eu ta id tr ko \
  --backend anthropic --model-name claude-sonnet-4-5 \
  --output-code global_set_A
```

Check completeness, and diff a fresh run against the shipped one:

```bash
python -m src.runners.verify_languages configs/global_set_A_codes.toml
python -m src.runners.compare_runs --baseline data --rerun <your-output-dir>
```

Because LLM informants are non-deterministic, exact strings will differ run to run; the claims are about structural patterns, and `data_reproducibility/` is an independent second run included precisely so you can measure run-to-run stability.

## The data

Every directory is a complete run — ship-and-diff is the point.

| Directory | What it is |
|---|---|
| `data/` | Canonical Anthropic (Claude Sonnet) run, Sets A & B — the primary evidence |
| `data_gpt54/` | Parallel GPT-5.4 run — cross-model robustness check |
| `data_reproducibility/` | Independent second Anthropic run — within-protocol run-to-run stability |
| `data_union/` | 16-language union pipeline (K-probe merge → consolidated F + G) behind AOML v2.2 |
| `data_saturation/` | P-phase saturation-curve runs |
| `data_baseline_4_6/` | Earlier baseline comparison run |
| `data_opus/` | Higher-tier (Opus) cross-tier probe |

Each `<lang>/` directory holds the per-phase P / I / F outputs; each `global_set_*/` holds the G1–G9 cross-language synthesis, including **G7b**, the step that compares the elicited data against the AOML reference architecture.

## License

- **Code:** Apache 2.0 (`LICENSE_APACHE_2.0`)
- **Data / prompts / documents:** CC-BY-4.0 (`LICENSE_CC_by_4.0`)

You are free to use, modify, and build upon this work (including commercially) as long as you provide appropriate credit and keep provenance of derived datasets/code. These copyright licenses do **not** grant patent rights (see Patent below).

## Patent

The knowledge here — the architecture, the legality matrix, the fallacy taxonomy, and the data — is **open under the licenses above**: read it, share it, teach it, build on it with attribution. **Applying it in a computational or AI system** (using the axes, operators, legality matrix, or AOML tuples to tag, validate, constrain, or enforce semantic structure in software or an AI model) is **patent-pending** and may require a separate patent license. The patent-pending enforcement systems are not contained in this repository. See [`PATENTS.md`](PATENTS.md). _(Informational, not legal advice.)_

## Citation

Seeley, B. A. (2026). *Cross-Linguistic Compositional Analysis (CLCA): A Reproducible Protocol for Recovering Shared Conceptual Structure from Cross-Linguistic Evidence.* Paper I, Foundations of the Convergent Semantic Architecture. https://doi.org/10.5281/zenodo.21709636

The series as a whole: Seeley, B. A. (2026). *Foundations of the Convergent Semantic Architecture* (Papers I-IV). Papers II-IV forthcoming.
