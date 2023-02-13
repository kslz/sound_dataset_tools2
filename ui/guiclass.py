# -*- coding: utf-8 -*-
"""
    @Time : 2023/1/30/030 18:08
    @Author : 李子
    @Url : https://github.com/kslz
"""
import configparser
import os

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QTableWidgetItem, QPushButton, QLabel

from ui.mygui import *
from ui.ui_select_dataset import Ui_MainWindow
from ui.ui_select_workspace import Ui_Form
from utils import global_obj
from utils.log import creatlogger
from utils.tools import update_ini_config, inti_workspace


def main():
    global guilogger
    global config
    config = global_obj.get_value("config")
    guilogger = creatlogger("guilogger")
    app = QApplication([])
    select_workspace_window = SelectWorkspaceWindow()
    select_dataset_window = SelectDatasetWindow()
    select_workspace_window.show_select_dataset_window.connect(select_dataset_window.show)

    select_workspace_window.show()
    guilogger.debug("进入工作区选择窗口")





    app.exec()


if __name__ == "__main__":
    main()
