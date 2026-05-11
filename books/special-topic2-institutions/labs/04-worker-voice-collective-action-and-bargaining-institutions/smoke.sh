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

run_cmd python src/build_week4_synthetic_data.py

run_cmd python src/reproduce_union_close_elections.py \
  --elections original/reduced/close_elections_synthetic.csv \
  --workers original/reduced/matched_worker_establishment_synthetic.csv \
  --outdir output/reproduced

run_cmd python src/transfer_voice_spillover_classifier.py \
  --input transfer/data/collective_institution_designs_synthetic.csv \
  --outdir output/transfer
