# -*- coding: utf-8 -*-
"""
    @Time : 2023/09/11 18:27
    @Author : 李子
    @Url : https://github.com/kslz
    存放ui相关工具函数
"""
from PySide6.QtWidgets import QTableWidget, QHeaderView


def modify_table_style(table: QTableWidget, properties: list):

    header = table.horizontalHeader()
    header.setSectionResizeMode(QHeaderView.Interactive)





    pass
