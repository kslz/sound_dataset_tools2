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

channels_dict = {}


def del_file_by_dataset_id(dataset_id):
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


def del_file_by_path(file_path):
    os.remove(file_path)


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


def fast_output_sound(wav_path, start_time, end_time, output_name, output_path):
    os.makedirs(output_path, exist_ok=True)
    output_path = os.path.join(output_path, output_name)
    output_wav_file(wav_path, start_time, end_time, output_path)


def output_wav_file(wav_path, start_time, end_time, new_path, sample_rate="", channels="", normalization=""):
    codec = 'pcm_s16le'
    if sample_rate == "":
        sample_rate = 44100

    # 将毫秒转换为ffmpeg需要的时间格式
    duration = (end_time - start_time) / 1000
    start_time = start_time / 1000

    result = ffmpeg.input(wav_path, ss=start_time, t=duration)

    raw_channels = get_wav_channels(wav_path)
    if normalization:
        if raw_channels > channels == 1:
            normalization += 3
        result = result.filter("loudnorm", I=normalization, TP=-1, LRA=11, linear="true")
    result.output(new_path, format='wav', ac=channels, ar=sample_rate, acodec=codec, y='-y').run_async(quiet=True)
    # 从长音频文件中提取指定时间段的音频并先转为单声道音频，再进行归一化
    # 注意：如果直接将双声道音频转换为单声道，并进行归一化，会导致单声道音频的输出结果偏低（相当于降低了3）
    # 换句话说，如果你用一个双声道音频分别转为双声道I=-16和单声道I=-16，输出的结果中双声道音频的响度比单声道音频高3LUFS 也就是单声道的响度为-19
    # 如果你将两者放入AU中进行响度匹配至-16，你会发现单声道音频的音量会被放大，而双声道音频将不会受影响


def get_wav_channels(wav_path):
    c = channels_dict.get(wav_path)
    if c is not None:
        return c
    probe = ffmpeg.probe(wav_path)
    # 从元数据信息中获取音频流的信息
    audio_stream = next((stream for stream in probe['streams'] if stream['codec_type'] == 'audio'), None)
    c = audio_stream['channels']
    channels_dict[wav_path] = c
    return c
