# -*- coding: utf-8 -*-
"""
    @Time : 2023/08/25 10:36
    @Author : 李子
    @Url : https://github.com/kslz
    优化逻辑协议定义
"""
from typing import Protocol


class OptimizationService(Protocol):

    def need_args(self) -> dict:
        """
        返回所需参数信息字典
        """
        pass

    def init_data(self, args_dict: dict):
        pass

    def optimize_data(self):
        pass
