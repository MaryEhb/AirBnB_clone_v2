#!/usr/bin/python3
'''1. HBNB'''

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    '''/: display “Hello HBNB!”'''
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''/hbnb: display “HBNB”'''
    return "HBNB"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
