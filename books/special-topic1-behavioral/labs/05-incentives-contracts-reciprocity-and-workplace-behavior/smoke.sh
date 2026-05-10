#!/usr/bin/env bash
set -euo pipefail

LAB_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$LAB_DIR"
export MPLCONFIGDIR="${TMPDIR:-/tmp}/behavioral-week5-mpl-cache"

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

run_cmd python src/build_week5_synthetic_data.py

run_cmd python src/reproduce_gift_exchange.py \
  --input original/reduced/gift_exchange_synthetic.csv \
  --outdir output/reproduced

run_cmd python src/transfer_monitoring_and_evaluation.py \
  --monitoring-input transfer/data/monitoring_synthetic.csv \
  --evaluation-input transfer/data/subjective_evaluation_synthetic.csv \
  --outdir output/transfer
