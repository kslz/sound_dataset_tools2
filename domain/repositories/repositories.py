# -*- coding: utf-8 -*-
"""
    @Time : 2023/08/25 10:52
    @Author : 李子
    @Url : https://github.com/kslz
    数据库相关增删改查操作
"""
from domain.repositories.models import *

def get_dataset_info():
    """
    返回所有数据集数据
    """

    return Dataset.select()



def init_database(database_path):
    """
    初始化PEEWEE数据库连接

    """
    db.init(database_path)
    db.connect()
    db.pragma('foreign_keys', 'on')
    db.create_tables([Dataset])

