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

run_cmd python src/build_week2_synthetic_data.py

run_cmd python src/reproduce_child_penalties.py \
  --input original/reduced/kleven_child_penalty_synthetic.csv \
  --outdir output/reproduced

run_cmd python src/transfer_fertility_design.py \
  --input transfer/data/lundborg_ivf_synthetic.csv \
  --outdir output/transfer
