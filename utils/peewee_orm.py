# -*- coding: utf-8 -*-
"""
    @Time : 2023/2/10/010 17:25
    @Author : 李子
    @Url : https://github.com/kslz
"""
from datetime import datetime

from peewee import *

db = SqliteDatabase(None)


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
    dataset_name = CharField(null=False, unique=True)
    dataset_create_time = DateTimeField(default=datetime.now().replace(microsecond=0))
    dataset_last_use_time = DateTimeField(default=datetime.now().replace(microsecond=0))
    dataset_info = TextField(null=True, help_text='数据集介绍')

    class Meta:
        table_name = 'dataset_tbl'


class Info(BaseModel):
    info_id = PrimaryKeyField()
    dataset_id = ForeignKeyField(Dataset, "dataset_id", "infos")
    info_text = CharField(null=True, )
    info_pinyin = CharField(null=True, )
    info_speaker = CharField(null=True, )
    info_raw_file_path = TextField(null=True, )
    info_start_time = IntegerField(null=True, )
    info_end_time = IntegerField(null=True, )
    info_acc_score = FloatField(null=True, )
    info_flu_score = FloatField(null=True, )
    info_int_score = FloatField(null=True, )
    info_all_score = FloatField(null=True, )
    info_file_path = TextField(null=True, )
    info_is_del = BooleanField(default=False)

    class Meta:
        table_name = 'info_tbl'


class SpkInfo(BaseModel):
    spkinfo_id = PrimaryKeyField()
    info_id = ForeignKeyField(Info, "info_id", "spkinfos")
    spkinfo_name = CharField()
    spkinfo_score = FloatField()

    class Meta:
        table_name = 'spkinfo_tbl'


def get_dataset_window_info():
    page_size = 15  # 每页15条数据
    page_number = 1  # 第1页
    dataset_id = 1  # 指定的 dataset_id

    # 下面的查询是chatGPT写的
    # 都说先进的科技乍一看和魔法无异，想来这就是了
    query = (Info
    .select(
        Info.info_id.alias('index'),
        Info.info_id,
        Info.info_text,
        fn.COALESCE(
            SpkInfo.spkinfo_name,
            Info.info_speaker).alias('speaker'),
        SQL('(CASE WHEN info_file_path = "" OR info_file_path IS NULL THEN 0 ELSE 1 END)').alias('is_separate_file'))
    .join(
        SpkInfo,
        JOIN.LEFT_OUTER,
        on=(Info.info_id == SpkInfo.info_id)
    )
    .where(
        (Info.info_is_del == 0) &
        (Info.dataset_id == dataset_id)
    )
    .group_by(
        Info.info_id
    )
    .order_by(
        Info.info_id.asc()
    ))

    total_count = query.count()  # 总共有多少条数据
    print(total_count)

    # 分页
    query = query.paginate(page_number, page_size)

    # 执行查询
    results = list(query.dicts())

    # 显示结果
    for i, result in enumerate(results, start=1):
        print(
            f"{i + (page_number - 1) * page_size} {result['info_id']} {result['info_text']} {result['speaker']} {result['is_separate_file']}")


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


def add_fake_data():
    Info.create(dataset_id=1, info_text="你好世界", info_speaker="说话人1", )
    Info.create(dataset_id=1, info_text="你好世界2", info_speaker="说话人1", )
    Info.create(dataset_id=1, info_text="你好世界3", info_speaker="说话人2", )
    Info.create(dataset_id=1, info_text="你好世界4", info_speaker="说话人2", )
    Info.create(dataset_id=1, info_text="你好世界5", info_speaker="说话人2", )
    Info.create(dataset_id=1, info_text="你好世界6", info_speaker="说话人2", )
    Info.create(dataset_id=1, info_text="你好世界7", info_speaker="说话人2", )
    Info.create(dataset_id=2, info_text="你好世界8", )
    Info.create(dataset_id=1, info_text="你好世界9", )
    Info.create(dataset_id=1, info_text="你好世界10", info_speaker="说话人1", )
    Info.create(dataset_id=1, info_text="你好世界11", info_speaker="说话人1", )
    Info.create(dataset_id=1, info_text="你好世界12", info_speaker="说话人1", )
    Info.create(dataset_id=1, info_text="你好世界13", info_speaker="说话人1", )
    Info.create(dataset_id=1, info_text="你好世界14", )
    Info.create(dataset_id=1, info_text="你好世界15", )
    Info.create(dataset_id=1, info_text="你好世界16", info_speaker="说话人1", )
    Info.create(dataset_id=1, info_text="你好世界17", )
    Info.create(dataset_id=1, info_text="你好世界18", info_speaker="说话人1", )
    Info.create(dataset_id=1, info_text="你好世界19", )
    Info.create(dataset_id=1, info_text="你好世界20", info_speaker="说话人1", )
    SpkInfo.create(info_id=2, spkinfo_name="说话人a", spkinfo_score=0.89)
    SpkInfo.create(info_id=2, spkinfo_name="说话人b", spkinfo_score=0.81)
    SpkInfo.create(info_id=2, spkinfo_name="说话人c", spkinfo_score=0.19)
    SpkInfo.create(info_id=3, spkinfo_name="说话人a", spkinfo_score=0.89)


if __name__ == "__main__":
    db.init("../workspace/db/workspace.db")
    add_fake_data()
    get_dataset_window_info()
    # init_peewee_db()
    # db1 = get_peewee_db()
    #
    # db1.connect()
    # create_all_tables(db1)
    # db.create_tables([Workspace, Dataset, Info])
    # dataset1 = Dataset.create(dataset_name="test2")
    # info1 = Info.create(info_text="你好世界", dataset_id=dataset1)

    pass
