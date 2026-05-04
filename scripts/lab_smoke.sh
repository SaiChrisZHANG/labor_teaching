#!/usr/bin/env bash
set -euo pipefail
source "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/_common.sh"
LAB_DIR="$(lab_dir)"
ensure_exists "$LAB_DIR"
SMOKE_SCRIPT="$LAB_DIR/smoke.sh"
ensure_exists "$SMOKE_SCRIPT"
cd "$LAB_DIR"
BOOK="$BOOK" WEEK="$WEEK" ENV_NAME="$ENV_NAME" ROOT_DIR="$ROOT_DIR" bash "$SMOKE_SCRIPT"
