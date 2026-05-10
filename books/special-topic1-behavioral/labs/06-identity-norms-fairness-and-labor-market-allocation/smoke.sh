#!/usr/bin/env bash
set -euo pipefail

LAB_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$LAB_DIR"
export MPLCONFIGDIR="${TMPDIR:-/tmp}/behavioral-week6-mpl-cache"

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

run_cmd python src/reproduce_peer_pressure.py \
  --input original/reduced/peer_pressure_synthetic.csv \
  --outdir output/reproduced

run_cmd python src/transfer_fairness_culture.py \
  --fairness-input transfer/data/pay_comparison_synthetic.csv \
  --culture-input transfer/data/culture_sorting_synthetic.csv \
  --manager-input transfer/data/manager_transmission_synthetic.csv \
  --outdir output/transfer
