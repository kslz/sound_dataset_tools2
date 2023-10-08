# -*- coding: utf-8 -*-
"""
    @Time : 2023/10/01 21:14
    @Author : 李子
    @Url : https://github.com/kslz
"""
from PySide6.QtCore import QRect, Signal

from domain.repositories.repositories import get_info_by_id, update_info
from presentation.my_qt_class.my_audio_button import AudioButton, AudioNowButton
from presentation.my_qt_class.my_base_dialog import BaseDialog
from presentation.pyuic.ui_EditInfoDialog import Ui_EditInfoDialog


class EditInfoDialog(BaseDialog):
    windowClosed = Signal()

    def __init__(self, parent, info_id=None):
        super().__init__(parent)
        # 使用ui文件导入定义界面类
        self.wav_path = None
        self.start_time = None
        self.end_time = None
        self.text = None
        self.speaker = None
        self.ui = Ui_EditInfoDialog()
        # 初始化界面
        self.ui.setupUi(self)
        self.my_init()

        self.info_id = info_id
        self.add_info()
        self.ui.pushButton_3.clicked.connect(self.update_info)
        self.ui.pushButton_2.clicked.connect(self.close)

    def add_info(self):
        info = get_info_by_id(self.info_id)
        self.wav_path = info.info_raw_file_path
        self.start_time = str(info.info_start_time)
        self.end_time = str(info.info_end_time)
        self.text = info.info_text
        self.speaker = info.info_speaker

        self.ui.lineEdit_info_text.setText(self.text)
        self.ui.lineEdit_info_starttime.setText(self.start_time)
        self.ui.lineEdit_info_endtime.setText(self.end_time)
        self.ui.label_info_id.setText(str(self.info_id))
        self.ui.label_info_speaker.setText(self.speaker)

        start_time = self.ui.lineEdit_info_starttime.text()
        end_time = self.ui.lineEdit_info_endtime.text()

        self.btn_shiting = AudioNowButton(self.wav_path, int(start_time), int(end_time), self)
        self.btn_shiting.clicked.connect(self.shiting)
        self.btn_shiting.setGeometry(QRect(290, 20, 91, 24))

    def shiting(self):
        start_time = self.ui.lineEdit_info_starttime.text()
        end_time = self.ui.lineEdit_info_endtime.text()
        self.btn_shiting.on_button_clicked_new(start_time, end_time)

    def update_info(self):
        text = self.ui.lineEdit_info_text.text()
        start_time = self.ui.lineEdit_info_starttime.text()
        end_time = self.ui.lineEdit_info_endtime.text()
        update_info(text, start_time, end_time, self.info_id)
        self.close()

    def closeEvent(self, event):
        self.windowClosed.emit()
        super().closeEvent(event)
