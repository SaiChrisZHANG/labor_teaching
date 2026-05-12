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

run_cmd python src/build_week10_synthetic_data.py

run_cmd python src/reproduce_tilcsik_audit.py \
  --input original/reduced/tilcsik_pride_prejudice_synthetic.csv \
  --outdir output/reproduced

run_cmd python src/diagnose_lgbtq_designs.py \
  --audit original/reduced/tilcsik_pride_prejudice_synthetic.csv \
  --trans transfer/data/granberg_andersson_ahmed_trans_hiring_synthetic.csv \
  --outdir output/diagnosed

run_cmd python src/transfer_law_benefits.py \
  --policy transfer/data/sansone_marriage_policy_synthetic.csv \
  --benefits transfer/data/carpenter_postolek_warman_benefits_synthetic.csv \
  --outdir output/transfer
