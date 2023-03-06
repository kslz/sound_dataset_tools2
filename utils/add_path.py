# -*- coding: utf-8 -*-
"""
    @Time : 2023/3/6/006 9:42
    @Author : 李子
    @Url : https://github.com/kslz
"""
import os

if os.path.isfile(os.path.join("./lib/ffmpeg/", "ffmpeg.exe")):
    ffmpeg_path = "./lib/ffmpeg/"
else:
    ffmpeg_path = ""
os.environ["PATH"] += os.pathsep + os.path.dirname(ffmpeg_path)