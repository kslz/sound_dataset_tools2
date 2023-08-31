# -*- coding: utf-8 -*-
"""
    @Time : 2023/08/25 10:52
    @Author : 李子
    @Url : https://github.com/kslz
    数据库相关增删改查操作
"""
from domain.repositories.models import *


# 增
def add_dataset(dataset_name, datset_info):
    dataset = Dataset(dataset_name=dataset_name, dataset_info=datset_info)
    dataset.save()


# 删

def del_dataset_by_id(dataset_id):
    dataset = Dataset.get(Dataset.dataset_id == dataset_id)
    dataset.delete_instance()


# 改

# 查
def get_file_raw_path_by_dataset_id(dataset_id):
    # todo 获取要删除的文件，需要等Info模型写完
    # query = Info.select(Info.info_raw_file_path).distinct().where(Info.dataset_id == dataset_id)
    return []

    pass

def get_dataset_info():
    """
    返回所有数据集数据
    """

    return Dataset.select()


def get_dataset_info_by_id(dataset_id):
    return Dataset.get_by_id(dataset_id)


# 其他

def init_database(database_path):
    """
    初始化PEEWEE数据库连接

    """
    db.init(database_path)
    db.connect()
    db.pragma('foreign_keys', 'on')
    db.create_tables([Dataset])
