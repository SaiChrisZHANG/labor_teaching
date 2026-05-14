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

run_cmd python src/mental_health_productivity_lab.py

test -s original/reduced/mental_health_workplace_synthetic.csv
test -s output/reproduced/mental_health_productivity_profile.csv
test -s output/reproduced/reproduction_note.txt
test -s output/diagnosed/mental_health_mechanism_diagnosis.csv
test -s output/transfer/mental_health_design_transfer.csv
