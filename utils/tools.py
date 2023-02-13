# -*- coding: utf-8 -*-
"""
    @Time : 2023/1/29/029 11:19
    @Author : 李子
    @Url : https://github.com/kslz
"""
import configparser
import os

from utils import global_obj
from utils.peewee_orm import *
from utils.sqlitedb import MyDB


def file_r(path):
    """
    用于从文件中读取

    :param path:
    :return:
    """
    with open(path, 'r', encoding="UTF-8") as f:
        return f.read()


def file_w(path, text, mode, encoding="UTF-8"):
    """
    用于向文件中写入

    :param path: 文件路径
    :param text: 要写入的数据
    :param mode: 写入模式 a为追加 w为覆写
    :param encoding: 文档编码格式

    """
    with open(path, mode, encoding=encoding) as f:
        f.write(text)


def read_ini_config(ini_path="conf/config.ini"):
    config = ConfigParserWithFile()
    config.read(ini_path)
    global_obj.set_value("config", config)
    print(config["program_configs"]["default_workspace"])


def update_ini_config(config, config_path="conf/config.ini"):
    with open(config_path, "w+") as f:
        config.write(f)


def init_program():
    """
    初始化程序

    """
    read_ini_config()


def init_database(database_path):
    db.init(database_path)
    db.connect()
    db.create_tables([Workspace, Dataset, Info])
    global_obj.set_value("peewee_db", db)


def inti_workspace(workspace_path):
    """
    初始化工作区
    1、新建目录：workspace_path、workspace_path/db
    2、连接数据库

    """
    os.makedirs(workspace_path, exist_ok=True)
    os.makedirs(os.path.join(workspace_path, "db"), exist_ok=True)
    # mydb = MyDB(os.path.join(workspace_path, "db/workspace.db"))
    # global_obj.set_value("mydb", mydb)

    init_database(os.path.join(workspace_path, "db/workspace.db"))
    peewee_db: SqliteDatabase = global_obj.get_value("peewee_db")
    table_names = peewee_db.get_tables()
    print(table_names)


class ConfigParserWithFile(configparser.ConfigParser):
    file = None

    def read(self, filenames, encoding=None):
        self.file = filenames
        return super().read(filenames, encoding)

    def refresh_config(self, encoding=None):
        return super().read(self.file, encoding)


if __name__ == '__main__':
    init_program()
