#!/usr/bin/env bash
set -euo pipefail

LAB_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$LAB_DIR"
export MPLCONFIGDIR="${TMPDIR:-/tmp}/behavioral-week4-mpl-cache"

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

run_cmd python src/reproduce_schedule_learning.py \
  --input original/reduced/schedule_learning_synthetic.csv \
  --outdir output/reproduced

run_cmd python src/transfer_policy_navigation.py \
  --policy-input transfer/data/policy_navigation_synthetic.csv \
  --workplace-input transfer/data/workplace_complexity_synthetic.csv \
  --outdir output/transfer
