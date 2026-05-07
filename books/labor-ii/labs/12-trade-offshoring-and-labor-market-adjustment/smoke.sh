#!/usr/bin/env bash
set -euo pipefail

LAB_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$LAB_DIR"

export MPLCONFIGDIR="${LAB_DIR}/output/.mplconfig"
export XDG_CACHE_HOME="${LAB_DIR}/output/.cache"
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

run_cmd python src/reproduce_trade_exposure.py \
  --outdir output/reproduced

run_cmd python src/transfer_trade_adjustment.py \
  --reproduced output/reproduced/cz_trade_panel.csv \
  --outdir output/transfer
