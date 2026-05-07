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

run_cmd python src/reproduce_lachowska_wage_setting.py \
  --input original/reduced/lachowska_dual_jobholders_synthetic.csv \
  --outdir output/reproduced

run_cmd python src/transfer_wage_setting_regimes.py \
  --input transfer/data/wage_setting_regimes_synthetic.csv \
  --outdir output/transfer
