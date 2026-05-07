#!/usr/bin/env bash
set -euo pipefail

LAB_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$LAB_DIR"

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

run_cmd python src/reproduce_hall_schulhofer_wohl.py \
  --input original/reduced/hall_schulhofer_wohl_synthetic.csv \
  --outdir output/reproduced

run_cmd python src/transfer_job_ladder_search.py \
  --input transfer/data/job_ladder_scenarios.csv \
  --outdir output/transfer
