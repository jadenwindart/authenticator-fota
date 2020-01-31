from flask import request , abort
from app import app , db
from app.models.user import Device
import hmac
from hashlib import sha256

def register():
    if request.method == 'POST':
        data = request.json
        identifier = data['identifier']
        password = data['password']
        key = app.config.get('SECRET_KEY')
        new_password = hmac.new(key,password,sha256)
        new_device = Device(device_identifier=identifier,password=new_password)
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