# -*- coding: utf-8 -*-
"""
    @Time : 2023/1/30/030 18:08
    @Author : 李子
    @Url : https://github.com/kslz
"""

from ui.mygui import *
from utils import global_obj
from utils.log import creatlogger


def main():
    global guilogger
    global config
    config = global_obj.get_value("config")
    guilogger = creatlogger("guilogger")
    app = QApplication([])
    select_workspace_window = SelectWorkspaceWindow()
    select_dataset_window = SelectDatasetWindow()
    select_workspace_window.show_select_dataset_window.connect(select_dataset_window.add_dataset_data)
    select_workspace_window.show_select_dataset_window.connect(select_dataset_window.show)

    select_workspace_window.show()
    guilogger.debug("进入工作区选择窗口")





    app.exec()


if __name__ == "__main__":
    main()
