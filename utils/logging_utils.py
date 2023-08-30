# -*- coding: utf-8 -*-
"""
    @Time : 2023/08/25 11:07
    @Author : 李子
    @Url : https://github.com/kslz
    日志记录工具
"""

import logging


class LoggerSingleton:
    _instance = None

    def __new__(cls, log_path=None):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.logger = init_logger(log_path)
        return cls._instance

    @staticmethod
    def get_logger(log_path=None):
        return LoggerSingleton(log_path)._instance.logger


def init_logger(log_path):
    # 创建一个日志记录器
    logger = logging.getLogger("tool")
    # 设置日志级别
    logger.setLevel(logging.DEBUG)

    # 创建一个文件处理器，将日志写入到文件
    file_handler = logging.FileHandler(log_path)
    # 创建一个格式化器
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    # 将格式化器添加到处理器
    file_handler.setFormatter(formatter)
    # 将处理器添加到日志记录器
    logger.addHandler(file_handler)

    # 创建一个控制台处理器，将日志消息打印到控制台
    console_handler = logging.StreamHandler()
    # 设置控制台处理器的日志级别
    console_handler.setLevel(logging.INFO)
    # 将格式化器添加到控制台处理器
    console_handler.setFormatter(formatter)
    # 将控制台处理器添加到日志记录器
    logger.addHandler(console_handler)

    return logger
