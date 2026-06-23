#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VENV_DIR="$ROOT_DIR/.venv"

source "$VENV_DIR/bin/activate"

export DISPLAY=:0
export PORTALPI_VERSION="0.1.0"

python3 "$ROOT_DIR/app/server.py" &
SERVER_PID=$!

cleanup() {
  kill "$SERVER_PID" 2>/dev/null || true
}
trap cleanup EXIT

# Give Flask a moment to boot before Chromium starts.
sleep 2

openbox-session &
chromium-browser \
  --kiosk \
  --noerrdialogs \
  --disable-infobars \
  --autoplay-policy=no-user-gesture-required \
  http://127.0.0.1:8080
