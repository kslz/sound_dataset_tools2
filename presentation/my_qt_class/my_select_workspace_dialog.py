# -*- coding: utf-8 -*-
"""
    @Time : 2023/08/25 14:30
    @Author : 李子
    @Url : https://github.com/kslz
"""
import sys

from PySide6.QtWidgets import QApplication

from presentation.my_qt_class.my_base_dialog import BaseDialog
from presentation.pyuic.ui_SelectWorkspaceDialog import Ui_SelectWorkspaceDialog


class SelectWorkspaceDialog(BaseDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        # 使用ui文件导入定义界面类
        self.ui = Ui_SelectWorkspaceDialog()
        # 初始化界面
        self.ui.setupUi(self)
        self.my_init()
        self.ui.submit_button.clicked.connect(self.submit)
        self.ui.cancel_button.clicked.connect(self.cancel)

    def submit(self):
        workspace_path = self.ui.lineEdit.text()
        print(workspace_path)
        self.accept()

    def cancel(self):
        self.reject()
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    workspace_dialog = SelectWorkspaceDialog()
    workspace_dialog.exec()
    sys.exit(app.exec())
