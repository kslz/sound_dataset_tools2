# -*- coding: utf-8 -*-
"""
    @Time : 2023/2/13/013 13:35
    @Author : 李子
    @Url : https://github.com/kslz
"""
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QTableWidgetItem, QPushButton, QLabel
from PySide6.QtCore import Signal

from ui.ui_select_dataset import Ui_MainWindow
from ui.ui_select_workspace import Ui_Form
from utils import global_obj
from utils.peewee_orm import *
from utils.tools import update_ini_config, inti_workspace

global config


def getconfig():
    global config
    config = global_obj.get_value("config")


class SelectDatasetWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # 使用ui文件导入定义界面类
        self.ui = Ui_MainWindow()
        # 初始化界面
        self.ui.setupUi(self)
        self.ui.tableWidget.setColumnWidth(0, 100)
        self.ui.tableWidget.setColumnWidth(1, 150)
        self.ui.tableWidget.setColumnWidth(2, 150)
        self.ui.tableWidget.setColumnWidth(3, 200)
        self.ui.tableWidget.setColumnWidth(4, 100)

    def add_dataset_data(self):
        # dataset1 = Dataset.create(dataset_name="test1")
        # dataset2 = Dataset.create(dataset_name="test2")
        datasets = Dataset.select()
        print(len(datasets))
        for dataset in datasets:
            self.addData(dataset.dataset_name,
                         dataset.dataset_create_time,
                         dataset.dataset_last_use_time,
                         dataset.dataset_info)

    def addData(self, data1=None, data2=None, data3=None, data4=None):
        row = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(row)
        self.ui.tableWidget.setItem(row, 0, QTableWidgetItem(str(data1)))
        self.ui.tableWidget.setItem(row, 1, QTableWidgetItem(str(data2)))
        self.ui.tableWidget.setItem(row, 2, QTableWidgetItem(str(data3)))
        self.ui.tableWidget.setItem(row, 3, QTableWidgetItem(str(data4)))

        btn = QPushButton('进入', self)
        self.ui.tableWidget.setCellWidget(row, 4, btn)
        btn.clicked.connect(lambda: self.openNewWindow(self.ui.tableWidget.item(row, 0).text()))

    def openNewWindow(self, rowtext):
        window = QMainWindow(self)
        window.setWindowTitle('New Window')
        window.setGeometry(100, 100, 300, 200)

        window.label = QLabel(window)
        window.label.setText(rowtext)
        window.show()


class SelectWorkspaceWindow(QWidget):
    show_select_dataset_window = Signal()

    def __init__(self):
        super().__init__()
        # 使用ui文件导入定义界面类
        self.ui = Ui_Form()
        # 初始化界面
        self.ui.setupUi(self)
        getconfig()
        self.input_default_workspace()

    def input_default_workspace(self):
        default_workspace = config["program_configs"]["default_workspace"]
        # default_workspace = os.path.abspath(default_workspace)
        self.ui.lineEdit.setText(default_workspace)

    def close_program(self):
        self.close()

    def get_workspace(self):
        workspace_path = self.ui.lineEdit.text()
        global_obj.set_value("workspace_path", workspace_path)
        inti_workspace(workspace_path)
        config["program_configs"]["default_workspace"] = workspace_path
        update_ini_config(config)
        self.show_select_dataset_window.emit()
        self.close()

        # if os.path.exists(workspace_path):
        #     print("路径存在")
        # else:
        #     print("路径不存在")

    pass
