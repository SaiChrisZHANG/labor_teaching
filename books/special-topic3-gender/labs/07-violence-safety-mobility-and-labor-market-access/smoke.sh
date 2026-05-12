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

run_cmd python src/build_week7_synthetic_data.py

run_cmd python src/reproduce_workplace_violence.py \
  --input original/reduced/adams_prassl_huttunen_nix_zhang_workplace_violence_synthetic.csv \
  --outdir output/reproduced

run_cmd python src/transfer_harassment_sorting.py \
  --input transfer/data/folke_rickne_harassment_sorting_synthetic.csv \
  --outdir output/transfer
