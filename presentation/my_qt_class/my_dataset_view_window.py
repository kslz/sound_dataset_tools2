# -*- coding: utf-8 -*-
"""
    @Time : 2023/09/13 9:22
    @Author : 李子
    @Url : https://github.com/kslz
"""
from PySide6 import QtCore, QtGui
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QTableWidgetItem, QPushButton

from domain.repositories.repositories import *
from presentation.my_qt_class.my_add_from_wav_srt_dialog import AddFromWavSrtDialog
from presentation.my_qt_class.my_audio_button import AudioButton
from presentation.my_qt_class.my_base_main_window import BaseMainWindow
from presentation.my_qt_class.my_delete_info_by_wav_dialog import DeleteInfoByWavDialog
from presentation.my_qt_class.my_factory_function import *
from presentation.my_qt_class.my_tool_function import *
from presentation.pyuic.ui_DatasetViewMainWindow import Ui_DatasetViewMainWindow


class DatasetViewMainWindow(BaseMainWindow):
    closed = Signal()
    def __init__(self, dataset_id):
        super().__init__()
        # 使用ui文件导入定义界面类
        self.ui = Ui_DatasetViewMainWindow()
        # 初始化界面
        self.ui.setupUi(self)
        self.my_init()
        self.set_table_style()

        self.dataset_id = dataset_id
        self.page_number = 1
        self.page_size = 15
        self.refresh_table()

        # 连接信号
        self.ui.comboBox.currentIndexChanged.connect(self.change_page_number)
        self.ui.pushButton_add_wav_srt.clicked.connect(self.add_from_file_wav_srt)
        self.ui.pushButton_del_by_raw_wav.clicked.connect(self.open_del_info_by_wav_dialog)

    def set_table_style(self):
        # 数据集概览表格
        properties = [
            ("序号", False, 100),
            ("标注文本", True, 130),
            ("发音人", False, 130),
            ("标签", False, 100),
            ("操作", False, 250),
        ]
        modify_table_style(self.ui.tableWidget, properties)

        self.ui.tableWidget.verticalHeader().setDefaultSectionSize(26)  # 设置行高24
        header = self.ui.tableWidget.horizontalHeader()
        header.setDefaultAlignment(QtCore.Qt.AlignLeft)  # 设置表头左对齐
        # 创建一个字体对象，并设置字号为12
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        # 将字体对象设置为表头的字体
        header.setFont(font)

    def refresh_table(self, page_number=0):
        # 注意 QcomboBox在被清空的时候也会发出currentIndexChanged信号
        self.ui.comboBox.blockSignals(True)

        page_size = self.page_size
        if page_number == 0:
            page_number = self.page_number
        self.ui.tableWidget.setRowCount(0)
        self.ui.comboBox.clear()
        total_count, results = get_dataset_view_window_info(self.dataset_id, page_size, page_number)
        pagecount = 1
        while total_count > 0:
            start = page_size * (pagecount - 1) + 1
            if total_count >= page_size:
                end = start + page_size - 1
            else:
                end = start + total_count - 1
            self.ui.comboBox.addItem(f"第 {str(pagecount)} 页  {str(start)} ~ {str(end)}", pagecount)
            total_count -= page_size
            pagecount += 1

        self.btn_dict = {}
        for i, result in enumerate(results, start=1):
            index = i + (page_number - 1) * page_size
            info_id = result['info_id']
            info_text = result['info_text']
            info_start_time = result['info_start_time']
            info_end_time = result['info_end_time']
            info_file_path = result['info_raw_file_path']
            info_is_del = result['info_is_del']
            speaker = result['info_speaker']
            # if result['info_shibie_speaker'] != None:
            #     speaker = result['info_shibie_speaker']
            # else:
            #     speaker = result['info_speaker']
            # is_separate_file = result['is_separate_file']
            row = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(row)
            self.ui.tableWidget.setItem(row, 0, QTableWidgetItem(str(index)))
            self.ui.tableWidget.setItem(row, 1, QTableWidgetItem(info_text))
            self.ui.tableWidget.setItem(row, 2, QTableWidgetItem(speaker))

            data_list = [
                {'btn': AudioButton,'args': {'wav_path': info_file_path, 'start_time': info_start_time, 'end_time': info_end_time,'parent': self}, 'slot': None, 'length': 2},
                {'btn': QPushButton, 'args': {'text': '快速导出', 'parent': self}, 'slot': lambda: self.fast_output(info_id), 'length': 3},
                {'btn': QPushButton, 'args': {'text': '编辑', 'parent': self}, 'slot': lambda: self.edit_info(info_id)},
                {'btn': QPushButton, 'args': {'text': '删除', 'parent': self}, 'slot': lambda: self.del_info(info_id, info_is_del)},
            ]

            caozuo_widget = make_my_operate_btns(parent=self, data_list=data_list)
            self.ui.tableWidget.setCellWidget(row, 4, caozuo_widget)

        self.ui.comboBox.setCurrentIndex(page_number - 1)
        self.ui.comboBox.blockSignals(False)

    def fast_output(self, info_id):
        print(f'快速导出{info_id}')
        pass

    def edit_info(self, info_id):
        print(f'编辑{info_id}')
        pass

    def del_info(self, info_id, info_is_del):
        print(f'删除{info_id}')
        pass

    def add_from_file_wav_srt(self):
        add_wav_srt_window = AddFromWavSrtDialog(self, self.dataset_id)
        add_wav_srt_window.exec()

    def change_page_number(self, index):
        new_page_num = self.ui.comboBox.itemData(index)
        self.refresh_table(new_page_num)
        self.page_number = new_page_num

    def closeEvent(self, event):
        self.closed.emit()
        super().closeEvent(event)

    def open_del_info_by_wav_dialog(self):
        del_info_by_wav = DeleteInfoByWavDialog(self, self.dataset_id)
        del_info_by_wav.exec()
