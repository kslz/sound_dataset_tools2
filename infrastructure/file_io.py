# -*- coding: utf-8 -*-
"""
    @Time : 2023/08/25 11:02
    @Author : 李子
    @Url : https://github.com/kslz
    文件操作
"""
import os
from datetime import datetime

import ffmpeg

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


def copy_file_to_workspace(raw_path, to_path):
    file_name = os.path.basename(raw_path)
    now = datetime.now()
    formatted_time = now.strftime("%Y-%m-%d_%H-%M-%S")

    file_name_new = os.path.splitext(file_name)[0] + "_" + formatted_time + ".flac"
    new_path = os.path.join(to_path, file_name_new)

    (
        ffmpeg
        .input(raw_path)
        .output(new_path, codec="flac", compression_level=5, sample_fmt='s16', bits_per_raw_sample=16)
        .run(quiet=True)
    )

    # shutil.copyfile(raw_path, new_path)
    return new_path
