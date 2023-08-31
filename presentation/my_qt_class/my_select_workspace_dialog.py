# -*- coding: utf-8 -*-
"""
    @Time : 2023/08/25 14:30
    @Author : 李子
    @Url : https://github.com/kslz
    工作区选择界面
"""
import sys

from PySide6.QtWidgets import QApplication

from presentation.my_qt_class.my_base_dialog import BaseStartDialog
from presentation.pyuic.ui_SelectWorkspaceDialog import Ui_SelectWorkspaceDialog
from utils.init_tools import read_ini_config


class SelectWorkspaceDialog(BaseStartDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.workspace_path = None
        # 使用ui文件导入定义界面类
        self.ui = Ui_SelectWorkspaceDialog()
        # 初始化界面
        self.ui.setupUi(self)
        self.my_init()
        self.ui.submit_button.clicked.connect(self.submit)
        self.ui.cancel_button.clicked.connect(self.cancel)

        # 读取配置文件
        config = read_ini_config()
        default_workspace_path = config["program_configs"]["default_workspace"]
        self.ui.lineEdit.setText(default_workspace_path)

    def submit(self):
        workspace_path = self.ui.lineEdit.text().strip()
        if workspace_path == "":
            workspace_path = ".\workspace"
        self.workspace_path = workspace_path
        self.accept()

    def cancel(self):
        self.reject()
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    workspace_dialog = SelectWorkspaceDialog()
    workspace_dialog.exec()
    sys.exit(app.exec())
