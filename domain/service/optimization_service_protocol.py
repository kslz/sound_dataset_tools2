# -*- coding: utf-8 -*-
"""
    @Time : 2023/08/25 10:36
    @Author : 李子
    @Url : https://github.com/kslz
    优化逻辑协议定义
"""
from typing import Protocol


class OptimizationService(Protocol):
    def optimize_data(self):
        pass
