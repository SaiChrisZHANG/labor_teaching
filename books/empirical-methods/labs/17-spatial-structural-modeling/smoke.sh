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

run_cmd python src/reproduce_spatial_flows.py \
  --locations original/reduced/locations_synthetic.csv \
  --flows original/reduced/bilateral_commuting_synthetic.csv \
  --outdir output/reproduced

run_cmd python src/diagnose_structural_fit.py \
  --locations original/reduced/locations_synthetic.csv \
  --flows original/reduced/bilateral_commuting_synthetic.csv \
  --outdir output/reproduced

run_cmd python src/transfer_dynamic_spatial.py \
  --locations original/reduced/locations_synthetic.csv \
  --flows original/reduced/bilateral_commuting_synthetic.csv \
  --policy transfer/data/dynamic_policy_synthetic.csv \
  --outdir output/transfer
