# -*- coding: utf-8 -*-
"""
    @Time : 2023/10/08 17:12
    @Author : 李子
    @Url : https://github.com/kslz
"""
from PySide6.QtWidgets import QPushButton

from domain.repositories.repositories import update_is_delete


class DeleteBTN(QPushButton):
    def __init__(self, text, info_id, parent, info_is_del):
        super().__init__(text, parent)
        self.info_id = info_id
        self.info_is_del = info_is_del
        if self.info_is_del == False:
            self.setText("删除")
        else:
            self.setText("恢复")

        self.clicked.connect(self.change_is_del_sound)

    def change_is_del_sound(self):
        # 肯定是伪删除
        new_is_del = True if self.info_is_del == False else False
        update_is_delete(self.info_id, new_is_del)
        self.info_is_del = new_is_del
        if self.info_is_del == False:
            self.setText("删除")
        else:
            self.setText("恢复")
