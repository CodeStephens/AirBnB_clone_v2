#!/usr/bin/python3
""" a script that starts a Flask web application with 2 routes """


from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_with_text(text):
    c_formatted = text.replace('_', ' ')
    return f"C {c_formatted}"


@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    python_formatted = text.replace('_', ' ')
    return f"Python {python_formatted}"


@app.route('/python', strict_slashes=False)
def python():
    return "Python is cool"


@app.route('/python/', strict_slashes=False)
def python_():
    return "Python is cool"


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return f"{n} is a number"


@app.route('/number_temlate/<int:n>', strict_slashes=False)
def number_template(n):
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
