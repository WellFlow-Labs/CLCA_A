#!/usr/bin/env bash
#
# Re-run G-phase on data_reproducibility/ for Set A and Set B in parallel.
# Default model is claude-sonnet-4-6 (1M-context Sonnet generation).
#
# Override the model if needed (e.g. opus for higher quality):
#   CLCA_G_MODEL=claude-opus-4-7 ./run_g_phase_reproducibility.sh
#
# API key resolution: uses ANTHROPIC_API_KEY if set, otherwise re-exports
# AOML_ANTHROPIC_API_KEY into ANTHROPIC_API_KEY for the runner.

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

# ---- Parameters ----------------------------------------------------------
MODEL="${CLCA_G_MODEL:-claude-sonnet-4-6}"
DATA_DIR="${CLCA_DATA_DIR:-data_reproducibility}"

mkdir -p logs

echo "============================================"
echo "  CLCA G-phase rerun (parallel: Set A + Set B)"
echo "  Model:    $MODEL"
echo "  Data dir: $DATA_DIR"
echo "  Logs in:  logs/"
echo "============================================"
echo

# ---- Clean prior G-phase outputs (idempotent) ----------------------------
rm -rf "$DATA_DIR/global_set_A" "$DATA_DIR/global_set_B"

# ---- Launch both sets in parallel ----------------------------------------
echo "Starting Set A G-phase in background..."
python3 -m src.runners.run_global_analysis \
  --data-dir "$DATA_DIR" \
  --languages ka yo fi eu ta id tr ko \
  --backend anthropic \
  --model-name "$MODEL" \
  --output-code global_set_A \
  > logs/g_phase_A.log 2>&1 &
PID_A=$!
echo "  PID $PID_A  (log: logs/g_phase_A.log)"

echo "Starting Set B G-phase in background..."
python3 -m src.runners.run_global_analysis \
  --data-dir "$DATA_DIR" \
  --languages zh he sa el en tl sw qu \
  --backend anthropic \
  --model-name "$MODEL" \
  --output-code global_set_B \
  > logs/g_phase_B.log 2>&1 &
PID_B=$!
echo "  PID $PID_B  (log: logs/g_phase_B.log)"

echo
echo "Both sets running. Tail the logs to watch progress:"
echo "  tail -f logs/g_phase_A.log logs/g_phase_B.log"
echo

# ---- Wait for both, report status ----------------------------------------
RC_A=0
RC_B=0
wait "$PID_A" || RC_A=$?
wait "$PID_B" || RC_B=$?

echo
echo "============================================"
if [ "$RC_A" -eq 0 ]; then
  echo "  Set A: ✓ complete"
else
  echo "  Set A: ✗ failed (exit $RC_A) — tail of log:"
  tail -25 logs/g_phase_A.log | sed 's/^/    /'
fi
if [ "$RC_B" -eq 0 ]; then
  echo "  Set B: ✓ complete"
else
  echo "  Set B: ✗ failed (exit $RC_B) — tail of log:"
  tail -25 logs/g_phase_B.log | sed 's/^/    /'
fi
echo "============================================"

if [ "$RC_A" -eq 0 ] && [ "$RC_B" -eq 0 ]; then
  echo
  echo "Next: run the G-phase comparison:"
  echo "  python3 -m src.runners.compare_g_phase \\"
  echo "    --baseline data \\"
  echo "    --rerun $DATA_DIR \\"
  echo "    --set all \\"
  echo "    --output $DATA_DIR/g_phase_comparison_report.txt"
fi

# Propagate worst exit code
exit $(( RC_A > RC_B ? RC_A : RC_B ))
