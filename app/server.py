from __future__ import annotations

from flask import Flask, jsonify, render_template

from services.chiaki import launch_chiaki
from services.power import reboot, shutdown
from services.system_info import get_system_snapshot

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.get("/api/status")
def status():
    return jsonify(get_system_snapshot())


@app.post("/api/launch/chiaki")
def launch_remote_play():
    result = launch_chiaki()
    return jsonify({"ok": result.ok, "message": result.message}), (200 if result.ok else 500)


@app.post("/api/power/reboot")
def reboot_device():
    result = reboot()
    return jsonify({"ok": result.ok, "message": result.message}), (200 if result.ok else 500)


@app.post("/api/power/shutdown")
def shutdown_device():
    result = shutdown()
    return jsonify({"ok": result.ok, "message": result.message}), (200 if result.ok else 500)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=False)
