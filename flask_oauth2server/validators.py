# -*- coding: utf-8 -*-
#
# This file is part of Flask-OAuth2Server
# Copyright (C) 2014 CERN.
#
# Flask-OAuth2Server is free software; you can redistribute it and/or
# modify it under the terms of the Revised BSD License; see LICENSE
# file for more details.

from __future__ import absolute_import

from oauthlib.oauth2.rfc6749.errors import InsecureTransportError, \
    InvalidRedirectURIError
from six.moves.urllib_parse import urlparse

from .errors import ScopeDoesNotExists


def validate_redirect_uri(value):
    """Validate a redirect URI.

    Redirect URIs must be a valid URL and use https unless the host is
    localhost for which http is accepted.
    """
    sch, netloc, path, par, query, fra = urlparse(value)
    if not (sch and netloc):
        raise InvalidRedirectURIError()
    if sch != 'https':
        if ':' in netloc:
            netloc, port = netloc.split(':', 1)
        if not (netloc in ('localhost', '127.0.0.1') and sch == 'http'):
            raise InsecureTransportError()


def validate_scopes(value_list):
    """Validate if each element in a list is a registered scope."""
    from .registry import scopes as scopes_registry

    for value in value_list:
        if value not in scopes_registry:
            raise ScopeDoesNotExists(value)
    return True
