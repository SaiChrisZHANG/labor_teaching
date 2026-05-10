#!/usr/bin/env bash
set -euo pipefail

LAB_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$LAB_DIR"
export MPLCONFIGDIR="${TMPDIR:-/tmp}/behavioral-week8-equilibrium-mpl-cache"
export XDG_CACHE_HOME="${TMPDIR:-/tmp}/behavioral-week8-equilibrium-xdg-cache"
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

run_cmd python src/build_week8_synthetic_data.py

run_cmd python src/reproduce_default_design.py \
  --input original/reduced/retirement_defaults_synthetic.csv \
  --outdir output/reproduced

run_cmd python src/transfer_beliefs_and_markets.py \
  --belief-input transfer/data/outside_option_beliefs_synthetic.csv \
  --market-input transfer/data/plan_disclosure_market_synthetic.csv \
  --outdir output/transfer
