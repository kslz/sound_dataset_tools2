# -*- coding: utf-8 -*-
"""
    @Time : 2023/08/25 11:02
    @Author : 李子
    @Url : https://github.com/kslz
    文件操作
"""
import os

from domain.repositories.repositories import get_file_raw_path_by_dataset_id
from utils.logging_utils import LoggerSingleton


def del_file_by_dataset_id(dataset_id):
    print("删除文件")
    logger = LoggerSingleton.get_logger()
    query_list = get_file_raw_path_by_dataset_id(dataset_id)
    for row in query_list:
        file_path = row.info_raw_file_path
        if os.path.exists(file_path):
            try:
                os.remove(file_path)
                logger.info(f"文件 {file_path} 已被删除")
            except:
                logger.error(f"文件 {file_path} 删除失败")
