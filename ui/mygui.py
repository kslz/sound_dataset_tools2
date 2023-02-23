# -*- coding: utf-8 -*-
"""
    @Time : 2023/2/13/013 13:35
    @Author : 李子
    @Url : https://github.com/kslz
"""
import _thread
import os
import time

import peewee
import pysrt
from PySide6 import QtCore, QtGui
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QTableWidgetItem, QPushButton, QLabel, QHBoxLayout, \
    QDialog, QMessageBox, QFileDialog
from PySide6.QtCore import Signal, Qt, QThread

import ui.ui_dataset_view
from ui.ui_add_dataset import Ui_Dialog
from ui.ui_select_dataset import Ui_MainWindow
from ui.ui_select_file_wav_srt import Ui_select_file_wav_srt_Dialog
from ui.ui_select_workspace import Ui_Form
from utils import global_obj
from utils.log import creatlogger
from utils.peewee_orm import *
from utils.tools import *

global config

guilogger = creatlogger("guilogger")


def getconfig():
    global config
    config = global_obj.get_value("config")


class SelectWavSrtFile(QDialog):
    def __init__(self, parent, dataset_id):
        super().__init__(parent)
        # 使用ui文件导入定义界面类
        self.ui = Ui_select_file_wav_srt_Dialog()
        # 初始化界面
        self.ui.setupUi(self)
        self.ui.lineEdit_wav.setReadOnly(True)
        self.ui.lineEdit_srt.setReadOnly(True)
        self.file_paths = {}
        self.dataset_id = dataset_id
        self.ui.pushButton_select_wav.clicked.connect(self.select_file_wav)
        self.ui.pushButton_select_srt.clicked.connect(self.select_file_srt)
        self.ui.pushButton_submit.clicked.connect(self.save_to_dataset)
        self.ui.pushButton_back.clicked.connect(self.go_back)

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
        workspace_path = global_obj.get_value("workspace_path")
        wav_path = copy_file_to_workspace(wav_path, os.path.join(workspace_path, "sounds"))
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
        # 多写return就不用写else了，某种意义上来讲能少几段缩进，提高可读性（也许

        if os.path.isfile(wav_path) and os.path.isfile(srt_path):
            try:
                duration = get_audio_duration(wav_path)
            except:
                self.ui.error_lable.setText("音频文件解析失败，请检查所选文件是否正确")
                guilogger.error(f"音频文件 {wav_path} 解析失败，请检查所选文件是否正确")
                return

            try:
                mysrt = pysrt.open(srt_path)
                if len(mysrt) == 0:
                    raise Exception('所选文件不是SRT格式的文件！')

            except:
                self.ui.error_lable.setText(f"字幕文件解析失败，请检查所选文件是否正确")
                guilogger.error(f"字幕文件 {srt_path} 解析失败，请检查所选文件是否正确")
                return

            srt_end_time = mysrt[-1].end.ordinal / 1000
            if srt_end_time > duration:
                self.ui.error_lable.setText(f"字幕文件长度长于音频文件，请检查是否选择错误")
                guilogger.error(f"字幕文件长度长于音频文件，请检查是否选择错误")
                return
            if add_info_by_file_wav_srt(self.dataset_id, wav_path, srt_path, speaker):
                self.parent().refresh_table()
                self.close()




        else:
            self.ui.error_lable.setText("音频文件或字幕文件不存在！")
            guilogger.error(f"音频文件 {wav_path} 或字幕文件 {srt_path} 不存在")
        pass

    def go_back(self):
        self.close()


class PlaySoundBTN(QPushButton):
    class PlaySoundThread(QtCore.QThread):
        update_signal = Signal(str, bool)
        # stop_thread_signal = Signal()

        def __init__(self, wav_path, start_time, end_time):
            super().__init__()
            # self.stop_flag = False
            # self.stop_thread_signal.connect(self.stop_thread)
            self.wav_path = wav_path
            self.start_time = start_time
            self.end_time = end_time

        def run(self):
            self.update_signal.emit("播放中", False)
            play_by_ffmpeg(self.wav_path, self.start_time, self.end_time)
            self.update_signal.emit("试听", True)

        # def stop_thread(self):
        #     self.stop_flag = True
        #     print("收到停止信号")
        #     self.wait()

    def __init__(self, text, info_id, parent):
        super().__init__(text, parent)
        self.info_id = info_id
        self.clicked.connect(self.play_or_stop_sound)
        info = Info.get_by_id(self.info_id)
        wav_path = info.info_raw_file_path
        start_time = info.info_start_time
        end_time = info.info_end_time
        # self.thread1 = QThread(self)  # 创建一个线程 不行 没用明白，先这样吧
        self.play_thread = self.PlaySoundThread(wav_path, start_time, end_time)  # 实例化线程类
        # self.play_thread.moveToThread(self.thread1)  # 将类移动到线程中运行
        # self.thread1.started.connect(self.play_thread.run)
        self.play_thread.update_signal.connect(lambda text, is_enabled: self.set_text(text, is_enabled))

    def play_or_stop_sound(self):
        # 多线程避免阻塞界面
        if self.text() == "试听":
            self.play_thread.start()
        else:
            # 终止播放失败
            # self.play_thread.stop_thread_signal.emit()
            # self.play_thread.exit()
            # self.set_text("试听", True)
            pass

    def set_text(self, text, is_enabled):
        self.setText(text)
        # self.setEnabled(is_enabled)


class DatasetWindow(QMainWindow):
    reopen = Signal()
    need_refresh_table = Signal(object)

    def __init__(self, dataset_id):
        super().__init__()
        # 使用ui文件导入定义界面类
        self.ui = ui.ui_dataset_view.Ui_DatasetMainWindow()
        # 初始化界面
        self.ui.setupUi(self)
        self.ui.tableWidget.setColumnWidth(0, 100)
        self.ui.tableWidget.setColumnWidth(1, 500)
        self.ui.tableWidget.setColumnWidth(2, 100)
        self.ui.tableWidget.setColumnWidth(3, 75)
        self.ui.tableWidget.setColumnWidth(4, 150)
        self.ui.tableWidget.setColumnWidth(5, 200)
        self.set_table_style()
        self.dataset_id = dataset_id
        self.page_number = 1
        self.page_size = 15
        self.refresh_done = False
        self.refresh_table()
        self.refresh_done = True

        # 连接信号
        self.ui.comboBox.currentIndexChanged.connect(self.change_page_number)
        self.ui.pushButton_add_wav_srt.clicked.connect(self.add_from_file_wav_srt)

    def set_table_style(self):
        self.ui.tableWidget.verticalHeader().setDefaultSectionSize(26)  # 设置行高24

        header = self.ui.tableWidget.horizontalHeader()
        header.setDefaultAlignment(QtCore.Qt.AlignLeft)  # 设置表头左对齐
        # 创建一个字体对象，并设置字号为12
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)

        # 将字体对象设置为表头的字体
        header.setFont(font)

    def change_page_number(self, index):
        new_page_num = self.ui.comboBox.itemData(index)
        self.refresh_table(new_page_num)
        self.page_number = new_page_num

    def refresh_table(self, page_number=0):
        # QcomboBox在被清空的时候也会发出currentIndexChanged信号，找这个问题花了一个小时
        # 警钟敲烂
        self.ui.comboBox.blockSignals(True)
        page_size = self.page_size
        if page_number == 0:
            page_number = self.page_number
        self.ui.tableWidget.setRowCount(0)
        self.ui.comboBox.clear()
        total_count, results = get_dataset_window_info(self.dataset_id, page_size, page_number)
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
            speaker = result['speaker']
            is_separate_file = result['is_separate_file']
            row = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(row)
            self.ui.tableWidget.setItem(row, 0, QTableWidgetItem(str(index)))
            self.ui.tableWidget.setItem(row, 1, QTableWidgetItem(info_text))
            self.ui.tableWidget.setItem(row, 2, QTableWidgetItem(speaker))
            if is_separate_file == 0:
                is_separate_file = "否"
            if is_separate_file == 1:
                is_separate_file = "是"
            self.ui.tableWidget.setItem(row, 3, QTableWidgetItem(is_separate_file))
            # self.ui.tableWidget.setItem(row, 5, QTableWidgetItem(str(info_id) + "一些操作"))

            btn_shiting = PlaySoundBTN('试听', info_id, self)
            btn_bianji = QPushButton('编辑', self)
            btn_shiting.clicked.connect(lambda: self.edit_info(info_id))
            self.btn_dict[f"{row}_shiting"] = btn_shiting
            self.btn_dict[f"{row}_bianji"] = btn_bianji
            layout = QHBoxLayout()
            layout.addWidget(self.btn_dict[f"{row}_shiting"])
            layout.addWidget(self.btn_dict[f"{row}_bianji"])
            layout.setContentsMargins(0, 0, 0, 0)
            layout.setSpacing(1)
            caozuo_widget = QWidget()
            caozuo_widget.setLayout(layout)
            self.ui.tableWidget.setCellWidget(row, 5, caozuo_widget)

        self.ui.comboBox.setCurrentIndex(page_number - 1)
        self.ui.comboBox.blockSignals(False)

    def closeEvent(self, event):
        self.reopen.emit()
        super().closeEvent(event)

    def add_from_file_wav_srt(self):
        add_wav_srt_window = SelectWavSrtFile(self, self.dataset_id)
        add_wav_srt_window.exec_()

    def edit_info(self, info_id):
        pass


class AddDatasetWindow(QDialog):
    refresh_table = Signal()

    def __init__(self, parent, useby="add", dataset_id=None):
        super().__init__(parent)
        # 使用ui文件导入定义界面类
        self.ui = Ui_Dialog()
        # 初始化界面
        self.ui.setupUi(self)
        self.ui.buttonBox.rejected.connect(self.goback)
        self.useby = useby
        self.dataset_id = dataset_id
        if useby != "add":
            self.setWindowTitle("编辑数据集")
            self.ui.buttonBox.accepted.connect(self.edit_dataset)
            dataset = Dataset.get_by_id(self.dataset_id)
            self.ui.lineEdit.setText(dataset.dataset_name)
            self.ui.textEdit.setText(dataset.dataset_info)
            self.dataset_oldname = dataset.dataset_name
        else:
            self.ui.buttonBox.accepted.connect(self.add_dataset)

    def edit_dataset(self):
        dataset_name = self.ui.lineEdit.text()
        dataset_info = self.ui.textEdit.toPlainText()
        if dataset_name == "":
            guilogger.error("修改失败，数据集名称为空")
            self.show_error("修改失败，数据集名称为空")
            return
        try:
            dataset = Dataset.update(dataset_name=dataset_name, dataset_info=dataset_info).where(
                Dataset.dataset_id == self.dataset_id).execute()
        except peewee.IntegrityError as e:
            if "UNIQUE constraint failed" in str(e):
                guilogger.error("修改失败，数据集名称重复")
                self.show_error("修改失败，数据集名称重复")
            else:
                guilogger.error(e)
        else:
            guilogger.info(f"数据集 {dataset_name} 成功修改")
            self.refresh_table.emit()
            self.close()

        pass

    def add_dataset(self):
        dataset_name = self.ui.lineEdit.text()
        datset_info = self.ui.textEdit.toPlainText()
        # print(datset_info)
        if dataset_name == "":
            guilogger.error("添加失败，数据集名称为空")
            self.show_error("添加失败，数据集名称为空")
            return

        try:
            dataset = Dataset(dataset_name=dataset_name, dataset_info=datset_info)
            dataset.save()
        except peewee.IntegrityError as e:
            if "UNIQUE constraint failed" in str(e):
                guilogger.error("添加失败，数据集名称重复")
                self.show_error("添加失败，数据集名称重复")
            else:
                guilogger.error(e)
        else:
            guilogger.info(f"数据集 {dataset_name} 添加成功")
            self.refresh_table.emit()
            self.close()

    def show_error(self, text):
        self.ui.label_3.setText(text)

    def goback(self):
        self.close()


class SelectDatasetWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # 使用ui文件导入定义界面类
        self.ui = Ui_MainWindow()
        # 初始化界面
        self.ui.setupUi(self)
        self.ui.tableWidget.setColumnWidth(0, 100)
        self.ui.tableWidget.setColumnWidth(1, 130)
        self.ui.tableWidget.setColumnWidth(2, 130)
        self.ui.tableWidget.setColumnWidth(3, 200)
        self.ui.tableWidget.setColumnWidth(4, 120)
        # self.ui.tableWidget.verticalHeader().setVisible(True)

    def add_dataset_data(self):
        """
        刷新表格数据，从数据库中取出数据集信息填入表格

        :return:
        """
        # dataset1 = Dataset.create(dataset_name="test1")
        # dataset2 = Dataset.create(dataset_name="test2")
        self.ui.tableWidget.setRowCount(0)
        datasets = Dataset.select()
        for dataset in datasets:
            self.addData(dataset.dataset_id,
                         dataset.dataset_name,
                         dataset.dataset_create_time,
                         dataset.dataset_last_use_time,
                         dataset.dataset_info)

    def addData(self, dataset_id=None, dataset_name=None, dataset_createtime=None, dataset_lastusetime=None,
                dataset_info=None):
        row = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(row)
        self.ui.tableWidget.setItem(row, 0, QTableWidgetItem(str(dataset_name)))
        self.ui.tableWidget.setItem(row, 1, QTableWidgetItem(str(dataset_createtime)))
        self.ui.tableWidget.setItem(row, 2, QTableWidgetItem(str(dataset_lastusetime)))
        # self.ui.tableWidget.setItem(row, 3, QTableWidgetItem(str(dataset_info)))
        info_cell = QTableWidgetItem()
        info_cell.setText(dataset_info)
        info_cell.setToolTip(f"<pre>{huanhang(dataset_info)}</pre>")
        self.ui.tableWidget.setItem(row, 3, info_cell)

        btn_jr = QPushButton('进入', self)
        btn_jr.clicked.connect(lambda: self.openDatasetWindow(dataset_id))
        btn_bj = QPushButton('编辑', self)
        btn_bj.clicked.connect(lambda: self.edit_dataset(dataset_id))
        btn_sc = QPushButton('删除', self)
        btn_sc.clicked.connect(lambda: self.del_dataset(dataset_id, dataset_name))
        layout = QHBoxLayout()
        layout.addWidget(btn_jr)
        layout.addWidget(btn_bj)
        layout.addWidget(btn_sc)
        layout.setContentsMargins(1, 1, 1, 1)
        layout.setSpacing(1)
        caozuo_widget = QWidget()
        caozuo_widget.setLayout(layout)
        self.ui.tableWidget.setCellWidget(row, 4, caozuo_widget)

    def open_add_dataset_window(self, useby="add"):
        self.add_window = AddDatasetWindow(self)
        self.add_window.refresh_table.connect(self.add_dataset_data)
        # self.add_window.setModal(True)
        # self.add_window.show()
        self.add_window.exec_()

    def openDatasetWindow(self, dataset_id):
        self.hide()
        self.dataset_window = DatasetWindow(dataset_id)
        self.dataset_window.show()
        self.dataset_window.reopen.connect(self.show)

        pass

    def edit_dataset(self, dataset_id):
        self.edit_window = AddDatasetWindow(self, useby="edit", dataset_id=dataset_id)
        self.edit_window.refresh_table.connect(self.add_dataset_data)
        # self.add_window.setModal(True)
        # self.add_window.show()
        self.edit_window.exec_()

    def del_dataset(self, dataset_id, dataset_name):
        """
        考虑做伪删除，但是感觉没必要

        """
        msg_box = QMessageBox()  # 后悔药（不
        msg_box.setWindowTitle("提示")
        msg_box.setText(f"确认删除数据集 {dataset_name} 吗？\n{dataset_name} 将会永久失去!(真的很久!)")
        msg_box.setIcon(QMessageBox.Question)

        # 添加按钮
        yes_button = msg_box.addButton("确定", QMessageBox.AcceptRole)
        no_button = msg_box.addButton("取消", QMessageBox.RejectRole)

        # 显示消息框，等待用户响应
        msg_box.exec()

        # 获取用户的响应
        button_clicked = msg_box.clickedButton()
        if button_clicked == yes_button:
            try:
                # dataset = Dataset.delete().where(Dataset.dataset_id == dataset_id)
                # self.add_dataset_data()
                dataset = Dataset.get(Dataset.dataset_id == dataset_id)
                name = dataset.dataset_name
                dataset.delete_instance()

            except Exception as e:
                guilogger.error(f"删除数据集 id={dataset_id} 失败")
                guilogger.error(e)
            else:
                guilogger.info(f"数据集 {name} 成功删除")
            finally:
                self.add_dataset_data()

        else:
            pass


class SelectWorkspaceWindow(QWidget):
    show_select_dataset_window = Signal()

    def __init__(self):
        super().__init__()
        # 使用ui文件导入定义界面类
        self.ui = Ui_Form()
        # 初始化界面
        self.ui.setupUi(self)
        getconfig()
        self.input_default_workspace()

    def input_default_workspace(self):
        default_workspace = config["program_configs"]["default_workspace"]
        # default_workspace = os.path.abspath(default_workspace)
        self.ui.lineEdit.setText(default_workspace)

    def close_program(self):
        self.close()

    def get_workspace(self):
        workspace_path = self.ui.lineEdit.text()
        global_obj.set_value("workspace_path", workspace_path)
        inti_workspace(workspace_path)
        config["program_configs"]["default_workspace"] = workspace_path
        update_ini_config(config)
        self.show_select_dataset_window.emit()
        self.close()

        # if os.path.exists(workspace_path):
        #     print("路径存在")
        # else:
        #     print("路径不存在")

    pass
