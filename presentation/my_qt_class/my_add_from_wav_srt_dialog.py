# -*- coding: utf-8 -*-
"""
    @Time : 2023/9/17 22:07
    @Author : 李子
    @Url : https://github.com/kslz
"""
import os

import pysrt
from PySide6.QtWidgets import QFileDialog, QTableWidgetItem
from pydub import AudioSegment

from application.services.input_service import InputByWavSrtService
from domain.service.input_service_protocol import InputService
from infrastructure.file_io import copy_file_to_workspace
from presentation.my_qt_class.my_base_dialog import BaseDialog
from presentation.my_qt_class.my_tool_function import modify_table_style
from presentation.pyuic.ui_AddFromWavSrtDialog import Ui_AddFromWavSrtDialog
from utils.tools import get_audio_duration


class AddFromWavSrtDialog(BaseDialog):
    def __init__(self, parent, dataset_id):
        super().__init__(parent)
        # 使用ui文件导入定义界面类
        self.ui = Ui_AddFromWavSrtDialog()
        # 初始化界面
        self.ui.setupUi(self)
        self.my_init()

        self.ui.lineEdit_wav.setReadOnly(True)
        self.ui.lineEdit_srt.setReadOnly(True)
        self.file_paths = {}
        self.dataset_id = dataset_id
        self.ui.pushButton_select_wav.clicked.connect(self.select_file_wav)
        self.ui.pushButton_select_srt.clicked.connect(self.select_file_srt)
        self.ui.pushButton_submit.clicked.connect(self.save_to_dataset)
        self.ui.pushButton_back.clicked.connect(self.go_back)

        self.input_service = InputByWavSrtService()
        self.need_optimization_args = self.input_service.optimization_args
        self.init_optimization_tbl()

    def init_optimization_tbl(self):
        tbl = self.ui.tableWidget_optimization
        tbl.setRowCount(0)
        properties = [
            ("是否启用", False, 80),
            ("优化名称", False, 150),
            ("所需参数", True, 130),
        ]
        modify_table_style(tbl, properties)
        print(self.need_optimization_args)
        for name, args_info in self.need_optimization_args.items():
            row = tbl.rowCount()
            tbl.insertRow(row)
            info_cell = QTableWidgetItem()
            info_cell.setText(args_info['show_name'])
            info_cell.setToolTip(f"<pre>{args_info['show_name']}</pre>")
            tbl.setItem(row, 1, info_cell)

            pass

    def select_file_wav(self):
        filePath, _ = QFileDialog.getOpenFileName(
            self,  # 父窗口对象
            "选择你要导入的音频文件",  # 标题
            r"./",  # 起始目录
            "音频文件 (*)"  # 选择类型过滤项，过滤内容在括号中
        )
        self.file_paths["wav"] = filePath
        self.ui.lineEdit_wav.setText(filePath)

    def select_file_srt(self):
        filePath, _ = QFileDialog.getOpenFileName(
            self,  # 父窗口对象
            "选择你要导入的字幕文件",  # 标题
            r"./",  # 起始目录
            "字幕文件 (*.srt)"  # 选择类型过滤项，过滤内容在括号中
        )
        self.file_paths["srt"] = filePath
        self.ui.lineEdit_srt.setText(filePath)

    def save_to_dataset(self):
        wav_path = self.file_paths["wav"]
        workspace_path = self.workspace.workspace_path
        wav_path = copy_file_to_workspace(wav_path, self.workspace.file_path)
        srt_path = self.file_paths["srt"]
        speaker = self.ui.lineEdit_spk.text()
        is_merge_srt = self.ui.checkBox_ismerge.isChecked()

        if wav_path.strip() == "" or None:
            self.ui.error_lable.setText("输入音频路径为空")
            return
        if srt_path.strip() == "" or None:
            self.ui.error_lable.setText("输入字幕路径为空")
            return
        if speaker.strip() == "" or None:
            self.ui.error_lable.setText("输入发音人为空")
            return

        if os.path.isfile(wav_path) and os.path.isfile(srt_path):
            try:
                duration = get_audio_duration(wav_path)
            except:
                self.ui.error_lable.setText("音频文件解析失败，请检查所选文件是否正确")
                self.logger.error(f"音频文件 {wav_path} 解析失败，请检查所选文件是否正确")
                return

            try:
                mysrt = pysrt.open(srt_path)
                if len(mysrt) == 0:
                    raise Exception('所选文件不是SRT格式的文件！')

            except:
                self.ui.error_lable.setText(f"字幕文件解析失败，请检查所选文件是否正确")
                self.logger.error(f"字幕文件 {srt_path} 解析失败，请检查所选文件是否正确")
                return

            srt_end_time = mysrt[-1].end.ordinal / 1000
            if srt_end_time > duration:
                self.ui.error_lable.setText(f"字幕文件长度长于音频文件，请检查是否选择错误")
                self.logger.error(f"字幕文件长度长于音频文件，请检查是否选择错误")
                return
            self.input_service.init_info(dataset_id=self.dataset_id,
                                         wav_path=wav_path,
                                         srt_path=srt_path,
                                         speaker=speaker,
                                         optimization={"OptimizationMergeService": {"min_time": 40}})
            if self.input_service.input_data():
                self.parent().refresh_table()
                self.close()




        else:
            self.ui.error_lable.setText("音频文件或字幕文件不存在！")
            self.logger.error(f"音频文件 {wav_path} 或字幕文件 {srt_path} 不存在")
        pass

    def go_back(self):
        self.close()
