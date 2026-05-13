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

run_cmd python src/technology_measurement_lab.py

test -s output/reproduced/exposure_by_occupation.csv
test -s output/reproduced/reproduction_note.txt
test -s output/diagnosed/measurement_contrast.csv
test -s output/transfer/firm_measurement_contrast.csv
