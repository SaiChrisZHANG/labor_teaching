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

run_cmd python src/reproduce_composition_adjustment.py \
  --input original/reduced/composition_panel_synthetic.csv \
  --outdir output/reproduced

run_cmd python src/transfer_factbook.py \
  --input transfer/data/labor_micro_synthetic.csv \
  --date-col date \
  --status-col employment_status \
  --weight-col weight \
  --hours-col hours \
  --earnings-col weekly_earnings \
  --group-col group \
  --outdir output/transfer
