#!/usr/bin/python3
""" Start a Flask web application listening on 0.0.0.0, port 5000
Routes: /: display "Hello HBNB!", /hbnb: display "HBNB", /c/<text>:
display c followed by text, /python/(<text>): display python, followed text
default text value "is cool"
/number/<n>: display n is a number ONLY if n is an integer
/number_template/<n>: display a HTML page ONLY if n is an integer, H1 tag:
"Number: n" inside the tag BODY
Must use strict_slashes=False in route definition """
from flask import Flask
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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
