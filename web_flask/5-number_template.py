#!/usr/bin/python3
"""Flask"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Returns string"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Returns string"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def cText(text):
    """displays text variable"""
    return "C {}".format(text.replace("_", " "))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythonText(text="is cool"):
    """displays text variable"""
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def isNumber(n):
    """display an integer"""
    if isinstance(n, int):
        return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n=None):
    """display integer"""
    if isinstance(n, int):
        return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run()
