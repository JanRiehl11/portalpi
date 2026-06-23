#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VENV_DIR="$ROOT_DIR/.venv"

sudo apt update
sudo apt install -y \
  python3 \
  python3-venv \
  python3-pip \
  xserver-xorg \
  xinit \
  openbox \
  chromium-browser \
  network-manager

python3 -m venv "$VENV_DIR"
source "$VENV_DIR/bin/activate"
pip install --upgrade pip
pip install -r "$ROOT_DIR/requirements.txt"

echo "PortalPi dependencies installed."
echo "Next: sudo cp systemd/portalpi.service /etc/systemd/system/portalpi.service && sudo systemctl enable --now portalpi.service"
