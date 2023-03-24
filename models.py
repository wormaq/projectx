from peewee import *
import datetime
from flask_login import UserMixin
import re

db = PostgresqlDatabase(
    'flask_db',
    host = 'localhost',
    port = 5433,
    user = 'flask_user',
    password = 'qwe123'
)


class BaseModel(Model):
    class Meta:
        database = db


class MyUser(UserMixin, BaseModel):
    email = CharField (max_length=225, null = False, unique = True)
    name = CharField(max_length=225, null = False)
    second_name = CharField(max_length=225, null = False)
    password = CharField(max_length=225, null = False)
    age = IntegerField()
    
    def validate(self):
        if len(self.password) < 8:
            return False
        if not re.search(r'\d', self.password):
            return False
        return True
    
        

    def __repr__ (self):
        return self.email


class Post(BaseModel):
    author = ForeignKeyField (MyUser, on_delete='CASCADE')
    title = CharField (max_length=225, null = False)
    description = TextField()
    date = DateTimeField(default = datetime.datetime.now)




    def __repr__ (self):
        return self.title

db.create_tables([MyUser,Post])


