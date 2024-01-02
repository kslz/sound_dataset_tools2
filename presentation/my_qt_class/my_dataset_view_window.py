# -*- coding: utf-8 -*-
"""
    @Time : 2023/09/13 9:22
    @Author : 李子
    @Url : https://github.com/kslz
"""
import math
import os

from PySide6 import QtCore, QtGui
from PySide6.QtCore import Signal, Slot
from PySide6.QtWidgets import QTableWidgetItem, QLabel

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
        self.total_count = 0
        self.order_by_info = None  # (0, "asc")  # 保存排序列索引和排序方式

        self.apply_columns_setting()
        self.init_comboBox_page_size()

        # self.refresh_table()
        #
        # # 连接信号
        self.ui.pushButton_columns_setting.clicked.connect(self.columns_setting)
        self.ui.comboBox_page_size.currentIndexChanged.connect(self.change_page_size)
        # self.ui.pushButton_add_wav_srt.clicked.connect(self.add_from_file_wav_srt)
        # self.ui.pushButton_del_by_raw_wav.clicked.connect(self.open_del_info_by_wav_dialog)
        self.ui.pushButton_jump_to.clicked.connect(self.jump_to)
        self.ui.tableWidget_info_show.horizontalHeader().sectionClicked.connect(self.change_order_by)

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
        self.order_by_info = (self.get_header_label(0), "asc")
        # header = self.ui.tableWidget_info_show.horizontalHeader()
        self.refresh_table()
        self.ui.tableWidget_info_show.resizeColumnsToContents()  # 使表格自动列宽

    def set_table_style(self):
        """
        设置表格和页面样式

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

        self.ui.lineEdit_jump_to.setFixedWidth(50)

    def refresh_page_utils(self):
        widget_page_change = self.ui.widget_page_change
        layout = widget_page_change.layout()
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()
            else:
                layout.removeItem(item)
        button_last = SmallButton(" 上一页 ")
        layout.addWidget(button_last)
        button_last.auto_width()
        if self.page_number - 1 > 0:
            button_last.clicked.connect(self.to_last_page)
        else:
            button_last.setEnabled(False)

        all_button_count = 5

        all_page_num = math.ceil(self.total_count / self.page_size)

        size_length = int(all_button_count / 2)

        # left_btn_num = self.page_number - 1
        # right_btn_num = min(all_button_count, all_page_num) - 1 - left_btn_num

        if self.page_number - size_length > 1:
            left_need_cut = True
        else:
            left_need_cut = False
        if self.page_number + size_length < all_page_num:
            right_need_cut = True
        else:
            right_need_cut = False

        if left_need_cut:
            left_start = self.page_number - size_length + 1
            left_end = self.page_number
        else:
            left_start = 1
            left_end = self.page_number

        if right_need_cut:
            right_start = self.page_number + 1
            right_end = self.page_number + size_length
        else:
            right_start = self.page_number + 1
            right_end = all_page_num + 1

        # if left_end - left_start <= 1 and right_need_cut:
        def get_lamda(fun, args):
            return lambda: fun(*args)

        if left_need_cut:
            button_start = SmallButton("1")
            layout.addWidget(button_start)
            button_start.auto_width()
            button_start.clicked.connect(lambda: self.to_num_page(1))
            label_left = QLabel("···")
            layout.addWidget(label_left)
        for _page_num in range(left_start, left_end):
            _button_to_num = SmallButton(str(_page_num))
            layout.addWidget(_button_to_num)
            _button_to_num.auto_width()
            _button_to_num.clicked.connect(get_lamda(self.to_num_page, [_page_num]))

        button_now = SmallButton(str(self.page_number))
        layout.addWidget(button_now)
        button_now.auto_width()
        button_now.setEnabled(False)
        # button_now.clicked.connect(lambda: self.to_num_page(self.page_number))

        for _page_num in range(right_start, right_end):
            _button_to_num = SmallButton(str(_page_num))
            layout.addWidget(_button_to_num)
            _button_to_num.auto_width()
            _button_to_num.clicked.connect(get_lamda(self.to_num_page, [_page_num]))

        if right_need_cut:
            label_left = QLabel("···")
            layout.addWidget(label_left)
            button_end = SmallButton(str(all_page_num))
            layout.addWidget(button_end)
            button_end.auto_width()
            button_end.clicked.connect(lambda: self.to_num_page(all_page_num))

        button_next = SmallButton(" 下一页 ")
        layout.addWidget(button_next)
        button_next.auto_width()
        if self.page_number != all_page_num:
            button_next.clicked.connect(self.to_next_page)
        else:
            button_next.setEnabled(False)

        self.refresh_label_page_info()

        pass

    def jump_to(self):
        jump_to_num = self.ui.lineEdit_jump_to.text()
        try:
            jump_to_num = int(jump_to_num)
        except:
            self.logger.error("输入的跳转页码不是有效数字")
            return
        self.to_num_page(jump_to_num)

    def refresh_label_page_info(self):
        total_count = self.total_count
        now_start = (self.page_number - 1) * self.page_size + 1
        now_end = min(self.page_number * self.page_size, total_count)
        self.ui.label_page_info.setText(f"当前{now_start}到{now_end}，共{total_count}条数据")

    def to_last_page(self):
        self.page_number -= 1
        self.refresh_table()
        pass

    def to_next_page(self):
        self.page_number += 1
        self.refresh_table()
        pass

    def to_num_page(self, page_num):
        # print(f"去{page_num}页")
        self.page_number = page_num
        self.refresh_table()
        pass

    def get_header_label(self, index=0):

        header_label = self.ui.tableWidget_info_show.horizontalHeaderItem(index).text()
        if header_label in ["序号","操作"]:
            header_label = "数据ID"
        return header_label

    def change_order_by(self, index):
        old_order = self.order_by_info[0]
        old_adesc = self.order_by_info[1]

        new_order = self.get_header_label(index)
        if old_order == new_order:
            new_adesc = "asc" if old_adesc == "desc" else "desc"
        else:
            new_adesc = "asc"
        self.order_by_info = (new_order, new_adesc)
        self.refresh_table()

    def refresh_table(self, page_number=0):
        """
        刷新表格和页面

        :param page_number:
        :return:
        """
        # 注意 QcomboBox在被清空的时候也会发出currentIndexChanged信号
        page_size = self.page_size
        if page_number <= 0:
            page_number = self.page_number
        self.ui.tableWidget_info_show.setRowCount(0)
        k_list = self.config['program_configs']['default_columns'].split(",")

        total_count, page_number, results = get_dataset_view_window_info(self.dataset_id, page_size, page_number,
                                                                         k_list, self.order_by_info)

        # print(total_count, page_number, results)
        self.total_count = total_count
        all_page_num = math.ceil(self.total_count / self.page_size)
        if self.page_number > all_page_num:
            self.page_number = all_page_num

        table_tool = TableTool(results, self.ui.tableWidget_info_show, self)
        table_tool.add_to_table(k_list)

        self.refresh_page_utils()

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
        self.fun_dict["数据字数"] = self.info_text_length
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

    def info_text_length(self, row, column, result_dict):
        self.table.setItem(row, column, QTableWidgetItem(str(result_dict["info_text_length"])))

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


class SmallButton(QPushButton):
    def __init__(self, text):
        super().__init__(text=text)

    def auto_width(self):
        text = self.text()
        new_width = 20 + len(text) * 10
        self.setFixedWidth(new_width)
