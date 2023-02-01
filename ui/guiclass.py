# -*- coding: utf-8 -*-
"""
    @Time : 2023/1/30/030 18:08
    @Author : 李子
    @Url : https://github.com/kslz
"""
from PySide6.QtWidgets import QApplication, QMainWindow

from ui.ui_select_workspace import Ui_Form


class SelectWorkspaceWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # 使用ui文件导入定义界面类
        self.ui = Ui_Form()
        # 初始化界面
        self.ui.setupUi(self)

    pass


def main():
    app = QApplication([])
    select_workspace_window = SelectWorkspaceWindow()
    select_workspace_window.show()
    print("展示工作区选择窗口")

    app.exec()


if __name__ == "__main__":
    main()
