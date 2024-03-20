#!/usr/bin/python3
""" web flask application script:
"""

from flask import Flask

app = Flask("__name__")


@app.route('/', strict_slashes=False)
def hello():
    """Returns a string"""
    return ("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Returns a string"""
    return ("HBNB")


@app.route("/c/<text>", strict_slashes=False)
def cText(text):
    """display text variable"""
    return "C {}".format(text.replace("_", " "))


@app.route('/python', strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def pythonText(text="is cool"):
    """display text variable"""
    return "Python {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
