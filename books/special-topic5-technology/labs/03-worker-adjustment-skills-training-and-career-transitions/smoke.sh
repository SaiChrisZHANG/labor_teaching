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

run_cmd python src/worker_adjustment_lab.py

test -s output/reproduced/worker_exposure_outcomes.csv
test -s output/reproduced/reproduction_note.txt
test -s output/diagnosed/adjustment_diagnosis.csv
test -s output/transfer/training_retirement_transfer.csv
test -s output/transfer/ai_training_transfer.csv
