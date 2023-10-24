#!/usr/bin/python3
"""
The Python script that starts a Flask web application:
listening on 0.0.0.0, port 5000
"""
from flask import Flask, render_template
from models import *
from models import storage

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<states_id>', strict_slashes=False)
def states(state_id=None):
    """ This method displays the states and cities listed in
	alphabetical order."""
	states = storage.all("State")
	if state_id is not None:
		state_id = 'State.' + state_id
	return render_template('9-states.html', states=states,
state_id=state_id))

if __name__ == "__main__":
    app.run(host="0.0.0.0")

@app.teardown_appcontext
def teardown(e):
	""" This method removes the current SQLAlchemy Session after each
	request """
	storage.close()

if __name__ == "__main__":
	app.run(host="0.0.0.0")
