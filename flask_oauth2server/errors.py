# -*- coding: utf-8 -*-
#
# This file is part of Flask-OAuth2Server
# Copyright (C) 2014 CERN.
#
# Flask-OAuth2Server is free software; you can redistribute it and/or
# modify it under the terms of the Revised BSD License; see LICENSE
# file for more details.


class OAuth2ServerError(Exception):

    """Base class for errors in oauth2server module."""


class ScopeDoesNotExists(OAuth2ServerError):

    """Scope is not registered it scopes registry."""

    def __init__(self, scope, *args, **kwargs):
        """Initialize exception by storing invalid scope."""
        super(ScopeDoesNotExists, self).__init__(*args, **kwargs)
        self.scope = scope
