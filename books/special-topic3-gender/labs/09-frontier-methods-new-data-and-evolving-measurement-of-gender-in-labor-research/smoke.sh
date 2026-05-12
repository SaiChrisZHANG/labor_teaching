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

run_cmd python src/build_week9_synthetic_data.py

run_cmd python src/reproduce_application_gap.py \
  --input original/reduced/fluchtmann_application_gap_synthetic.csv \
  --outdir output/reproduced

run_cmd python src/diagnose_design_shortfalls.py \
  --input original/reduced/fluchtmann_application_gap_synthetic.csv \
  --outdir output/diagnosed

run_cmd python src/transfer_methods_frontier.py \
  --worker-firm transfer/data/card_worker_firm_synthetic.csv \
  --postings transfer/data/kuhn_shen_posting_policy_synthetic.csv \
  --outdir output/transfer
