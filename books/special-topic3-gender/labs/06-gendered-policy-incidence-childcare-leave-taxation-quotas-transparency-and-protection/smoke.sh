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

run_cmd python src/build_week6_synthetic_data.py

run_cmd python src/reproduce_pay_transparency.py \
  --input original/reduced/blundell_uk_pay_transparency_synthetic.csv \
  --outdir output/reproduced

run_cmd python src/transfer_equal_pay.py \
  --input transfer/data/gentile_equal_pay_similar_work_synthetic.csv \
  --outdir output/transfer
