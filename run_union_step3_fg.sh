#!/usr/bin/env bash
#
# Union pipeline — Step 3: F-phase (on merged P-phase) + G-phase.
#
# For each language, runs ``run_language.py --resume`` against
# data_union/<lang>/. With merged P-phase outputs already present, the
# runner skips all P-phase prompts and runs only I-phase and F-phase
# against the merged inputs.
#
# Then runs the G-phase global analysis for Set A (8 langs) and Set B
# (8 langs) in parallel, writing to data_union/global_set_{A,B}/.
#
# Cost: 16 langs × ~6 F-phase prompts + 2 sets × ~10 G-phase prompts ≈
#       ~120 calls on Sonnet 4-6 (G-phase uses Sonnet 4-6 because the
#       1M context window is needed for cross-language synthesis).
#
# Overrides:
#   CLCA_UNION_F_MODEL=claude-sonnet-4-6   (default)
#   CLCA_UNION_G_MODEL=claude-sonnet-4-6   (default)
#   CLCA_UNION_OUT=data_union              (default)

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

F_MODEL="${CLCA_UNION_F_MODEL:-claude-sonnet-4-6}"
G_MODEL="${CLCA_UNION_G_MODEL:-claude-sonnet-4-6}"
OUT="${CLCA_UNION_OUT:-data_union}"

SET_A="ka yo fi eu ta id tr ko"
SET_B="zh he sa el en tl sw qu"

# CLCA_UNION_SETS selects which sets to F+G-process: "A", "B", or "A B"
# (default). Useful when running set-by-set (Set A first, inspect, then Set B).
SETS_TO_RUN="${CLCA_UNION_SETS:-A B}"

# Build the F-phase language list from the selected sets.
F_LANGS=""
case " $SETS_TO_RUN " in
  *" A "*) F_LANGS="$F_LANGS $SET_A" ;;
esac
case " $SETS_TO_RUN " in
  *" B "*) F_LANGS="$F_LANGS $SET_B" ;;
esac
# Strip leading whitespace.
F_LANGS="${F_LANGS# }"

mkdir -p logs

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
echo "  Union pipeline — Step 3a: F-phase on merged P"
echo "  F model: $F_MODEL"
echo "  Sets:    $SETS_TO_RUN"
echo "  Out:     $OUT/<lang>/F*.format.txt"
echo "============================================"
echo

# ---- F-phase: launch all 16 in parallel -----------------------------------
PID_KEYS=()
PID_VALS=()
launch_f() {
  local code="$1"
  local info name script pid
  info="$(lookup_lang "$code")"
  name="${info%%|*}"
  script="${info##*|}"
  python3 -m src.runners.run_language \
    --data-dir "$OUT" \
    --language-name "$name" \
    --language-code "$code" \
    --script "$script" \
    --backend anthropic \
    --model-name "$F_MODEL" \
    --resume \
    > "logs/union_f_${code}.log" 2>&1 &
  pid=$!
  PID_KEYS+=("$code")
  PID_VALS+=("$pid")
  echo "  $code → PID $pid (log: logs/union_f_${code}.log)"
}

for code in $F_LANGS; do
  launch_f "$code"
done

echo
echo "Waiting for F-phase completion..."
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
    echo "  $key: ✗ (exit $rc) — tail logs/union_f_${key}.log"
    worst=$rc
  fi
  i=$((i + 1))
done

if [ "$worst" -ne 0 ]; then
  echo
  echo "F-phase had errors — not proceeding to G-phase. Fix and re-run."
  exit "$worst"
fi

# ---- G-phase: Set A and Set B in parallel ---------------------------------
echo
echo "============================================"
echo "  Step 3b: G-phase global synthesis"
echo "  G model: $G_MODEL"
echo "  Out:     $OUT/global_set_{A,B}/"
echo "============================================"
echo

G_PIDS=()
G_LABELS=()

case " $SETS_TO_RUN " in
  *" A "*)
    rm -rf "$OUT/global_set_A"
    python3 -m src.runners.run_global_analysis \
      --data-dir "$OUT" \
      --languages $SET_A \
      --backend anthropic \
      --model-name "$G_MODEL" \
      --output-code global_set_A \
      > logs/union_g_setA.log 2>&1 &
    PID_A=$!
    G_PIDS+=("$PID_A")
    G_LABELS+=("Set A")
    echo "  Set A → PID $PID_A (log: logs/union_g_setA.log)"
    ;;
esac

case " $SETS_TO_RUN " in
  *" B "*)
    rm -rf "$OUT/global_set_B"
    python3 -m src.runners.run_global_analysis \
      --data-dir "$OUT" \
      --languages $SET_B \
      --backend anthropic \
      --model-name "$G_MODEL" \
      --output-code global_set_B \
      > logs/union_g_setB.log 2>&1 &
    PID_B=$!
    G_PIDS+=("$PID_B")
    G_LABELS+=("Set B")
    echo "  Set B → PID $PID_B (log: logs/union_g_setB.log)"
    ;;
esac

echo
echo "Waiting for G-phase..."
g_worst=0
i=0
while [ $i -lt ${#G_PIDS[@]} ]; do
  rc=0
  wait "${G_PIDS[$i]}" || rc=$?
  if [ "$rc" -eq 0 ]; then
    echo "  ${G_LABELS[$i]}: ✓"
  else
    echo "  ${G_LABELS[$i]}: ✗ (exit $rc)"
    g_worst=$rc
  fi
  i=$((i + 1))
done

echo
echo "============================================"
if [ "$g_worst" -eq 0 ]; then
  echo "Union pipeline ($SETS_TO_RUN) complete. Results:"
  echo "  Merged P-phase: $OUT/<lang>/P*.content.txt"
  echo "  F-phase:        $OUT/<lang>/F*.format.txt"
  echo "  G-phase:        $OUT/global_set_{$(echo $SETS_TO_RUN | tr ' ' ',')}/"
fi

exit "$g_worst"
