# -*- coding: utf-8 -*-
#
# This file is part of Flask-OAuth2Server
# Copyright (C) 2014 CERN.
#
# Flask-OAuth2Server is free software; you can redistribute it and/or
# modify it under the terms of the Revised BSD License; see LICENSE
# file for more details.

from __future__ import absolute_import

from .helpers import FlaskTestCase
from flask_oauth2server import OAuth2Server


class TestOAuth2Server(FlaskTestCase):
    """
    Tests of extension creation
    """
    def test_version(self):
        # Assert that version number can be parsed.
        from flask_oauth2server import __version__
        from distutils.version import LooseVersion
        LooseVersion(__version__)

    def test_creation(self):
        assert 'oauth2server' not in self.app.extensions
        OAuth2Server(app=self.app)
        assert isinstance(self.app.extensions['oauth2server'], OAuth2Server)

    def test_creation_old_flask(self):
        # Simulate old Flask (pre 0.9)
        del self.app.extensions
        OAuth2Server(app=self.app)
        assert isinstance(self.app.extensions['oauth2server'], OAuth2Server)

    def test_creation_init(self):
        assert 'oauth2server' not in self.app.extensions
        r = OAuth2Server()
        r.init_app(app=self.app)
        assert isinstance(self.app.extensions['oauth2server'], OAuth2Server)

    def test_double_creation(self):
        OAuth2Server(app=self.app)
        self.assertRaises(RuntimeError, OAuth2Server, app=self.app)
