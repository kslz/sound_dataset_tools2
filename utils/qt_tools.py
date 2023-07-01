# -*- coding: utf-8 -*-
"""
    @Time : 2023/6/27/027 9:11
    @Author : 李子
    @Url : https://github.com/kslz
"""
from PySide6.QtCore import QMutex, Signal, QObject, QMutexLocker, QRunnable, QThreadPool, Qt
from PySide6.QtWidgets import QWidget, QLabel, QSpinBox, QHBoxLayout


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
    started = Signal()
    finished = Signal()
    change_count = Signal(int)


class CustomThreadPool(QThreadPool):
    noTasksRunning = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.activeTasks = 0
        self.mutex = QMutex()

    def start(self, arg__1, priority=0):
        self.changeActiveTasks(1)
        super().start(arg__1, priority)
        self.changeActiveTasks(-1)
        self.taskFinished()

    def changeActiveTasks(self, change):
        with QMutexLocker(self.mutex):
            self.activeTasks += change

    def taskFinished(self):
        with QMutexLocker(self.mutex):
            if self.activeTasks == 0:
                self.noTasksRunning.emit()


class ScoreWdiget(QWidget):
    def __init__(self, name, k, v, parent):
        super().__init__(parent)

        self.k = k

        # 创建标签和旋钮框
        self.label = QLabel(name)
        self.spinbox = QSpinBox()

        font = self.label.font()
        font.setPointSize(12)
        self.label.setFont(font)
        self.spinbox.setFont(font)

        # 设置旋钮框的范围和初始值
        self.spinbox.setMinimum(0)
        self.spinbox.setMaximum(100)
        self.spinbox.setValue(v)

        # 创建水平布局
        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)  # 这个布局的边框我找了2个小时才找出来，警钟长鸣

        # 将标签和旋钮框添加到布局中
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.spinbox)

        # 设置标签靠左，旋钮框靠右
        self.layout.setAlignment(self.label, Qt.AlignLeft)
        self.layout.setAlignment(self.spinbox, Qt.AlignRight)

    def change_text(self, name, k, v):
        self.label.setText(name)
        self.k = k
        self.spinbox.setValue(v)

    def get_score(self, score_dict: dict):
        score_dict[self.k] = self.spinbox.value()
