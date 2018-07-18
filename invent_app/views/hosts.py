#!/usr/bin/python
# -*- coding: utf-8
#
from invent_app import app
from invent_app.models import Host
from flask import render_template
# from datetime import datetime


def default_val(data):
    return data if data else ''

def default_date(data):
    return "{:%Y-%m-%d %H:%M}".format(data) if data else ''


@app.route('/')
@app.route('/index')
@app.route('/hosts')
def hosts():
    data = Host.query.all()
    return render_template('index.html', title='Hosts', data=data)

