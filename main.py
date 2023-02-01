# -*- coding: utf-8 -*-
"""
    @Time : 2023/1/30/030 17:53
    @Author : 李子
    @Url : https://github.com/kslz
"""
import configparser

import ui.guiclass
from utils import global_obj
from utils.tools import init_program


def main():
    ini_path = "conf/config.ini"
    global_obj._init()
    init_program()
    config = global_obj.get_value("config")
    config: configparser.ConfigParser
    ui.guiclass.main()

    pass


if __name__ == '__main__':
    main()
