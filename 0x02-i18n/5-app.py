#!/usr/bin/env python3
"""
    Module: Use Babel to get user locale
"""

from flask_babel import Babel
from flask import Flask, render_template

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

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[dict, None]:
    """
        Get user from session as per variable.
    """
    try:
        login_as = request.args.get('login_as', None)
        user = users[int(login_as)]
    except Exception:
        user = None


@app.before_request
def before_request() -> None:
    """
        Performs some routines before each request's resolution.
    """
    user = get_user()
    g.user = user


@app.route('/', methods=['GET'])
def get_index() -> str:
    """
        Render the Home/Index template page for Babel usage.
    """
    return render_template('1-index.html')


@babel.localeselector
def get_locale() -> str:
    """
        Retrieves the locale and render the web page based on the locale
    """
    queries = request.query_string.decode('utf-8').split('&')
    query_table = dict(map(
        lambda x: (x if '=' in x else '{}='.format(x)).split('='),
        queries,
    ))
    if 'locale' in query_table:
        if query_table['locale'] in app.config["LANGUAGES"]:
            return query_table['locale']
    return request.accept_languages.best_match(app.config["LANGUAGES"])


if __name__ == '__main__':
    app.run()