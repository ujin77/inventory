#!/usr/bin/python
# -*- coding: utf-8
#

import os

class Configuration():
    DEBUG = True
    # SERVER_NAME = '0.0.0.0:5000'
    APPLICATION_DIR = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(APPLICATION_DIR, 'inventory.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_AS_ASCII = False