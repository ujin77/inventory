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
    query_hosts = Host.query.all()
    data = []
    for host in query_hosts:
        data.append([
            host.Hostname,
            default_date(host.Pub_date),
            host.CsDNSHostName,
            host.CsDomain,
            host.WindowsProductName,
            host.WindowsInstallationType,
            host.WindowsEditionId,
            host.WindowsCurrentVersion,
            host.WindowsBuildLabEx
        ])
    return render_template('hosts.html', title='Hosts', data=data)

