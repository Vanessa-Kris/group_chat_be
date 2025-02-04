from peewee import Model, CharField, ForeignKeyField, TextField, DateTimeField, AutoField
from datetime import datetime
from db import db

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    id = AutoField()
    random_name = CharField(unique=True)
    session_id = CharField(unique=True)

class Post(BaseModel):
    id = AutoField()
    user = ForeignKeyField(User, backref="posts", on_delete="CASCADE")
    content = TextField()
    created_at = DateTimeField(default=datetime.utcnow)

class Reply(BaseModel):
    id = AutoField()
    post = ForeignKeyField(Post, backref="replies", on_delete="CASCADE")
    user = ForeignKeyField(User, backref="replies", on_delete="CASCADE")
    content = TextField()
    created_at = DateTimeField(default=datetime.utcnow)
