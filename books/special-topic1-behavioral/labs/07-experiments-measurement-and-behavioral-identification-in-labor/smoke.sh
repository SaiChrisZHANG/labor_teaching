#!/usr/bin/env bash
set -euo pipefail

LAB_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$LAB_DIR"
export MPLCONFIGDIR="${TMPDIR:-/tmp}/behavioral-week7-mpl-cache"

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

run_cmd python src/build_week7_synthetic_data.py

run_cmd python src/reproduce_information_design.py \
  --worker-input original/reduced/job_search_information_synthetic.csv \
  --duration-input original/reduced/job_search_duration_panel_synthetic.csv \
  --outdir output/reproduced

run_cmd python src/transfer_method_bridge.py \
  --gift-input transfer/data/gift_exchange_method_synthetic.csv \
  --schedule-input transfer/data/schedule_bunching_synthetic.csv \
  --outdir output/transfer
