# -*- coding: utf-8 -*-
"""
    @Time : 2023/8/27 0:06
    @Author : 李子
    @Url : https://github.com/kslz
"""
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QDialog


class BaseDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

    def my_init(self):
        # 设置窗口左上角图标
        self.setWindowIcon(QIcon("./img/logo.png"))

        # 禁止拖拽缩放窗口
        self.setFixedSize(self.size())  # 禁止窗口大小变化
