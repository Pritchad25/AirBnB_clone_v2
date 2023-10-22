#!/usr/bin/python3
""" This Python script starts a Flask web application:
listening on 0.0.0.0, port 5000 Routes /: display “Hello HBNB!”
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home_hbnb():
    """ This function defines the home route """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ This function defines the hbnb route return HBNB"""
    return "HBNB"

@app.route("/c/<text>",  strict_slashes=False)
def c_route(text):
    """ This function displays “C ” followed by the value of the
	text variable """
    return "C {}".format(text.replace("_", " "))

@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_route(text="is cool"):
    """ This function displays “Python ”, followed by the value of the
	text variable """
    return f"Python {text.replace('_', ' ')}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
