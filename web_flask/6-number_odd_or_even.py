#!/usr/bin/python3
"""
This application listens on 0port 5000.
Routes:
/: display “Hello HBNB!”
/hbnb: display “HBNB”
/c/<text>: display “C ” followed by the value\
    of the text variable\
        (replace underscore _ symbols with a space )
"""
from flask import Flask, render_template

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

@app.route('/number_template/<int:n>', strict_slashes=False)
def num(n):
    """This function displays HTML only if n is an integer."""
    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
	""" This function displays an HTML page only if n is even or odd. """
	if n % 2 == 0:
		evenness = 'even'
	else:
		evenness = 'odd'
	return render_template('6-number_odd_or_even.html', n=n, evenness=evenness)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
