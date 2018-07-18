# -*- coding: utf-8
#
from invent_app import app, db
from invent_app.models import Soft
from flask import render_template
from sqlalchemy import func
from sqlalchemy.sql import label
import urllib2


def default_val(data):
    return data if data else ''


def default_date(data):
    return data.date() if data else ''


@app.route('/all_software')
def all_software():
    data = db.session.query(Soft.Name, label('Count', func.count(Soft.Name)), Soft.IsUpdate ).group_by(Soft.Name).all()
    return render_template('all_software.html', title='Software', data=data)


@app.route('/software/<s_name>')
def software(s_name):
    name = urllib2.unquote(s_name)
    data = Soft.query.filter_by(Name=name).group_by(Soft.Hostname).order_by(Soft.Hostname)
    return render_template('software.html', title=name, data=data)


@app.route('/host/<h_name>')
def host(h_name):
    data = Soft.query.filter_by(Hostname=h_name).order_by(Soft.Name)
    return render_template('host.html', title=h_name, data=data)
