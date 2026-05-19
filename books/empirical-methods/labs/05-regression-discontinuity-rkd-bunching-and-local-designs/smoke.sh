#!/usr/bin/env bash
set -euo pipefail

LAB_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$LAB_DIR"
export MPLCONFIGDIR="${TMPDIR:-/tmp}/empirical_methods_week5_matplotlib"
export XDG_CACHE_HOME="${TMPDIR:-/tmp}/empirical_methods_week5_cache"
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

run_cmd python src/reproduce_rd_design.py \
  --input original/reduced/close_election_synthetic.csv \
  --outdir output/reproduced

run_cmd python src/transfer_bunching_design.py \
  --input transfer/data/tax_kink_bunching_synthetic.csv \
  --outdir output/transfer
