# -*- coding: utf-8 -*-
"""
    @Time : 2023/08/28 16:47
    @Author : 李子
    @Url : https://github.com/kslz
    工具函数
"""
import math
import string


def huanhang(text: str, num=30):
    """
    长文本换行

    """
    # 这么简单的需求前前后后墨迹了一个小时才解决，难顶
    if text == None:
        return None
    # 定义字符宽度
    WIDTH = num
    CHINESE_WIDTH = 2
    ENGLISH_WIDTH = 1

    # 定义中英文标点
    punctuation = string.punctuation + '，。！？、；：‘’“”《》【】（）'

    # 将字符串分割成多行
    lines = []
    for line in text.split('\n'):
        # 每行的可用宽度
        line_width = 0
        for c in line:
            if c in punctuation:
                line_width += CHINESE_WIDTH
            elif c.isascii():
                line_width += ENGLISH_WIDTH
            else:
                line_width += CHINESE_WIDTH
        if line_width <= WIDTH:
            lines.append(line)
            continue
        line_now = ""
        width_now = 0
        for i in range(len(line)):
            line_now += line[i]
            if line[i] in punctuation:
                width_now += CHINESE_WIDTH
            elif line[i].isascii():
                width_now += ENGLISH_WIDTH
            else:
                width_now += CHINESE_WIDTH

            if i < len(line) - 1:
                if width_now == WIDTH - 1:
                    if line[i + 1].isascii():
                        continue
                    else:
                        # line_now += "\n"
                        lines.append(line_now)
                        line_now = ""
                        width_now = 0
            if width_now == WIDTH:
                # line_now += "\n"
                lines.append(line_now)
                line_now = ""
                width_now = 0
        lines.append(line_now)

    formatted_text = '\n'.join(lines)
    return formatted_text

def check_pagenumber_is_out(total_count, page_number, page_size):
    """
    验证页码数是否超过上限并如超过则返回上限页码数，不超过则返回当前页码数

    :param total_count: 数据总数
    :param page_number: 页码数
    :param page_size: 分页大小
    :return: 返回页码数
    """
    if page_number * page_size > total_count:
        return True, math.ceil(total_count / page_size)
    else:
        return False, page_number