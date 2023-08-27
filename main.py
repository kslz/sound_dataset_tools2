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



def main():
    app = QApplication(sys.argv)

    select_dataset_main_window = SelectDatasetMainWindow()
    select_workspace_dialog = SelectWorkspaceDialog()

    if select_workspace_dialog.exec() == QDialog.Accepted:
        select_dataset_main_window.show()
    else:
        quit()

    app.exec()

    # app = QApplication(sys.argv)
    #
    # window1 = Window1()
    # if window1.exec() == QDialog.Accepted:
    #     value = window1.value
    #     window2 = Window2(value)
    #     window2.show()
    #
    # sys.exit(app.exec())

    pass


if __name__ == "__main__":
    main()
