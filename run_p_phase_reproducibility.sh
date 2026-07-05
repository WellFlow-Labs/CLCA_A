#!/usr/bin/env bash
#
# Re-run P+I+F for Set A on data_reproducibility/ — 8 languages in parallel.
# Use only if you want a fresh P-phase rerun; the existing data_reproducibility/
# P-phase data is intact and not truncated.
#
# Override the model if needed (e.g. opus for higher quality):
#   CLCA_PF_MODEL=claude-opus-4-7 ./run_p_phase_reproducibility.sh
#
# Parallelism is bounded by the runner's TPM throttling (settings.toml
# tpm_limit = 400000 per Tier 3/4 limit).

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
echo "  CLCA P+I+F rerun, Set A (parallel: 8 languages)"
echo "  Model:    $MODEL"
echo "  Data dir: $DATA_DIR"
echo "  Logs in:  logs/"
echo "============================================"
echo

# Clean only Set A subdirs (Set B and globals untouched).
for lang in ka yo fi eu ta id tr ko; do
  rm -rf "$DATA_DIR/$lang"
done

# ---- Per-language launch helper -----------------------------------------
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

launch "Georgian"   ka Georgian
launch "Yoruba"     yo Latin
launch "Finnish"    fi Latin
launch "Basque"     eu Latin
launch "Tamil"      ta Tamil
launch "Indonesian" id Latin
launch "Turkish"    tr Latin
launch "Korean"     ko Hangul

echo
echo "All 8 languages running. Tail any log with:  tail -f logs/pf_<code>.log"
echo "Waiting for completion..."
echo

# ---- Wait + per-language status -----------------------------------------
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
  echo "  P+I+F rerun complete for Set A"
  echo
  echo "  Next: run Set B with  ./run_p_phase_reproducibility_B.sh"
  echo "        then G-phase with ./run_g_phase_reproducibility.sh"
else
  echo "  P+I+F rerun finished with errors (worst exit $worst)"
fi
echo "============================================"

exit "$worst"
