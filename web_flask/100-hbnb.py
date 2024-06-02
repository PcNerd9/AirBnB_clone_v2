#!/usr/bin/python3

"""
Starting a flask web application
"""

from flask import Flask, render_template
from markupsafe import escape
from models import storage
from models.state import State
from models.place import Place
from models.amenity import Amenity
from models.user import User


app = Flask(__name__)


@app.teardown_appcontext
def close(exec):
    storage.close()


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    render an hbnb full page
    """
    all_states = storage.all(State).values()
    all_places = storage.all(Place).values()
    all_amenities = storage.all(Amenity).values()
    all_users = storage.all(User)
    return render_template("100-hbnb.html", states=all_states,
                           amenities=all_amenities,
                           places=all_places,
                           users=all_users
                           )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
