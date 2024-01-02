# -*- coding: utf-8 -*-
"""
    @Time : 2024/01/02 18:03
    @Author : 李子
    @Url : https://github.com/kslz
"""
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout, QWidget, QHBoxLayout, QPushButton, QLabel, QSizePolicy


class MyDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setFixedSize(350, 0)  # 0表示高度自动适应内容

        # 创建主布局
        self.main_layout = QVBoxLayout(self)

        font = QFont()
        font.setPointSize(12)
        self.setFont(font)

    def add_line(self, name, introduction):
        widget_line = QWidget(self)
        widget_line_layout = QHBoxLayout(widget_line)
        button = QPushButton(name, widget_line)
        label = MyLabel("?", widget_line)
        widget_line_layout.addWidget(button)
        widget_line_layout.addWidget(label)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.main_layout.addWidget(widget_line)

class MyLabel(QLabel):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)

    def enterEvent(self, event):
        # 鼠标进入时，设置字体加粗
        font = self.font()
        font.setBold(True)
        self.setFont(font)

    def leaveEvent(self, event):
        # 鼠标离开时，恢复原始字体
        font = self.font()
        font.setBold(False)
        self.setFont(font)

if __name__ == '__main__':
    app = QApplication([])
    dialog = MyDialog()
    dialog.add_line("name", "介绍")
    dialog.exec_()
    app.exec_()
