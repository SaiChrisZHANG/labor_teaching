#!/usr/bin/env bash
set -euo pipefail

LAB_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$LAB_DIR"
export MPLCONFIGDIR="${LAB_DIR}/.mpl-cache"

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

run_cmd python src/build_week1_synthetic_data.py

run_cmd python src/reproduce_royer_stehr_sydnor.py \
  --input original/reduced/royer_stehr_sydnor_worker_wellness_synthetic.csv \
  --outdir output/reproduced

run_cmd python src/transfer_altmann_job_search.py \
  --input transfer/data/altmann_job_search_synthetic.csv \
  --outdir output/transfer
