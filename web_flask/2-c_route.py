#!/usr/bin/python3
""" a script that starts a Flask web application with 2 routes """


from flask import Flask

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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
