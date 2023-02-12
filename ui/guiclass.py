# -*- coding: utf-8 -*-
"""
    @Time : 2023/1/30/030 18:08
    @Author : 李子
    @Url : https://github.com/kslz
"""
import configparser
import os

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QTableWidgetItem, QPushButton, QLabel

from ui.ui_select_dataset import Ui_MainWindow
from ui.ui_select_workspace import Ui_Form
from utils import global_obj
from utils.log import creatlogger
from utils.tools import update_ini_config, inti_workspace


class SelectDatasetWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # 使用ui文件导入定义界面类
        self.ui = Ui_MainWindow()
        # 初始化界面
        self.ui.setupUi(self)
        self.addData("1", "2", "3", "4")

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
    def __init__(self):
        super().__init__()
        # 使用ui文件导入定义界面类
        self.ui = Ui_Form()
        # 初始化界面
        self.ui.setupUi(self)
        self.input_default_workspace()

    def input_default_workspace(self):
        default_workspace = config["program_configs"]["default_workspace"]
        default_workspace = os.path.abspath(default_workspace)
        self.ui.lineEdit.setText(default_workspace)

    def close_program(self):
        self.close()

    def get_workspace(self):
        workspace_path = self.ui.lineEdit.text()
        global_obj.set_value("workspace_path", workspace_path)
        inti_workspace(workspace_path)
        config["program_configs"]["default_workspace"] = workspace_path
        update_ini_config(config)
        select_window = SelectDatasetWindow()
        select_window.show()

        # if os.path.exists(workspace_path):
        #     print("路径存在")
        # else:
        #     print("路径不存在")

    pass


def main():
    global guilogger
    global config
    config = global_obj.get_value("config")
    guilogger = creatlogger("guilogger")
    app = QApplication([])
    select_workspace_window = SelectWorkspaceWindow()
    select_workspace_window.show()
    guilogger.debug("进入工作区选择窗口")

    app.exec()


if __name__ == "__main__":
    main()
