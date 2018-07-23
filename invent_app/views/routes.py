#!/usr/bin/python
# -*- coding: utf-8
#
from invent_app import app, db, excel
from invent_app.models import Host, Soft
from flask import render_template, request
from sqlalchemy import func, desc
from sqlalchemy.sql import label
# import urllib2


def get_request_order(default_order=''):
    order_by = request.args.get('order_by')
    order = request.args.get('order')
    if not order_by:
        order_by = default_order
    if order:
        order_by = desc(order_by)
        order = None
    else:
        order = 'desc'

    return order_by, order


@app.route('/')
@app.route('/index')
@app.route('/hosts')
def hosts():
    (order_by, order) = get_request_order('Hostname')
    data = Host.query.order_by(order_by).all()
    return render_template('index.html', title='Hosts', data=data, order=order)


@app.route('/all_software')
def all_software():
    (order_by, order) = get_request_order('Name')
    vendor = request.args.get('vendor')
    if vendor:
        data = db.session.query(Soft.Name,
                                Soft.Version,
                                Soft.Vendor,
                                label('Count', func.count(Soft.Name)),
                                Soft.IsUpdate).group_by(Soft.Name).filter_by(Vendor=vendor).order_by(order_by)
    else:
        data = db.session.query(Soft.Name,
                                Soft.Version,
                                Soft.Vendor,
                                label('Count', func.count(Soft.Name)),
                                Soft.IsUpdate).group_by(Soft.Name).order_by(order_by).all()
    return render_template('all_software.html', title='Software', data=data, order=order, vendor=vendor)


@app.route('/software/<name>')
def software(name):
    data = Soft.query.filter_by(Name=name).group_by(Soft.Hostname).order_by(Soft.Hostname)
    return render_template('software.html', title=name, data=data)


@app.route('/host/<h_name>')
def host(h_name):
    (order_by, order) = get_request_order('Name')
    vendor = request.args.get('vendor')
    if vendor:
        data = Soft.query.filter_by(Hostname=h_name, Vendor=vendor).order_by(order_by)
    else:
        data = Soft.query.filter_by(Hostname=h_name).order_by(order_by)
    return render_template('host.html', title=h_name, data=data, order=order, vendor=vendor)


@app.route('/inventory_software.csv', methods=['GET'])
def export_software():
    data = db.session.query(Soft.Hostname, Soft.Name, Soft.Version, Soft.Vendor).order_by(Soft.Hostname, Soft.Name).all()
    column_names = ['Hostname', 'Name', 'Version', 'Vendor']
    return excel.make_response_from_query_sets(data, column_names, "csv")

@app.route('/inventory_hosts.csv', methods=['GET'])
def export_hosts():
    data = db.session.query(Host.Hostname,
                            Host.WindowsProductName,
                            Host.WindowsInstallationType,
                            Host.WindowsEditionId,
                            Host.WindowsCurrentVersion,
                            Host.WindowsBuildLabEx,
                            Host.PowerShell,
                            Host.Pub_date
    ).order_by(Host.Hostname).all()
    column_names = ['Hostname',
                    'WindowsProductName',
                    'WindowsInstallationType',
                    'WindowsEditionId',
                    'WindowsCurrentVersion',
                    'WindowsBuildLabEx',
                    'PowerShell',
                    'Pub_date'
                    ]
    return excel.make_response_from_query_sets(data, column_names, "csv")
