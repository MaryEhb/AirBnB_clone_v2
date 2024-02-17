#!/usr/bin/python3
'''8. List of states'''

from flask import Flask, render_template
from models import storage

app = Flask(__name__)

states = list(storage.all("State").values())


@app.route('/states_list', strict_slashes=False)
def show_states():
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
