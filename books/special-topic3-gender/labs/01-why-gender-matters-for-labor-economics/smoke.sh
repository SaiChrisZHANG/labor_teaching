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

run_cmd python src/build_week1_synthetic_data.py

run_cmd python src/reproduce_gendered_laws.py \
  --input original/reduced/gendered_laws_workforce_synthetic.csv \
  --outdir output/reproduced

run_cmd python src/transfer_child_penalty.py \
  --input transfer/data/child_penalty_event_time_synthetic.csv \
  --outdir output/transfer
