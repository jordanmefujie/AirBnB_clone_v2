#!/usr/bin/python3
"""
Starts a Flask web application
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """
    After each request, remove the current SQLAlchemy Session
    """
    storage.close()


@app.route('/states', strict_slashes=False)
def states_list():
    """
    Display a HTML page with a list of all State objects present in DBStorage
    """
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)

    return render_template('9-states_list.html', states=sorted_states)


@app.route('/states/<id>', strict_slashes=False)
def state_cities(id):
    """
    Display a HTML page with details of a specific State and its linked cities
    """
    state = storage.get(State, id)
    if state:
        return render_template('9-state_cities.html', state=state)
    else:
        return render_template('9-not_found.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

