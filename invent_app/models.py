#!/usr/bin/python
# -*- coding: utf-8
#

from datetime import datetime
from invent_app import db
import re

RE_UPD = re.compile(r'^(Security )?(Definition )?Update for')


class Host(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    Hostname = db.Column(db.String(64), index=True, unique=True)
    Pub_date = db.Column(db.DateTime, nullable=False, default=datetime.now(), onupdate=datetime.now())
    CsDNSHostName = db.Column(db.String(250))
    CsDomain = db.Column(db.String(250))
    WindowsProductName = db.Column(db.String(250))
    WindowsInstallationType = db.Column(db.String(250))
    WindowsEditionId = db.Column(db.String(250))
    WindowsCurrentVersion = db.Column(db.String(250))
    WindowsBuildLabEx = db.Column(db.String(250))
    PowerShell = db.Column(db.String(64))

    def __init__(self, Hostname=None, data=None):
        super(Host, self).__init__()
        if data:
            self.from_json(data)
        else:
            self.Hostname = Hostname

    def __repr__(self):
        return '<Host %r>' % self.Hostname

    def __str__(self):
        return '<Host %r>' % self.hostname

    def from_json(self, data):
        if data.has_key('Hostname'): self.Hostname = data['Hostname']
        if data.has_key('CsDNSHostName'): self.CsDNSHostName = data['CsDNSHostName']
        if data.has_key('CsDomain'): self.CsDomain = data['CsDomain']
        if data.has_key('WindowsProductName'): self.WindowsProductName = data['WindowsProductName']
        if data.has_key('WindowsInstallationType'): self.WindowsInstallationType = data['WindowsInstallationType']
        if data.has_key('WindowsEditionId'): self.WindowsEditionId = data['WindowsEditionId']
        if data.has_key('WindowsCurrentVersion'): self.WindowsCurrentVersion = data['WindowsCurrentVersion']
        if data.has_key('WindowsBuildLabEx'): self.WindowsBuildLabEx = data['WindowsBuildLabEx']
        if data.has_key('PowerShell'):
            ps = data['PowerShell']
            self.PowerShell = '{}.{}.{}'.format(ps['Major'], ps['Minor'], ps['Build'])


class Soft(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Hostname = db.Column(db.String(64), index=True, unique=False)
    Name = db.Column(db.String(250))
    Version = db.Column(db.String(64))
    Vendor = db.Column(db.String(64))
    IsUpdate = db.Column(db.Boolean())

    def __init__(self, Hostname, data):
        super(Soft, self).__init__()
        self.Hostname = Hostname
        if data.has_key('Name'):
            self.Name = data['Name']
            if RE_UPD.match(data['Name']):
                self.IsUpdate = True
            else:
                self.IsUpdate = False
        if data.has_key('Version'):
            self.Version = data['Version']
        if data.has_key('Vendor'):
            self.Vendor = data['Vendor']
