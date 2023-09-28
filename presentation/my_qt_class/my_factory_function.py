# -*- coding: utf-8 -*-
"""
    @Time : 2023/08/29 9:20
    @Author : 李子
    @Url : https://github.com/kslz
    存放工厂函数
"""
import copy

from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton, QSizePolicy


def make_operate_btns(parent, data_list: list):
    """
    生成表格中的操作列按钮组（只会生成QPushButton）

    例：data_list = [
        {'text': '进入', 'slot': lambda: self.open_dataset_window(dataset_id)},
        {'text': '编辑', 'slot': lambda: self.edit_dataset(dataset_id)},
        {'text': '删除', 'slot': lambda: self.del_dataset(dataset_id, dataset_name)},
    ]


    :param parent:
    :param data_list: 格式为[['text':"按钮名",'slot':要绑定的槽函数,'length':指定的按钮宽度(不填则默认为一个字占用1比例单位)]...]
    :param btns:
    :param length_list:
    :return:
    """

    caozuo_widget = QWidget()
    layout = QHBoxLayout()
    layout.setContentsMargins(1, 1, 1, 1)
    layout.setSpacing(1)
    caozuo_widget.setLayout(layout)

    for data in data_list:
        data: dict
        btn = QPushButton(data['text'], parent=parent)
        # 创建一个QSizePolicy对象，并设置水平拉伸因子
        btn.setMinimumWidth(1)
        size_policy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        size_policy.setHorizontalStretch(data.get('length', len(data['text'])))
        btn.setSizePolicy(size_policy)
        btn.clicked.connect(data['slot'])
        layout.addWidget(btn)

    return caozuo_widget


def make_my_operate_btns(parent, data_list: list):
    """
    生成表格中的操作列按钮组（需要传入按钮类型，支持自定义按钮）

    例：data_list = [
        {'btn': AudioButton,'args': {'wav_path': info_file_path, 'start_time': info_start_time, 'end_time': info_end_time,'parent': self}, 'slot': None, 'length': 2},
        {'btn': QPushButton, 'args': {'text': '快速导出', 'parent': self}, 'slot': lambda: self.fast_output(info_id)},
        {'btn': QPushButton, 'args': {'text': '编辑', 'parent': self}, 'slot': lambda: self.edit_info(info_id)},
        {'btn': QPushButton, 'args': {'text': '删除', 'parent': self}, 'slot': lambda: self.del_info(info_id, info_is_del)},
    ]


    :param parent:
    :param data_list: 格式为[['text':"按钮名",'slot':要绑定的槽函数,'length':指定的按钮宽度(不填则默认为一个字占用1比例单位)]...]
    :param btns:
    :param length_list:
    :return:
    """

    caozuo_widget = QWidget()
    layout = QHBoxLayout()
    layout.setContentsMargins(0, 0, 0, 0)
    layout.setSpacing(1)
    caozuo_widget.setLayout(layout)

    for data in data_list:
        data: dict
        btn = data['btn'](**data['args'])
        # 创建一个QSizePolicy对象，并设置水平拉伸因子
        btn.setMinimumWidth(1)
        size_policy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        size_policy.setHorizontalStretch(data.get('length', len(data['args'].get('text', "默认"))))
        btn.setSizePolicy(size_policy)
        if data['slot']:
            btn.clicked.connect(data['slot'])
        layout.addWidget(btn)

    return caozuo_widget
