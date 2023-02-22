# -*- coding: utf-8 -*-
"""
    @Time : 2023/1/29/029 11:19
    @Author : 李子
    @Url : https://github.com/kslz
"""
import configparser
import json
import os
import re
import shutil
import string
import subprocess
import textwrap

import ffmpeg
import pysrt
from pysrt import SubRipTime

from utils import global_obj
from utils.peewee_orm import *
from utils.sqlitedb import MyDB

if os.path.isfile(os.path.join("./lib/ffmpeg/", "ffmpeg.exe")):
    ffmpeg_path = "./lib/ffmpeg/"
else:
    ffmpeg_path = ""


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

def copy_file_to_workspace(raw_path,to_path):
    file_name = os.path.basename(raw_path)
    now = datetime.now()
    formatted_time = now.strftime("%Y-%m-%d_%H-%M-%S")

    file_name_new = os.path.splitext(file_name)[0]+"_"+formatted_time+".flac"
    new_path = os.path.join(to_path,file_name_new)

    (
        ffmpeg
        .input(raw_path)
        .output(new_path, codec="flac", compression_level=5)
        .run()
    )

    # shutil.copyfile(raw_path, new_path)
    return new_path




def add_info_by_file_wav_srt(dataset_id, wav_path, srt_path, speaker, is_merge=True):
    subs = pysrt.open(srt_path)
    if is_merge:
        subs = merge_srt(subs)
    data_list = []
    for line in subs:
        line: pysrt.srtitem.SubRipItem
        line_data = {}
        line_data["dataset_id"] = dataset_id
        line_data["info_text"] = line.text
        line_data["info_speaker"] = speaker
        line_data["info_raw_file_path"] = wav_path
        line_data["info_start_time"] = line.start.ordinal
        line_data["info_end_time"] = line.end.ordinal
        data_list.append(line_data)

    insert_info_many(data_list)

    return True


def merge_srt(subs, min_time=35):
    """
    剪映生成的字幕偶尔会出现长句被截成两个紧贴着的短句的情况，这个函数可以将紧贴着的两个或更多短句合成一句

    """
    subs: pysrt.SubRipFile  # 加上编辑器也不给我代码提示 寄
    subs2 = pysrt.SubRipFile()
    i = 0
    while i < len(subs):  # 经典for循环

        if i + 1 == len(subs):
            subs2.append(subs[i])
            break
        this_start_time = subs[i].start.ordinal
        this_end_time = subs[i].end.ordinal
        next_start_time = subs[i + 1].start.ordinal
        next_end_time = subs[i + 1].end.ordinal

        if next_start_time - this_end_time > min_time:
            subs2.append(subs[i])
            i += 1
            continue
        start_time = this_start_time
        end_time = next_end_time
        text = subs[i].text
        for n in range(i + 1, len(subs)):
            end_time = subs[n].end.ordinal
            text += subs[n].text
            if n == len(subs) - 1 or subs[n + 1].start.ordinal - subs[n].end.ordinal > min_time:
                start = SubRipTime(milliseconds=start_time)
                end = SubRipTime(milliseconds=end_time)
                line = subtitle = pysrt.SubRipItem(index=i, start=start, end=end, text=text)
                i = n + 1
                subs2.append(line)
                break
    return subs2

def play_by_ffmpeg(wav_path,start_time,end_time):
    # 将毫秒转换为ffmpeg需要的时间格式
    duration = (end_time - start_time) / 1000
    start_time = start_time / 1000

    # 从长音频文件中提取指定时间段的音频
    output = (
        ffmpeg
        .input(wav_path, ss=start_time, t=duration)
        .output('pipe:', format='wav')
        .run(capture_stdout=True)
    )

    # 播放输出的音频
    process = subprocess.Popen(['ffplay', "-nodisp", "-autoexit", '-'], stdin=subprocess.PIPE)
    process.communicate(output[0])


def get_audio_duration(file_path):
    """
    获取音频持续时间

    :param file_path:
    :return:
    """
    # 构造 ffprobe 命令行
    ffprobe_cmd = [
        os.path.join(ffmpeg_path, 'ffprobe'), '-v', 'quiet', '-print_format', 'json', '-show_format', file_path
    ]

    # 执行命令行并解析 JSON 输出
    process = subprocess.Popen(ffprobe_cmd, stdout=subprocess.PIPE)
    output, error = process.communicate()
    output = output.decode('utf-8')
    metadata = json.loads(output)

    # 提取音频文件长度
    duration = float(metadata['format']['duration'])
    return duration


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
    db.pragma('foreign_keys', 'on')
    db.create_tables([Workspace, Dataset, Info, SpkInfo])
    global_obj.set_value("peewee_db", db)


def inti_workspace(workspace_path):
    """
    初始化工作区
    1、新建目录：workspace_path、workspace_path/db
    2、连接数据库

    """
    global_obj.set_value("workspace_path", workspace_path)
    os.makedirs(workspace_path, exist_ok=True)
    os.makedirs(os.path.join(workspace_path, "db"), exist_ok=True)
    os.makedirs(os.path.join(workspace_path, "sounds"), exist_ok=True)
    # mydb = MyDB(os.path.join(workspace_path, "db/workspace.db"))
    # global_obj.set_value("mydb", mydb)

    init_database(os.path.join(workspace_path, "db/workspace.db"))
    peewee_db: SqliteDatabase = global_obj.get_value("peewee_db")
    table_names = peewee_db.get_tables()
    # print(table_names)


class ConfigParserWithFile(configparser.ConfigParser):
    file = None

    def read(self, filenames, encoding=None):
        self.file = filenames
        return super().read(filenames, encoding)

    def refresh_config(self, encoding=None):
        return super().read(self.file, encoding)


if __name__ == '__main__':
    init_program()
