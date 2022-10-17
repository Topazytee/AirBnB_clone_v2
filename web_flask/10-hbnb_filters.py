#!/usr/bin/python3
""" Start a Flask web application listening on 0.0.0.0, port 5000
Must use strict_slashes=False in route definition """
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from flask import Flask
from flask import render_template
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/hbnb_filters')
def hbnb_filters():
    """ Return rendered HTML template with static files """
    states = storage.all('State').values()
    cities = storage.all('City').values()
    amenities = storage.all('Amenity').values()
    return render_template('10-hbnb_filters.html', **locals())


@app.teardown_appcontext
def teardown(self):
    """ Remove SQLAlchemy Session """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
