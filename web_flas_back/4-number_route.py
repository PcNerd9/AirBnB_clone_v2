#!/usr/bin/python3

"""
Start a web application that listen on ip 0.0.0.0:5000
and serves the following url:
    /
    /hbnb
    /c/<text>
    /python/<text>
    /number/n
"""

from flask import Flask


app = Flask(__name__)


@app.route("/")
def hello():
    """
    return Hello HBNB
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    return HBNB
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """
    return user input
    """
    return "C {}".format(text.replace("_", " "))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is_cool"):
    """
    return user input
    """
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """
    return user input
    """
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
