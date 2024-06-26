#!/usr/bin/python3

"""
Starts a Flask web application
"""

from flask import Flask
from markupsafe import escape


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def display_c(text):
    formated_text = escape(text.replace("_", " "))
    return f"C {formated_text}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
