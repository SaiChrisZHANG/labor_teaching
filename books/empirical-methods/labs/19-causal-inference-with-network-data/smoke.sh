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

run_cmd python src/reproduce_peer_effects.py \
  --workers original/reduced/workplace_peers_synthetic.csv \
  --edges original/reduced/coworker_edges_synthetic.csv \
  --outdir output/reproduced

run_cmd python src/diagnose_network_causality.py \
  --workers original/reduced/workplace_peers_synthetic.csv \
  --edges original/reduced/coworker_edges_synthetic.csv \
  --outdir output/reproduced

run_cmd python src/transfer_referral_dyads.py \
  --referrals transfer/data/referral_dyads_synthetic.csv \
  --outdir output/transfer
