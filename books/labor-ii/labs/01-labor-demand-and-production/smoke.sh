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

run_cmd python src/reproduce_beaudry_city_industry.py \
  --input original/reduced/beaudry_city_industry_synthetic.csv \
  --outdir output/reproduced

run_cmd python src/transfer_static_labor_demand.py \
  --input transfer/data/static_labor_demand_scenarios.csv \
  --outdir output/transfer
