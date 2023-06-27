# -*- coding: utf-8 -*-
"""
    @Time : 2023/6/27/027 9:11
    @Author : 李子
    @Url : https://github.com/kslz
"""
from PySide6.QtCore import QMutex, Signal, QObject, QMutexLocker


class ProgressUpdater(QObject):
    """
    进度更新器，用于接收任务完成信号并更新进度条
    """
    progressUpdated = Signal(int)

    def __init__(self, progress_bar):
        super().__init__()
        self.progress_bar = progress_bar
        self.mutex = QMutex()

    def updateProgress(self):
        with QMutexLocker(self.mutex):
            # 更新进度条
            self.progress_bar.setValue(self.progress_bar.value() + 1)


class SignalTool(QObject):
    """
    这个类唯一的作用是用来帮发不出信号的物件发出信号
    """
    finished = Signal()
