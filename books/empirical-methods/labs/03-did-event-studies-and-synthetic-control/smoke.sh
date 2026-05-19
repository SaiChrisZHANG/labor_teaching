#!/usr/bin/env bash
set -euo pipefail

LAB_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$LAB_DIR"
export MPLCONFIGDIR="${TMPDIR:-/tmp}/empirical_methods_week3_matplotlib"
export XDG_CACHE_HOME="${TMPDIR:-/tmp}/empirical_methods_week3_cache"
export PYTHONDONTWRITEBYTECODE=1
mkdir -p "$MPLCONFIGDIR"
mkdir -p "$XDG_CACHE_HOME/fontconfig"

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

run_cmd python src/make_synthetic_data.py

run_cmd python src/reproduce_did_event_study.py \
  --card-input original/reduced/card_krueger_synthetic.csv \
  --staggered-input original/reduced/staggered_minimum_wage_synthetic.csv \
  --outdir output/reproduced

run_cmd python src/transfer_synthetic_control.py \
  --input transfer/data/synthetic_control_city.csv \
  --outdir output/transfer
