# PortalPi

PortalPi is a lightweight PS Portal-inspired launcher that runs **on top of Raspberry Pi OS Lite** for a Raspberry Pi 3 handheld build.

## v1 scope
- Boot screen
- Home screen
- Quick settings overlay
- Remote Play / Chiaki launch flow
- Lightweight backend for Wi-Fi/system status and power actions
- Kiosk/autostart setup for Raspberry Pi OS Lite

## Stack
- **Backend:** Python 3 + Flask
- **Frontend:** Vanilla HTML/CSS/JS (kept light for Pi 3)
- **Deployment target:** Raspberry Pi OS Lite + X11/Openbox + Chromium kiosk

## Project structure
```text
portalpi/
├─ app/
│  ├─ server.py
│  ├─ services/
│  │  ├─ chiaki.py
│  │  ├─ power.py
│  │  └─ system_info.py
│  ├─ static/
│  │  ├─ app.js
│  │  └─ styles.css
│  └─ templates/
│     └─ index.html
├─ scripts/
│  ├─ install.sh
│  └─ start-portalpi.sh
├─ systemd/
│  └─ portalpi.service
├─ requirements.txt
└─ .gitignore
```

## Quick start on Raspberry Pi OS Lite
```bash
sudo apt update
sudo apt install -y python3 python3-venv python3-pip xserver-xorg xinit openbox chromium-browser network-manager

git clone https://github.com/JanRiehl11/portalpi.git
cd portalpi
chmod +x scripts/install.sh scripts/start-portalpi.sh
./scripts/install.sh
```

Then enable the service:
```bash
sudo cp systemd/portalpi.service /etc/systemd/system/portalpi.service
sudo systemctl daemon-reload
sudo systemctl enable portalpi.service
sudo systemctl start portalpi.service
```

## Notes
- By default the **Remote Play** button launches `chiaki` if installed.
- You can change the launch command with the `PORTALPI_CHAIAKI_CMD` environment variable.
- Battery data is mocked unless you wire in a battery monitor / UPS HAT integration.
