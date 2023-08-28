# -*- coding: utf-8 -*-
"""
    @Time : 2023/08/25 10:51
    @Author : 李子
    @Url : https://github.com/kslz
    存放PEEWEE的数据库模型
"""
from datetime import datetime

from peewee import *

db = SqliteDatabase(None)


class BaseModel(Model):
    class Meta:
        database = db


class Dataset(BaseModel):
    dataset_id = PrimaryKeyField()
    dataset_name = CharField(null=False, unique=True)
    dataset_create_time = DateTimeField(default=datetime.now().replace(microsecond=0))
    dataset_last_use_time = DateTimeField(default=datetime.now().replace(microsecond=0))
    dataset_info = TextField(null=True, help_text='数据集介绍')

    class Meta:
        table_name = 'dataset_tbl'

