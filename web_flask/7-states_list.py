#!/usr/bin/python3
"""
Script to starts a flask app
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """Displays HTML page of all State objects in DBStorage.
    """
    states = storage.all(State).values()
    states_s = sorted(states, key=lambda st: st.name)
    return render_template('7-states_list.html', states=states_s)


@app.teardown_appcontext
def teardown(exception):
    """close the current session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
