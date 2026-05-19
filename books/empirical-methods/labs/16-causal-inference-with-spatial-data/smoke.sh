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

run_cmd python src/reproduce_border_design.py \
  --counties original/reduced/border_counties_synthetic.csv \
  --links original/reduced/neighbor_links_synthetic.csv \
  --outdir output/reproduced

run_cmd python src/diagnose_spatial_design.py \
  --counties original/reduced/border_counties_synthetic.csv \
  --links original/reduced/neighbor_links_synthetic.csv \
  --outdir output/reproduced

run_cmd python src/transfer_shift_share_spatial.py \
  --counties transfer/data/shift_share_counties_synthetic.csv \
  --shares original/reduced/sector_shares_synthetic.csv \
  --shocks original/reduced/sector_shocks_synthetic.csv \
  --outdir output/transfer
