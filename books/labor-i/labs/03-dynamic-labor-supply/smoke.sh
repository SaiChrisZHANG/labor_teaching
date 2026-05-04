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

run_cmd python src/build_week3_synthetic_data.py

run_cmd python src/reproduce_fehr_goette_design.py \
  --input original/reduced/fehr_goette_shift_synthetic.csv \
  --outdir output/reproduced

run_cmd python src/transfer_dynamic_response.py \
  --input transfer/data/fehr_goette_persistence_synthetic.csv \
  --outdir output/transfer
