# -*- coding: utf-8 -*-
"""
    @Time : 2023/2/10/010 17:25
    @Author : 李子
    @Url : https://github.com/kslz
"""
from datetime import datetime
from time import sleep

from peewee import *

global db


def get_peewee_db(db_path="test.db"):
    global db
    db = SqliteDatabase(db_path)


get_peewee_db()


class BaseModel(Model):
    class Meta:
        database = db


class Workspace(BaseModel):
    workspace_id = PrimaryKeyField()
    workspace_name = CharField(null=False)
    workspace_create_time = DateTimeField(default=datetime.now)
    workspace_last_use_time = DateTimeField(default=datetime.now)
    workspace_info = CharField(null=True, help_text='工作区介绍，不要超过255字')

    class Meta:
        table_name = 'workspace_tbl'


class Dataset(BaseModel):
    dataset_id = PrimaryKeyField()
    dataset_name = CharField(null=False)
    dataset_create_time = DateTimeField(default=datetime.now)
    dataset_last_use_time = DateTimeField(default=datetime.now)
    dataset_info = TextField(null=True, help_text='数据集介绍')

    class Meta:
        table_name = 'dataset_tbl'


class Info(BaseModel):
    info_id = PrimaryKeyField()
    dataset_id = ForeignKeyField(Dataset, "dataset_id", "infos")
    info_text = CharField(null=True, )
    info_pinyin = CharField(null=True, )
    info_speaker = CharField(null=True, )
    info_file_path = TextField(null=True, )
    info_start_time = IntegerField(null=True, )
    info_end_time = IntegerField(null=True, )
    info_acc_score = FloatField(null=True, )
    info_flu_score = FloatField(null=True, )
    info_int_score = FloatField(null=True, )
    info_all_score = FloatField(null=True, )
    info_is_del = BooleanField(default=False)

    class Meta:
        table_name = 'info_tbl'


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


if __name__ == "__main__":
    db.connect()
    # db.create_tables([Workspace, Dataset, Info])
    dataset1 = Dataset.create(dataset_name="test2")
    info1 = Info.create(info_text="你好世界",dataset_id=dataset1)
