# -*- coding: utf-8 -*-
"""
    @Time : 2023/09/11 18:27
    @Author : 李子
    @Url : https://github.com/kslz
    存放ui相关工具函数
"""
from PySide6.QtWidgets import QTableWidget, QHeaderView


def modify_table_style(table: QTableWidget, properties: list):
    """
    传入QTableWidget和列属性list，自动添加列进表格中
    例:[("列名1", False, 100),("列名2", True, 200),...]

    :param table: QTableWidget对象
    :param properties: 由元组组成的列表，元组格式为(列名, 是否为自动宽度列, 列宽)

    """
    table.setColumnCount(len(properties))
    header_list = [item[0] for item in properties]
    table.setHorizontalHeaderLabels(header_list)
    header = table.horizontalHeader()
    for column in range(len(properties)):
        info = properties[column]
        if info[1]:
            header.setSectionResizeMode(column, QHeaderView.ResizeMode.Stretch)
            header.setMinimumSectionSize(info[2])
        else:
            header.setSectionResizeMode(column, QHeaderView.ResizeMode.Fixed)
            table.setColumnWidth(column, info[2])

    return True
