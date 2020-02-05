from flask import request , abort
from app import app , db
from app.models.user import Device , FotaSession
import hmac
from hashlib import sha256
import json
import secrets

def register():
    if request.method == 'POST':
        data = request.json
        identifier = data['identifier']
        password = data['password']
        key = app.config.get('SECRET_KEY')
        new_password = hmac.new(key.encode('ASCII'),password.encode('ASCII'),sha256)
        new_device = Device(device_identifier=identifier,password=new_password.hexdigest())
        db.session.add(new_device)
        db.session.commit()
        response = app.response_class(
            response ='Device Has Been Added',
            status=200,
            mimetype='application/json'
        )
        return response
    else:
        abort(403)

def get_credentials():
    if request.method == 'GET':
        data = request.json
        identifier = data['identifier']
        device = Device.query.filter_by(device_identifier=identifier)
        device_json = json.dumps({
            'identifier' : identifier,
            'password' : device.password
        })
        salt = secrets.token_urlsafe(32)
        enc_json = hmac.new(salt.encode('ASCII'),device_json.encode('ASCII'),sha256)
        response = app.response_class(
            response=json.dumps({
                'identifier' : device.device_identifier,
                'password' : enc_json.hexdigest()
                }),
            status=200,
            mimetype='application/json'
        )
        return response

def authenticate_device():
    if request.method == 'POST':
        data = request.json
        identifier = data['identifier']
        request_password = data['password']
        device = Device.query.filter_by(device_identifier=identifier)
        device_dumps = json.dumps({
            'identifier' : device.device_identifier,
            'password' : device.password
        })
        fota_session = FotaSession.query.filter_by(password=request_password)
        received_password = hmac.new(fota_session.salt.encode('ASCII'),device_dumps.encode('ASCII'),sha256)
        if hmac.compare_digest(fota_session.password,received_password.hexdigest()):
            response = app.response_class(
                status=200,
                mimetype='application/json'
            )
            return response
        else:
            abort(401)

        