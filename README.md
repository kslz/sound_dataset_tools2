# sound_dataset_tools2

## 介绍
本工具主要用于快速制作语音数据集，可一键导出VITS等项目所需的训练数据集

## 软件架构
数据库：sqlite、peewee
界面：PySide6
音频处理：FFMPEG、pydub等


## 安装教程

1. 克隆本项目

   gitee:

   ```
   git clone https://gitee.com/kslizi/sound_dataset_tools2.git
   ```

   github:

   ```
   git clone https://github.com/kslz/sound_dataset_tools2.git
   ```

2. 安装[ffmpeg](https://www.gyan.dev/ffmpeg/builds/ffmpeg-git-full.7z)

3. 安装其他库

   ```
   pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
   ```

   

## 使用说明

1. 运行项目

   ```
   python main.py
   ```

2. 待续......

## 开发计划

编译exe版本

通过ASR标注

应用语音评测

应用声纹识别

......

