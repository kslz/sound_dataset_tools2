# -*- coding: utf-8 -*-
"""
    @Time : 2023/09/18 16:44
    @Author : 李子
    @Url : https://github.com/kslz
"""

import pysrt
from pydub import AudioSegment

from application.services.optimization_service import optimization_service_dict
from domain.repositories.repositories import insert_info_many
from domain.service.optimization_service_protocol import OptimizationService


class InputBaseService:

    def optimization(self, subs: pysrt.SubRipFile) -> pysrt.SubRipFile:
        for optimization_name, optimization_obj in self.optimizations.items():
            args_dict = {
                "wav_path": self.wav_path,
                "subs": subs,
                "sound": self.sound,
            }
            args_dict.update(self.optimizations[optimization_name])
            optimization_obj.init_data(args_dict)
            new_wav_path, subs = optimization_obj.optimize_data()
            self.change_sound(new_wav_path)
        return subs

    def change_sound(self, new_wav_path):
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
        self.optimizations = {}
        self.optimization_args = None

    def init_optimizations(self):
        for key, value in optimization_service_dict.items():
            optimization_service_obj = value()
            self.optimizations[key] = optimization_service_obj

    def init_info(self, **kwargs):
        self.dataset_id = kwargs['dataset_id']
        self.wav_path = kwargs['wav_path']
        self.srt_path = kwargs['srt_path']
        self.speaker = kwargs['speaker']
        self.sound = AudioSegment.from_file(self.wav_path)
        self.optimizations = kwargs['optimization']

    def input_data(self) -> bool:
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
