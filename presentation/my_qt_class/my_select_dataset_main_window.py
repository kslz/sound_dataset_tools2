# -*- coding: utf-8 -*-
"""
    @Time : 2023/8/27 14:56
    @Author : 李子
    @Url : https://github.com/kslz
"""
from presentation.my_qt_class.my_base_main_window import BaseMainWindow
from presentation.pyuic.ui_SelectDatasetMainWindow import Ui_SelectDatasetMainWindow


class SelectDatasetMainWindow(BaseMainWindow):
    def __init__(self, tool_workspace):
        super().__init__()
        # 使用ui文件导入定义界面类
        self.ui = Ui_SelectDatasetMainWindow()
        # 初始化界面
        self.ui.setupUi(self)
        self.my_init()

        self.tool_workspace = tool_workspace
        print(self.tool_workspace.db_file_path)
