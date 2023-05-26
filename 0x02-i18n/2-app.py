#!/usr/bin/env python3
""" Basic Flask app with Babel """

from flask import Flask, render_template, request
from flask_babel import Babel, gettext

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """ Config class for Flask app """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """ Determine the best match for the user's locale """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """ Main route """
    return render_template(
            '2-index.html', title=gettext('Welcome to Holberton'),
            header=gettext('Hello world')
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
