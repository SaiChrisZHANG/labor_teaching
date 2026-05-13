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

run_cmd python src/reproduce_hsieh_moretti_reduced.py
run_cmd python src/transfer_notowidigdo_incidence.py

test -s output/reproduced/housing_constraint_adjustment.csv
test -s output/reproduced/housing_constraint_summary.csv
test -s output/reproduced/reproduction_note.txt
test -s output/transfer/local_demand_incidence_transfer.csv
test -s output/transfer/incidence_summary_by_group.csv
test -s output/transfer/transfer_note.txt

