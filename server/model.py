import datetime
from flask import app
from server import db

# SQLAlchemy Database Models 
class Users(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column(db.String)
    notes = db.relationship('Note', backref='user', lazy=True)

class Note(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow, server_default=db.func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)


with app.app_context():
    db.create_all()