#!/usr/bin/env bash
set -euo pipefail

LAB_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$LAB_DIR"
export MPLCONFIGDIR="${TMPDIR:-/tmp}/empirical_methods_week10_matplotlib"
export XDG_CACHE_HOME="${TMPDIR:-/tmp}/empirical_methods_week10_cache"
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

run_cmd python src/reproduce_dml_online_labor.py \
  --input original/reduced/online_labor_synthetic.csv \
  --outdir output/reproduced

run_cmd python src/transfer_heterogeneity.py \
  --input transfer/data/youth_program_synthetic.csv \
  --outdir output/transfer
