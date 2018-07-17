# -*- coding: utf-8
#
from invent_app import app, db
from invent_app.models import Soft
from flask import render_template
from sqlalchemy import func
from sqlalchemy.sql import label

def default_val(data):
    return data if data else ''


def default_date(data):
    return data.date() if data else ''


@app.route('/software')
def all_software():
    software = db.session.query(Soft.DisplayName,
                                label('Count', func.count(Soft.DisplayName))).group_by(Soft.DisplayName).all()
    data = []
    for soft in software:
        data.append([
            soft.DisplayName,
            default_val(soft.Count),
        ])
    return render_template('software.html', title='Software', data=data)


@app.route('/software/<host>')
def software(host):
    software = Soft.query.filter_by(hostname=host).order_by(Soft.DisplayName)
    data = []
    for soft in software:
        data.append([
            soft.DisplayName,
            default_val(soft.DisplayVersion),
            soft.Publisher,
            default_date(soft.InstallDate),
            'Update' if soft.IsUpdate else ''
        ])
    return render_template('software_on_host.html', title=host, data=data)
