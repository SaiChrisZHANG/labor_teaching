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

run_cmd python src/contracts_incentives_lab.py

test -s original/reduced/performance_pay_synthetic.csv
test -s original/reduced/subjective_evaluation_synthetic.csv
test -s output/reproduced/performance_pay_summary.csv
test -s output/reproduced/reproduction_note.txt
test -s output/diagnosed/incentive_sorting_decomposition.csv
test -s output/diagnosed/hidden_object_diagnostics.csv
test -s output/diagnosed/subjective_evaluation_comparison.csv
test -s output/transfer/contract_design_transfer.csv
