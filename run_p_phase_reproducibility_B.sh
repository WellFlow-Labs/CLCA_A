#!/usr/bin/env bash
#
# Re-run P+I+F for Set B on data_reproducibility/ — 8 languages in parallel.
# See run_p_phase_reproducibility.sh for Set A.

set -euo pipefail
cd "$(dirname "$0")"

# ---- Activate project venv if present ------------------------------------
if [ -f .venv/bin/activate ]; then
  # shellcheck disable=SC1091
  . .venv/bin/activate
fi

# ---- API key indirection -------------------------------------------------
if [ -z "${ANTHROPIC_API_KEY:-}" ] && [ -n "${AOML_ANTHROPIC_API_KEY:-}" ]; then
  export ANTHROPIC_API_KEY="$AOML_ANTHROPIC_API_KEY"
fi
: "${ANTHROPIC_API_KEY:?Set ANTHROPIC_API_KEY or AOML_ANTHROPIC_API_KEY before running.}"

MODEL="${CLCA_PF_MODEL:-claude-sonnet-4-6}"
DATA_DIR="${CLCA_DATA_DIR:-data_reproducibility}"

mkdir -p logs

echo "============================================"
echo "  CLCA P+I+F rerun, Set B (parallel: 8 languages)"
echo "  Model:    $MODEL"
echo "  Data dir: $DATA_DIR"
echo "  Logs in:  logs/"
echo "============================================"
echo

for lang in zh he sa el en tl sw qu; do
  rm -rf "$DATA_DIR/$lang"
done

declare -A pids
launch() {
  local name="$1" code="$2" script="$3"
  python3 -m src.runners.run_language \
    --data-dir "$DATA_DIR" \
    --language-name "$name" \
    --language-code "$code" \
    --script "$script" \
    --backend anthropic \
    --model-name "$MODEL" \
    > "logs/pf_${code}.log" 2>&1 &
  pids[$code]=$!
  echo "  $code ($name) → PID ${pids[$code]} (log: logs/pf_${code}.log)"
}

launch "Chinese"  zh Han
launch "Hebrew"   he Hebrew
launch "Sanskrit" sa Devanagari
launch "Greek"    el Greek
launch "English"  en Latin
launch "Tagalog"  tl Latin
launch "Swahili"  sw Latin
launch "Quechua"  qu Latin

echo
echo "All 8 languages running. Tail any log with:  tail -f logs/pf_<code>.log"
echo "Waiting for completion..."
echo

worst=0
for code in "${!pids[@]}"; do
  rc=0
  wait "${pids[$code]}" || rc=$?
  if [ "$rc" -eq 0 ]; then
    echo "  $code: ✓"
  else
    echo "  $code: ✗ (exit $rc)  — tail logs/pf_${code}.log"
    worst=$rc
  fi
done

echo
echo "============================================"
if [ "$worst" -eq 0 ]; then
  echo "  P+I+F rerun complete for Set B"
  echo
  echo "  Next: G-phase with ./run_g_phase_reproducibility.sh"
else
  echo "  P+I+F rerun finished with errors (worst exit $worst)"
fi
echo "============================================"

exit "$worst"
