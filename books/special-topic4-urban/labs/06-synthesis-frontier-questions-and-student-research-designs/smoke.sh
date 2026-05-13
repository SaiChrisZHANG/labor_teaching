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

run_cmd python src/research_design_lab.py

test -s output/reproduced/design_architecture_examples.csv
test -s output/diagnosed/failure_mode_checklist.csv
test -s output/transfer/frontier_project_scores.csv
test -s output/transfer/one_page_research_memo_template.md
