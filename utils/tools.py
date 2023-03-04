# -*- coding: utf-8 -*-
"""
    @Time : 2023/1/29/029 11:19
    @Author : 李子
    @Url : https://github.com/kslz
"""
import configparser
import io
import json
import os
import re
import string
import subprocess
import time

import ffmpeg
import pypinyin
import pysrt
from pysrt import SubRipTime

from utils import global_obj
from utils.peewee_orm import *
from utils.log import *
from utils.request_tools import get_biaobei_token

if os.path.isfile(os.path.join("./lib/ffmpeg/", "ffmpeg.exe")):
    ffmpeg_path = "./lib/ffmpeg/"
else:
    ffmpeg_path = ""


class GeshiStr():
    aishell3 = "AISHELL-3"
    default = "默认"
    vits = "VITS"
    sovits = "sovits"


channels_dict = {}


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


def file_wb(path, text, mode="wb"):
    """
    用于向文件中写入

    :param path: 文件路径
    :param text: 要写入的数据
    :param mode: 写入模式

    """
    with open(path, mode) as f:
        f.write(text)


def is_all_chinese(text):
    pattern = re.compile(r'^[\u4e00-\u9fa5]+$')
    return bool(pattern.match(text))


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


def refresh_biaobei_token(authorizationinfo_id):
    authorizationinfo = AuthorizationInfo.get_by_id(authorizationinfo_id)
    token = get_biaobei_token(authorizationinfo.authorizationinfo_APIKey, authorizationinfo.authorizationinfo_APISecret)
    if token:
        AuthorizationInfo.update(authorizationinfo_token=token).where(
            AuthorizationInfo.authorizationinfo_id == authorizationinfo_id).execute()
        return token
    else:
        return False


def del_file_end_blank_line(file_path):
    with open(file_path, 'r', encoding="UTF-8") as f:
        lines = f.readlines()

    # 判断最后一行是否为空行
    while lines[-1] == '\n':
        lines.pop()

    if lines[-1].endswith("\n"):
        lines[-1] = lines[-1][:-1]

    # 写回txt文件
    with open(file_path, 'w', encoding="UTF-8") as f:
        f.writelines(lines)


def output_wav_file(wav_path, start_time, end_time, new_path, sample_rate, channels, normalization):
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
        result.output(new_path, format='wav', ac=channels, ar=sample_rate, acodec=codec).run_async(quiet=True)

    # 从长音频文件中提取指定时间段的音频并先转为单声道音频，再进行归一化
    # 注意：如果直接将双声道音频转换为单声道，并进行归一化，会导致单声道音频的输出结果偏低（相当于降低了3）
    # 换句话说，如果你用一个双声道音频分别转为双声道I=-16和单声道I=-16，输出的结果中双声道音频的响度比单声道音频高3LUFS 也就是单声道的响度为-19
    # 如果你将两者放入AU中进行响度匹配至-16，你会发现单声道音频的音量会被放大，而双声道音频将不会受影响
    # 我在这里卡了超过24小时，熬了一个大夜，太坑了，耽误我做锅包肉了（做好了，嘎嘎香
    # 这里的逻辑过于复杂，我又不想在导入数据集时就把音频转为单声道，所以我目前限制导出只能为单声道，简化这里的逻辑待日后修改
    # 日后到了 优化好了

    # if normalization:
    #     output_audio = (
    #         ffmpeg
    #         .input(wav_path, ss=start_time, t=duration)
    #         .output("pipe:", format='wav', ac=channels, ar=sample_rate, acodec=codec)
    #         .run(capture_stdout=True, quiet=True)
    #     )
    #     output_audio = output_audio[0]
    #     audio_io = io.BytesIO(output_audio)
    #     audio_input = ffmpeg.input('pipe:').filter("loudnorm", I=normalization, TP=-1, LRA=11, linear="true")
    #     audio = (
    #         ffmpeg
    #         .output(audio_input, new_path, ac=channels, ar=sample_rate, acodec=codec)
    #         .overwrite_output()
    #         .run_async(pipe_stdin=True, pipe_stdout=True, quiet=True)
    #     )
    #     audio.communicate(input=audio_io.read())
    # else:
    #     (
    #         ffmpeg
    #         .input(wav_path, ss=start_time, t=duration)
    #         .output(new_path, format='wav', ac=channels, ar=sample_rate, acodec=codec)
    #         .run_async(quiet=True)
    #     )

    # result = ffmpeg.input(wav_path, ss=start_time, t=duration)
    # if normalization:
    #     result = result.filter("loudnorm", I=normalization, TP=-1, LRA=11, linear="true")  # 归一化
    #
    # result = result.output(new_path, format='wav', ac=channels, ar=sample_rate, acodec=codec).run_async()

    # codec = 'pcm_s16le'
    # output_audio = (
    #     ffmpeg
    #     .input(wav_path)
    #     .output("pipe:", format='wav', ac=1, ar=44100, acodec=codec)
    #     .run(capture_stdout=True)
    # )
    # output_audio = output_audio[0]
    # audio_io = io.BytesIO(output_audio)
    # audio_input = ffmpeg.input('pipe:').filter("loudnorm", I=-16, TP=-1, LRA=11, linear="true")
    # audio = (
    #     ffmpeg
    #     .output(audio_input, output_file)
    #     .overwrite_output()
    #     .run_async(pipe_stdin=True, pipe_stdout=True, quiet=True)
    # )
    # audio.communicate(input=audio_io.read())


def output_like_aishell3(qianzhui, sample_rate, channels, results, output_path, is_auto_skip, normalization):
    """
    将数据集模仿aishell3格式导出
    data_aishell3/
      -train/
        -wav/
          -speaker1/
            -1.wav
            -2.wav
            ...
        -content.txt
          -1.wav    你 ni3 好 hao3 世 shi4 界 jie4
           2.wav...

    """
    output_path = os.path.join(output_path, "data_aishell3", "train")
    os.makedirs(output_path, exist_ok=True)
    label_path = os.path.join(output_path, "content.txt")
    os.makedirs(os.path.join(output_path, "wav"), exist_ok=True)

    name_index = 1
    for result in results:
        try:
            raw_path = result["info_raw_file_path"]
            info_text = result["info_text"]
            if is_auto_skip:
                is_ok = True
                for c in info_text:
                    if c.isascii():
                        is_ok = False
                        break
                if not is_ok:
                    continue
            start = result["info_start_time"]
            end = result["info_end_time"]
            line_name = f"{qianzhui}{str(name_index)}.wav"
            output_file = os.path.join(output_path, "wav", line_name)
            line_text = f"{line_name}\t{text_to_aishell3_like(info_text)}\n"
            file_w(label_path, line_text, "a")
            output_wav_file(raw_path, start, end, output_file, sample_rate, channels, normalization)
            name_index += 1
        except:
            guilogger.error(f"id为 {result['info_id']} 的数据导出失败")
    return name_index - 1


def output_like_default(qianzhui, sample_rate, channels, results, output_path, is_auto_skip, normalization):
    """
    将数据集按照默认格式导出,相对简明
    -wavs/
      -1.wav
      -2.wav
      ...
    -labels.txt
      -1.wav|你好世界
      -2.wav...

    """
    wavs_path = os.path.join(output_path, "wavs")
    os.makedirs(wavs_path, exist_ok=True)
    label_path = os.path.join(output_path, "labels.txt")

    name_index = 1
    for result in results:
        try:
            raw_path = result["info_raw_file_path"]
            info_text = result["info_text"]
            if is_auto_skip:
                is_ok = True
                for c in info_text:
                    if c.isascii():
                        is_ok = False
                        break
                if not is_ok:
                    continue
            start = result["info_start_time"]
            end = result["info_end_time"]
            line_name = f"{qianzhui}{str(name_index)}.wav"
            output_file = os.path.join(output_path, "wavs", line_name)
            line_text = f"{line_name}|{info_text}\n"
            file_w(label_path, line_text, "a")

            output_wav_file(raw_path, start, end, output_file, sample_rate, channels, normalization)
            name_index += 1
        except:
            guilogger.error(f"id为 {result['info_id']} 的数据导出失败")
    return name_index - 1


def output_like_vits(qianzhui, sample_rate, channels, results, output_path, is_auto_skip, normalization):
    """
    将数据集按照默认格式导出,相对简明
    -wavs/
      -1.wav
      -2.wav
      ...
    -labels.txt
      -1.wav|你好世界
      -2.wav...

    """
    wavs_path = os.path.join(output_path, "wavs")
    os.makedirs(wavs_path, exist_ok=True)
    label_path = os.path.join(output_path, "list.txt")

    name_index = 1
    for result in results:
        try:
            raw_path = result["info_raw_file_path"]
            info_text = result["info_text"]
            if is_auto_skip:
                is_ok = True
                for c in info_text:
                    if c.isascii():
                        is_ok = False
                        break
                if not is_ok:
                    continue
            start = result["info_start_time"]
            end = result["info_end_time"]
            line_name = f"{qianzhui}{str(name_index)}.wav"
            output_file = os.path.join(output_path, "wavs", line_name)
            line_text = f"wavs/{line_name}|{info_text}\n"
            file_w(label_path, line_text, "a")
            output_wav_file(raw_path, start, end, output_file, sample_rate, channels, normalization)
            name_index += 1
        except:
            guilogger.error(f"id为 {result['info_id']} 的数据导出失败")
    del_file_end_blank_line(label_path)
    return name_index - 1


def copy_file_to_workspace(raw_path, to_path):
    file_name = os.path.basename(raw_path)
    now = datetime.now()
    formatted_time = now.strftime("%Y-%m-%d_%H-%M-%S")

    file_name_new = os.path.splitext(file_name)[0] + "_" + formatted_time + ".flac"
    new_path = os.path.join(to_path, file_name_new)

    (
        ffmpeg
        .input(raw_path)
        .output(new_path, codec="flac", compression_level=5)
        .run(quiet=True)
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


def play_by_ffmpeg(wav_path, start_time, end_time):
    # 将毫秒转换为ffmpeg需要的时间格式
    duration = (end_time - start_time) / 1000
    start_time = start_time / 1000

    # 从长音频文件中提取指定时间段的音频
    output = (
        ffmpeg
        .input(wav_path, ss=start_time, t=duration)
        # .filter("loudnorm", I="-23", dual_mono="true")  # 归一化
        .output('pipe:', format='wav', ar=44100)
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


def text_to_aishell3_like(text):
    """
    将汉字转换成汉字+拼音 例：【疯狂地叫着】→【疯 feng1 狂 kuang2 地 de5 叫 jiao4 着 zhe5】

    """
    # 将整个文本转换为拼音列表
    pinyin_list = pypinyin.pinyin(text, style=pypinyin.TONE3, neutral_tone_with_five=True)

    # 将每个汉字的拼音和汉字组合成需要的格式
    result = []
    for i, char in enumerate(text):
        # 获取该汉字的拼音
        pinyin = pinyin_list[i][0]
        # 判断是否有轻声
        # if "5" in pinyin:
        #     pinyin = pinyin.replace("5", "") + "5"
        # 按照格式拼接汉字和拼音
        result.append(f"{char} {pinyin}")

    # 输出结果
    output = " ".join(result)
    return output


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
    db.create_tables([Workspace, Dataset, Info, AuthorizationInfo])
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
    os.makedirs(os.path.join(workspace_path, "output"), exist_ok=True)
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
