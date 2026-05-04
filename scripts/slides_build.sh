#!/usr/bin/env bash
set -euo pipefail
source "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/_common.sh"
SLIDE_FILE="$(slide_file)"
ensure_exists "$SLIDE_FILE"
BOOK_DIR="$(book_dir)"
RELATIVE_SLIDE_PATH="slides/$(week_dir)/$WEEK.tex"
cd "$BOOK_DIR"
run_in_env 0 latexmk -cd -pdf -interaction=nonstopmode "$RELATIVE_SLIDE_PATH"
