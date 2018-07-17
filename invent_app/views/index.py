from flask import jsonify, request
from invent_app import app


@app.route('/test')
def index():
    return "Test OK"
