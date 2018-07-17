#!/usr/bin/python
# -*- coding: utf-8
#

from datetime import datetime
from invent_app import db
import re

RE_UPD = re.compile(r'^(Security )?(Definition )?Update for')


class Host(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    hostname = db.Column(db.String(64), index=True, unique=True)
    pub_date = db.Column(db.DateTime, nullable=False, default=datetime.now(), onupdate=datetime.now())
    CsDNSHostName = db.Column(db.String(250))
    CsDomain = db.Column(db.String(250))
    WindowsProductName = db.Column(db.String(250))
    WindowsInstallationType = db.Column(db.String(250))
    WindowsEditionId = db.Column(db.String(250))
    WindowsCurrentVersion = db.Column(db.String(250))
    WindowsBuildLabEx = db.Column(db.String(250))

    def __init__(self, hostname=None, data=None):
        super(Host, self).__init__()
        if data:
            self.from_json(data)
        else:
            self.hostname = hostname

    def __repr__(self):
        return '<Host %r>' % self.hostname

    def __str__(self):
        return '<Host %r>' % self.hostname

    def from_json(self, data):
        if data.has_key('hostname'): self.hostname = data['hostname']
        if data.has_key('CsDNSHostName'): self.CsDNSHostName = data['CsDNSHostName']
        if data.has_key('CsDomain'): self.CsDomain = data['CsDomain']
        if data.has_key('WindowsProductName'): self.WindowsProductName = data['WindowsProductName']
        if data.has_key('WindowsInstallationType'): self.WindowsInstallationType = data['WindowsInstallationType']
        if data.has_key('WindowsEditionId'): self.WindowsEditionId = data['WindowsEditionId']
        if data.has_key('WindowsCurrentVersion'): self.WindowsCurrentVersion = data['WindowsCurrentVersion']
        if data.has_key('WindowsBuildLabEx'): self.WindowsBuildLabEx = data['WindowsBuildLabEx']


class Soft(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hostname = db.Column(db.String(64), index=True, unique=False)
    DisplayName = db.Column(db.String(250))
    DisplayVersion = db.Column(db.String(64))
    Publisher = db.Column(db.String(64))
    InstallDate = db.Column(db.DateTime)
    IsUpdate = db.Column(db.Boolean())

    def __init__(self, hostname, data):
        super(Soft, self).__init__()
        self.hostname = hostname
        if data.has_key('DisplayName'):
            self.DisplayName = data['DisplayName']
            if RE_UPD.match(data['DisplayName']):
                self.IsUpdate = True
            else:
                self.IsUpdate = False

        if data.has_key('DisplayVersion'): self.DisplayVersion = data['DisplayVersion']
        if data.has_key('Publisher'): self.Publisher = data['Publisher']
        if data.has_key('InstallDate'):
            if data['InstallDate']:
                self.InstallDate = datetime.strptime(data['InstallDate'], '%Y%m%d')
