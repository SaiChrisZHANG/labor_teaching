#!/usr/bin/env bash
set -euo pipefail

LAB_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$LAB_DIR"
export MPLCONFIGDIR="${LAB_DIR}/.mpl-cache"

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

run_cmd python src/reproduce_lundborg_ivf.py \
  --input original/reduced/lundborg_ivf_synthetic.csv \
  --outdir output/reproduced

run_cmd python src/transfer_child_penalty_event_study.py \
  --input transfer/data/kleven_child_penalty_synthetic.csv \
  --outdir output/transfer
