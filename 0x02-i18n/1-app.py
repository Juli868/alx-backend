#!/usr/bin/env python3
"""Language preferences."""
from flask import Flask
from flask_babel import Babel
app = Flask(__name__)
babel = Babel(app)


class Config():
    """Illustratee the used languages."""

    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
