# -*- coding: utf-8 -*-
"""
    @Time : 2024/01/21 22:08
    @Author : 李子
    @Url : https://github.com/kslz
    检查输入字段是否正确的函数
"""


def check_not_empty(text, name):
    if text is None or len(text.strip()) == 0:
        return False, f"{name} 字段不能为空"
    else:
        return True, None


def check_is_type(text, need_type, name):
    try:
        need_type(text)
    except:
        return False, f"{name} 字段不是 {str(need_type)} 类型"
    else:
        return True, None


if __name__ == '__main__':
    print(check_is_type("-666", int, "姓名"))
