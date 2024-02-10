#!/usr/bin/env python3
"""
    Module: Babel i18n
"""

from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')
app.url_map.strict_slashes = False


@app.route('/', methods=['GET'])
def get_index() -> str:
    """
        Render the Home/Index page template
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
