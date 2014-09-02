# This file is part of Flask-OAuth2Server
# Copyright (C) 2014 CERN.
#
# Flask-OAuth2Server is free software; you can redistribute it and/or
# modify it under the terms of the Revised BSD License; see LICENSE
# file for more details.

pep257 --ignore=D100,D101,D102,D103 flask_oauth2server
sphinx-build -qnNW docs docs/_build/html
python setup.py test