#!/usr/bin/python
# -*- coding: utf-8
#

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Configuration


app = Flask(__name__)
app.config.from_object(Configuration)
db = SQLAlchemy(app)

from invent_app.views import rest, routes
from invent_app.models import Host, Soft

db.create_all()
