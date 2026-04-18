from flask import Flask, request
import os
import subprocess

app = Flask(__name__)

password = "SuperSecret123"

@app.route("/eval")
def eval_route():
    expr = request.args.get("expr", "")
    return str(eval(expr))

@app.route("/cmd")
def cmd_route():
    cmd = request.args.get("cmd", "")
    os.system(cmd)
    return "ok"

@app.route("/subprocess")
def subprocess_route():
    cmd = request.args.get("cmd", "")
    subprocess.run(cmd, shell=True)
    return "done"

if __name__ == "__main__":
    app.run(debug=True)