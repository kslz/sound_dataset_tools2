# -*- coding: utf-8 -*-
"""
    @Time : 2023/09/18 16:44
    @Author : 李子
    @Url : https://github.com/kslz
"""

import pysrt
from pydub import AudioSegment
from pydub.silence import detect_nonsilent

from application.services.optimization_service import optimization_service_dict
from domain.repositories.repositories import insert_info_many
from domain.service.optimization_service_protocol import OptimizationService


class InputBaseService:
    """
    导入服务基类
    """

    def optimization(self, subs: pysrt.SubRipFile) -> pysrt.SubRipFile:
        """
        将导入参数和优化参数合并，并循环执行所有选中的优化参数

        :param subs:
        :return:
        """
        for optimization_name, optimization_obj in self.optimizations.items():
            if optimization_name not in self.optimizations_get_args.keys():
                continue
            args_dict = {
                "wav_path": self.wav_path,
                "subs": subs,
                "sound": self.sound,
            }
            args_dict.update(self.optimizations_get_args[optimization_name])
            optimization_obj.init_data(args_dict)
            new_wav_path, subs = optimization_obj.optimize_data()
            self.change_sound(new_wav_path)
        return subs

    def change_sound(self, new_wav_path):
        """
        检查如果优化后的音频文件有改变，则更新音频路径和sound
        :param new_wav_path:
        :return:
        """
        if self.wav_path == new_wav_path:
            self.wav_path = new_wav_path
            self.sound = AudioSegment.from_file(self.wav_path)


class InputByWavSrtService(InputBaseService):
    """
    通过音频和对应的字幕文件导入数据
    """

    def __init__(self):
        self.dataset_id = None
        self.wav_path = None
        self.srt_path = None
        self.speaker = None
        self.sound = None
        self.optimizations = {}  # 存放优化服务对象
        self.optimization_args = {}  # 存放优化服务信息和所需参数
        self.optimizations_get_args = {}  # 存放获取到的优化服务参数
        self.init_optimizations()

    def init_optimizations(self):
        """
        获取优化服务对象

        :return:
        """
        for key, value in optimization_service_dict.items():
            optimization_service_obj = value()
            self.optimizations[key] = optimization_service_obj
            self.optimization_args[key] = optimization_service_obj.need_info()

    def init_info(self, **kwargs):
        """
        初始化导入服务各项参数

        :param kwargs:
        :return:
        """
        self.dataset_id = kwargs['dataset_id']
        self.wav_path = kwargs['wav_path']
        self.srt_path = kwargs['srt_path']
        self.speaker = kwargs['speaker']
        self.sound = None
        if kwargs['need_sound']:
            self.sound = AudioSegment.from_file(self.wav_path)
        self.optimizations_get_args = kwargs['optimization']

    def input_data(self) -> bool:
        """
        进行数据库写入操作

        :return:
        """
        subs = pysrt.open(self.srt_path)
        subs = self.optimization(subs)

        data_list = []
        for line in subs:
            line: pysrt.srtitem.SubRipItem
            start = line.start.ordinal
            end = line.end.ordinal
            # start, end = cut_wav_better(sound, start, end)
            line_data = {}
            line_data["dataset_id"] = self.dataset_id
            line_data["info_text"] = line.text
            line_data["info_speaker"] = self.speaker
            line_data["info_raw_file_path"] = self.wav_path
            line_data["info_start_time"] = start
            line_data["info_end_time"] = end
            data_list.append(line_data)

        insert_info_many(data_list)

        return True


class InputByLongWavService(InputBaseService):
    """
    通过音频和对应的字幕文件导入数据
    """

    def __init__(self):
        self.dataset_id = None
        self.wav_path = None
        self.srt_path = None
        self.speaker = None
        self.sound = None
        self.min_silence_len = None
        self.non_silent_ranges = None
        self.seek_step = None
        self.optimizations = {}  # 存放优化服务对象
        self.optimization_args = {}  # 存放优化服务信息和所需参数
        self.optimizations_get_args = {}  # 存放获取到的优化服务参数
        self.init_optimizations()

    def init_optimizations(self):
        """
        获取优化服务对象

        :return:
        """
        for key, value in optimization_service_dict.items():
            optimization_service_obj = value()
            self.optimizations[key] = optimization_service_obj
            self.optimization_args[key] = optimization_service_obj.need_info()

    def init_info(self, **kwargs):
        """
        初始化导入服务各项参数

        :param kwargs:
        :return:
        """
        self.dataset_id = kwargs['dataset_id']
        self.wav_path = kwargs['wav_path']
        # self.srt_path = kwargs['srt_path']
        self.speaker = kwargs['speaker']
        self.min_silence_len = kwargs['min_silence_len']
        self.non_silent_ranges = kwargs['non_silent_ranges']
        self.seek_step = 10

        self.sound = AudioSegment.from_file(self.wav_path)
        self.optimizations_get_args = kwargs['optimization']

    def input_data(self) -> bool:
        """
        进行数据库写入操作

        :return:
        """
        subs = subs = pysrt.SubRipFile()
        nonsilent_times = detect_nonsilent(self.sound,
                                           self.min_silence_len,
                                           self.non_silent_ranges,
                                           self.seek_step)
        for start, end in nonsilent_times:
            # 创建一个 SubRipItem 对象
            sub = pysrt.SubRipItem()
            # 设置字幕开始时间
            sub.start.hours, sub.start.minutes, sub.start.seconds, sub.start.milliseconds = self.ms_to_srt_time(start)

            # 设置字幕结束时间
            sub.end.hours, sub.end.minutes, sub.end.seconds, sub.end.milliseconds = self.ms_to_srt_time(end)
            sub.text = ''
            subs.append(sub)

        subs = self.optimization(subs)

        data_list = []
        for line in subs:
            line: pysrt.srtitem.SubRipItem
            start = line.start.ordinal
            end = line.end.ordinal
            # start, end = cut_wav_better(sound, start, end)
            line_data = {}
            line_data["dataset_id"] = self.dataset_id
            line_data["info_text"] = line.text
            line_data["info_speaker"] = self.speaker
            line_data["info_raw_file_path"] = self.wav_path
            line_data["info_start_time"] = start
            line_data["info_end_time"] = end
            data_list.append(line_data)

        insert_info_many(data_list)

        return True

    # 将毫秒转换为小时、分钟、秒和毫秒
    def ms_to_srt_time(self, ms):
        hours, ms = divmod(ms, 3600000)
        minutes, ms = divmod(ms, 60000)
        seconds, ms = divmod(ms, 1000)
        return hours, minutes, seconds, ms
