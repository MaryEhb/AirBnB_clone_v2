#!/usr/bin/python3
'''4. Is it a number?'''

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


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    '''display “C ” followed by the value of the text variable'''
    return "C {}".format(text.replace('_', ' '))


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    '''3. Python is cool!'''
    if not text:
        return 'Python is cool'
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def is_number(n):
    '''display if int'''
    return "{} is a number".format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
