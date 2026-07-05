#!/usr/bin/env bash
#
# Cross-tier P-phase probe with Claude Opus 4.8.
#
# Runs ONE P-phase pass per language (K=1) using claude-opus-4-8 as the
# informant, on the same 4 representative languages used in the K=5
# Sonnet saturation experiment (en, zh, ka, qu). The purpose is to
# compare Opus's single-probe P1 coverage against (a) Sonnet's single-
# probe baseline (data/<lang>/) and (b) Sonnet's K=5 union
# (data_saturation/<lang>/run_1..5/). The headline question: does a
# higher-capability model recover more vocabulary per probe, and does
# its K=1 coverage approach Sonnet's K=5 union?
#
# Output layout (flat — single probe per language):
#   data_opus/<lang>/
#     P1_vocab.content.txt
#     P5_oppositions.content.txt
#     ... etc.
#
# Cost estimate: 4 langs × ~9 P-phase prompts on Opus 4.8 ≈ 36 LLM calls.
#
# Overrides:
#   CLCA_OPUS_MODEL=claude-opus-4-8       (default)
#   CLCA_OPUS_LANGS="en zh ka qu"          (default)
#   CLCA_OPUS_OUT=data_opus                (default)

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

MODEL="${CLCA_OPUS_MODEL:-claude-opus-4-8}"
LANGS="${CLCA_OPUS_LANGS:-en zh ka qu}"
OUT="${CLCA_OPUS_OUT:-data_opus}"

mkdir -p logs "$OUT"

# Language code → "Name|Script" (bash 3.2 compatible).
lookup_lang() {
  case "$1" in
    en) echo "English|Latin" ;;
    zh) echo "Chinese|Han" ;;
    ka) echo "Georgian|Georgian" ;;
    qu) echo "Quechua|Latin" ;;
    fi) echo "Finnish|Latin" ;;
    yo) echo "Yoruba|Latin" ;;
    eu) echo "Basque|Latin" ;;
    ta) echo "Tamil|Tamil" ;;
    ko) echo "Korean|Hangul" ;;
    he) echo "Hebrew|Hebrew" ;;
    sa) echo "Sanskrit|Devanagari" ;;
    el) echo "Greek|Greek" ;;
    tl) echo "Tagalog|Latin" ;;
    sw) echo "Swahili|Latin" ;;
    id) echo "Indonesian|Latin" ;;
    tr) echo "Turkish|Latin" ;;
    *)  echo "" ;;
  esac
}

echo "============================================"
echo "  CLCA P-phase, Opus cross-tier probe"
echo "  Model:    $MODEL"
echo "  Langs:    $LANGS"
echo "  Out dir:  $OUT/"
echo "  Logs in:  logs/opus_*.log"
echo "============================================"
echo

PID_KEYS=()
PID_VALS=()

launch() {
  local code="$1"
  local info name script pid
  info="$(lookup_lang "$code")"
  if [ -z "$info" ]; then
    echo "  WARN: unknown language code '$code' — skipping"
    return
  fi
  name="${info%%|*}"
  script="${info##*|}"
  python3 -m src.runners.run_language \
    --data-dir "$OUT" \
    --language-name "$name" \
    --language-code "$code" \
    --script "$script" \
    --backend anthropic \
    --model-name "$MODEL" \
    --no-formatting \
    > "logs/opus_${code}.log" 2>&1 &
  pid=$!
  PID_KEYS+=("$code")
  PID_VALS+=("$pid")
  echo "  $code → PID $pid (log: logs/opus_${code}.log)"
}

for code in $LANGS; do
  launch "$code"
done

echo
echo "All Opus P-phase probes running. Tail with:  tail -f logs/opus_<code>.log"
echo "Waiting for completion..."
echo

worst=0
n=${#PID_KEYS[@]}
i=0
while [ $i -lt $n ]; do
  key="${PID_KEYS[$i]}"
  pid="${PID_VALS[$i]}"
  rc=0
  wait "$pid" || rc=$?
  if [ "$rc" -eq 0 ]; then
    echo "  $key: ✓"
  else
    echo "  $key: ✗ (exit $rc) — tail logs/opus_${key}.log"
    worst=$rc
  fi
  i=$((i + 1))
done

echo
echo "============================================"
if [ "$worst" -eq 0 ]; then
  echo "  Opus P-phase complete"
  echo
  echo "  Compare Opus vs Sonnet P1 coverage with:"
  echo "    python3 -m src.runners.compare_opus_vs_sonnet \\"
  echo "      --opus $OUT --sonnet data --saturation data_saturation \\"
  echo "      --langs $LANGS --output $OUT/opus_vs_sonnet.md"
else
  echo "  Opus P-phase finished with errors (worst exit $worst)"
fi
echo "============================================"

exit "$worst"
