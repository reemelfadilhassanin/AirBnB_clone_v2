#!/usr/bin/python3
"""
Starts a Flask web app
"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from os import environ

app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Displays a HTML page
    """
    states = sorted(storage.all(State).values(), key=lambda x: x.name)
    cities = sorted(storage.all(City).values(), key=lambda x: x.name)
    amenities = sorted(storage.all(Amenity).values(), key=lambda x: x.name)
    places = sorted(storage.all(Place).values(), key=lambda x: x.name)

    return render_template('100-hbnb.html',
                           states=states, cities=cities,
                           amenities=amenities, places=places)


@app.teardown_appcontext
def teardown(exception):
    """
    Remove  Session
    """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
