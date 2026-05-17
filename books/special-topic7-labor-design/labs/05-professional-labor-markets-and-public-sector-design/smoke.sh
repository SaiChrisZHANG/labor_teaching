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

run_cmd python src/professional_public_design_lab.py

test -s original/reduced/army_officer_preferences_synthetic.csv
test -s original/reduced/army_assignment_outcomes_synthetic.csv
test -s original/reduced/public_service_assignment_synthetic.csv
test -s output/reproduced/army_assignment_summary.csv
test -s output/reproduced/reproduction_note.txt
test -s output/diagnosed/design_diagnostics.csv
test -s output/diagnosed/ladders_training_mobility.csv
test -s output/diagnosed/public_sector_entry_exit_diagnostics.csv
test -s output/transfer/public_service_design_transfer.csv
