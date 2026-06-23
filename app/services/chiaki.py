from __future__ import annotations

import os
import shlex
import subprocess
from dataclasses import dataclass


DEFAULT_CHIAKI_CMD = os.getenv("PORTALPI_CHAIAKI_CMD", "chiaki")


@dataclass
class LaunchResult:
    ok: bool
    message: str


def launch_chiaki() -> LaunchResult:
    """Launch Chiaki / Chiaki-NG from PortalPi.

    This keeps the first version intentionally simple: PortalPi starts the
    external Remote Play app and immediately returns success/failure.
    """
    try:
        cmd = shlex.split(DEFAULT_CHIAKI_CMD)
        subprocess.Popen(cmd)
        return LaunchResult(ok=True, message="Chiaki launched")
    except FileNotFoundError:
        return LaunchResult(
            ok=False,
            message="Chiaki command not found. Install chiaki or set PORTALPI_CHAIAKI_CMD.",
        )
    except Exception as exc:  # pragma: no cover - defensive path
        return LaunchResult(ok=False, message=f"Failed to launch Chiaki: {exc}")
