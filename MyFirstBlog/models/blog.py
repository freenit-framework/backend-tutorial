import datetime

from freenit.db import db
from .user import User

from peewee import DateTimeField, ForeignKeyField, TextField, BooleanField

Model = db.Model


class Blog(Model):
    author = ForeignKeyField(User, backref='blogs')
    content = TextField()
    date = DateTimeField(default=datetime.datetime.utcnow)
    title = TextField()
