# -*- coding: utf-8 -*-
"""
    @Time : 2023/10/01 21:14
    @Author : 李子
    @Url : https://github.com/kslz
"""
from presentation.my_qt_class.my_base_dialog import BaseDialog
from presentation.pyuic.ui_EditInfoDialog import Ui_EditInfoDialog


class EditInfoDialog(BaseDialog):
    def __init__(self, parent, info_id=None):
        super().__init__(parent)
        # 使用ui文件导入定义界面类
        self.ui = Ui_EditInfoDialog()
        # 初始化界面
        self.ui.setupUi(self)
        self.my_init()

        self.info_id = info_id
        self.add_info()


    def add_info(self):
        pass

