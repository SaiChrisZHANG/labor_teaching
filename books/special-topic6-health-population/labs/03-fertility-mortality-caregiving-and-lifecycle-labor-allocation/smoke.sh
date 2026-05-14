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

run_cmd python src/lifecycle_labor_allocation_lab.py

test -s original/reduced/lifecycle_family_shocks_synthetic.csv
test -s output/reproduced/family_health_shock_event_study.csv
test -s output/reproduced/reproduction_note.txt
test -s output/diagnosed/lifecycle_mechanism_diagnosis.csv
test -s output/transfer/lifecycle_design_transfer.csv
