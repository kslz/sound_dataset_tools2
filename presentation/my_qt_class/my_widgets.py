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
    def __init__(self, check_fun, arg_name, need_type):
        super().__init__()
        self.check_fun = check_fun
        self.arg_name = arg_name
        self.need_type = need_type

    def get_ok(self):
        is_ok, msg = self.check_fun(self.text())
        return is_ok, msg

    def get_result(self):
        return self.need_type(self.text())
