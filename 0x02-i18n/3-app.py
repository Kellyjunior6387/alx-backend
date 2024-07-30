#!/usr/bin/env python3
"""Module to config babel"""
from flask import Flask, render_template, g, request
from flask_babel import Babel
app = Flask(__name__)


class Config():
    """The default configurations"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'fr'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Determine the best match with our supported languages."""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """Function to render 0-index template"""
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run()
