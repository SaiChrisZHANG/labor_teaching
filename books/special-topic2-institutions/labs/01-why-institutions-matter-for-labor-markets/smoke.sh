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

run_cmd python src/build_week1_synthetic_data.py

run_cmd python src/reproduce_inherited_norms.py \
  --input original/reduced/inherited_norms_labor_synthetic.csv \
  --outdir output/reproduced

run_cmd python src/transfer_network_mobility.py \
  --input transfer/data/network_mobility_synthetic.csv \
  --outdir output/transfer
