# -*- coding: utf-8 -*-
#
# This file is part of Flask-OAuth2Server
# Copyright (C) 2014, 2016 CERN.
#
# Flask-OAuth2Server is free software; you can redistribute it and/or
# modify it under the terms of the Revised BSD License; see LICENSE
# file for more details.

"""flask_oauth2server views."""

from __future__ import absolute_import

from .server import blueprint as server_blueprint
from .settings import blueprint as settings_blueprint

blueprints = [
    server_blueprint,
    settings_blueprint,
]
