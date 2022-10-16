#!/usr/bin/python3
""" Start a Flask web application listening on 0.0.0.0, port 5000
Must use strict_slashes=False in route definition """
from models import storage
from models.state import State
from flask import Flask
from flask import render_template
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list')
def fetch_data_state():
    """ Fetch sorted states, display HTML """
    return render_template('7-states_list.html',
                           states=storage.all('State').values())


@app.teardown_appcontext
def teardown(self):
    """ Remove SQLAlchemy Session """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
