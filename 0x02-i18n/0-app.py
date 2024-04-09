#!/usr/bin/env python3
"""View a web."""
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def index():
    """Index view."""
    return render_template("0-index.html")
