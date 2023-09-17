# -*- coding: utf-8 -*-
"""
    @Time : 2023/9/17 23:23
    @Author : 李子
    @Url : https://github.com/kslz
"""
import pysrt

from domain.repositories.repositories import insert_info_many
from domain.service.optimization_service_protocol import cut_wav_better


def add_info_by_file_wav_srt_better(dataset_id, wav_path, srt_path, speaker, sound, is_merge=True):
    """
    通过音频文件和srt字幕文件导入数据
    :param dataset_id:
    :param wav_path:
    :param srt_path:
    :param speaker:
    :param sound:
    :param is_merge:
    :return:
    """

    subs = pysrt.open(srt_path)
    # todo: 优化逻辑
    # if is_merge:
    #     subs = merge_srt(subs)
    data_list = []
    for line in subs:
        line: pysrt.srtitem.SubRipItem
        start = line.start.ordinal
        end = line.end.ordinal
        start, end = cut_wav_better(sound, start, end)
        line_data = {}
        line_data["dataset_id"] = dataset_id
        line_data["info_text"] = line.text
        line_data["info_speaker"] = speaker
        line_data["info_raw_file_path"] = wav_path
        line_data["info_start_time"] = start
        line_data["info_end_time"] = end
        data_list.append(line_data)

    insert_info_many(data_list)

    return True
