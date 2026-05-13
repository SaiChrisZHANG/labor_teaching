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

run_cmd python src/risk_feasible_set_lab.py

test -s output/reproduced/displacement_crime_event_study.csv
test -s output/diagnosed/risk_mechanism_diagnosis.csv
test -s output/transfer/environment_productivity_transfer.csv
test -s output/transfer/risk_adjusted_job_ranking.csv
