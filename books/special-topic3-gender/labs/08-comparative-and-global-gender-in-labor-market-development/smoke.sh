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

run_cmd python src/build_week8_synthetic_data.py

run_cmd python src/reproduce_comparative_family_policy.py \
  --input original/reduced/olivetti_petrongolo_family_policy_synthetic.csv \
  --outdir output/reproduced

run_cmd python src/transfer_norms_development.py \
  --input transfer/data/jayachandran_norms_transfer_synthetic.csv \
  --outdir output/transfer
