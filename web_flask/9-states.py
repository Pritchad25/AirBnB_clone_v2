#!/usr/bin/python3
"""
The Python script that starts a Flask web application:
listening on 0.0.0.0, port 5000
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown(e):
    """ This method removes the current SQLAlchemy Session after each
	 request """
    storage.close()


@app.route("/states", strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def states(id=None):
    """ This method displays a HTML page """
    if id:
        states = storage.all(State).values()
        for state in states:
            if state.id == id:
                return render_template("9-states.html", state=state)
        else:
            return render_template("9-states.html", states=None)
    else:
        states = storage.all(State).values()
        return render_template("7-states_list.html", states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
