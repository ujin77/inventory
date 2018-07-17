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
    host = Host.query.filter_by(hostname=request.json['hostname']).first()
    if host:
        host.pub_date = datetime.now()
        host.from_json(request.json)
    else:
        db.session.add(Host(data=request.json))
    Soft.query.filter_by(hostname=request.json['hostname']).delete()
    for soft in request.json['Software']:
        if soft['DisplayName']:
            db.session.add(Soft(request.json['hostname'], soft))
    db.session.commit()
    # print json.dumps(request.json, indent=2, ensure_ascii=False)
    return jsonify({'Inventory': "OK"}), 201
