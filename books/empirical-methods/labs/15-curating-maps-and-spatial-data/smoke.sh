#!/usr/bin/env bash
set -euo pipefail

LAB_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$LAB_DIR"
export PYTHONDONTWRITEBYTECODE=1

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

run_cmd python src/make_synthetic_data.py

run_cmd python src/reproduce_commuting_zone_exposure.py \
  --tracts original/reduced/tract_sector_employment_synthetic.csv \
  --shocks original/reduced/sector_trade_shocks_synthetic.csv \
  --outdir output/reproduced

run_cmd python src/diagnose_spatial_choices.py \
  --tracts original/reduced/tract_sector_employment_synthetic.csv \
  --shocks original/reduced/sector_trade_shocks_synthetic.csv \
  --crosswalk original/reduced/boundary_crosswalk_synthetic.csv \
  --outdir output/reproduced

run_cmd python src/transfer_job_access.py \
  --residences transfer/data/residential_tracts_synthetic.csv \
  --centers transfer/data/workplace_centers_synthetic.csv \
  --outdir output/transfer
