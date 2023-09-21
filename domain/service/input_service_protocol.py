# -*- coding: utf-8 -*-
"""
    @Time : 2023/9/17 23:23
    @Author : 李子
    @Url : https://github.com/kslz
"""
from typing import Protocol


class InputService(Protocol):

    def init_info(self, **kwargs):
        pass

    def input_data(self) -> bool:
        pass
