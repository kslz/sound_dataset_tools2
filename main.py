# -*- coding: utf-8 -*-
"""
    @Time : 2023/1/30/030 17:53
    @Author : 李子
    @Url : https://github.com/kslz
"""
import utils.add_path
import configparser

from utils import global_obj
from utils.tools import init_program
import ui.guiclass


def main():
    init_program()
    config = global_obj.get_value("config")
    config: configparser.ConfigParser
    ui.guiclass.main()

    pass


if __name__ == '__main__':
    main()
