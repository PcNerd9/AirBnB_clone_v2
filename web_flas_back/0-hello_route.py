#!/usr/bin/python3

"""
Start a web application listening on ip address 0.0.0.0
and port 5000
"""
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    """
    return Hello HBNB!
    """
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
