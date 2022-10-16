#!/usr/bin/python3
""" Start a Flask web application listening on 0.0.0.0, port 5000
Routes: /: display "Hello HBNB!", /hbnb: display "HBNB", /c/<text>:
display c followed by text, /python/(<text>): display python, followed text
default text value "is cool"
/number/<n>: display n is a number ONLY if n is an integer
/number_template/<n>: display a HTML page ONLY if n is an integer, H1 tag:
"Number: n" inside the tag BODY
/number_odd_or_even/<n>: display a HTML page ONLY if n is an integer, H1 tag:
"Number: n is odd | even inside BODY tag
/states_list: display a HTML page:(inside the tag BODY), H1 tag: "States"
UL tag: list all State object in DBStorage sorted by name
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
                           state=storage.all('State').values())


@app.teardown_appcontext
def teardown(self):
    """ Remove SQLAlchemy Session """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
