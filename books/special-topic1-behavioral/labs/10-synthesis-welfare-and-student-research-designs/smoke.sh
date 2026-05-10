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

run_cmd python src/research_design_studio.py \
  --anchor muellerSpinnewijnTopa2021 \
  --comparison bhargavaManoli2015 \
  --outdir output/studio

test -f output/studio/anchor_menu.csv
test -f output/studio/selected_anchor_diagnostic.csv
test -f output/studio/research_design_memo.md
grep -q "## 7. Welfare or policy interpretation" output/studio/research_design_memo.md
grep -q "muellerSpinnewijnTopa2021" output/studio/research_design_memo.md
