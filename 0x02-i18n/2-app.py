#!/usr/bin/env python3

@babel.localeselector
def get_locale():
    return request.accept_languages
