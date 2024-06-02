#!/usr/bin/python3

"""
Start a flask web application
"""

from flask import Flask, render_template
from markupsafe import escape
from models import storage
from models.state import State
from models.amenity import Amenity


app = Flask(__name__)


@app.teardown_appcontext
def close(exec):
    storage.close()


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """
    render the hbnb page
    """
    all_states = storage.all(State)
    all_amenities = storage.all(Amenity)
    return render_template("10-hbnb_filters.html",
                           states=all_states.values(),
                           amenities=all_amenities.values())


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
