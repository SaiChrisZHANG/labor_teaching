#!/usr/bin/env bash
set -euo pipefail
source "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/_common.sh"
BOOK_DIR="$(book_dir)"
ensure_exists "$BOOK_DIR"
cd "$BOOK_DIR"
run_in_env 0 jupyter book clean --templates --cache -y
