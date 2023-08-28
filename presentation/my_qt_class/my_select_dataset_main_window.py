# -*- coding: utf-8 -*-
"""
    @Time : 2023/8/27 14:56
    @Author : 李子
    @Url : https://github.com/kslz
"""
from PySide6.QtWidgets import QTableWidgetItem, QPushButton, QHBoxLayout, QWidget

from domain.repositories.models import Dataset
from presentation.my_qt_class.my_base_main_window import BaseMainWindow
from presentation.pyuic.ui_SelectDatasetMainWindow import Ui_SelectDatasetMainWindow
from utils.tools import *


class SelectDatasetMainWindow(BaseMainWindow):
    def __init__(self, tool_workspace):
        super().__init__()
        # 使用ui文件导入定义界面类
        self.ui = Ui_SelectDatasetMainWindow()
        # 初始化界面
        self.ui.setupUi(self)
        self.my_init()
        self.ui.tableWidget.setColumnWidth(0, 100)
        self.ui.tableWidget.setColumnWidth(1, 130)
        self.ui.tableWidget.setColumnWidth(2, 130)
        self.ui.tableWidget.setColumnWidth(3, 200)
        self.ui.tableWidget.setColumnWidth(4, 120)

        self.tool_workspace = tool_workspace
        self.add_dataset_data()

    def add_dataset_data(self):
        """
        刷新表格数据，从数据库中取出数据集信息填入表格

        :return:
        """
        self.ui.tableWidget.setRowCount(0)
        datasets = Dataset.select()
        for dataset in datasets:
            print(dataset.dataset_id)
            self.addData(dataset.dataset_id,
                         dataset.dataset_name,
                         dataset.dataset_create_time,
                         dataset.dataset_last_use_time,
                         dataset.dataset_info)

    def addData(self, dataset_id=None, dataset_name=None, dataset_createtime=None, dataset_lastusetime=None,
                dataset_info=None):
        # todo 使用工厂函数新建编辑按钮组
        row = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(row)
        self.ui.tableWidget.setItem(row, 0, QTableWidgetItem(str(dataset_name)))
        self.ui.tableWidget.setItem(row, 1, QTableWidgetItem(str(dataset_createtime)))
        self.ui.tableWidget.setItem(row, 2, QTableWidgetItem(str(dataset_lastusetime)))
        # self.ui.tableWidget.setItem(row, 3, QTableWidgetItem(str(dataset_info)))
        info_cell = QTableWidgetItem()
        info_cell.setText(dataset_info)
        info_cell.setToolTip(f"<pre>{huanhang(dataset_info)}</pre>")
        self.ui.tableWidget.setItem(row, 3, info_cell)

        btn_jr = QPushButton('进入', self)
        btn_jr.clicked.connect(lambda: self.openDatasetWindow(dataset_id))
        btn_bj = QPushButton('编辑', self)
        btn_bj.clicked.connect(lambda: self.edit_dataset(dataset_id))
        btn_sc = QPushButton('删除', self)
        btn_sc.clicked.connect(lambda: self.del_dataset(dataset_id, dataset_name))
        layout = QHBoxLayout()
        layout.addWidget(btn_jr)
        layout.addWidget(btn_bj)
        layout.addWidget(btn_sc)
        layout.setContentsMargins(1, 1, 1, 1)
        layout.setSpacing(1)
        caozuo_widget = QWidget()
        caozuo_widget.setLayout(layout)
        self.ui.tableWidget.setCellWidget(row, 4, caozuo_widget)

    def openDatasetWindow(self, dataset_id):
        pass

    def edit_dataset(self, dataset_id):
        pass

    def del_dataset(self, dataset_id, dataset_name):
        pass


