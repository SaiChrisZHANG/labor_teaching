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

run_cmd python src/reproduce_llm_workflow.py \
  --input original/reduced/labor_mismatch_documents_synthetic.csv \
  --outdir output/reproduced

run_cmd python src/transfer_llm_workflow.py \
  --source-input original/reduced/labor_mismatch_documents_synthetic.csv \
  --input transfer/data/workforce_case_notes_synthetic.csv \
  --outdir output/transfer
