#!/usr/bin/python3

"""
Start a web application
"""

from flask import Flask, render_template
from markupsafe import escape
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def close(exec):
    storage.close()


@app.route("/states", strict_slashes=False)
def all_states():
    """
    Get all states
    """
    all_states = storage.all(State)
    return render_template("7-states_list.html", states=all_states.values())


@app.route("/states/<id>", strict_slashes=False)
def get_state(id):
    """
    get a state
    """
    state_cls = None
    all_states = storage.all(State)
    for state in all_states.values():
        if id == state.id:
            state_cls = state
            break
    return render_template("9-states.html", state=state_cls)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
