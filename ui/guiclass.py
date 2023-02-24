# -*- coding: utf-8 -*-
"""
    @Time : 2023/1/30/030 18:08
    @Author : 李子
    @Url : https://github.com/kslz
"""
from PySide6.QtWidgets import QApplication

from ui.mygui import *
from utils import global_obj
from utils.log import creatlogger


def main():
    global config
    config = global_obj.get_value("config")
    app = QApplication([])
    select_workspace_window = SelectWorkspaceWindow()
    select_dataset_window = SelectDatasetWindow()

    # 绑定【展示数据集选择页面】的信号和槽，并且提前查询数据库，将数据库信息填入表格中
    select_workspace_window.show_select_dataset_window.connect(select_dataset_window.add_dataset_data)
    select_workspace_window.show_select_dataset_window.connect(select_dataset_window.show)

    # 绑定添加数据集按钮信号和对应的槽
    select_dataset_window.ui.pushButton.clicked.connect(select_dataset_window.open_add_dataset_window)





    select_workspace_window.show()
    guilogger.debug("进入工作区选择窗口")





    app.exec()


if __name__ == "__main__":
    main()
