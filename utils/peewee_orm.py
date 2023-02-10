# -*- coding: utf-8 -*-
"""
    @Time : 2023/2/10/010 17:25
    @Author : 李子
    @Url : https://github.com/kslz
"""

from peewee import *

from utils import global_obj

global_obj._init()


def get_peewee_db(db_path):
    db = SqliteDatabase('test.db')
    global_obj.set_value("peewee_db", db)


class BaseModel(Model):
    class Meta:
        database = global_obj.get_value("peewee_db")

class Workspace(BaseModel):
    workspace_id = PrimaryKeyField()
    workspace_name = CharField(null=False)



class Course(BaseModel):
    id = PrimaryKeyField()
    title = CharField(null=False)
    period = IntegerField()
    description = CharField()

    class Meta:
        order_by = ('title',)
        db_table = 'course'


class Teacher(BaseModel):
    id = PrimaryKeyField()
    name = CharField(null=False)
    gender = BooleanField()
    address = CharField()
    course_id = ForeignKeyField(Course, to_field='id', related_name="course")

    class Meta:
        order_by = ('name',)
        db_table = 'teacher'
