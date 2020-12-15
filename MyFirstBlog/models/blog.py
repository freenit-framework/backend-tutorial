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
    slug = TextField()
    published = BooleanField()
    image = TextField()

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = self.title.lower().replace(" ","-")
        super(Blog, self).save(*args, **kwargs)
