#!/usr/bin/env bash
set -euo pipefail

LAB_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$LAB_DIR"
export PYTHONDONTWRITEBYTECODE=1

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

run_cmd python src/reproduce_network_formation.py \
  --nodes original/reduced/workers_synthetic.csv \
  --dyads original/reduced/dyad_opportunities_synthetic.csv \
  --edges original/reduced/network_edges_synthetic.csv \
  --outdir output/reproduced

run_cmd python src/diagnose_structural_network.py \
  --nodes original/reduced/workers_synthetic.csv \
  --dyads original/reduced/dyad_opportunities_synthetic.csv \
  --edges original/reduced/network_edges_synthetic.csv \
  --outdir output/reproduced

run_cmd python src/transfer_referral_search.py \
  --referrals transfer/data/referral_search_synthetic.csv \
  --outdir output/transfer
