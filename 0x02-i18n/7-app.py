#!/usr/bin/env python3
"""Module to config babel"""
from flask import Flask, render_template, g, request
from flask_babel import Babel
from typing import Dict, Union
import pytz
from pytz.exceptions import UnknownTimeZoneError
app = Flask(__name__)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config():
    """The default configurations"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """Determine the best match with our supported languages."""
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    if g.user and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user['locale']
    header_locale = request.headers.get('locale', '')
    if header_locale in app.config["LANGUAGES"]:
        return header_locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user() -> Union[Dict, None]:
    """Retrieve a user dictionary or None if ID not found or
    login_as not passed."""
    try:
        id = int(request.args.get('login_as'))
        return users[id]
    except (TypeError, ValueError):
        return None


@app.before_request
def before_request() -> None:
    """Set the current user in flask.g"""
    g.user = get_user()


@app.route('/')
def index() -> str:
    """Function to render 0-index template"""
    return render_template('6-index.html')


@babel.timezoneselector
def get_timezone():
    # Check URL parameters for timezone
    timezone = request.args.get('timezone')
    if timezone:
        try:
            return pytz.timezone(timezone).zone
        except UnknownTimeZoneError:
            pass

    # Check user settings for timezone
    if g.user:
        user_timezone = g.user.get('timezone')
        if user_timezone:
            try:
                return pytz.timezone(user_timezone).zone
            except UnknownTimeZoneError:
                pass

    # Default to UTC
    return app.config['BABEL_DEFAULT_TIMEZONE']


if __name__ == '__main__':
    app.run()
