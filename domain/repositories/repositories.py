# -*- coding: utf-8 -*-
"""
    @Time : 2023/08/25 10:52
    @Author : 李子
    @Url : https://github.com/kslz
    数据库相关增删改查操作
"""
from domain.repositories.models import *
from utils.tools import check_pagenumber_is_out


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


def get_dataset_view_window_info(dataset_id=1, page_size=15, page_number=1, show_delete=True):
    subquery = (
        Info
        .select(
            Info.info_id,
            fn.row_number().over(order_by=[Info.info_id]).alias('row_number')
        )
        .where(
            (Info.dataset_id == dataset_id) &
            (Info.info_is_del == 0) if not show_delete else True
        )
        .order_by(Info.info_id)
        .alias('subquery')
    )

    query = (Info
    .select(
        subquery.c.row_number.alias('index'),
        Info.info_id,
        Info.info_text,
        Info.info_speaker,
        # Info.info_shibie_speaker,
        Info.info_start_time,
        Info.info_end_time,
        Info.info_raw_file_path,
        Info.info_is_del,
    )
    .join(subquery, on=(Info.info_id == subquery.c.info_id))
    .where(
        (Info.dataset_id == dataset_id)
    )
    .order_by(
        Info.info_id.asc()
    ))
    total_count = query.count()
    _, page_number = check_pagenumber_is_out(total_count, page_number, page_size)
    query = query.paginate(page_number, page_size)

    results = list(query.dicts())
    return total_count, results


# 其他

def init_database(database_path):
    """
    初始化PEEWEE数据库连接

    """
    db.init(database_path)
    db.connect()
    db.pragma('foreign_keys', 'on')
    db.create_tables([Dataset, Info])
