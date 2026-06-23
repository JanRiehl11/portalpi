from __future__ import annotations

import subprocess
from dataclasses import dataclass


@dataclass
class PowerResult:
    ok: bool
    message: str


def _run(action: list[str]) -> PowerResult:
    try:
        subprocess.Popen(action)
        return PowerResult(ok=True, message="Command sent")
    except Exception as exc:  # pragma: no cover
        return PowerResult(ok=False, message=str(exc))


def shutdown() -> PowerResult:
    return _run(["sudo", "shutdown", "now"])


def reboot() -> PowerResult:
    return _run(["sudo", "reboot"])
