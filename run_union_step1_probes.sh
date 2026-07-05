#!/usr/bin/env bash
#
# Union pipeline — Step 1: generate K=3 P-phase probes per language.
#
# For each of the 16 languages:
#   - If the language already has K>=3 probes in data_saturation/, copy the
#     first 3 into data_union/<lang>/probes/run_<k>/  (no API cost)
#   - Otherwise, run K=3 fresh P-phase passes with --no-formatting and
#     write to data_union/<lang>/probes/run_<k>/
#
# Reuses run_p_phase_saturation infrastructure. Cost: ~36 fresh P-phase
# pipelines (~324 LLM calls on Sonnet 4-6) for the 12 langs not covered
# by data_saturation/.
#
# Overrides:
#   CLCA_UNION_MODEL=claude-sonnet-4-6        (default)
#   CLCA_UNION_K=3                            (default)
#   CLCA_UNION_OUT=data_union                 (default)
#   CLCA_UNION_LANGS="ka yo fi eu ta id tr ko zh he sa el en tl sw qu"  (default: all 16)

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
K="${CLCA_UNION_K:-3}"
OUT="${CLCA_UNION_OUT:-data_union}"
LANGS="${CLCA_UNION_LANGS:-ka yo fi eu ta id tr ko zh he sa el en tl sw qu}"

mkdir -p logs "$OUT"

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
echo "  Union pipeline — Step 1: K=$K P-phase probes"
echo "  Model: $MODEL"
echo "  Out:   $OUT/<lang>/probes/run_<k>/"
echo "============================================"
echo

# ---- Seed from data_saturation/ where possible ------------------------------
seed_from_saturation() {
  local code="$1"
  local saturation_dir="data_saturation/$code"
  [ -d "$saturation_dir" ] || return 1
  local probes_dir="$OUT/$code/probes"
  mkdir -p "$probes_dir"
  local k
  for k in $(seq 1 "$K"); do
    local src="$saturation_dir/run_$k"
    local dst="$probes_dir/run_$k"
    if [ -d "$src" ] && [ ! -d "$dst" ]; then
      cp -R "$src" "$dst"
      echo "  $code/run_$k: seeded from data_saturation/"
    elif [ -d "$dst" ]; then
      echo "  $code/run_$k: already present, skipping"
    else
      return 1
    fi
  done
  return 0
}

# ---- Fresh P-phase run for one (lang, k) ------------------------------------
PID_KEYS=()
PID_VALS=()

launch_fresh() {
  local code="$1" k="$2"
  local info name script pid out_root
  info="$(lookup_lang "$code")"
  if [ -z "$info" ]; then
    echo "  WARN: unknown language code '$code' — skipping"
    return
  fi
  name="${info%%|*}"
  script="${info##*|}"
  # Use a per-(lang,k) data-dir wrapper. We post-process to move output to the
  # final ``probes/run_<k>/`` layout once the run finishes.
  out_root="$OUT/_staging/k${k}"
  mkdir -p "$out_root"
  python3 -m src.runners.run_language \
    --data-dir "$out_root" \
    --language-name "$name" \
    --language-code "$code" \
    --script "$script" \
    --backend anthropic \
    --model-name "$MODEL" \
    --no-formatting \
    > "logs/union_p_${code}_k${k}.log" 2>&1 &
  pid=$!
  PID_KEYS+=("${code}_k${k}")
  PID_VALS+=("$pid")
  echo "  $code k=$k → PID $pid (log: logs/union_p_${code}_k${k}.log)"
}

# ---- Dispatch -------------------------------------------------------------
needs_fresh=()
for code in $LANGS; do
  if seed_from_saturation "$code"; then
    continue
  fi
  needs_fresh+=("$code")
done

if [ "${#needs_fresh[@]}" -eq 0 ]; then
  echo
  echo "All requested languages have K=$K probes seeded from data_saturation/."
  echo "Nothing to run."
  exit 0
fi

echo
echo "Fresh runs needed: ${needs_fresh[*]}"
echo "Total fresh pipelines to launch: $(( ${#needs_fresh[@]} * K ))"
echo

for code in "${needs_fresh[@]}"; do
  for k in $(seq 1 "$K"); do
    launch_fresh "$code" "$k"
  done
done

echo
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
    echo "  $key: ✗ (exit $rc) — tail logs/union_p_${key}.log"
    worst=$rc
  fi
  i=$((i + 1))
done

# ---- Reorganize staged output to final probes/run_<k>/ layout --------------
echo
echo "Reorganizing fresh probes to $OUT/<lang>/probes/run_<k>/ ..."
for code in "${needs_fresh[@]}"; do
  for k in $(seq 1 "$K"); do
    src_dir="$OUT/_staging/k${k}/$code"
    dst_dir="$OUT/$code/probes/run_$k"
    if [ -d "$src_dir" ]; then
      mkdir -p "$OUT/$code/probes"
      rm -rf "$dst_dir"
      mv "$src_dir" "$dst_dir"
    fi
  done
done
rm -rf "$OUT/_staging"

echo
echo "============================================"
if [ "$worst" -eq 0 ]; then
  echo "  Step 1 complete — K=$K probes ready for all 16 languages"
  echo "  Next:  ./run_union_step2_merge.sh"
else
  echo "  Step 1 finished with errors (worst exit $worst)"
fi
echo "============================================"

exit "$worst"
