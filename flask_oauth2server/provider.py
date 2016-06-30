# -*- coding: utf-8 -*-
#
# This file is part of Flask-OAuth2Server
# Copyright (C) 2014, 2016 CERN.
#
# Flask-OAuth2Server is free software; you can redistribute it and/or
# modify it under the terms of the Revised BSD License; see LICENSE
# file for more details.

"""Configuration of flask-oauthlib provider."""

from datetime import datetime, timedelta

from flask import current_app
from flask.ext.login import current_user
from flask_oauthlib.provider import OAuth2Provider

from invenio.ext.sqlalchemy import db
from invenio.modules.accounts.models import User
from .models import Token


oauth2 = OAuth2Provider()


@oauth2.usergetter
def get_user(username, password, *args, **kwargs):
    """Get user for grant type password.

    Needed for grant type 'password'. Note, grant type password is by default
    disabled.
    """
    user = User.query.filter_by(username=username).first()
    if user.check_password(password):
        return user


@oauth2.tokengetter
def get_token(access_token=None, refresh_token=None):
    """Load an access token.

    Add support for personal access tokens compared to flask-oauthlib
    """
    if access_token:
        t = Token.query.filter_by(access_token=access_token).first()
        if t and t.is_personal:
            t.expires = datetime.utcnow() + timedelta(
                seconds=int(current_app.config.get(
                    'OAUTH2_PROVIDER_TOKEN_EXPIRES_IN'
                ))
            )
        return t
    elif refresh_token:
        return Token.query.filter_by(
            refresh_token=refresh_token, is_personal=False,
            ).first()
    else:
        return None


@oauth2.tokensetter
def save_token(token, request, *args, **kwargs):
    """Token persistence."""
    # Exclude the personal access tokens which doesn't expire.
    uid = request.user.id if request.user else current_user.get_id()

    tokens = Token.query.filter_by(
        client_id=request.client.client_id,
        user_id=uid,
        is_personal=False,
    )

    # make sure that every client has only one token connected to a user
    if tokens:
        for tk in tokens:
            db.session.delete(tk)
        db.session.commit()

    expires_in = token.pop('expires_in')
    expires = datetime.utcnow() + timedelta(seconds=int(expires_in))

    tok = Token(
        access_token=token['access_token'],
        refresh_token=token.get('refresh_token'),
        token_type=token['token_type'],
        _scopes=token['scope'],
        expires=expires,
        client_id=request.client.client_id,
        user_id=uid,
        is_personal=False,
    )
    db.session.add(tok)
    db.session.commit()
    return tok
