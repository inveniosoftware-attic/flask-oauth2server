# -*- coding: utf-8 -*-
#
# This file is part of Flask-OAuth2Server
# Copyright (C) 2014, 2016 CERN.
#
# Flask-OAuth2Server is free software; you can redistribute it and/or
# modify it under the terms of the Revised BSD License; see LICENSE
# file for more details.

"""Flask extension.

Flask-OAuth2Server is initialized like this:

>>> from flask import Flask
>>> from flask_oauth2server import OAuth2Server
>>> app = Flask('myapp')
>>> ext = OAuth2Server(app=app)
"""

from __future__ import absolute_import


class OAuth2Server(object):
    """Flask extension.

    Initialization of the extension:

    >>> from flask import Flask
    >>> from flask.ext.oauth2server import OAuth2Server
    >>> app = Flask('myapp')
    >>> ext = OAuth2Server(app=app)

    or alternatively using the factory pattern:

    >>> app = Flask('myapp')
    >>> ext = OAuth2Server()
    >>> ext.init_app(app)
    """

    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        """Initialize a Flask application."""
        # Follow the Flask guidelines on usage of app.extensions
        if not hasattr(app, 'extensions'):
            app.extensions = {}
        if 'oauth2server' in app.extensions:
            raise RuntimeError("Flask application already initialized")
        app.extensions['oauth2server'] = self


# Version information
from .version import __version__

__all__ = ('OAuth2Server', '__version__')
