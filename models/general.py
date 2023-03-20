from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, time

db = SQLAlchemy()


class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))
    description = db.Column(db.String(512))
    admin_name = db.Column(db.String(80), nullable=False)

    def __init__(self, title, description, admin_name):
        self.title = title
        self.description = description
        self.admin_name = admin_name

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))
    description = db.Column(db.String(512))
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    blog_id = db.Column(db.Integer, db.ForeignKey(Blog.id))

    def __init__(self, title, description, date_posted):
        self.title = title
        self.description = description
        self.date_posted = date_posted

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(20), unique=True)


    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

