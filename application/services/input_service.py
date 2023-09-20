# -*- coding: utf-8 -*-
"""
    @Time : 2023/09/18 16:44
    @Author : 李子
    @Url : https://github.com/kslz
"""

import pysrt
from pydub import AudioSegment

from application.services.optimization_service import optimization_server_dict, OptimizationMergeService
from domain.repositories.repositories import insert_info_many


class InputByWavSrtService:
    """
    通过音频和对应的字幕文件导入数据
    """

    def __init__(self, **kwargs):
        self.dataset_id = kwargs['dataset_id']
        self.wav_path = kwargs['wav_path']
        self.srt_path = kwargs['srt_path']
        self.speaker = kwargs['speaker']
        self.sound = AudioSegment.from_file(self.wav_path)
        self.optimizations = kwargs['optimization']

    def input_data(self):
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

    def optimization(self, subs):
        for optimization_name in self.optimizations.keys():
            optimization = optimization_server_dict[optimization_name]
            args_dict = {
                "wav_path": self.wav_path,
                "subs": subs,
                "sound": self.sound,
            }
            args_dict.update(self.optimizations[optimization_name])
            optimization_obj = optimization(args_dict)
            new_wav_path, subs = optimization_obj.optimize_data()
            self.change_sound(new_wav_path)
        return subs

    def change_sound(self, new_wav_path):
        if self.wav_path == new_wav_path:
            self.wav_path = new_wav_path
            self.sound = AudioSegment.from_file(self.wav_path)
