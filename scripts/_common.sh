#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ENV_NAME="${ENV_NAME:-research}"
BOOK="${BOOK:-labor-i}"
WEEK="${WEEK:-01-labor-market-facts}"

book_dir() {
  printf '%s\n' "$ROOT_DIR/books/$BOOK"
}

lab_dir() {
  printf '%s\n' "$ROOT_DIR/books/$BOOK/labs/$WEEK"
}

week_dir() {
  if [[ "$WEEK" =~ ^0*([1-9][0-9]*)[-_] ]]; then
    printf 'week%s\n' "${BASH_REMATCH[1]}"
    return
  fi

  echo "WEEK must start with a numeric prefix like 01-... so slides can live under slides/weekN/." >&2
  exit 1
}

slide_file() {
  printf '%s\n' "$ROOT_DIR/books/$BOOK/slides/$(week_dir)/$WEEK.tex"
}

ensure_exists() {
  local path="$1"
  if [[ ! -e "$path" ]]; then
    echo "Missing required path: $path" >&2
    exit 1
  fi
}

run_in_env() {
  local stream="${1:-0}"
  shift

  if [[ "${CONDA_DEFAULT_ENV:-}" == "$ENV_NAME" ]]; then
    "$@"
    return
  fi

  if ! command -v conda >/dev/null 2>&1; then
    echo "Conda is not available; running command in the current shell instead." >&2
    "$@"
    return
  fi

  if [[ "$stream" == "1" ]]; then
    conda run -n "$ENV_NAME" --live-stream "$@"
  else
    conda run -n "$ENV_NAME" "$@"
  fi
}
