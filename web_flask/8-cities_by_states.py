#!/usr/bin/python3
'''8. List of states'''

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)

states = storage.all(State).values()


@app.route('/cities_by_states', strict_slashes=False)
def show_states():
    """show states"""
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
