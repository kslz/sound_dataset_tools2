# -*- coding: utf-8 -*-
"""
    @Time : 2023/9/16 19:49
    @Author : 李子
    @Url : https://github.com/kslz
"""
import subprocess

import ffmpeg
from PySide6.QtCore import QThread, Signal
from PySide6.QtWidgets import QPushButton


class AudioButton(QPushButton):
    def __init__(self, wav_path, start_time, end_time, parent=None):
        super().__init__(parent)
        self.setText("试听")
        self.audio_thread = None
        self.wav_path = wav_path
        self.start_time = start_time
        self.end_time = end_time

        # 连接按钮点击事件的槽函数
        self.clicked.connect(self.on_button_clicked)

    def on_button_clicked(self):
        if self.audio_thread is not None and self.audio_thread.is_playing:
            # 如果音频正在播放，停止播放
            # print("停止播放")
            self.audio_thread.stop()
            self.audio_thread.wait()
            self.audio_thread = None
            self.setText("试听")
        else:
            # 如果音频没有在播放，开始播放
            self.audio_thread = AudioThread(self.wav_path, self.start_time, self.end_time)
            self.audio_thread.finished.connect(self.on_audio_finished)
            self.audio_thread.start()
            self.setText("停止")

    def on_audio_finished(self):
        self.audio_thread = None
        self.setText("试听")


# 自定义的音频播放线程
class AudioThread(QThread):
    finished = Signal()  # 定义一个信号，用于通知播放完成

    def __init__(self, wav_path, start_time, end_time, parent=None):
        super().__init__(parent)
        self.is_playing = False
        self.wav_path = wav_path
        self.start_time = start_time
        self.end_time = end_time

    def run(self):
        self.is_playing = True

        # play_by_ffmpeg(self.wav_path, self.start_time, self.end_time)
        # 如果用函数形式调用，执行self.audio_thread.terminate()的时候声音就会卡几秒才停，直接写代码就可以秒停，原因未知
        wav_path = self.wav_path
        start_time = self.start_time
        end_time = self.end_time

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
        self.process = subprocess.Popen(['ffplay', "-nodisp", "-autoexit", '-'], stdin=subprocess.PIPE)
        self.process.communicate(output[0])

        self.is_playing = False
        self.finished.emit()  # 发送播放完成的信号

    def stop(self):
        if self.process and self.process.poll() is None:  # 检查子进程是否在运行
            self.process.terminate()  # 终止子进程