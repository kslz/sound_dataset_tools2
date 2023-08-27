# -*- coding: utf-8 -*-
"""
    @Time : 2023/08/21 15:33
    @Author : 李子
    @Url : https://github.com/kslz
    梦开始的地方
"""
import sys

from PySide6.QtWidgets import QApplication, QDialog

from presentation.my_qt_class.my_select_dataset_main_window import SelectDatasetMainWindow
from presentation.my_qt_class.my_select_workspace_dialog import SelectWorkspaceDialog
from utils.init_tools import ToolWorkspace


def main():
    app = QApplication(sys.argv)

    select_workspace_dialog = SelectWorkspaceDialog()

    if select_workspace_dialog.exec() == QDialog.Accepted:
        tool_workspace = ToolWorkspace(select_workspace_dialog.workspace_path)
        tool_workspace.check_and_create_files()
        select_dataset_main_window = SelectDatasetMainWindow(tool_workspace)
        select_dataset_main_window.show()
    else:
        quit()

    app.exec()

    pass


if __name__ == "__main__":
    main()
