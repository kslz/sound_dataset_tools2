# -*- coding: utf-8 -*-
"""
    @Time : 2023/09/26 13:39
    @Author : 李子
    @Url : https://github.com/kslz
"""
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget, QLineEdit


class MyClickableWidget(QWidget):
    clicked = Signal()

    def mousePressEvent(self, event):
        self.clicked.emit()


class MyCheckOkLineEdit(QLineEdit):
    def __init__(self, check_fun):
        super().__init__()
        self.check_fun = check_fun
