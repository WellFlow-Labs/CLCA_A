#!/usr/bin/env bash
#
# Union pipeline — Step 2: LLM-based merge of K P-phase probes per language.
#
# Calls src.runners.run_merge for each of the 16 languages. For each
# language, writes one consolidated output per P-phase layer at
# data_union/<lang>/<layer>.content.txt — the same filename the F-phase
# expects, so Step 3 (F-phase via run_language.py --resume) reads the
# merged P-phase as if it were a single probe.
#
# Cost: 16 langs × 9 P-phase layers = 144 merge calls on Sonnet 4-6.
#
# Overrides:
#   CLCA_UNION_MODEL=claude-sonnet-4-6  (default)
#   CLCA_UNION_OUT=data_union           (default)
#   CLCA_UNION_LANGS="..."              (default: all 16)
#   CLCA_UNION_LAYERS="P1_vocab P5_oppositions ..."  (default: all 9)
#   CLCA_UNION_FORCE=1                   to overwrite existing merged outputs

set -euo pipefail
cd "$(dirname "$0")"

if [ -f .venv/bin/activate ]; then
  # shellcheck disable=SC1091
  . .venv/bin/activate
fi

if [ -z "${ANTHROPIC_API_KEY:-}" ] && [ -n "${AOML_ANTHROPIC_API_KEY:-}" ]; then
  export ANTHROPIC_API_KEY="$AOML_ANTHROPIC_API_KEY"
fi
: "${ANTHROPIC_API_KEY:?Set ANTHROPIC_API_KEY or AOML_ANTHROPIC_API_KEY before running.}"

MODEL="${CLCA_UNION_MODEL:-claude-sonnet-4-6}"
OUT="${CLCA_UNION_OUT:-data_union}"
LANGS="${CLCA_UNION_LANGS:-ka yo fi eu ta id tr ko zh he sa el en tl sw qu}"
LAYERS="${CLCA_UNION_LAYERS:-}"
FORCE_FLAG=""
if [ -n "${CLCA_UNION_FORCE:-}" ]; then
  FORCE_FLAG="--force"
fi

mkdir -p logs

echo "============================================"
echo "  Union pipeline — Step 2: merge probes"
echo "  Model: $MODEL"
echo "  Out:   $OUT/<lang>/<layer>.content.txt"
echo "============================================"
echo

CMD=(python3 -m src.runners.run_merge --root "$OUT" --langs $LANGS --model-name "$MODEL")
if [ -n "$LAYERS" ]; then
  CMD+=(--layers $LAYERS)
fi
if [ -n "$FORCE_FLAG" ]; then
  CMD+=("$FORCE_FLAG")
fi

echo "Running: ${CMD[*]}"
echo
"${CMD[@]}" 2>&1 | tee logs/union_merge.log
rc=${PIPESTATUS[0]}

echo
echo "============================================"
if [ "$rc" -eq 0 ]; then
  echo "  Step 2 complete — merged P-phase ready for all languages"
  echo "  Next:  ./run_union_step3_fg.sh"
else
  echo "  Step 2 finished with errors (exit $rc) — see logs/union_merge.log"
fi
echo "============================================"

exit "$rc"
