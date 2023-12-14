# -*- coding: utf-8 -*-
"""
    @Time : 2023/09/13 9:22
    @Author : 李子
    @Url : https://github.com/kslz
"""
import os

from PySide6 import QtCore, QtGui
from PySide6.QtCore import Signal, Slot
from PySide6.QtWidgets import QTableWidgetItem

from domain.repositories.repositories import *
from infrastructure.file_io import fast_output_sound
from presentation.my_qt_class.my_add_from_wav_srt_dialog import AddFromWavSrtDialog
from presentation.my_qt_class.my_audio_button import AudioButton
from presentation.my_qt_class.my_base_main_window import BaseMainWindow
from presentation.my_qt_class.my_columns_setting_dialog import ColumnsSettingDialog
from presentation.my_qt_class.my_delete_button import DeleteBTN
from presentation.my_qt_class.my_delete_info_by_wav_dialog import DeleteInfoByWavDialog
from presentation.my_qt_class.my_edit_info_dialog import EditInfoDialog
from presentation.my_qt_class.my_factory_function import *
from presentation.pyuic.ui_DatasetViewMainWindow import Ui_DatasetViewMainWindow
from utils.init_tools import read_ini_config


class DatasetViewMainWindow(BaseMainWindow):
    closed = Signal()

    def __init__(self, dataset_id):
        super().__init__()
        # 使用ui文件导入定义界面类
        self.ui = Ui_DatasetViewMainWindow()
        # 初始化界面
        self.ui.setupUi(self)
        self.my_init(False)
        self.set_table_style()

        self.config = read_ini_config()
        self.dataset_id = dataset_id
        self.page_number = 1
        self.page_size = int(self.config["program_configs"]["default_pagesize"])
        self.apply_columns_setting()
        self.init_comboBox_page_size()

        # self.refresh_table()
        #
        # # 连接信号
        self.ui.pushButton_columns_setting.clicked.connect(self.columns_setting)
        self.ui.comboBox_page_size.currentIndexChanged.connect(self.change_page_size)
        # self.ui.pushButton_add_wav_srt.clicked.connect(self.add_from_file_wav_srt)
        # self.ui.pushButton_del_by_raw_wav.clicked.connect(self.open_del_info_by_wav_dialog)

    def change_page_size(self, select_index):
        new_pagesize = self.ui.comboBox_page_size.currentData()
        self.page_size = new_pagesize
        self.refresh_table()
        self.ui.tableWidget_info_show.resizeColumnsToContents()  # 使表格自动列宽

    def init_comboBox_page_size(self):
        """
        初始化分页大小下拉框

        :return:
        """
        size_list = [15, 20, 30, 50, 100]
        combox = self.ui.comboBox_page_size
        combox.blockSignals(True)  # 阻止发送信号
        combox.clear()
        for size in size_list:
            combox.addItem(str(size), size)
        combox.setCurrentText(str(self.page_size))
        combox.blockSignals(False)  # 恢复发送信号

    def columns_setting(self):
        columns_setting_dialog = ColumnsSettingDialog(self, self.config)
        columns_setting_dialog.saveWindowClosed.connect(self.apply_columns_setting)
        columns_setting_dialog.exec()

    def apply_columns_setting(self):
        """
        应用自定义列修改

        :return:
        """
        # self.logger.debug(f"已选择自定义列：{','.join(checked_list)}")
        checked_str = self.config['program_configs']['default_columns']
        checked_list = checked_str.split(",")
        # checked_list.append("操作")
        self.logger.info(f"已选择自定义列：{checked_str}")
        self.ui.tableWidget_info_show.setColumnCount(len(checked_list))
        self.ui.tableWidget_info_show.setHorizontalHeaderLabels(checked_list)
        # header = self.ui.tableWidget_info_show.horizontalHeader()
        self.refresh_table()
        self.ui.tableWidget_info_show.resizeColumnsToContents()  # 使表格自动列宽

    def set_table_style(self):
        """
        设置表格样式

        :return:
        """

        self.ui.tableWidget_info_show.verticalHeader().setDefaultSectionSize(26)  # 设置行高24
        header = self.ui.tableWidget_info_show.horizontalHeader()
        header.setDefaultAlignment(QtCore.Qt.AlignLeft)  # 设置表头左对齐
        # 创建一个字体对象，并设置字号为12
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        # 将字体对象设置为表头的字体
        header.setFont(font)

        # 不展示行号
        self.ui.tableWidget_info_show.verticalHeader().setVisible(False)

    def refresh_table(self, page_number=0):
        """
        刷新表格

        :param page_number:
        :return:
        """
        # 注意 QcomboBox在被清空的时候也会发出currentIndexChanged信号
        page_size = self.page_size
        if page_number == 0:
            page_number = self.page_number
        self.ui.tableWidget_info_show.setRowCount(0)
        k_list = self.config['program_configs']['default_columns'].split(",")

        total_count, page_number, results = get_dataset_view_window_info(self.dataset_id, page_size, page_number,
                                                                         k_list)

        # print(total_count, page_number, results)

        table_tool = TableTool(results, self.ui.tableWidget_info_show, self)
        table_tool.add_to_table(k_list)

    @Slot()
    def fast_output(self, info_id):
        info = get_info_by_id(info_id)
        wav_path = info.info_raw_file_path
        start_time = info.info_start_time
        end_time = info.info_end_time
        output_name = str(info_id) + ".wav"
        output_path = os.path.join(self.workspace.output_path, "fastoutput")
        fast_output_sound(wav_path, start_time, end_time, output_name, output_path)
        self.logger.info(f"快速导出音频文件文件 {os.path.join(output_path, output_name)}")

    def edit_info(self, info_id):
        edit_info_dialog = EditInfoDialog(self, info_id)
        edit_info_dialog.windowClosed.connect(self.refresh_table)
        edit_info_dialog.exec()
        pass

    def del_info(self, info_id, info_is_del):
        print(f'删除{info_id}')
        pass

    def add_from_file_wav_srt(self):
        add_wav_srt_window = AddFromWavSrtDialog(self, self.dataset_id)
        add_wav_srt_window.exec()


    def closeEvent(self, event):
        self.closed.emit()
        super().closeEvent(event)

    def open_del_info_by_wav_dialog(self):
        del_info_by_wav = DeleteInfoByWavDialog(self, self.dataset_id)
        del_info_by_wav.exec()


class TableTool:
    """
    用于从列名和数据库查询得到的数据获取页面信息
    """

    def __init__(self, results, table, parent_window):
        self.parent_window = parent_window
        self.page_size = self.parent_window.page_size
        self.page_number = self.parent_window.page_number
        self.results = results
        self.table = table

        self.fun_dict = {}
        self.fun_dict["序号"] = self.index
        self.fun_dict["数据ID"] = self.info_id
        self.fun_dict["数据集ID"] = self.dataset_id
        self.fun_dict["数据文本"] = self.info_text
        self.fun_dict["数据拼音"] = self.info_pinyin
        self.fun_dict["发音人"] = self.info_speaker
        self.fun_dict["音频文件位置"] = self.info_raw_file_path
        self.fun_dict["音频开始时间"] = self.info_start_time
        self.fun_dict["音频结束时间"] = self.info_end_time
        self.fun_dict["是否已删除"] = self.info_is_del
        self.fun_dict["操作"] = self.caozuo

        pass

    def add_to_table(self, k_list):
        for i, result in enumerate(self.results, start=1):
            column_now = 0
            row = self.table.rowCount()
            self.table.insertRow(row)
            for k in k_list:
                fun_now = self.fun_dict[k]
                fun_now(row, column_now, result)
                column_now += 1

    def index(self, row, column, result_dict):
        index = (self.page_number - 1) * self.page_size + row + 1
        self.table.setItem(row, column, QTableWidgetItem(str(index)))

    def info_id(self, row, column, result_dict):
        self.table.setItem(row, column, QTableWidgetItem(str(result_dict["info_id"])))

    def dataset_id(self, row, column, result_dict):
        self.table.setItem(row, column, QTableWidgetItem(str(result_dict["dataset_id"])))

    def info_text(self, row, column, result_dict):
        self.table.setItem(row, column, QTableWidgetItem(str(result_dict["info_text"])))

    def info_pinyin(self, row, column, result_dict):
        self.table.setItem(row, column, QTableWidgetItem(str(result_dict["info_pinyin"])))

    def info_speaker(self, row, column, result_dict):
        self.table.setItem(row, column, QTableWidgetItem(str(result_dict["info_speaker"])))

    def info_raw_file_path(self, row, column, result_dict):
        self.table.setItem(row, column, QTableWidgetItem(str(result_dict["info_raw_file_path"])))

    def info_start_time(self, row, column, result_dict):
        self.table.setItem(row, column, QTableWidgetItem(str(result_dict["info_start_time"])))

    def info_end_time(self, row, column, result_dict):
        self.table.setItem(row, column, QTableWidgetItem(str(result_dict["info_end_time"])))

    def info_is_del(self, row, column, result_dict):
        self.table.setItem(row, column, QTableWidgetItem(str(result_dict["info_is_del"])))

    def caozuo(self, row, column, result_dict):

        def get_lamda(fun, args):
            return lambda: fun(*args)

        data_list = [
            {'btn': AudioButton,
             'args': {'wav_path': result_dict["info_raw_file_path"], 'start_time': result_dict["info_start_time"],
                      'end_time': result_dict["info_end_time"],
                      'parent': self.parent_window}, 'slot': None, 'length': 2},
            {'btn': QPushButton, 'args': {'text': '快速导出', 'parent': self.parent_window},
             'slot': get_lamda(self.parent_window.fast_output, [result_dict["info_id"]]), 'length': 3},
            {'btn': QPushButton, 'args': {'text': '编辑', 'parent': self.parent_window},
             'slot': get_lamda(self.parent_window.edit_info, [result_dict["info_id"]])},
            {'btn': DeleteBTN, 'args': {'text': '删除', "info_id": result_dict["info_id"], 'parent': self.parent_window,
                                        "info_is_del": result_dict["info_is_del"]}, 'slot': None},
        ]
        caozuo_widget = make_my_operate_btns(parent=self, data_list=data_list)
        self.table.setCellWidget(row, column, caozuo_widget)

