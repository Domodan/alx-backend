#!/usr/bin/env python3
"""
    Module: Use Babel to get user locale
"""

from flask_babel import Babel
from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')


class Config(object):
    """
        Represents a Flask Babel configuration
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """
        Retrieves the locale and render the web page based on the locale
    """
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/', methods=['GET'])
def get_index() -> str:
    """
        Render the Home/Index template page for Babel usage.
    """
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run()
