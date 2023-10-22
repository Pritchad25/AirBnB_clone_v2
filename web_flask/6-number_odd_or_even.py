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

@app.route("/number/<int:n>", strict_slashes=False)
def number_route(n):
	""" Function displays a number if n is an integer. """
    return "{} is a number".format(n)

@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
	""" This function displays an HTML page only if n is an integer. """
    return render_template("5-number.html", n=n)

@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
	""" This function displays an HTML page only if n is even or odd. """
    text = "{} is odd".format(n)

    if n % 2 == 0:
        text = "{} is even".format(n)

    return render_template("6-number_odd_or_even.html", text=text)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
