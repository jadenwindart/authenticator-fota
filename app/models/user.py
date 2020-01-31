from app import db

class Device(db.Model):
    id = db.Column(db.Integer ,primary_key=True)
    device_identifier = db.Column(db.String(255),unique=True)
    password = db.Column(db.String(255))

    def __repr__(self):
        return '<Device {}>'.format(self.device_identifier)
