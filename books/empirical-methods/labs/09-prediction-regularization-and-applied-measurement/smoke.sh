#!/usr/bin/env bash
set -euo pipefail

LAB_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$LAB_DIR"
export MPLCONFIGDIR="${TMPDIR:-/tmp}/empirical_methods_week9_matplotlib"
export XDG_CACHE_HOME="${TMPDIR:-/tmp}/empirical_methods_week9_cache"
export PYTHONDONTWRITEBYTECODE=1
mkdir -p "$MPLCONFIGDIR"
mkdir -p "$XDG_CACHE_HOME/fontconfig"

run_cmd() {
  if [[ "${CONDA_DEFAULT_ENV:-}" == "${ENV_NAME:-research}" ]]; then
    "$@"
    return
  fi

  if command -v conda >/dev/null 2>&1; then
    conda run -n "${ENV_NAME:-research}" --live-stream "$@"
    return
  fi

  "$@"
}

run_cmd python src/make_synthetic_data.py

run_cmd python src/reproduce_prediction_measurement.py \
  --input original/reduced/job_postings_synthetic.csv \
  --outdir output/reproduced

run_cmd python src/transfer_occupation_measurement.py \
  --train-input original/reduced/job_postings_synthetic.csv \
  --input transfer/data/occupation_titles_synthetic.csv \
  --outdir output/transfer \
  --reproduced-outdir output/reproduced
