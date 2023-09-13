# -*- coding: utf-8 -*-
"""
    @Time : 2023/09/13 9:22
    @Author : 李子
    @Url : https://github.com/kslz
"""
from PySide6 import QtCore, QtGui

from presentation.my_qt_class.my_base_main_window import BaseMainWindow
from presentation.my_qt_class.my_tool_function import *
from presentation.pyuic.ui_DatasetViewMainWindow import Ui_DatasetViewMainWindow


class DatasetViewMainWindow(BaseMainWindow):
    def __init__(self, dataset_id):
        super().__init__()
        # 使用ui文件导入定义界面类
        self.ui = Ui_DatasetViewMainWindow()
        # 初始化界面
        self.ui.setupUi(self)
        self.my_init()
        self.set_table_style()

        self.dataset_id = dataset_id
        self.page_number = 1
        self.page_size = 15

    def set_table_style(self):
        # 数据集概览表格
        properties = [
            ("序号", False, 100),
            ("标注文本", True, 130),
            ("发音人", False, 130),
            ("标签", True, 100),
            ("操作", False, 120),
        ]
        modify_table_style(self.ui.tableWidget, properties)

        self.ui.tableWidget.verticalHeader().setDefaultSectionSize(26)  # 设置行高24
        header = self.ui.tableWidget.horizontalHeader()
        header.setDefaultAlignment(QtCore.Qt.AlignLeft)  # 设置表头左对齐
        # 创建一个字体对象，并设置字号为12
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        # 将字体对象设置为表头的字体
        header.setFont(font)


