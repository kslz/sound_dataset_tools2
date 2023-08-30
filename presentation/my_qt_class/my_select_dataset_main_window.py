# -*- coding: utf-8 -*-
"""
    @Time : 2023/8/27 14:56
    @Author : 李子
    @Url : https://github.com/kslz
    数据集选择界面
"""
from PySide6.QtWidgets import QTableWidgetItem

from domain.repositories.repositories import *
from presentation.my_qt_class.my_add_dataset_dialog import AddDatasetDialog
from presentation.my_qt_class.my_base_main_window import BaseMainWindow
from presentation.my_qt_class.my_factory_function import *
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

        self.ui.pushButton.clicked.connect(self.open_add_dataset_window)

    def add_dataset_data(self):
        """
        刷新表格数据，从数据库中取出数据集信息填入表格

        :return:
        """
        self.ui.tableWidget.setRowCount(0)
        datasets = get_dataset_info()
        for dataset in datasets:
            self.addData(dataset.dataset_id,
                         dataset.dataset_name,
                         dataset.dataset_create_time,
                         dataset.dataset_last_use_time,
                         dataset.dataset_info)

    def addData(self, dataset_id=None, dataset_name=None, dataset_createtime=None, dataset_lastusetime=None,
                dataset_info=None):
        row = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(row)
        self.ui.tableWidget.setItem(row, 0, QTableWidgetItem(str(dataset_name)))
        self.ui.tableWidget.setItem(row, 1, QTableWidgetItem(str(dataset_createtime)))
        self.ui.tableWidget.setItem(row, 2, QTableWidgetItem(str(dataset_lastusetime)))

        info_cell = QTableWidgetItem()
        info_cell.setText(dataset_info)
        info_cell.setToolTip(f"<pre>{huanhang(dataset_info)}</pre>")
        self.ui.tableWidget.setItem(row, 3, info_cell)

        data_list = [
            ['进入', lambda: self.open_dataset_window(dataset_id)],
            ['编辑', lambda: self.edit_dataset(dataset_id)],
            ['删除', lambda: self.del_dataset(dataset_id, dataset_name)]
        ]

        caozuo_widget = make_operate_btns(self, data_list)
        self.ui.tableWidget.setCellWidget(row, 4, caozuo_widget)

    def open_dataset_window(self, dataset_id):
        print("进入", dataset_id)
        pass

    def edit_dataset(self, dataset_id):
        print("编辑", dataset_id)
        pass

    def del_dataset(self, dataset_id, dataset_name):
        print("删除", dataset_id, dataset_name)
        pass

    def open_add_dataset_window(self):
        self.add_window = AddDatasetDialog(self)
        self.add_window.exec()
