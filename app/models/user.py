from app import db
import datetime

class Device(db.Model):
    id = db.Column(db.Integer ,primary_key=True)
    device_identifier = db.Column(db.String(255),unique=True)
    password = db.Column(db.String(255))

    def __repr__(self):
        return '<Device {}>'.format(self.device_identifier)

class Client(db.Model):
    id = db.Column(db.Integer , primary_key=True)
    username = db.Column(db.String(255),unique=True)
    password = db.Column(db.String(255))

    def __repr__(self):
        return '<Client {}'.format(self.username)

class Permission(db.Model):
    id = db.Column(db.Integer , primary_key=True)
    client = db.Column(db.Integer , db.ForeignKey('client.id'))
    permission = db.Column(db.Integer)

class FotaSession(db.Model):
    id = db.Column(db.Integer , primary_key=True)
    salt = db.Column(db.String(32))
    password = db.Column(db.String(255))
    timestamp = db.Column(db.DateTime,nullable=False,default=datetime.utcnow,onupdate=datetime.utcnow)