#!/usr/bin/env python3
"""
    Module: Basic Babel setup.
"""

from flask_babel import Babel
from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')


class Config(object):
    """
        BRepresents a Flask Babel configuratio
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@app.route('/', methods=['GET'])
def get_index() -> str:
    """
        Render the Home/Index template page for Babel usage.
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()
