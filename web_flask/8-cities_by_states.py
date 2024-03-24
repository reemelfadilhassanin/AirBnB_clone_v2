#!/usr/bin/python3
"""
Script to starts a flask app
"""

from models.state import State
from models import storage
import sys
import os
from flask import Flask, render_template

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Append the parent directory to the Python path
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

# Now you should be able to import the models module

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """
    Displays html page of all cities by State objects in DBStorage.
    """
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template('8-cities_by_states.html', states=sorted_states)


@app.teardown_appcontext
def teardown(exception):
    """close the current session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
