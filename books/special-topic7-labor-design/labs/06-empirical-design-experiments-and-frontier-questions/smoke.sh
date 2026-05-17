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

run_cmd python src/empirical_design_capstone_lab.py

test -s original/reduced/professional_entry_preferences_synthetic.csv
test -s original/reduced/design_evaluation_observations_synthetic.csv
test -s output/reproduced/matching_counterfactual_summary.csv
test -s output/reproduced/reproduction_note.txt
test -s output/diagnosed/mechanism_counterfactual_diagnostics.csv
test -s output/diagnosed/equilibrium_portability_diagnostics.csv
test -s output/transfer/frontier_research_designs.csv
