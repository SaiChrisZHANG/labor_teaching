#!/usr/bin/env bash
set -euo pipefail

LAB_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$LAB_DIR"
export PYTHONDONTWRITEBYTECODE=1

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

run_cmd python src/reproduce_computational_measurement.py \
  --input original/reduced/job_postings_remote_synthetic.csv \
  --outdir output/reproduced

run_cmd python src/transfer_multimodal_measurement.py \
  --source-input original/reduced/job_postings_remote_synthetic.csv \
  --input transfer/data/multimodal_work_records_synthetic.csv \
  --outdir output/transfer
