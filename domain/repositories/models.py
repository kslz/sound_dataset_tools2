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

class Info(BaseModel):
    info_id = PrimaryKeyField()
    dataset_id = ForeignKeyField(Dataset, "dataset_id", "infos", on_delete='CASCADE')
    info_text = CharField(null=True, )
    info_pinyin = CharField(null=True, )
    info_speaker = CharField(null=True, )
    info_raw_file_path = TextField(null=True, )
    info_start_time = IntegerField(null=True, )
    info_end_time = IntegerField(null=True, )
    info_is_del = BooleanField(default=False)

    class Meta:
        table_name = 'info_tbl'

