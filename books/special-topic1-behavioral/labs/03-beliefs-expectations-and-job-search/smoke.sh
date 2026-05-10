#!/usr/bin/env bash
set -euo pipefail

LAB_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$LAB_DIR"
export MPLCONFIGDIR="${TMPDIR:-/tmp}/behavioral-week3-mpl-cache"

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

run_cmd python src/build_week3_synthetic_data.py

run_cmd python src/reproduce_beliefs_duration.py \
  --input original/reduced/job_search_beliefs_synthetic.csv \
  --outdir output/reproduced

run_cmd python src/transfer_certification_search.py \
  --certification-input transfer/data/skill_certification_synthetic.csv \
  --wage-input transfer/data/wage_signal_applications_synthetic.csv \
  --outdir output/transfer
