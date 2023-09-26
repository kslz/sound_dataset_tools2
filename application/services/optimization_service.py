# -*- coding: utf-8 -*-
"""
    @Time : 2023/08/24 10:14
    @Author : 李子
    @Url : https://github.com/kslz
    优化逻辑服务
"""
import pydub
import pysrt


class OptimizationMergeService:
    """
    剪映生成的字幕偶尔会出现长句被截成两个紧贴着的短句的情况，这个优化方案可以将紧贴着的两个或更多短句合成一句
    """
    OPTIMIZATION_MIN_TIME = 'min_time'

    def __init__(self):
        self.wav_path = None
        self.subs = None
        self.sound = None
        self.min_time = None

    def need_info(self):
        show_text = '最小合并间隔(ms)'

        def check_min_time(input_str):
            try:
                if int(input_str) >= 0:
                    return True, ''
                else:
                    return False, f'{show_text} 应为不小于0的整数'
            except:
                return False, f'{show_text} 应为不小于0的整数'

        need_info_dict = {
            'show_name': '合并相邻过近条目',
            'show_help': '剪映生成的字幕偶尔会出现长句被截成两个紧贴着的短句的情况，这个优化方案可以将紧贴着的两个或更多短句合成一句',
            'need_sound': False,
            'args': [
                {
                    'name': self.OPTIMIZATION_MIN_TIME,
                    'show_text': show_text,
                    'type': int,
                    'default': 35,
                    'check': check_min_time
                }
            ]
        }
        return need_info_dict

    def init_data(self, args_dict):
        self.wav_path = args_dict['wav_path']
        self.subs = args_dict['subs']
        self.sound = args_dict['sound']
        self.min_time = args_dict.get(self.OPTIMIZATION_MIN_TIME, 35)

    def optimize_data(self):
        subs = self.subs
        optimized_subs = pysrt.SubRipFile()
        min_time = self.min_time
        index = 0

        # 遍历每个字幕
        while index < len(subs):
            # 如果是最后一个字幕，将其添加到优化后的字幕中并结束循环
            if index + 1 == len(subs):
                optimized_subs.append(subs[index])
                break
            this_start_time = subs[index].start.ordinal
            this_end_time = subs[index].end.ordinal
            next_start_time = subs[index + 1].start.ordinal
            next_end_time = subs[index + 1].end.ordinal

            # 如果当前字幕与下一个字幕之间的时间间隔大于min_time，
            # 将当前字幕添加到优化后的字幕中并继续下一个字幕
            if next_start_time - this_end_time > min_time:
                optimized_subs.append(subs[index])
                index += 1
                continue
            start_time = this_start_time
            end_time = next_end_time
            text = subs[index].text

            # 合并连续的字幕，直到它们之间的时间间隔大于min_time
            for i in range(index + 1, len(subs)):
                end_time = subs[i].end.ordinal
                text += subs[i].text

                # 如果是最后一个字幕或者当前字幕与下一个字幕之间的时间间隔大于min_time，
                # 创建一个新的合并字幕并将其添加到优化后的字幕中
                if i == len(subs) - 1 or subs[i + 1].start.ordinal - subs[i].end.ordinal > min_time:
                    start = pysrt.SubRipTime(milliseconds=start_time)
                    end = pysrt.SubRipTime(milliseconds=end_time)
                    line = pysrt.SubRipItem(index=index, start=start, end=end, text=text)
                    index = i + 1
                    optimized_subs.append(line)
                    break
        return self.wav_path, optimized_subs


optimization_service_dict = {
    "OptimizationMergeService": OptimizationMergeService
}


def merge_srt(wav_path: str, sound: pydub.audio_segment.AudioSegment, subs: pysrt.srtfile.SubRipFile):
    print(wav_path)
    pass


def cut_wav_better2(wav_path: str, sound: pydub.audio_segment.AudioSegment, subs: pysrt.srtfile.SubRipFile):
    for sub in subs:
        sub: pysrt.srtitem.SubRipItem
        start = sub.start.ordinal
        end = sub.end.ordinal
        start, end = cut_wav_better(sound, start, end)


def cut_wav_better(sound, start, end, step=50):
    start = max(0, start)
    end = min(end, len(sound))

    # 向前寻找响度更小的start
    current_start = start - step
    volume = sound[start:start + step].dBFS
    while current_start >= 0:
        current_end = current_start + step
        current_segment = sound[current_start:current_end]
        current_volume = current_segment.dBFS
        if current_volume > volume:
            break
        volume = current_volume
        start = current_start
        current_start -= step

    # 向后寻找响度更小的end
    current_end = end + step
    volume = sound[current_end - step:current_end].dBFS
    while current_end <= len(sound):
        current_start = current_end - step
        current_segment = sound[current_start:current_end]
        current_volume = current_segment.dBFS
        if current_volume > volume:
            break
        volume = current_volume
        end = current_end
        current_end += step

    return start, end
