#!/usr/bin/env bash
set -euo pipefail
source "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/_common.sh"
"$ROOT_DIR/scripts/book_build_strict.sh"
"$ROOT_DIR/scripts/slides_build.sh"
"$ROOT_DIR/scripts/lab_smoke.sh"
