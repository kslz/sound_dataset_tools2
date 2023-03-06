# sound_dataset_tools2

## 介绍
本工具主要用于快速制作语音数据集，可一键导出VITS等项目所需的训练数据集

特色：

GUI界面！

支持 音频+字幕/纯音频自动切割 两种方式导入数据

自动优化了音频的切割效果，（尽量）避免出现断音

可直接导出符合VITS等项目要求的数据集格式，声道数/采样率均可设置

**中文文档**

## 软件架构
数据库：sqlite、peewee
界面：PySide6
音频处理：FFMPEG、pydub等


## 安装教程

### 运行编译好的exe文件











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

导出多发音人数据集

......

