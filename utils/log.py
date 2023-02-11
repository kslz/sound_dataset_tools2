# -*- coding: utf-8 -*-
"""
    @Time : 2023/2/1/001 14:17
    @Author : 李子
    @Url : https://github.com/kslz
"""

import logging
import os


def creatlogger(logname):
    # 1、创建一个logger
    logger = logging.getLogger(logname)  # 创建 logger
    logger.setLevel(logging.DEBUG)  # 写入内容的严重级别

    # Handler方法有很多下面主要介绍两种：StreamHandler 和 FileHandler
    # 2、创建一个handler，用于写入日志文件
    os.makedirs('logs', exist_ok=True)
    fh = logging.FileHandler('logs/program.log', encoding="utf-8")  # 将日志写入到logs/program.log文件
    fh.setLevel(logging.DEBUG)  # 并且需要指定写入的内容严重级别
    # 再创建一个handler，用于输出到控制台
    ch = logging.StreamHandler()  # 将日志写入控制台
    ch.setLevel(logging.DEBUG)  # 并且需要指定写入的内容严重级别

    # 3、定义handler的输出格式（formatter）
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # 4、给handler添加formatter
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    # 5、给logger添加handler
    logger.addHandler(fh)
    logger.addHandler(ch)

    return logger

if __name__ == '__main__':
    logger = creatlogger("testlog")
    # 6、进行日志输出
    logger.info("这是一条INFO级别的信息。")
    logger.debug('debug message')
    logger.info('info message')
    logger.warning('warn message')
    logger.error('error message')
    logger.critical('critical message')
