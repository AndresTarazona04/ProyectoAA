from datetime import datetime
from app import db, login 
from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    rests = db.relationship('Rest', backref='cliente', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))



class Rest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), index=True, unique=False)
    lat = db.Column(db.Float, index=True, unique=False)
    lon = db.Column(db.Float, index=True, unique=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    

    def __repr__(self):
        return '<Rest {}>'.format(self.name,self.lat,self.lon)