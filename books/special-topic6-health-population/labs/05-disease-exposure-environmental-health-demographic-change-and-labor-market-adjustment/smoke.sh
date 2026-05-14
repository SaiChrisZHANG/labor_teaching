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

run_cmd python src/disease_environment_demography_lab.py

test -s original/reduced/disease_environment_demography_synthetic.csv
test -s output/reproduced/labor_market_incidence_profile.csv
test -s output/reproduced/reproduction_note.txt
test -s output/diagnosed/adjustment_mechanism_diagnosis.csv
test -s output/transfer/disease_environment_demography_design_transfer.csv
