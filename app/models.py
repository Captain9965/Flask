from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from app import db, login
from flask_login import UserMixin

@login.user_loader  #The user loader is registered with Flask-Login with the @login.user_loader decorator. 
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin, db.Model):   # inherits from db.Model, a base class for all models from Flask-SQLAlchemy.
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):     #tells python  how to print objects of this class, which is going to be useful for debugging.   
        return '<User {}>'.format(self.username)    
    def set_password(self, password):   # generate password hash
        self.password_hash = generate_password_hash(password)

    def check_password(self, password): #verify password
        return check_password_hash(self.password_hash, password)
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow) #When you pass a function as a default, SQLAlchemy will set the field to the value of calling that function 
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))   #references an id value from the users table.

    def __repr__(self):
        return '<Post {}>'.format(self.body)