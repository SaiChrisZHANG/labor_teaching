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

run_cmd python src/build_week3_synthetic_data.py

run_cmd python src/reproduce_role_models.py \
  --input original/reduced/porter_serra_role_models_synthetic.csv \
  --outdir output/reproduced

run_cmd python src/transfer_competitiveness.py \
  --input transfer/data/buser_competitiveness_synthetic.csv \
  --outdir output/transfer
