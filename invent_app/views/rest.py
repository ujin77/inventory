from flask import jsonify, request
from invent_app import app, db
from invent_app.models import Host, Soft
import json
from datetime import datetime
import re

RE_UPD = re.compile(r'^(Security )?(Definition )?Update for')


@app.route('/inventory/api/v1.0/host', methods=['POST'])
def create_task():
    if not request.json:
        abort(400)
    # print json.dumps(request.json, indent=2, ensure_ascii=False)
    # print request.json['Hostname']
    host = Host.query.filter_by(Hostname=request.json['Hostname']).first()
    if host:
        host.Pub_date = datetime.now()
        host.from_json(request.json)
    else:
        db.session.add(Host(data=request.json))
    Soft.query.filter_by(Hostname=request.json['Hostname']).delete()
    for soft in request.json['Software']:
        if soft['Name']:
            db.session.add(Soft(request.json['Hostname'], soft))
    db.session.commit()
    return jsonify({'Inventory': "OK"}), 201
