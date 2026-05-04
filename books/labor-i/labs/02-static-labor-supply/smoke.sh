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

run_cmd python src/reproduce_saez_bunching.py \
  --input original/reduced/saez_bunching_synthetic.csv \
  --earnings-col earnings \
  --kink 30 \
  --bin-width 1 \
  --window 12 \
  --outdir output/reproduced

run_cmd python src/transfer_bunching_design.py \
  --input transfer/data/saez_transfer_synthetic.csv \
  --earnings-col earnings \
  --group-col group \
  --kink 30 \
  --bin-width 2 \
  --window 14 \
  --outdir output/transfer
