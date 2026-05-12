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

run_cmd python src/build_project_idea_bank.py

run_cmd python src/reproduce_design_table.py \
  --input original/reduced/week10_candidate_project_ideas.csv \
  --outdir output/reproduced

run_cmd python src/diagnose_project_ideas.py \
  --input original/reduced/week10_candidate_project_ideas.csv \
  --outdir output/diagnosed

run_cmd python src/design_research_memo.py \
  --ideas original/reduced/week10_candidate_project_ideas.csv \
  --scores output/diagnosed/project_scores.csv \
  --outdir output/design
