# -*- coding: utf-8 -*-
"""
    @Time : 2023/11/27 14:40
    @Author : 李子
    @Url : https://github.com/kslz
"""
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QCheckBox, QSpacerItem, QSizePolicy, QButtonGroup, QPushButton

from domain.repositories.repositories import SearchField
from presentation.my_qt_class.my_base_dialog import BaseDialog
from presentation.pyuic.ui_ColumnsSettingDialog import Ui_ColumnsSettingDialog


class ColumnsSettingDialog(BaseDialog):
    saveWindowClosed = Signal()

    def __init__(self, parent, config):
        super().__init__(parent)
        # 使用ui文件导入定义界面类
        self.ui = Ui_ColumnsSettingDialog()
        # 初始化界面
        self.ui.setupUi(self)
        self.my_init()

        self.config = config
        self.sf = SearchField()
        self.btn_group = QButtonGroup()
        self.btn_group.setExclusive(False)
        self.add_info_line()

        self.ui.pushButton_ok.clicked.connect(self.update_check_colums)
        self.ui.pushButton_cancel.clicked.connect(self.close)



    def add_info_line(self):
        check_colums_list = self.config["program_configs"]["default_columns"].split(",")
        for colum_name in self.sf.get_all_keys():
            checkbox = QCheckBox(colum_name, self)
            # checkbox.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
            if colum_name in check_colums_list:
                checkbox.setChecked(True)
            self.ui.gridLayout.addWidget(checkbox)
            self.btn_group.addButton(checkbox)
        spacer_item = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.ui.gridLayout.addItem(spacer_item)

    def update_check_colums(self):
        new_list = []
        checked_checkboxes = [button for button in self.btn_group.buttons() if button.isChecked()]
        for checkbox in checked_checkboxes:
            new_list.append(checkbox.text())
        self.config['program_configs']['default_columns'] = ",".join(new_list)
        self.config.write_to_file()
        self.saveWindowClosed.emit()
        self.close()

    def closeEvent(self, event):
        super().closeEvent(event)


