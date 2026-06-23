from __future__ import annotations

import os
import platform
import shutil
import socket
import subprocess
from typing import Any


def _run(command: list[str]) -> str:
    try:
        return subprocess.check_output(command, text=True, stderr=subprocess.DEVNULL).strip()
    except Exception:
        return ""


def _wifi_name() -> str:
    ssid = _run(["nmcli", "-t", "-f", "active,ssid", "dev", "wifi"])
    for line in ssid.splitlines():
        if line.startswith("yes:"):
            return line.split(":", 1)[1] or "Connected"
    return "Offline"


def _cpu_temp_c() -> float | None:
    thermal_path = "/sys/class/thermal/thermal_zone0/temp"
    try:
        with open(thermal_path, "r", encoding="utf-8") as handle:
            return round(int(handle.read().strip()) / 1000, 1)
    except Exception:
        return None


def _disk_usage() -> dict[str, Any]:
    total, used, free = shutil.disk_usage("/")
    gb = 1024 ** 3
    return {
        "total_gb": round(total / gb, 1),
        "used_gb": round(used / gb, 1),
        "free_gb": round(free / gb, 1),
    }


def get_system_snapshot() -> dict[str, Any]:
    temp = _cpu_temp_c()
    return {
        "device_name": socket.gethostname(),
        "platform": platform.platform(),
        "ip_address": _run(["hostname", "-I"]).split(" ")[0] if _run(["hostname", "-I"]) else "unknown",
        "wifi": _wifi_name(),
        "cpu_temp_c": temp,
        "battery_percent": None,
        "disk": _disk_usage(),
        "chiaki_installed": bool(shutil.which("chiaki") or shutil.which("chiaki-ng")),
        "portalpi_version": os.getenv("PORTALPI_VERSION", "0.1.0"),
    }
