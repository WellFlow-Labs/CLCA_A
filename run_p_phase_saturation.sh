#!/usr/bin/env bash
#
# P-phase saturation experiment.
#
# Runs the P-phase pipeline K=5 times for each of 4 representative languages,
# with --no-formatting so each run is a pure P-phase probe (no F-phase
# tabulation, no G-phase synthesis). The cumulative-union growth across the K
# runs gives the saturation curve referenced in Paper I §4.2 (two-probes-of-
# the-elephant framing).
#
# Output layout:
#   data_saturation/<lang>/run_<k>/
#     P1_vocab.content.txt
#     P5_oppositions.content.txt
#     P6_naturalness.content.txt
#     ... etc.
#
# Analysis: src/runners/compute_saturation.py
#
# Cost estimate: 4 langs × 5 runs × ~9 P-phase prompts ≈ 180 LLM calls.
#
# Override the model / K / language set with environment variables:
#   CLCA_PF_MODEL=claude-sonnet-4-6  (default)
#   CLCA_SATURATION_K=5              (default)
#   CLCA_SATURATION_LANGS="en zh ka qu"  (default — representative subset)

set -euo pipefail
cd "$(dirname "$0")"

# ---- Activate project venv if present ----------------------------------------
if [ -f .venv/bin/activate ]; then
  # shellcheck disable=SC1091
  . .venv/bin/activate
fi

# ---- API key indirection -----------------------------------------------------
if [ -z "${ANTHROPIC_API_KEY:-}" ] && [ -n "${AOML_ANTHROPIC_API_KEY:-}" ]; then
  export ANTHROPIC_API_KEY="$AOML_ANTHROPIC_API_KEY"
fi
: "${ANTHROPIC_API_KEY:?Set ANTHROPIC_API_KEY or AOML_ANTHROPIC_API_KEY before running.}"

MODEL="${CLCA_PF_MODEL:-claude-sonnet-4-6}"
K="${CLCA_SATURATION_K:-5}"
LANGS="${CLCA_SATURATION_LANGS:-en zh ka qu}"
ROOT="data_saturation"

mkdir -p logs "$ROOT"

# Map language codes to (name, script). Uses a case statement instead of
# associative arrays so this script runs on the bash 3.2 that ships with
# macOS — `declare -A` is bash 4+.
lookup_lang() {
  # Echoes "Name|Script" for a known code; empty string for unknown.
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
echo "  CLCA P-phase saturation experiment"
echo "  Model:    $MODEL"
echo "  K (runs): $K"
echo "  Langs:    $LANGS"
echo "  Root:     $ROOT/"
echo "  Logs in:  logs/sat_*.log"
echo "============================================"
echo

# ---- Launch helper (single P-phase run for one language, one K-index) -------
# Output goes to ROOT/<lang>/run_<k>/ — we create a per-(lang,k) data-dir
# wrapper that the runner treats as its own per-language root, then move
# the results into the final layout below.

# Parallel arrays for tracking PIDs (bash 3.2 compatible — no `declare -A`).
PID_KEYS=()
PID_VALS=()

launch() {
  local code="$1" k="$2"
  local info name script out_root pid
  info="$(lookup_lang "$code")"
  name="${info%%|*}"
  script="${info##*|}"
  out_root="$ROOT/_runs/k${k}"
  mkdir -p "$out_root"
  python3 -m src.runners.run_language \
    --data-dir "$out_root" \
    --language-name "$name" \
    --language-code "$code" \
    --script "$script" \
    --backend anthropic \
    --model-name "$MODEL" \
    --no-formatting \
    > "logs/sat_${code}_k${k}.log" 2>&1 &
  pid=$!
  PID_KEYS+=("${code}_k${k}")
  PID_VALS+=("$pid")
  echo "  $code k=$k → PID $pid (log: logs/sat_${code}_k${k}.log)"
}

# Launch all (lang, k) pairs in parallel. TPM throttling in settings.toml
# bounds concurrency at the API layer.
for code in $LANGS; do
  info="$(lookup_lang "$code")"
  if [ -z "$info" ]; then
    echo "  WARN: unknown language code '$code' — skipping"
    continue
  fi
  for k in $(seq 1 "$K"); do
    launch "$code" "$k"
  done
done

echo
echo "All P-phase probes running. Tail with:  tail -f logs/sat_<code>_k<k>.log"
echo "Waiting for completion..."
echo

# ---- Wait + status ----------------------------------------------------------
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
    echo "  $key: ✗ (exit $rc) — tail logs/sat_${key}.log"
    worst=$rc
  fi
  i=$((i + 1))
done

# ---- Reorganize per-lang/per-run layout -------------------------------------
# Move from ROOT/_runs/k<k>/<code>/ → ROOT/<code>/run_<k>/ so analysis is by
# language with K subdirectories beneath it.
echo
echo "Reorganizing output layout to $ROOT/<lang>/run_<k>/ ..."
for code in $LANGS; do
  for k in $(seq 1 "$K"); do
    src_dir="$ROOT/_runs/k${k}/$code"
    dst_dir="$ROOT/$code/run_$k"
    if [ -d "$src_dir" ]; then
      mkdir -p "$ROOT/$code"
      rm -rf "$dst_dir"
      mv "$src_dir" "$dst_dir"
    fi
  done
done
rm -rf "$ROOT/_runs"

echo
echo "============================================"
if [ "$worst" -eq 0 ]; then
  echo "  P-phase saturation experiment complete"
  echo
  echo "  Compute the saturation curve with:"
  echo "    python3 -m src.runners.compute_saturation \\"
  echo "      --root $ROOT --langs $LANGS --output $ROOT/saturation_curve.md"
else
  echo "  P-phase saturation finished with errors (worst exit $worst)"
fi
echo "============================================"

exit "$worst"
