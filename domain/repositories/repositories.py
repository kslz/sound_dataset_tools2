# -*- coding: utf-8 -*-
"""
    @Time : 2023/08/25 10:52
    @Author : 李子
    @Url : https://github.com/kslz
    数据库相关增删改查操作
"""
from domain.repositories.models import *
from utils.tools import check_pagenumber_is_out


class SearchField:
    """
    用于提前写好可能需要查询的字段，我猜在一个地方写比在所有地方写强一点
    """

    def __init__(self):
        self.field_dict = {}
        self.field_dict["info_id"] = {"name": "数据ID", "field": Info.info_id}
        self.field_dict["dataset_id"] = {"name": "数据集ID", "field": Info.dataset_id}
        self.field_dict["info_text"] = {"name": "数据文本", "field": Info.info_text}
        self.field_dict["info_pinyin"] = {"name": "数据拼音", "field": Info.info_pinyin}
        self.field_dict["info_speaker"] = {"name": "发音人", "field": Info.info_speaker}
        self.field_dict["info_raw_file_path"] = {"name": "音频文件位置", "field": Info.info_raw_file_path}
        self.field_dict["info_start_time"] = {"name": "音频开始时间", "field": Info.info_start_time}
        self.field_dict["info_end_time"] = {"name": "音频结束时间", "field": Info.info_end_time}
        self.field_dict["info_is_del"] = {"name": "是否已删除", "field": Info.info_is_del}

        # self.field_dict[""] = {"name": "", "field": }
        pass

    def get_field_list(self, k_list=None):
        if k_list is None:
            k_list = []

        field_list = []
        if not k_list:
            for v in self.field_dict.values():
                field_list.append(v['field'])
        else:
            for k in k_list:
                field_list.append(self.field_dict[k]['field'])
        return field_list

class SearchInfo:

    def __init__(self, field_list):
        self.query = Info.select(*field_list)

    def search_dataset_id(self,dataset_id):
        self.query = self.query.where(Info.dataset_id == dataset_id)

    def do_join(self, args):
        self.query = self.query.join(*args)

    def do_where(self, args):
        self.query = self.query.where(*args)






# 增
def add_dataset(dataset_name, datset_info):
    dataset = Dataset(dataset_name=dataset_name, dataset_info=datset_info)
    dataset.save()


def insert_info_many(data_list, batch_size=1000):
    for i in range(0, len(data_list), batch_size):
        with db.atomic():
            Info.insert_many(data_list[i:i + batch_size]).execute()


# 删

def del_dataset_by_id(dataset_id):
    dataset = Dataset.get(Dataset.dataset_id == dataset_id)
    dataset.delete_instance()


def del_info_by_raw_file_path(file_path):
    query = Info.delete().where(Info.info_raw_file_path == file_path)
    query.execute()


# 改
def update_info(text, start_time, end_time, info_id):
    updated_row = Info.update(info_text=text, info_start_time=start_time, info_end_time=end_time) \
        .where(Info.info_id == info_id).execute()


def update_is_delete(info_id, new_is_del):
    Info.update(info_is_del=new_is_del).where(Info.info_id == info_id).execute()


# 查
def get_file_raw_path_by_dataset_id(dataset_id):
    query = Info.select(Info.info_raw_file_path).distinct().where(Info.dataset_id == dataset_id)
    return query


def get_dataset_info():
    """
    返回所有数据集数据
    """

    return Dataset.select()


def get_dataset_info_by_id(dataset_id):
    return Dataset.get_by_id(dataset_id)


def get_info_by_id(info_id):
    return Info.get_by_id(info_id)


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
