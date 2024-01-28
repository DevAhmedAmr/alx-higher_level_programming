#!/usr/bin/python3
""" Web server
"""
from flask import Flask, request
from flask import jsonify

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """Root"""
    return "Index"


@app.route("/search_user", methods=["POST"], strict_slashes=False)
def search_user():
    data = {}
    q = request.form.get("q")
    if q is not None and type(q) is str and len(q) > 0 and ord(q[0]) in range(97, 123):
        first_letter = q[0]
        data["name"] = "{}{}".format(q, "olberton")
        data["id"] = 89
    res = jsonify(data)
    res.headers["Content-Type"] = "application/json"
    return {}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
