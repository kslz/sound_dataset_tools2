# -*- coding: utf-8 -*-
"""
    @Time : 2023/08/25 10:52
    @Author : 李子
    @Url : https://github.com/kslz
    数据库相关增删改查操作
"""
from domain.repositories.models import *


def init_database(database_path):
    db.init(database_path)
    db.connect()
    db.pragma('foreign_keys', 'on')
    db.create_tables([Dataset])

