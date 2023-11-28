# -*- coding: utf-8 -*-
"""
    @Time : 2023/8/27 1:10
    @Author : 李子
    @Url : https://github.com/kslz
    初始化程序工具
"""
import configparser
import os

from domain.repositories.repositories import *
from utils.logging_utils import init_logger, LoggerSingleton


def singleton(cls):
    instances = {}

    def wrapper(workspace_path=None):
        if cls not in instances:
            instances[cls] = cls(workspace_path)
        return instances[cls]

    return wrapper


@singleton
class ToolWorkspace:

    def __init__(self, workspace_path=None):
        """
        定义文件路径

        :param workspace_path:
        """
        workspace_path = os.path.abspath(workspace_path)
        self.workspace_path = workspace_path
        self.db_folder_path = os.path.join(workspace_path, "db")
        self.db_file_path = os.path.join(self.db_folder_path, "workspace.db")
        self.output_path = os.path.join(workspace_path, "output")
        self.file_path = os.path.join(workspace_path, "file")
        self.input_file_path = os.path.join(self.file_path, "input")
        self.log_path = os.path.join(workspace_path, "log")
        self.log_file_path = os.path.join(self.log_path, "tool.log")
        pass

    def check_and_create_files(self):
        """
        验证并创建工作区文件结构

        :return:
        """
        try:
            os.makedirs(self.db_folder_path, exist_ok=True)
            os.makedirs(self.output_path, exist_ok=True)
            os.makedirs(self.file_path, exist_ok=True)
            os.makedirs(self.input_file_path, exist_ok=True)
            os.makedirs(self.log_path, exist_ok=True)
            self.init_logger()
            self.init_database()

        except OSError as e:
            print("工作区创建失败\n", e)
            return False  # 创建失败时返回False
        except OperationalError as e:
            print("数据库初始化失败\n", e)
        except Exception as e:
            print("未知异常\n", e)
        else:
            self.logger.debug("日志模块启动成功")
            self.logger.debug("数据库连接成功")
            self.logger.info("工作区准备完毕")
            return True

    def init_database(self):
        """
        初始化数据库和PEEWEE
        """

        init_database(self.db_file_path)
        pass

    def init_logger(self):
        """
        初始化日志模块
        """
        self.logger = LoggerSingleton.get_logger(self.log_file_path)
        pass


@singleton
class ConfigParserWithFile(configparser.ConfigParser):
    file = None

    def read(self, filenames, encoding="UTF-8"):
        self.file = filenames
        return super().read(filenames, encoding)

    def refresh_config(self, encoding="UTF-8"):
        return super().read(self.file, encoding)

    def write_to_file(self):
        with open(self.file, 'w', encoding="UTF-8") as configfile:
            self.write(configfile)


def read_ini_config(ini_path="config/settings.ini"):
    """
    初始化配置文件，如果配置文件中没有对应字段则自动添加该字段，如果已有则不会进行修改

    :param ini_path:
    :return:
    """

    # 配置文件默认字段值
    config_dict = {
        "default_workspace": os.path.join(".", "workspace"),
        "default_pagesize": 15,
        "default_colums": "all"
    }

    config = ConfigParserWithFile()
    config.read(ini_path)

    for k in config_dict.keys():
        if config.has_option("program_configs", k):
            config_dict[k] = config.get("program_configs", k)

    if config_dict["default_colums"] == "all":
        sf = SearchField()
        config_dict["default_colums"] = ",".join(sf.get_all_keys())

    config['program_configs'] = config_dict

    config.write_to_file()
    return config
