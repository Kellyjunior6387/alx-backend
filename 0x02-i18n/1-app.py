#!/usr/bin/env python3
"""Module to config babel"""
from flask import Flask, render_template
from flask_babel import Babel
app = Flask(__name__)


class Config():
    """The default configurations"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def index():
    """Function to render 0-index template"""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()
