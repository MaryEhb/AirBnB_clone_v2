#!/usr/bin/python3
'''0. Hello Flask!'''

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    '''/: display “Hello HBNB!”'''
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
