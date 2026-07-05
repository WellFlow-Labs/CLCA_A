#!/usr/bin/env bash
#
# Re-run G-phase on the BASELINE F-phase data using Sonnet 4-6.
# Same input as data/ baseline; new synthesis model.
#
# Purpose: isolate the model-upgrade effect from the run-to-run variance.
# The reproducibility rerun used Sonnet 4-6 for G-phase (because 4-5's
# 200K context wasn't enough); the baseline used Sonnet 4-5. Comparing
# this 4-6-on-baseline-F output against the rerun-4-6 output gives a
# clean within-model G-phase reproducibility number.
#
# Output goes to data_baseline_4_6/. The original data/ is not touched.

set -euo pipefail
cd "$(dirname "$0")"

# Activate venv if present
if [ -f .venv/bin/activate ]; then
  # shellcheck disable=SC1091
  . .venv/bin/activate
fi

# API key indirection
if [ -z "${ANTHROPIC_API_KEY:-}" ] && [ -n "${AOML_ANTHROPIC_API_KEY:-}" ]; then
  export ANTHROPIC_API_KEY="$AOML_ANTHROPIC_API_KEY"
fi
: "${ANTHROPIC_API_KEY:?Set ANTHROPIC_API_KEY or AOML_ANTHROPIC_API_KEY before running.}"

MODEL="${CLCA_G_MODEL:-claude-sonnet-4-6}"
OUT_DIR="data_baseline_4_6"

mkdir -p logs "$OUT_DIR"

# ---- Symlink language F-phase data from data/ into OUT_DIR -----------------
# The runner expects per-language F-phase outputs at <data-dir>/<lang>/.
# Symlinks avoid duplicating ~2 MB per language.
echo "Symlinking language data from data/ into $OUT_DIR/ ..."
for lang in ka yo fi eu ta id tr ko zh he sa el en tl sw qu; do
  target="$OUT_DIR/$lang"
  if [ -e "$target" ] || [ -L "$target" ]; then
    rm -rf "$target"
  fi
  ln -s "../data/$lang" "$target"
done
echo "  done."
echo

# ---- Clean any prior G-phase outputs in the 4-6 directory ------------------
rm -rf "$OUT_DIR/global_set_A" "$OUT_DIR/global_set_B"

echo "============================================"
echo "  CLCA G-phase, baseline F-phase data, $MODEL"
echo "  Input symlinks → data/<lang>/"
echo "  G output:        $OUT_DIR/global_set_{A,B}/"
echo "  Logs in:         logs/"
echo "============================================"
echo

# ---- Launch both sets in parallel ------------------------------------------
echo "Starting Set A G-phase..."
python3 -m src.runners.run_global_analysis \
  --data-dir "$OUT_DIR" \
  --languages ka yo fi eu ta id tr ko \
  --backend anthropic \
  --model-name "$MODEL" \
  --output-code global_set_A \
  > logs/g_phase_baseline_4_6_A.log 2>&1 &
PID_A=$!
echo "  PID $PID_A  (log: logs/g_phase_baseline_4_6_A.log)"

echo "Starting Set B G-phase..."
python3 -m src.runners.run_global_analysis \
  --data-dir "$OUT_DIR" \
  --languages zh he sa el en tl sw qu \
  --backend anthropic \
  --model-name "$MODEL" \
  --output-code global_set_B \
  > logs/g_phase_baseline_4_6_B.log 2>&1 &
PID_B=$!
echo "  PID $PID_B  (log: logs/g_phase_baseline_4_6_B.log)"

echo
echo "Both sets running. Watch with:"
echo "  tail -f logs/g_phase_baseline_4_6_A.log logs/g_phase_baseline_4_6_B.log"
echo

# ---- Wait + status ---------------------------------------------------------
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
  tail -20 logs/g_phase_baseline_4_6_A.log | sed 's/^/    /'
fi
if [ "$RC_B" -eq 0 ]; then
  echo "  Set B: ✓ complete"
else
  echo "  Set B: ✗ failed (exit $RC_B) — tail of log:"
  tail -20 logs/g_phase_baseline_4_6_B.log | sed 's/^/    /'
fi
echo "============================================"

if [ "$RC_A" -eq 0 ] && [ "$RC_B" -eq 0 ]; then
  echo
  echo "Comparison commands (run after this finishes):"
  echo
  echo "  # Pure within-model G-phase reproducibility (both runs at 4-6):"
  echo "  python3 -m src.runners.compare_g_phase \\"
  echo "    --baseline $OUT_DIR --rerun data_reproducibility --set all \\"
  echo "    --output data_reproducibility/g_phase_comparison_within_4_6.txt"
  echo
  echo "  # Pure model-change effect (same F-phase data, 4-5 vs 4-6 G):"
  echo "  python3 -m src.runners.compare_g_phase \\"
  echo "    --baseline data --rerun $OUT_DIR --set all \\"
  echo "    --output data_reproducibility/g_phase_model_change_4_5_vs_4_6.txt"
fi

exit $(( RC_A > RC_B ? RC_A : RC_B ))
