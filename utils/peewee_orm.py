# -*- coding: utf-8 -*-
"""
    @Time : 2023/2/10/010 17:25
    @Author : 李子
    @Url : https://github.com/kslz
"""
from datetime import datetime
from typing import Optional

import peewee
from peewee import *

from utils.tool_str import *

db = SqliteDatabase(None)


class DbStr():
    BiaoBei = "标贝"
    XunFei = "讯飞"
    ShengWen = "声纹识别"
    PingCe = "语音评测"


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
    dataset_id = ForeignKeyField(Dataset, "dataset_id", "infos", on_delete='CASCADE')
    info_text = CharField(null=True, )
    info_pinyin = CharField(null=True, )
    info_speaker = CharField(null=True, )
    info_shibie_speaker = CharField(null=True, )
    info_shibie_score = FloatField(null=True, )
    info_raw_file_path = TextField(null=True, )
    info_start_time = IntegerField(null=True, )
    info_end_time = IntegerField(null=True, )
    info_file_path = TextField(null=True, )
    info_mfa = TextField(null=True, )
    info_is_del = BooleanField(default=False)

    class Meta:
        table_name = 'info_tbl'


# class SpkInfo(BaseModel):
#     spkinfo_id = PrimaryKeyField()
#     info_id = ForeignKeyField(Info, "info_id", "spkinfos", on_delete='CASCADE')
#     spkinfo_name = CharField()
#     spkinfo_score = FloatField()
#
#     class Meta:
#         table_name = 'spkinfo_tbl'


class AuthorizationInfo(BaseModel):
    authorizationinfo_id = PrimaryKeyField()
    authorizationinfo_name = CharField(null=False)
    authorizationinfo_APPID = CharField(null=False)
    authorizationinfo_APISecret = CharField(null=False)
    authorizationinfo_APIKey = CharField(null=False)
    authorizationinfo_company = CharField(null=False)
    authorizationinfo_app = CharField(null=False)
    authorizationinfo_token = TextField(null=True)

    class Meta:
        table_name = 'authorizationinfo_tbl'


class BiaoBeiPingCeInfo(BaseModel):
    biaobeipingce_id = PrimaryKeyField()
    info_id = ForeignKeyField(Info, "info_id", on_delete='CASCADE', unique=True)
    biaobeipingce_acc_score = IntegerField(null=True, )  # 句子准确度得分
    biaobeipingce_flu_score = IntegerField(null=True, )  # 句子流利度得分
    biaobeipingce_int_score = IntegerField(null=True, )  # 句子完整度得分
    biaobeipingce_all_score = IntegerField(null=True, )  # 总得分
    biaobeipingce_all_text = TextField(null=True)  # 完整返回数据

    class Meta:
        table_name = 'biaobeipingce_tbl'


def get_authorizationinfo_by_id(authorizationinfo_id):
    query = AuthorizationInfo.select().where(AuthorizationInfo.authorizationinfo_id == authorizationinfo_id)
    results = query.execute()
    return results


def get_pingce_info2(dataset_id):
    query = (BiaoBeiPingCeInfo
             .select(Info.info_id, BiaoBeiPingCeInfo.biaobeipingce_all_score)
             .join(Info)
             .where(Info.dataset_id == dataset_id))

    results = query.execute()
    for result in results:
        info_id = result.info_id
        biaobeipingce_all_score = result.biaobeipingce_all_score
        print(f"Info ID: {info_id}, Score: {biaobeipingce_all_score}")


def get_pingce_info(dataset_id, is_skip_done):
    query = (Info
             .select(Info, BiaoBeiPingCeInfo.biaobeipingce_all_score)
             .join(BiaoBeiPingCeInfo, JOIN.LEFT_OUTER)
             .where(
                Info.dataset_id == dataset_id,
                Info.info_is_del == 0,
             )
             )
    # for result in results:
    #     info_id = result.info_id
    #     biaobeipingce_all_score = result.biaobeipingceinfo.biaobeipingce_all_score if hasattr(result,
    #                                                                                           'biaobeipingceinfo') else None
    #     print(f"Info ID: {info_id}, Score: {biaobeipingce_all_score}")
    # 注意：在左外连接中，如果右表中没有与左表关联的数据，则在查询结果中对应的列会显示为 NULL。这在原生 SQL 查询中是可以直接访问和处理的。
    # 然而，在使用 Peewee ORM 进行查询时，它会尝试将查询结果映射到模型对象上，但如果某个字段在查询结果中为 NULL，Peewee 默认情况下不会为模型对象创建对应的属性。因此，在代码中直接访问不存在的属性时会引发 AttributeError。
    # 为了解决这个问题，我们可以使用 hasattr() 函数进行存在性检查，如之前提供的代码示例所示。这样，即使某些记录在右表中没有对应的数据，我们可以避免引发异常并正确处理这种情况。

    if is_skip_done:
        query = query.where(BiaoBeiPingCeInfo.biaobeipingce_all_score.is_null())

    results = query.execute()

    return results

    pass


def get_authorizationinfo(company: Optional[str] = None, app: Optional[str] = None):
    query = AuthorizationInfo.select()

    if company is not None:
        query = query.where(AuthorizationInfo.authorizationinfo_company == company)

    if app is not None:
        query = query.where(AuthorizationInfo.authorizationinfo_app == app)

    results = query.execute()

    return list(results)


def get_dataset_window_info(dataset_id=1, page_size=15, page_number=1):
    subquery = (
        Info
        .select(
            Info.info_id,
            fn.row_number().over(order_by=[Info.info_id]).alias('row_number')
        )
        .where(
            # (Info.info_is_del == 0) &
            (Info.dataset_id == dataset_id)
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
        Info.info_shibie_speaker,
        Info.info_start_time,
        Info.info_end_time,
        Info.info_raw_file_path,
        Info.info_is_del,
    )
    .join(subquery, on=(Info.info_id == subquery.c.info_id))
    .where(
        # (Info.info_is_del == 0) &
        (Info.dataset_id == dataset_id)
    )
    .order_by(
        Info.info_id.asc()
    ))
    total_count = query.count()
    query = query.paginate(page_number, page_size)
    # todo 待优化 目前搜索范围外的数据时会出现空白页

    # 执行查询
    # 我发现这里的查询好像会查询很多次数据库，不过也还好吧，应该不会有人存几百万条数据进去
    results = list(query.dicts())
    return total_count, results


# def get_dataset_window_info(dataset_id=1, page_size=15, page_number=1):
#     # 下面的查询是chatGPT写的
#     # 都说先进的科技乍一看和魔法无异，想来这就是了
#     # 整复杂了 重来
#     query = (Info
#     .select(
#         Info.info_id.alias('index'),
#         Info.info_id,
#         Info.info_text,
#         fn.COALESCE(
#             SpkInfo.spkinfo_name,
#             Info.info_speaker).alias('speaker'),
#         # SQL('(CASE WHEN info_file_path = "" OR info_file_path IS NULL THEN 0 ELSE 1 END)').alias('is_separate_file')
#     )
#     .join(
#         SpkInfo,
#         JOIN.LEFT_OUTER,
#         on=(Info.info_id == SpkInfo.info_id)
#     )
#     .where(
#         (Info.info_is_del == 0) &
#         (Info.dataset_id == dataset_id)
#     )
#     .group_by(
#         Info.info_id
#     )
#     .order_by(
#         Info.info_id.asc()
#     ))
#
#     total_count = query.count()
#     # print(total_count)
#
#     # 分页
#     query = query.paginate(page_number, page_size)
#     # todo 待优化 目前搜索范围外的数据时会出现空白页
#
#     # 执行查询
#     # 我发现这里的查询好像会查询很多次数据库，不过也还好吧，应该不会有人存几百万条数据进去
#     results = list(query.dicts())
#     return total_count, results


def get_speakers(dataset_id):
    """
    获取所有speaker值

    """
    query = (Info
    .select(Info.info_speaker, Info.info_shibie_speaker)
    .where(
        (Info.info_is_del == 0) &
        (Info.dataset_id == dataset_id)
    ))
    result_list = []
    for row in query.dicts():
        if row["info_shibie_speaker"] is not None:
            row_result = (row["info_shibie_speaker"], "shibie_spk")
        else:
            row_result = (row["info_speaker"], "spk")
        if result_list.count(row_result) == 0:
            result_list.append(row_result)
    return result_list


def get_file_raw_path_by_dataset_id(dataset_id):
    query = Info.select(Info.info_raw_file_path).distinct().where(Info.dataset_id == dataset_id)
    return list(query)


def get_output_info(dataset_id, spk_info, pingce_dict):
    query = (Info
    .select(
        Info.info_id,
        Info.info_text,
        Info.info_raw_file_path,
        Info.info_start_time,
        Info.info_end_time,
    )
    # .join(Dataset, on=(Dataset.dataset_id == Info.dataset_id))
    .where(
        (Info.info_is_del == 0) &
        (Info.dataset_id == dataset_id)
    )
    .order_by(
        Info.info_id.asc()
    ))
    if spk_info[1] == "shibie_spk":
        query = query.where(Info.info_shibie_speaker == spk_info[0])
    else:
        query = query.where(Info.info_speaker == spk_info[0])

    if len(pingce_dict) != 0:
        # print(pingce_dict)
        if pingce_dict["pingce"] == ToolStr.biaobei:
            query = query.join(BiaoBeiPingCeInfo, on=(Info.info_id == BiaoBeiPingCeInfo.info_id))\
                .where(
                    BiaoBeiPingCeInfo.biaobeipingce_acc_score >= pingce_dict["acc"],
                    BiaoBeiPingCeInfo.biaobeipingce_flu_score >= pingce_dict["flu"],
                    BiaoBeiPingCeInfo.biaobeipingce_int_score >= pingce_dict["int"],
                    BiaoBeiPingCeInfo.biaobeipingce_all_score >= pingce_dict["all"]
                )

    result = list(query.dicts())
    # print(result)
    return result


def update_info(text, start_time, end_time, info_id):
    updated_row = Info.update(info_text=text, info_start_time=start_time, info_end_time=end_time) \
        .where(Info.info_id == info_id).execute()
    print(updated_row)


def create_or_update_biaobeipingceinfo(info_id, acc_score, flu_score, int_score, all_score, all_text):
    try:
        BiaoBeiPingCeInfo.create(info_id=info_id,
                                 biaobeipingce_acc_score=acc_score,
                                 biaobeipingce_flu_score=flu_score,
                                 biaobeipingce_int_score=int_score,
                                 biaobeipingce_all_score=all_score,
                                 biaobeipingce_all_text=all_text)
    except peewee.IntegrityError:
        BiaoBeiPingCeInfo.update(biaobeipingce_acc_score=acc_score,
                                 biaobeipingce_flu_score=flu_score,
                                 biaobeipingce_int_score=int_score,
                                 biaobeipingce_all_score=all_score,
                                 biaobeipingce_all_text=all_text).where(BiaoBeiPingCeInfo.info_id == info_id).execute()

    pass


def insert_info_many(data_list, batch_size=1000):
    for i in range(0, len(data_list), batch_size):
        with db.atomic():
            Info.insert_many(data_list[i:i + batch_size]).execute()


def del_info_by_raw_file_path(file_path):
    query = Info.delete().where(Info.info_raw_file_path == file_path)
    query.execute()


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
    # SpkInfo.create(info_id=2, spkinfo_name="说话人a", spkinfo_score=0.89)
    # SpkInfo.create(info_id=2, spkinfo_name="说话人b", spkinfo_score=0.81)
    # SpkInfo.create(info_id=2, spkinfo_name="说话人c", spkinfo_score=0.19)
    # SpkInfo.create(info_id=3, spkinfo_name="说话人a", spkinfo_score=0.89)


if __name__ == "__main__":
    db.init("../workspace/db/workspace.db")
    try:
        BiaoBeiPingCeInfo.create(info_id=312, biaobeipingce_all_score=90)
    except peewee.IntegrityError:
        BiaoBeiPingCeInfo.update(biaobeipingce_all_score=80).where(BiaoBeiPingCeInfo.info_id == 312).execute()

    # add_fake_data()
    # get_dataset_window_info()
    # init_peewee_db()
    # db1 = get_peewee_db()
    #
    # db1.connect()
    # create_all_tables(db1)
    # db.create_tables([Workspace, Dataset, Info])
    # dataset1 = Dataset.create(dataset_name="test2")
    # info1 = Info.create(info_text="你好世界", dataset_id=dataset1)

    pass
