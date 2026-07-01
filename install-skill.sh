#!/usr/bin/env bash
set -euo pipefail

SKILL_NAME="xq-cli-bid-generation"
VERSION="${XQ_SKILL_VERSION:-20260701}"
DEFAULT_BASE_URL="${XQ_SKILL_BASE_URL:-https://example.com/xique-agent-skills}"
ARCHIVE_URL="${XQ_SKILL_ARCHIVE_URL:-${DEFAULT_BASE_URL}/${SKILL_NAME}-${VERSION}.zip}"
INSTALLER_URL="${XQ_SKILL_INSTALLER_URL:-${DEFAULT_BASE_URL}/install_xq_cli_bid_generation.py}"
SHA256_EXPECTED="${XQ_SKILL_SHA256:-8b62515374a0234b0a9052649095ff44b6d44da6bebb2d9f1e4ea5ebc9015033}"
TARGET="${XQ_SKILL_TARGET:-}"
TOOL="${XQ_SKILL_TOOL:-auto}"

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

need python3
need curl

tmp_dir="$(mktemp -d "${TMPDIR:-/tmp}/xq-skill-install.XXXXXX")"
trap 'rm -rf "$tmp_dir"' EXIT

installer="$tmp_dir/install_xq_cli_bid_generation.py"
fetch "$INSTALLER_URL" "$installer"

args=(python3 "$installer" --archive "$ARCHIVE_URL" --sha256 "$SHA256_EXPECTED" --force)
if [[ -n "$TARGET" ]]; then
  args+=(--target "$TARGET")
else
  args+=(--tool "$TOOL")
fi

"${args[@]}"

echo
echo "Skill install finished."
