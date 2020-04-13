from flask import request , abort , session , jsonify
from app import app , db
from app.models.user import Client
import hmac
from hashlib import sha256
import json
import secrets
import jwt
from werkzeug.security import generate_password_hash , check_password_hash
import datetime

def login():
    if request.method == 'POST':
        data = request.json
        username = data['username']
        password = data['password']
        user = Client.query.filter_by(username=username).first()
        if user:
            if check_password_hash(user.password,password):
                token = jwt.encode({'public_id': user.id, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
                return jsonify({'token' : token.decode('utf-8')})
        abort(401)
def register():
    if request.method == 'POST':
        try:
            data = request.json
            username = data['username']
            password = data['password']
            hashed_pass = generate_password_hash(password,method='sha256')
            user = Client(username=username,password=hashed_pass)
            db.session.add(user)
            db.session.commit()
            return app.response_class(
                status=200
                )
        except:
            return app.response_class(
                status = 400
            )