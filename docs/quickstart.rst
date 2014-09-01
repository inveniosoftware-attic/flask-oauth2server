.. _quickstart:

Quickstart
==========

This guide assumes you have successfully installed Flask-OAuth2Server and a working
understanding of Flask. If not, follow the installation steps and read about
Flask at http://flask.pocoo.org/docs/.


A Minimal Example
-----------------

A minimal Flask-OAuth2Server usage example looks like this. First create the
application and initialize the extension:

>>> from flask import Flask
>>> from flask_oauth2server import OAuth2Server
>>> app = Flask('myapp')
>>> ext = OAuth2Server(app=app)

Some Extended Example
---------------------
Flask-OAuth2Server also has support for ...

.. literalinclude:: ../tests/helpers.py
