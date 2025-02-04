from peewee import SqliteDatabase

db = SqliteDatabase("forum.db")

def init_db():
    from models import User, Post, Reply
    db.connect()
    db.create_tables([User, Post, Reply], safe=True)
    db.close()