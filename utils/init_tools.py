# -*- coding: utf-8 -*-
"""
    @Time : 2023/8/27 1:10
    @Author : 李子
    @Url : https://github.com/kslz
    初始化程序工具
"""
import configparser
import os


class ToolWorkspace:
    def __init__(self, workspace_path):
        """
        定义文件路径

        :param workspace_path:
        """
        workspace_path = os.path.abspath(workspace_path)
        self.db_folder_path = os.path.join(workspace_path, "db")
        self.db_file_path = os.path.join(self.db_folder_path, "workspace.db")
        self.output_path = os.path.join(workspace_path, "output")
        self.file_path = os.path.join(workspace_path, "file")
        self.input_file_path = os.path.join(self.file_path, "input")
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
            return True
        except OSError as e:
            print("工作区创建失败\n", e)
            return False  # 创建失败时返回False

    pass


class ConfigParserWithFile(configparser.ConfigParser):
    file = None

    def read(self, filenames, encoding=None):
        self.file = filenames
        return super().read(filenames, encoding)

    def refresh_config(self, encoding=None):
        return super().read(self.file, encoding)


def read_ini_config(ini_path="config/settings.ini"):
    info = """[program_configs]
default_workspace = .\workspace

"""
    if not os.path.exists(ini_path):
        # 如果不存在，则创建一个默认配置文件
        os.makedirs(os.path.dirname(ini_path), exist_ok=True)

        with open(ini_path, 'w') as f:
            f.write(info)
    config = ConfigParserWithFile()
    config.read(ini_path)
    try:
        config["program_configs"]["default_workspace"]
    except:
        with open(ini_path, 'w') as f:
            f.write(info)
        config.refresh_config()
    return config

