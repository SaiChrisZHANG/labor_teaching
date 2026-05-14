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

run_cmd python src/disability_chronic_conditions_lab.py

test -s original/reduced/disability_chronic_conditions_synthetic.csv
test -s output/reproduced/disability_onset_event_study.csv
test -s output/reproduced/reproduction_note.txt
test -s output/diagnosed/mechanism_diagnosis.csv
test -s output/transfer/disability_design_transfer.csv
