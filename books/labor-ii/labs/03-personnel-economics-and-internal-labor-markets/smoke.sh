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

run_cmd python src/reproduce_friebel_team_incentives.py \
  --input original/reduced/friebel_team_incentives_synthetic.csv \
  --outdir output/reproduced

run_cmd python src/transfer_personnel_assignment.py \
  --input transfer/data/personnel_assignment_scenarios.csv \
  --outdir output/transfer
