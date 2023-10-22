#!/usr/bin/python3
"""
A Python script that loads all cities of a State.
"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """
	The home route of our AirBnB application.
    """
    return "Hello HBNB!"


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """This function displays cities per state"""
    states = storage.all(State)
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def teardown_context(ctx):
    """This function displays cities per state"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)