__author__ = 'arthur'

import os
from peewee import *

# pyDir = os.path.abspath(os.path.dirname(__file__))
# database = SqliteDatabase(pyDir.join('db/warehouse.sqlite'))
database = SqliteDatabase('db/warehouse.sqlite')

class BaseModel(Model):
    class Meta:
        database = database

    def javascriptify(self):
        return self.__dict__['_data']


class Cargo(BaseModel):
    id = PrimaryKeyField(primary_key=True, unique=True)
    code = TextField(unique=True)
    name = TextField()
    standard = TextField()
    category = TextField()
    unit = TextField()
    in_price = DoubleField()
    ex_price = DoubleField()
    barcode = TextField()
    factory = TextField()
    note = TextField()
    state = IntegerField()
