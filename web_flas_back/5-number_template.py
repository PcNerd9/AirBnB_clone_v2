#!/usr/bin/python3

"""
start a web application listen on ip 0.0.0.0:5000
and serves the following url:
    /
    /hbnb
    /c/<text>
    /python/<text>
    /number/<n>
    /number_template/<n>
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """
    return Hello HBNB!
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
    return C with user input
    """
    return "C {}".format(text.replace("_", " "))


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is_cool"):
    """
    return Python with user input
    """
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """
    return user input
    """
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """
    render a template
    """
    return render_template("5-number.html", value=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
