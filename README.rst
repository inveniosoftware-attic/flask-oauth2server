==================
Flask-OAuth2Server
==================

.. image:: https://travis-ci.org/inveniosoftware/flask-oauth2server.png?branch=master
    :target: https://travis-ci.org/inveniosoftware/flask-oauth2server
.. image:: https://coveralls.io/repos/inveniosoftware/flask-oauth2server/badge.png?branch=master
    :target: https://coveralls.io/r/inveniosoftware/flask-oauth2server
.. image:: https://pypip.in/v/Flask-OAuth2Server/badge.png
   :target: https://pypi.python.org/pypi/Flask-OAuth2Server/
.. image:: https://pypip.in/d/Flask-OAuth2Server/badge.png
   :target: https://pypi.python.org/pypi/Flask-OAuth2Server/


About
=====
Flask-OAuth2Server is a Flask extension that allows you to quickly add an
OAuth2 provider to your Flask application.

Installation
============
Flask-OAuth2Server is on PyPI so all you need is: ::

    pip install Flask-OAuth2Server

Documentation
============
Documentation is available at <http://flask-oauth2server.readthedocs.org> or can be build using Sphinx: ::

    git submodule init
    git submodule update
    pip install Sphinx
    python setup.py build_sphinx

Testing
=======
Running the test suite is as simple as: ::

    python setup.py test

or, to also show code coverage: ::

    ./run-tests.sh