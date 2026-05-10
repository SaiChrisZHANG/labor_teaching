#!/usr/bin/env bash
set -euo pipefail

LAB_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$LAB_DIR"
export MPLCONFIGDIR="${TMPDIR:-/tmp}/behavioral-week9-mpl-cache"
export XDG_CACHE_HOME="${TMPDIR:-/tmp}/behavioral-week9-xdg-cache"
mkdir -p "$MPLCONFIGDIR" "$XDG_CACHE_HOME"

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

run_cmd python src/build_week9_synthetic_data.py

run_cmd python src/reproduce_takeup_design.py \
  --worker-input original/reduced/benefit_takeup_synthetic.csv \
  --duration-input original/reduced/benefit_takeup_duration_synthetic.csv \
  --outdir output/reproduced

run_cmd python src/transfer_policy_diagnostics.py \
  --eitc-input transfer/data/eitc_local_knowledge_synthetic.csv \
  --default-input transfer/data/retirement_default_welfare_synthetic.csv \
  --outdir output/transfer
