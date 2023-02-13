# -*- coding: utf-8 -*-
"""
    神奇的全局变量
    @Time : 2023/2/1/001 17:07
    @Author : 李子
    @Url : https://github.com/kslz
"""


def _init():
    global _global_dict
    _global_dict = {}


def set_value(key, value):
    """ 定义一个全局变量 """
    _global_dict[key] = value


def get_value(key, defValue=None):
    """ 获取一个全局变量，不存在则返回默认值 """
    try:
        return _global_dict[key]
    except KeyError:
        return defValue

_init()
