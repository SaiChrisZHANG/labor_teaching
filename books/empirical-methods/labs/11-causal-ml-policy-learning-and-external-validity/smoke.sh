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

run_cmd python src/reproduce_policy_learning.py \
  --input original/reduced/job_training_policy_synthetic.csv \
  --outdir output/reproduced

run_cmd python src/transfer_transportability.py \
  --source-input original/reduced/job_training_policy_synthetic.csv \
  --target-input transfer/data/job_training_target_synthetic.csv \
  --outdir output/transfer
