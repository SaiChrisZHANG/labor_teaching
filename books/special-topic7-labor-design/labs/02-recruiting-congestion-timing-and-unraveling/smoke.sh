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

run_cmd python src/recruiting_congestion_lab.py

test -s original/reduced/recruiting_funnel_synthetic.csv
test -s original/reduced/timing_regime_synthetic.csv
test -s output/reproduced/vacancy_yield_summary.csv
test -s output/reproduced/reproduction_note.txt
test -s output/diagnosed/design_diagnostics.csv
test -s output/diagnosed/timing_regime_comparison.csv
test -s output/transfer/recruiting_design_transfer.csv
