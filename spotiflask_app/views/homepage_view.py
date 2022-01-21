"""
Web application homepage views used, this module defines the following functions:
- `homepage`, that defines homepage view
"""
from flask import render_template
from .blueprint import home


@home.route("/", endpoint='homepage')
def homepage():
    """
    Returns rendered `home.html` template for url route `/` and endpoint
    `homepage`
    """
    title = 'Welcome to Spotiflask'
    return render_template('home.html', title=title)
