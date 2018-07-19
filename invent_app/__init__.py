#!/usr/bin/python
# -*- coding: utf-8
#

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Configuration
import flask_excel as excel


app = Flask(__name__)
app.config.from_object(Configuration)
db = SQLAlchemy(app)
excel.init_excel(app)


from invent_app.views import rest, routes
from invent_app.models import Host, Soft

db.create_all()
