# -*- coding: utf-8 -*-
"""
    @Time : 2023/8/27 0:06
    @Author : 李子
    @Url : https://github.com/kslz
"""
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QDialog

from utils.init_tools import ToolWorkspace
from utils.logging_utils import LoggerSingleton


class BaseDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.logger = LoggerSingleton.get_logger()
        self.workspace = ToolWorkspace()

    def my_init(self):
        # 设置窗口左上角图标
        self.setWindowIcon(QIcon("./img/logo.png"))

        # 禁止拖拽缩放窗口
        self.setFixedSize(self.size())  # 禁止窗口大小变化


class BaseStartDialog(QDialog):
    """
    专门给工作区选择窗口用，因为此时还没选工作区，不知道log要写在哪
    """
    def __init__(self, parent=None):
        super().__init__(parent)

    def my_init(self):
        # 设置窗口左上角图标
        self.setWindowIcon(QIcon("./img/logo.png"))

        # 禁止拖拽缩放窗口
        self.setFixedSize(self.size())  # 禁止窗口大小变化
