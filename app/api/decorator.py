from flask import jsonify , request
from functools import wraps
from ..models.user import Client
import jwt
from app import app

def token_required(f):  
    @wraps(f)  
    def decorator(*args, **kwargs):

        token = None 

        if 'x-access-tokens' in request.headers:  
            token = request.headers['x-access-tokens'] 


        if not token:  
            return jsonify({'message': 'a valid token is missing'})   

        try:  
            data = jwt.decode(token, app.config['SECRET_KEY'])
            current_user = Client.query.filter_by(id=data['public_id']).first()  
        except Exception as e:
            print(e)  
            return jsonify({'message': 'token is invalid'})  


        return f(current_user, *args,  **kwargs)  
    return decorator 