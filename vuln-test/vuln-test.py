"""Intentionally vulnerable Flask demo routes.

Purpose of this file:
- Give CodeQL realistic web-style data flow patterns to inspect.
- Show the difference between SAST alerts and direct pipeline failures.

Expected learning behavior:
- CodeQL may raise alerts for the vulnerable routes below.
- The workflow itself may still be GREEN because CodeQL uploads alerts instead
  of failing the job by default.
- If you want CodeQL findings to block merges, configure protection rules.
"""

from flask import Flask, request
import os
import subprocess

app = Flask(__name__)


@app.route("/eval")
def eval_route():
    """Unsafe route: user-controlled data flows into eval."""
    expr = request.args.get("expr", "")
    return str(eval(expr))


@app.route("/cmd")
def cmd_route():
    """Unsafe route: user-controlled data flows into os.system."""
    cmd = request.args.get("cmd", "")
    os.system(cmd)
    return "ok"


@app.route("/subprocess")
def subprocess_route():
    """Unsafe route: user-controlled data flows into shell=True."""
    cmd = request.args.get("cmd", "")
    subprocess.run(cmd, shell=True, check=False)
    return "done"


if __name__ == "__main__":
    app.run(debug=True)
