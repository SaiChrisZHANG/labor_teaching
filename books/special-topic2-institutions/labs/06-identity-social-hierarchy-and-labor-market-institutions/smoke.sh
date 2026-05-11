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

run_cmd python src/build_week6_synthetic_data.py

run_cmd python src/reproduce_resume_audit.py \
  --input original/reduced/resume_audit_synthetic.csv \
  --outdir output/reproduced

run_cmd python src/diagnose_hierarchy_barrier.py \
  --input original/reduced/hierarchy_barriers_synthetic.csv \
  --outdir output/diagnostics

run_cmd python src/transfer_hierarchy_design_classifier.py \
  --input transfer/data/hierarchy_designs_synthetic.csv \
  --outdir output/transfer
