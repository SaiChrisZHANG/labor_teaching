#!/usr/bin/env bash
set -euo pipefail

LAB_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$LAB_DIR"
export MPLCONFIGDIR="${TMPDIR:-/tmp}/behavioral-week2-mpl-cache"

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

run_cmd python src/build_week2_synthetic_data.py

run_cmd python src/reproduce_kaur_self_control.py \
  --input original/reduced/kaur_self_control_synthetic.csv \
  --outdir output/reproduced

run_cmd python src/transfer_work_linked_savings.py \
  --input transfer/data/work_linked_savings_synthetic.csv \
  --outdir output/transfer
