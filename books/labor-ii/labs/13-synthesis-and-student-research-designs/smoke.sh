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
  --anchor saezSchoeferSeim2019 \
  --comparison cengizDubeLindnerZipperer2019 \
  --outdir output/studio

test -f output/studio/anchor_menu.csv
test -f output/studio/selected_anchor_comparison.csv
test -f output/studio/research_design_memo.md
grep -q "## 7. Key equilibrium concern" output/studio/research_design_memo.md
grep -q "saezSchoeferSeim2019" output/studio/research_design_memo.md
