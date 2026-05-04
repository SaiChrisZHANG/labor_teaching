#!/usr/bin/env bash
set -euo pipefail

LAB_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$LAB_DIR"
export MPLCONFIGDIR="${LAB_DIR}/.mpl-cache"

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

run_cmd python src/build_week13_research_studio_packet.py

run_cmd python src/reproduce_week13_anchor_map.py \
  --input original/reduced/week13_anchor_papers.csv \
  --outdir output/reproduced

run_cmd python src/propose_week13_extension_memo.py \
  --input original/reduced/week13_anchor_papers.csv \
  --template transfer/templates/research-memo-template.md \
  --anchor card1999 \
  --outdir output/proposed

