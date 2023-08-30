# -*- coding: utf-8 -*-
"""
    @Time : 2023/08/29 9:20
    @Author : 李子
    @Url : https://github.com/kslz
    存放工厂函数
"""
from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton, QSizePolicy


def make_operate_btns(parent, data_list: list, length_list=None):
    """
    生成表格中的编辑列按钮组

    """

    caozuo_widget = QWidget()
    layout = QHBoxLayout()
    layout.setContentsMargins(1, 1, 1, 1)
    layout.setSpacing(1)
    caozuo_widget.setLayout(layout)

    if length_list is None:
        length_list = []
        for data in data_list:
            length_list.append(len(data[0]))

    for i, data in enumerate(data_list):
        btn = QPushButton(data[0])

        # 创建一个QSizePolicy对象，并设置水平拉伸因子
        btn.setMinimumWidth(1)
        size_policy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        size_policy.setHorizontalStretch(length_list[i])
        btn.setSizePolicy(size_policy)

        btn.clicked.connect(data[1])
        layout.addWidget(btn)

    return caozuo_widget
