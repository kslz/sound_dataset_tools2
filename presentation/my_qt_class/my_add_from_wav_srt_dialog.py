# -*- coding: utf-8 -*-
"""
    @Time : 2023/9/17 22:07
    @Author : 李子
    @Url : https://github.com/kslz
"""
import os

import pysrt
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtSvgWidgets import QSvgWidget
from PySide6.QtWidgets import QFileDialog, QTableWidgetItem, QWidget, QHBoxLayout, QLabel, QCheckBox, QToolTip, \
    QVBoxLayout
from pydub import AudioSegment

from application.services.input_service import InputByWavSrtService
from domain.service.input_service_protocol import InputService
from infrastructure.file_io import copy_file_to_workspace
from presentation.my_qt_class.my_base_dialog import BaseDialog
from presentation.my_qt_class.my_tool_function import modify_table_style
from presentation.my_qt_class.my_widgets import MyClickableWidget, MyCheckOkLineEdit
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
        self.page_input = {}
        self.need_sound = False

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
            ("启用", False, 40),
            ("优化名称", False, 150),
            ("所需参数", True, 130),
        ]
        modify_table_style(tbl, properties)
        self.logger.debug(f"获取到优化信息{self.need_optimization_args}")
        for name, args_info in self.need_optimization_args.items():
            info_obj = {}
            row = tbl.rowCount()
            tbl.insertRow(row)

            use_widget = MyClickableWidget()
            use_checkbox = QCheckBox()
            use_checkbox.setStyleSheet('''
                QCheckBox::indicator { width: 30px; height: 30px;}
                QCheckBox::indicator:checked {
                    image: url(img/checked.svg);
                }
                QCheckBox::indicator {
                image: url(img/unchecked.svg);
                }
            ''')
            if args_info['default_check']:
                use_checkbox.setChecked(True)

            use_layout = QHBoxLayout(use_widget)
            use_layout.setContentsMargins(1, 1, 1, 1)
            use_layout.setSpacing(0)
            use_layout.setAlignment(Qt.AlignCenter)
            use_layout.addWidget(use_checkbox)
            use_widget.clicked.connect(use_checkbox.click)
            tbl.setCellWidget(row, 0, use_widget)
            info_obj["use_checkbox"] = use_checkbox

            info_widget = QWidget()
            info_layout = QHBoxLayout(info_widget)
            info_layout.setContentsMargins(1, 1, 1, 1)
            info_layout.setSpacing(1)

            info_label = QLabel(args_info['show_name'])
            info_label.setToolTip(f"<pre>{args_info['show_name']}</pre>")
            help_widget = QSvgWidget()
            help_widget.load("img/基础_说明.svg")
            help_widget.setToolTip(f"<pre>{args_info['show_help']}</pre>")
            help_widget.setFixedSize(20, 20)

            info_layout.addWidget(info_label)
            info_layout.addWidget(help_widget)

            tbl.setCellWidget(row, 1, info_widget)

            args_widget = QWidget()
            args_layout = QVBoxLayout(args_widget)
            args_layout.setContentsMargins(1, 1, 1, 1)
            args_layout.setSpacing(1)
            args_obj_list = []
            for arg in args_info['args']:
                line_widget = QWidget()
                line_layout = QHBoxLayout(line_widget)
                line_layout.setContentsMargins(1, 1, 1, 1)
                line_layout.setSpacing(10)
                arg_label = QLabel(arg['show_text'])
                arg_line_edit = MyCheckOkLineEdit(arg['check'], arg['name'], arg['type'])
                arg_line_edit.setText(str(arg['default']))

                line_layout.addWidget(arg_label)
                line_layout.addWidget(arg_line_edit)

                args_layout.addWidget(line_widget)
                args_obj_list.append(arg_line_edit)
            info_obj['args'] = args_obj_list
            info_obj['need_sound'] = args_info['need_sound']
            tbl.setCellWidget(row, 2, args_widget)
            tbl.resizeRowToContents(row)
            self.page_input[name] = info_obj
        self.logger.debug(f"获取到程序优化区对象{self.page_input}")

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

    def get_and_check_optimization_args(self):
        result_dict = {}
        all_need_sound = False
        for name, args_obj in self.page_input.items():
            if args_obj['use_checkbox'].isChecked():
                all_dict = {}
                for arg_obj in args_obj['args']:
                    is_ok, msg = arg_obj.get_ok()
                    if is_ok:
                        all_dict[arg_obj.arg_name] = arg_obj.get_result()
                    else:
                        self.ui.error_lable.setText(msg)
                        return False, {}
                result_dict[name] = all_dict
                if args_obj['need_sound']:
                    all_need_sound = True
        self.need_sound = all_need_sound
        return True, result_dict

    def save_to_dataset(self):
        wav_path = self.file_paths["wav"]
        workspace_path = self.workspace.workspace_path
        # wav_path = copy_file_to_workspace(wav_path, self.workspace.file_path)
        srt_path = self.file_paths["srt"]
        speaker = self.ui.lineEdit_spk.text()

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
            result_ok, result = self.get_and_check_optimization_args()
            if result_ok:
                self.logger.debug(f"获取到优化参数result")

            else:
                return

            wav_path = copy_file_to_workspace(wav_path, self.workspace.file_path)
            self.input_service.init_info(dataset_id=self.dataset_id,
                                         wav_path=wav_path,
                                         srt_path=srt_path,
                                         speaker=speaker,
                                         need_sound=self.need_sound,
                                         optimization=result)
            if self.input_service.input_data():
                self.parent().refresh_table()
                self.close()




        else:
            self.ui.error_lable.setText("音频文件或字幕文件不存在！")
            self.logger.error(f"音频文件 {wav_path} 或字幕文件 {srt_path} 不存在")
        pass

    def go_back(self):
        self.close()
