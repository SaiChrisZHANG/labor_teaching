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

run_cmd python src/platform_rules_lab.py

test -s original/reduced/platform_visibility_synthetic.csv
test -s original/reduced/platform_steering_synthetic.csv
test -s output/reproduced/visibility_information_summary.csv
test -s output/reproduced/reproduction_note.txt
test -s output/diagnosed/assignment_information_diagnostics.csv
test -s output/diagnosed/rule_incidence_diagnostics.csv
test -s output/diagnosed/worker_welfare_components.csv
test -s output/transfer/platform_rule_transfer.csv
