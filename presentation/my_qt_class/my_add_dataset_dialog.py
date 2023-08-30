# -*- coding: utf-8 -*-
"""
    @Time : 2023/08/25 14:30
    @Author : 李子
    @Url : https://github.com/kslz
    工作区选择界面
"""
import peewee

from domain.repositories.repositories import *
from presentation.my_qt_class.my_base_dialog import BaseDialog
from presentation.pyuic.ui_AddDatasetDialog import Ui_AddDatasetDialog
from utils.logging_utils import LoggerSingleton


class AddDatasetDialog(BaseDialog):
    def __init__(self, parent, useby="add", dataset_id=None):
        super().__init__(parent)
        self.workspace_path = None
        # 使用ui文件导入定义界面类
        self.ui = Ui_AddDatasetDialog()
        # 初始化界面
        self.ui.setupUi(self)
        self.my_init()

        self.ui.buttonBox.rejected.connect(self.close)

        self.dataset_id = dataset_id

        if useby == "add":
            self.add_init()
        else:
            self.edit_init()

    def add_init(self):
        self.ui.buttonBox.accepted.connect(self.add_dataset)

    def edit_init(self):
        self.setWindowTitle("编辑数据集")
        self.ui.buttonBox.accepted.connect(self.edit_dataset)
        dataset = get_dataset_info_by_id(self.dataset_id)
        self.ui.lineEdit.setText(dataset.dataset_name)
        self.ui.textEdit.setText(dataset.dataset_info)

    def show_error(self, text):
        self.ui.label_3.setText(text)

    def add_dataset(self):
        dataset_name = self.ui.lineEdit.text()
        datset_info = self.ui.textEdit.toPlainText()
        if dataset_name == "":
            self.show_error("添加失败，数据集名称为空")
            return

        try:
            add_dataset(dataset_name, datset_info)
        except peewee.IntegrityError as e:
            if "UNIQUE constraint failed" in str(e):
                self.show_error("添加失败，数据集名称重复")
            else:
                # guilogger.error(e)

                pass
        else:
            logger = LoggerSingleton.get_logger()
            logger.info(f"添加数据集 {dataset_name} 成功")
            self.parent().add_dataset_data()
            self.close()

    def edit_dataset(self):

        pass
