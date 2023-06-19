# -*- coding: utf-8 -*-
"""
    @Time : 2023/2/13/013 13:35
    @Author : 李子
    @Url : https://github.com/kslz
"""

import peewee
from PySide6 import QtGui
from PySide6.QtWidgets import QMainWindow, QWidget, QTableWidgetItem, QHBoxLayout

from ui.mydialog import *
from ui.mywidget import *
from ui.pyuic.ui_add_dataset import Ui_Dialog
from ui.pyuic.ui_select_dataset import Ui_MainWindow
from ui.pyuic.ui_select_workspace import Ui_Form
from ui.pyuic.ui_dataset_view import Ui_DatasetMainWindow
from utils.tools import *

global config


def getconfig():
    global config
    config = global_obj.get_value("config")


class DatasetWindow(QMainWindow):
    reopen = Signal()

    # refresh_authorization_table = Signal(object)

    def __init__(self, dataset_id):
        super().__init__()
        # 使用ui文件导入定义界面类
        self.ui = Ui_DatasetMainWindow()
        # 初始化界面
        self.ui.setupUi(self)
        self.set_table_style()
        self.dataset_id = dataset_id
        self.page_number = 1
        self.page_size = 15
        self.refresh_table()
        self.refresh_authorization_table()
        # self.ui.tabWidget.setTabVisible(1, False)
        # self.ui.tabWidget.setTabVisible(2, False)

        # 连接信号
        self.ui.comboBox.currentIndexChanged.connect(self.change_page_number)
        self.ui.pushButton_add_wav_srt.clicked.connect(self.add_from_file_wav_srt)
        self.ui.pushButton_add_long_wav.clicked.connect(self.add_from_file_long_wav)
        self.ui.pushButton_add_biaobei.clicked.connect(lambda: self.open_add_authorization_dialog(DbStr.BiaoBei))
        self.ui.pushButton_add_xunfei.clicked.connect(lambda: self.open_add_authorization_dialog(DbStr.XunFei))
        self.ui.pushButton_output_speaker.clicked.connect(self.open_output_speaker_dialog)
        self.ui.pushButton_biaobei_pingce.clicked.connect(self.open_biaobei_pingce)
        self.ui.pushButton_del_by_raw_wav.clicked.connect(self.open_del_info_by_wav_dialog)

    def set_table_style(self):

        # 数据集表格
        self.ui.tableWidget.setColumnWidth(0, 100)
        self.ui.tableWidget.setColumnWidth(1, 500)
        self.ui.tableWidget.setColumnWidth(2, 125)
        self.ui.tableWidget.setColumnWidth(3, 200)
        self.ui.tableWidget.setColumnWidth(4, 200)
        self.ui.tableWidget.verticalHeader().setDefaultSectionSize(26)  # 设置行高24
        header = self.ui.tableWidget.horizontalHeader()
        header.setDefaultAlignment(QtCore.Qt.AlignLeft)  # 设置表头左对齐
        # 创建一个字体对象，并设置字号为12
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        # 将字体对象设置为表头的字体
        header.setFont(font)

        # 授权管理页两个表格
        self.ui.tableWidget_biaobei.setColumnWidth(0, 50)
        self.ui.tableWidget_biaobei.setColumnWidth(1, 150)
        self.ui.tableWidget_biaobei.setColumnWidth(2, 150)
        self.ui.tableWidget_biaobei.setColumnWidth(3, 200)
        self.ui.tableWidget_biaobei.setColumnWidth(4, 200)
        self.ui.tableWidget_biaobei.setColumnWidth(5, 200)

        self.ui.tableWidget_xunfei.setColumnWidth(0, 50)
        self.ui.tableWidget_xunfei.setColumnWidth(1, 150)
        self.ui.tableWidget_xunfei.setColumnWidth(2, 150)
        self.ui.tableWidget_xunfei.setColumnWidth(3, 200)
        self.ui.tableWidget_xunfei.setColumnWidth(4, 200)
        self.ui.tableWidget_xunfei.setColumnWidth(5, 200)

    def open_add_authorization_dialog(self, company):
        add_authorization_dialog = AddAuthentication(self, company)
        add_authorization_dialog.exec_()
        self.refresh_authorization_table()

    def open_output_speaker_dialog(self):
        output_speaker_dialog = OutPutSpeaker(self, self.dataset_id)
        output_speaker_dialog.exec_()

    def open_del_info_by_wav_dialog(self):
        del_info_by_wav = DelInfoByWav(self, self.dataset_id)
        del_info_by_wav.exec_()

    def refresh_authorization_table(self):
        self.ui.tableWidget_biaobei.setRowCount(0)
        biaobei_list = get_authorizationinfo(DbStr.BiaoBei)
        for line in biaobei_list:
            row = self.ui.tableWidget_biaobei.rowCount()
            self.ui.tableWidget_biaobei.insertRow(row)
            self.ui.tableWidget_biaobei.setItem(row, 0, QTableWidgetItem(str(line.authorizationinfo_id)))
            self.ui.tableWidget_biaobei.setItem(row, 1, QTableWidgetItem(line.authorizationinfo_name))
            self.ui.tableWidget_biaobei.setItem(row, 2, QTableWidgetItem(line.authorizationinfo_app))
            self.ui.tableWidget_biaobei.setItem(row, 3, QTableWidgetItem(line.authorizationinfo_APPID))
            self.ui.tableWidget_biaobei.setItem(row, 4, QTableWidgetItem(line.authorizationinfo_APISecret))
            self.ui.tableWidget_biaobei.setItem(row, 5, QTableWidgetItem(line.authorizationinfo_APIKey))

        self.ui.tableWidget_xunfei.setRowCount(0)
        xunfei_list = get_authorizationinfo(DbStr.XunFei)
        for line in xunfei_list:
            row = self.ui.tableWidget_xunfei.rowCount()
            self.ui.tableWidget_xunfei.insertRow(row)
            self.ui.tableWidget_xunfei.setItem(row, 0, QTableWidgetItem(line.authorizationinfo_id))
            self.ui.tableWidget_xunfei.setItem(row, 1, QTableWidgetItem(line.authorizationinfo_name))
            self.ui.tableWidget_xunfei.setItem(row, 2, QTableWidgetItem(line.authorizationinfo_app))
            self.ui.tableWidget_xunfei.setItem(row, 3, QTableWidgetItem(line.authorizationinfo_APPID))
            self.ui.tableWidget_xunfei.setItem(row, 4, QTableWidgetItem(line.authorizationinfo_APISecret))
            self.ui.tableWidget_xunfei.setItem(row, 5, QTableWidgetItem(line.authorizationinfo_APIKey))

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
            info_start_time = result['info_start_time']
            info_end_time = result['info_end_time']
            info_file_path = result['info_raw_file_path']
            if result['info_shibie_speaker'] != None:
                speaker = result['info_shibie_speaker']
            else:
                speaker = result['info_speaker']
            # is_separate_file = result['is_separate_file']
            row = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(row)
            self.ui.tableWidget.setItem(row, 0, QTableWidgetItem(str(index)))
            self.ui.tableWidget.setItem(row, 1, QTableWidgetItem(info_text))
            self.ui.tableWidget.setItem(row, 2, QTableWidgetItem(speaker))
            # if is_separate_file == 0:
            #     is_separate_file = "否"
            # if is_separate_file == 1:
            #     is_separate_file = "是"
            # self.ui.tableWidget.setItem(row, 3, QTableWidgetItem(is_separate_file))
            # self.ui.tableWidget.setItem(row, 5, QTableWidgetItem(str(info_id) + "一些操作"))

            # btn_shiting = PlaySoundBTN('试听', info_id, self)
            btn_shiting = AudioButton(info_file_path, info_start_time, info_end_time, self)
            btn_shiting.setMinimumWidth(50)
            btn_fastoutput = FastOutputSoundBTN('快速导出', info_id, self)
            btn_fastoutput.setMinimumWidth(80)
            btn_bianji = BianJiBTN('编辑', info_id)
            btn_bianji.setMinimumWidth(50)
            btn_bianji.on_clicked.connect(self.edit_info)
            self.btn_dict[f"{row}_shiting"] = btn_shiting
            self.btn_dict[f"{row}_fastoutput"] = btn_fastoutput
            self.btn_dict[f"{row}_bianji"] = btn_bianji
            layout = QHBoxLayout()
            layout.addWidget(self.btn_dict[f"{row}_shiting"])
            layout.addWidget(self.btn_dict[f"{row}_fastoutput"])
            layout.addWidget(self.btn_dict[f"{row}_bianji"])
            self.btn_dict = {}
            layout.setContentsMargins(0, 0, 0, 0)
            layout.setSpacing(1)
            caozuo_widget = QWidget()
            caozuo_widget.setLayout(layout)
            self.ui.tableWidget.setCellWidget(row, 4, caozuo_widget)

        self.ui.comboBox.setCurrentIndex(page_number - 1)
        self.ui.comboBox.blockSignals(False)

    def open_biaobei_pingce(self):
        biaobei_pingce = BiaobeiPingce(self, self.dataset_id)
        biaobei_pingce.exec_()

    def closeEvent(self, event):
        self.reopen.emit()
        super().closeEvent(event)

    def add_from_file_wav_srt(self):
        add_wav_srt_window = SelectWavSrtFile(self, self.dataset_id)
        add_wav_srt_window.exec_()

    def add_from_file_long_wav(self):
        add_long_wav_window = SelectLongWavFile(self, self.dataset_id)
        add_long_wav_window.exec_()

    def edit_info(self, info_id):
        edit_info_window = EditInfo(self,info_id)
        edit_info_window.windowClosed.connect(self.refresh_table)
        edit_info_window.exec_()
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
        self.update_dataset_dataset_last_use_time(dataset_id)
        self.add_dataset_data()
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

    def update_dataset_dataset_last_use_time(self, dataset_id):
        Dataset.update(dataset_last_use_time=datetime.now().replace(microsecond=0)).where(
            Dataset.dataset_id == dataset_id).execute()
        # User.update(age=20).where(User.username=="charlie").execute()

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
                del_file_by_dataset_id(dataset_id)

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
