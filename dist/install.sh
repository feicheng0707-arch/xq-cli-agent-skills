#!/usr/bin/env bash
set -euo pipefail

XQ_CLI_PACKAGE="${XQ_CLI_PACKAGE:-@xqyz/xq-cli@0.1.2}"
SKILL_NAME="xq-cli-bid-generation"
VERSION="${XQ_SKILL_VERSION:-20260701}"
DEFAULT_BASE_URL="${XQ_SKILL_BASE_URL:-https://example.com/xique-agent-skills}"
INSTALL_SKILL_URL="${XQ_SKILL_INSTALL_SKILL_URL:-${DEFAULT_BASE_URL}/install-skill.sh}"

need() {
  command -v "$1" >/dev/null 2>&1 || {
    echo "Missing required command: $1" >&2
    exit 127
  }
}

fetch() {
  local src="$1"
  local dst="$2"
  if [[ -f "$src" ]]; then
    cp "$src" "$dst"
  else
    curl -fsSL "$src" -o "$dst"
  fi
}

resolve_xq_cli() {
  local found=""
  found="$(command -v xq-cli 2>/dev/null || true)"
  if [[ -n "$found" ]]; then
    echo "$found"
    return 0
  fi
  local prefix=""
  prefix="$(npm config get prefix 2>/dev/null || true)"
  if [[ -n "$prefix" && -x "$prefix/bin/xq-cli" ]]; then
    echo "$prefix/bin/xq-cli"
    return 0
  fi
  return 1
}

need npm
need python3
need curl

if [[ "${XQ_SKIP_XQ_CLI_INSTALL:-0}" != "1" ]]; then
  echo "Installing ${XQ_CLI_PACKAGE} ..."
  npm install -g "$XQ_CLI_PACKAGE"
else
  echo "Skipping xq-cli npm install because XQ_SKIP_XQ_CLI_INSTALL=1."
fi

XQ_CLI_BIN="$(resolve_xq_cli || true)"
if [[ -z "$XQ_CLI_BIN" ]]; then
  echo "xq-cli was installed but is not on PATH. Check npm global bin: \$(npm config get prefix)/bin" >&2
  exit 1
fi

echo "xq-cli resolved at: $XQ_CLI_BIN"
"$XQ_CLI_BIN" --help >/dev/null
echo "xq-cli help check passed."

tmp_dir="$(mktemp -d "${TMPDIR:-/tmp}/xq-quickstart.XXXXXX")"
trap 'rm -rf "$tmp_dir"' EXIT

install_skill="$tmp_dir/install-skill.sh"
fetch "$INSTALL_SKILL_URL" "$install_skill"
bash "$install_skill"

echo
echo "Quickstart install finished."
echo "Next login command:"
echo "  $XQ_CLI_BIN login --browser"
echo
echo "If login prints verification_uri, a verification URL, or user_code, send it to the user and wait for login to finish."
