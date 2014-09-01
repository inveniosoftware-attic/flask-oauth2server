# -*- coding: utf-8 -*-
#
# This file is part of Flask-OAuth2Server
# Copyright (C) 2014 CERN.
#
# Flask-OAuth2Server is free software; you can redistribute it and/or
# modify it under the terms of the Revised BSD License; see LICENSE
# file for more details.

from setuptools import setup, find_packages
import os
import re

# Get the version string.  Cannot be done with import!
with open(os.path.join('flask_oauth2server', 'version.py'), 'rt') as f:
    version = re.search(
        '__version__\s*=\s*"(?P<version>.*)"\n',
        f.read()
    ).group('version')

setup(
    name='Flask-OAuth2Server',
    version=version,
    url='http://github.com/inveniosoftware/flask-oauth2server/',
    license='BSD',
    author='Invenio collaboration',
    author_email='info@invenio-software.org',
    description='Flask-OAuth2Server allows you to quickly add an OAuth2 '
                'provider to your Flask application.',
    long_description=open('README.rst').read(),
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask>=0.10.1',
        'six',
        'Flask-OAuthlib>=0.6.0',
        'Flask-Registry>=0.2.0',
        "Flask-Login>=0.2.7",
        "Flask-WTF>=0.10.0",
        "WTForms>=2.0",
        "wtforms-alchemy>=0.12.6",
        "SQLAlchemy>=0.8.3",
        "SQLAlchemy-Utils>=0.23.5,<0.24",
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Flask',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Development Status :: 5 - Production/Stable',
    ],
    test_suite='nose.collector',
    tests_require=['nose', 'coverage'],
)
