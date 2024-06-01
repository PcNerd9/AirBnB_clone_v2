#!/usr/bin/python3

"""
start a web application listen on ip 0.0.0.0:5000
and serve the following url:
    /
    /hbnb
    /c/<text>
    /python/<text>
    /number/<n>
    /number_template/<n>
    /number_odd_or_even/<n>
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


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is_cool"):
    """
    return Python with user input
    """
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """
    return the user input
    """
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """
    render a template
    """
    return render_template("5-number.html", value=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """
    render a template
    """
    if (n % 2 == 0):
        odd_even = "even"
    else:
        odd_even = "odd"
    return render_template("6-number_odd_or_even.html",
                           value=n, odd_even=odd_even)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
