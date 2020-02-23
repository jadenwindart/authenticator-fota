from flask import request , abort
from app import app , db
from app.models.user import Device , FotaSession , DeviceMQTT
import hmac
from hashlib import sha256
import json
import secrets

def register():
    if request.method == 'POST':
        data = request.json
        identifier = data['identifier']
        password = data['password']
        device = Device.query.filter_by(device_identifier=identifier).first()
        if not bool(device):
            key = app.config.get('SECRET_KEY')
            new_password = hmac.new(key.encode('ASCII'),password.encode('ASCII'),sha256)
            new_device = Device(device_identifier=identifier,password=new_password.hexdigest())
            db.session.add(new_device)
            rand_string = secrets.token_urlsafe(8)
            device_mqtt = DeviceMQTT(topic=rand_string,device=new_device.id)
            db.session.add(device_mqtt)
            db.session.commit()
            response = app.response_class(
                response ='Device Has Been Added',
                status=200,
                mimetype='application/json'
            )
            return response
        else:
            device_mqtt = DeviceMQTT.query.filter_by(device=device.id).first()
            if bool(device_mqtt):
                response = app.response_class(
                    response =json.dumps({
                        'status' : 'Device Already Exist',
                        'mqtt_topic' : device_mqtt.topic
                    }),
                    status=200,
                    mimetype='application/json'
                )
            else:
                rand_string = secrets.token_urlsafe(8)
                device_mqtt = DeviceMQTT(topic=rand_string,device=device.id)
                db.session.add(device_mqtt)
                db.session.commit()
                response = app.response_class(
                    response =json.dumps({
                        'status' : 'Device Already Exist',
                        'mqtt_topic' : device_mqtt.topic
                    }),
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
        device = Device.query.filter_by(device_identifier=identifier).first()
        device_json = json.dumps({
            'identifier' : identifier,
            'password' : device.password
        })
        salt = secrets.token_urlsafe(32)
        enc_json = hmac.new(salt.encode('ASCII'),device_json.encode('ASCII'),sha256)
        fota_session = FotaSession(salt=salt,password=enc_json.hexdigest())
        db.session.add(fota_session)
        db.session.commit()
        device_mqtt = DeviceMQTT.query.filter_by(device=device.id).first()
        response = app.response_class(
            response=json.dumps({
                'identifier' : device.device_identifier,
                'password' : enc_json.hexdigest(),
                'mqtt_session' : device_mqtt.topic
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
        print(identifier + " || " + request_password)
        device = Device.query.filter_by(device_identifier=identifier).first()
        device_dumps = json.dumps({
            'identifier' : device.device_identifier,
            'password' : device.password
        })
        fota_session = FotaSession.query.filter_by(password=request_password).first()
        received_password = hmac.new(fota_session.salt.encode('ASCII'),device_dumps.encode('ASCII'),sha256)
        if hmac.compare_digest(fota_session.password,received_password.hexdigest()):
            response = app.response_class(
                status=200,
                mimetype='application/json'
            )
            return response
        else:
            abort(401)

        