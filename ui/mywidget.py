# -*- coding: utf-8 -*-
"""
    @Time : 2023/4/10/010 11:10
    @Author : 李子
    @Url : https://github.com/kslz
"""
from PySide6 import QtCore
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QPushButton

from utils.tools import *


class FastOutputSoundBTN(QPushButton):
    def __init__(self, text, info_id, parent):
        super().__init__(text, parent)
        self.info_id = info_id
        self.clicked.connect(self.fast_output_sound)
        # self.setText("快速导出")
        # info = Info.get_by_id(self.info_id)
        # wav_path = info.info_raw_file_path
        # start_time = info.info_start_time
        # end_time = info.info_end_time

    def fast_output_sound(self):
        info = Info.get_by_id(self.info_id)
        wav_path = info.info_raw_file_path
        start_time = info.info_start_time
        end_time = info.info_end_time
        output_name = str(self.info_id) + ".wav"
        fast_output_sound(wav_path, start_time, end_time, output_name)


class PlaySoundBTN(QPushButton):
    class PlaySoundThread(QtCore.QThread):
        update_signal = Signal(str, bool)

        # stop_thread_signal = Signal()

        def __init__(self, wav_path, start_time, end_time):
            super().__init__()
            # self.stop_flag = False
            # self.stop_thread_signal.connect(self.stop_thread)
            self.wav_path = wav_path
            self.start_time = start_time
            self.end_time = end_time

        def run(self):
            self.update_signal.emit("播放中", False)
            play_by_ffmpeg(self.wav_path, self.start_time, self.end_time)
            self.update_signal.emit("试听", True)

        # def stop_thread(self):
        #     self.stop_flag = True
        #     print("收到停止信号")
        #     self.wait()

    def __init__(self, text, info_id, parent):
        super().__init__(text, parent)
        self.info_id = info_id
        self.clicked.connect(self.play_or_stop_sound)
        info = Info.get_by_id(self.info_id)
        wav_path = info.info_raw_file_path
        start_time = info.info_start_time
        end_time = info.info_end_time
        # self.thread1 = QThread(self)  # 创建一个线程 不行 没用明白，先这样吧
        self.play_thread = self.PlaySoundThread(wav_path, start_time, end_time)  # 实例化线程类
        # self.play_thread.moveToThread(self.thread1)  # 将类移动到线程中运行
        # self.thread1.started.connect(self.play_thread.run)
        self.play_thread.update_signal.connect(lambda text, is_enabled: self.set_text(text, is_enabled))

    def play_or_stop_sound(self):
        # 多线程避免阻塞界面
        if self.text() == "试听":
            self.play_thread.start()
        else:
            # 终止播放失败
            # self.play_thread.stop_thread_signal.emit()
            # self.play_thread.exit()
            # self.set_text("试听", True)
            pass

    def set_text(self, text, is_enabled):
        self.setText(text)
        # self.setEnabled(is_enabled)


class PlayNowSoundBTN(QPushButton):
    class PlaySoundThread(QtCore.QThread):
        update_signal = Signal(str, bool)

        # stop_thread_signal = Signal()

        def __init__(self, wav_path, start_time, end_time):
            super().__init__()
            # self.stop_flag = False
            # self.stop_thread_signal.connect(self.stop_thread)
            self.wav_path = wav_path
            self.start_time = start_time
            self.end_time = end_time

        def run(self):
            self.update_signal.emit("播放中", False)
            play_by_ffmpeg(self.wav_path, self.start_time, self.end_time)
            self.update_signal.emit("试听", True)

        # def stop_thread(self):
        #     self.stop_flag = True
        #     print("收到停止信号")
        #     self.wait()

    def __init__(self, text, parent):
        super().__init__(text, parent)

    def play_or_stop_sound(self, wav_path, start_time, end_time):
        # 多线程避免阻塞界面
        if self.text() == "试听":
            self.play_thread = self.PlaySoundThread(wav_path, start_time, end_time)  # 实例化线程类
            self.play_thread.update_signal.connect(lambda text, is_enabled: self.set_text(text, is_enabled))
            self.play_thread.start()
        else:
            # 终止播放失败
            # self.play_thread.stop_thread_signal.emit()
            # self.play_thread.exit()
            # self.set_text("试听", True)
            pass

    def set_text(self, text, is_enabled):
        self.setText(text)
        # self.setEnabled(is_enabled)


class BianJiBTN(QPushButton):

    on_clicked = Signal(int)
    def __init__(self, text, info_id):
        super().__init__(text=text)
        self.info_id = info_id
        self.clicked.connect(self.button_clicked)

    def button_clicked(self):
        self.on_clicked.emit(self.info_id)
