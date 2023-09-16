# -*- coding: utf-8 -*-
"""
    @Time : 2023/8/27 14:56
    @Author : 李子
    @Url : https://github.com/kslz
    数据集选择界面
"""
from PySide6.QtWidgets import QTableWidgetItem, QMessageBox, QHeaderView

from domain.repositories.repositories import *
from infrastructure.file_io import del_file_by_dataset_id
from presentation.my_qt_class.my_add_dataset_dialog import AddDatasetDialog
from presentation.my_qt_class.my_base_main_window import BaseMainWindow
from presentation.my_qt_class.my_dataset_view_window import DatasetViewMainWindow
from presentation.my_qt_class.my_factory_function import *
from presentation.my_qt_class.my_tool_function import *
from presentation.pyuic.ui_SelectDatasetMainWindow import Ui_SelectDatasetMainWindow
from utils.tools import *


class SelectDatasetMainWindow(BaseMainWindow):
    def __init__(self, tool_workspace):
        super().__init__()
        # 使用ui文件导入定义界面类
        self.ui = Ui_SelectDatasetMainWindow()
        # 初始化界面
        self.ui.setupUi(self)
        self.my_init()

        properties = [
            ("数据集名", False, 100),
            ("创建时间", False, 130),
            ("上次使用时间", False, 130),
            ("备注", True, 100),
            ("操作", False, 120),
        ]
        modify_table_style(self.ui.tableWidget, properties)

        self.tool_workspace = tool_workspace
        self.add_dataset_data()

        self.ui.pushButton.clicked.connect(self.open_add_dataset_window)

    def add_dataset_data(self):
        """
        刷新表格数据，从数据库中取出数据集信息填入表格

        :return:
        """
        self.ui.tableWidget.setRowCount(0)
        datasets = get_dataset_info()
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

        info_cell = QTableWidgetItem()
        info_cell.setText(dataset_info)
        info_cell.setToolTip(f"<pre>{huanhang(dataset_info)}</pre>")
        self.ui.tableWidget.setItem(row, 3, info_cell)

        data_list = [
            {'text': '进入', 'slot': lambda: self.open_dataset_window(dataset_id)},
            {'text': '编辑', 'slot': lambda: self.edit_dataset(dataset_id)},
            {'text': '删除', 'slot': lambda: self.del_dataset(dataset_id, dataset_name)},
        ]

        caozuo_widget = make_operate_btns(self, data_list)
        self.ui.tableWidget.setCellWidget(row, 4, caozuo_widget)

    def open_dataset_window(self, dataset_id):
        self.dataset_view_main_window = DatasetViewMainWindow(dataset_id)
        self.dataset_view_main_window.show()
        self.hide()
        pass

    def edit_dataset(self, dataset_id):
        self.edit_window = AddDatasetDialog(self, useby="edit", dataset_id=dataset_id)
        self.edit_window.exec_()
        pass

    def del_dataset(self, dataset_id, dataset_name):
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
                del_dataset_by_id(dataset_id)
                del_file_by_dataset_id(dataset_id)
            except Exception as e:
                self.logger.error(f"删除数据集 {dataset_name} id={dataset_id} 失败\n{e}")
            else:
                self.logger.info(f"数据集 {dataset_name} 成功删除")
            finally:
                self.add_dataset_data()

        else:
            pass

        pass

    def open_add_dataset_window(self):
        self.add_window = AddDatasetDialog(self)
        self.add_window.exec()
