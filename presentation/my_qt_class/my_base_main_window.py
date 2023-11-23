# -*- coding: utf-8 -*-
"""
    @Time : 2023/8/27 0:06
    @Author : 李子
    @Url : https://github.com/kslz
"""
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMainWindow

from utils.init_tools import ToolWorkspace
from utils.logging_utils import LoggerSingleton


class BaseMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.logger = LoggerSingleton.get_logger()
        self.workspace = ToolWorkspace()

    def my_init(self, is_fixed=True):
        # 设置窗口左上角图标
        self.setWindowIcon(QIcon("./img/logo.png"))

        if is_fixed:
            # 禁止拖拽缩放窗口
            self.setFixedSize(self.size())  # 禁止窗口大小变化

