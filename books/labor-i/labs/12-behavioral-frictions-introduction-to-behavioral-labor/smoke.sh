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

run_cmd python src/build_week12_synthetic_data.py

run_cmd python src/reproduce_abeler_huffman_raymond.py \
  --input original/reduced/abeler_huffman_raymond_incentive_complexity_synthetic.csv \
  --outdir output/reproduced

run_cmd python src/transfer_della_vigna_gift_exchange.py \
  --input transfer/data/della_vigna_gift_exchange_synthetic.csv \
  --outdir output/transfer
