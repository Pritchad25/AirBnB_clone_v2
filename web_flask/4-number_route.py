#!/usr/bin/python3
""" This Python script starts a Flask web application:
listening on 0.0.0.0, port 5000 Routes
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    """This functiom displays 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello_hbnb():
    """The /hbnb route which displays HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def dynamic_route(text):
    """This function displays 'C' followed by the value of <text>."""
    text = text.replace("_", " ")
    return f"C {text}"


@app.route('/python/')
@app.route('/python/<text>', strict_slashes=False)
def dynamic_route_pyton(text="is cool"):
    """This function displays 'C' followed by the value of <text>."""
    text = text.replace("_", " ")
    return f"Python {text}"


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ This function displays “n is a number” only if n is an integer"""
    return f"{n} is a number"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
