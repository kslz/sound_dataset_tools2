# -*- coding: utf-8 -*-
"""
    @Time : 2023/1/29/029 11:19
    @Author : 李子
    @Url : https://github.com/kslz
"""
import configparser
import os
import string
import textwrap

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


def huanhang(text: str, num=30):
    """
    长文本换行

    """
    # 这么简单的需求前前后后墨迹了一个小时才解决，难顶
    if text == None:
        return None
    # 定义字符宽度
    WIDTH = num
    CHINESE_WIDTH = 2
    ENGLISH_WIDTH = 1

    # 定义中英文标点
    punctuation = string.punctuation + '，。！？、；：‘’“”《》【】（）'

    # 将字符串分割成多行
    lines = []
    for line in text.split('\n'):
        # 每行的可用宽度
        line_width = 0
        for c in line:
            if c in punctuation:
                line_width += CHINESE_WIDTH
            elif c.isascii():
                line_width += ENGLISH_WIDTH
            else:
                line_width += CHINESE_WIDTH
        if line_width <= WIDTH:
            lines.append(line)
            continue
        line_now = ""
        width_now = 0
        for i in range(len(line)):
            line_now += line[i]
            if line[i] in punctuation:
                width_now += CHINESE_WIDTH
            elif line[i].isascii():
                width_now += ENGLISH_WIDTH
            else:
                width_now += CHINESE_WIDTH

            if i < len(line) - 1:
                if width_now == WIDTH - 1:
                    if line[i + 1].isascii():
                        continue
                    else:
                        # line_now += "\n"
                        lines.append(line_now)
                        line_now = ""
                        width_now = 0
            if width_now == WIDTH:
                # line_now += "\n"
                lines.append(line_now)
                line_now = ""
                width_now = 0
        lines.append(line_now)

    formatted_text = '\n'.join(lines)
    return formatted_text


def read_ini_config(ini_path="conf/config.ini"):
    config = ConfigParserWithFile()
    config.read(ini_path)
    global_obj.set_value("config", config)


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
