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
from models import *
from flask import Flask, render_template
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """ Display "Hello HBNB!" """
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """ Display "HBNB" """
    return "HBNB"


@app.route('/c/<text>')
def c_text(text):
    """ Display C followed by text variable """
    return "C {}".format(text.replace('_', ' '))


@app.route('/python')
@app.route('/python/<text>')
def python_text(text="is cool"):
    """ Display text variable """
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def number_if_int(n):
    """ Display only if n is an integer """
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>')
def number_template_if_html(n):
    """ Display HTML page ONLY if n is an integer
    inside the BODY tag """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    """ Display HTML page if n is an integer
    inside the BODY tag """
    odd_or_even = "even" if (n % 2 == 0) else "odd"
    return render_template('6-number_odd_or_even.html', n=n,
                           odd_or_even=odd_or_even)


@app.teardown_appcontext
def tear_down(self):
    """ Remove SQLAlchemy Session """
    storage.close()


@app.route('/states_list')
def fetch_data_state():
    """ Fetch sorted states, display HTML """
    states_obj = [s for s in storage.all("State").values()]
    return render_template('7-states_list.html', states_obj=states_obj)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
