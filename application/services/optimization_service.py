# -*- coding: utf-8 -*-
"""
    @Time : 2023/08/24 10:14
    @Author : 李子
    @Url : https://github.com/kslz
    优化逻辑服务
"""
import pydub
import pysrt


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
