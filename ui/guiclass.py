# -*- coding: utf-8 -*-
"""
    @Time : 2023/1/30/030 18:08
    @Author : 李子
    @Url : https://github.com/kslz
"""
import configparser
import os

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget

from ui.ui_select_workspace import Ui_Form
from utils import global_obj
from utils.log import creatlogger
from utils.tools import update_ini_config, inti_workspace


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
        self.ui.lineEdit.setText(default_workspace)

    def close_program(self):
        self.close()

    def get_workspace(self):
        workspace_path = self.ui.lineEdit.text()
        global_obj.set_value("workspace_path",workspace_path)
        inti_workspace(workspace_path)
        config["program_configs"]["default_workspace"] = workspace_path
        update_ini_config(config)

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
