# -*- coding: utf-8 -*-
"""
    @Time : 2023/09/28 14:48
    @Author : 李子
    @Url : https://github.com/kslz
"""
import os

from domain.repositories.repositories import get_file_raw_path_by_dataset_id, del_info_by_raw_file_path
from infrastructure.file_io import del_file_by_path
from presentation.my_qt_class.my_base_dialog import BaseDialog
from presentation.pyuic.ui_DeleteInfoByWavDialog import Ui_DeleteInfoByWavDialog


class DeleteInfoByWavDialog(BaseDialog):
    def __init__(self, parent, dataset_id):
        super().__init__(parent)
        # 使用ui文件导入定义界面类
        self.ui = Ui_DeleteInfoByWavDialog()
        # 初始化界面
        self.ui.setupUi(self)
        self.dataset_id = dataset_id
        self.add_file_select()
        self.ui.pushButton_submit.clicked.connect(self.del_info_and_file)
        self.ui.pushButton_back.clicked.connect(self.close)

    def add_file_select(self):
        self.ui.comboBox_files.clear()
        results = get_file_raw_path_by_dataset_id(self.dataset_id)
        for result in results:
            file_path = result.info_raw_file_path
            file_name = os.path.basename(file_path)
            file_name = os.path.splitext(file_name)[0]
            self.ui.comboBox_files.addItem(file_name, file_path)

    def del_info_and_file(self):
        file_path = self.ui.comboBox_files.currentData()
        self.logger.info(f"删除{file_path}")
        try:
            del_info_by_raw_file_path(file_path)
        except:
            self.logger.error(f"文件 {file_path} 关联的数据删除失败")
        else:
            self.logger.info(f"文件 {file_path} 关联的数据已被删除")
            if os.path.exists(file_path):
                try:
                    del_file_by_path(file_path)
                    self.logger.info(f"文件 {file_path} 已被删除")
                except:
                    self.logger.error(f"文件 {file_path} 删除失败")
        self.add_file_select()
        self.parent().refresh_table()
        self.close()
