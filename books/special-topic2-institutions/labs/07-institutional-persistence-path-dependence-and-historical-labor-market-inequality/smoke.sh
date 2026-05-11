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

run_cmd python src/build_week7_synthetic_data.py

run_cmd python src/reproduce_mita_boundary.py \
  --input original/reduced/mita_boundary_synthetic.csv \
  --outdir output/reproduced

run_cmd python src/diagnose_persistence_mechanism.py \
  --input original/reduced/persistence_claims_synthetic.csv \
  --outdir output/diagnostics

run_cmd python src/transfer_historical_design_classifier.py \
  --input transfer/data/historical_designs_synthetic.csv \
  --outdir output/transfer
