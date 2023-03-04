# -*- coding: utf-8 -*-
"""
    @Time : 2023/2/13/013 13:35
    @Author : 李子
    @Url : https://github.com/kslz
"""

import peewee
from PySide6 import QtCore, QtGui
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QMainWindow, QWidget, QTableWidgetItem, QPushButton, QHBoxLayout, \
    QDialog, QMessageBox, QFileDialog

import ui.pyuic.ui_dataset_view
from ui.pyuic.ui_add_authorizationinfo import Ui_AddAuthenticationDialog
from ui.pyuic.ui_add_dataset import Ui_Dialog
from ui.pyuic.ui_biaobei_pingce import Ui_BiaobeiPingceDialog
from ui.pyuic.ui_edit_info import Ui_EditInfoDialog
from ui.pyuic.ui_output_dataset_speaker import Ui_OutPutSpeakerDialog
from ui.pyuic.ui_select_dataset import Ui_MainWindow
from ui.pyuic.ui_select_file_wav_srt import Ui_select_file_wav_srt_Dialog
from ui.pyuic.ui_select_workspace import Ui_Form
from ui.pyuic.ui_dataset_view import Ui_DatasetMainWindow
from utils.log import *
from utils.request_tools import get_biaobei_token, test_biaobei_pingce, pingce_biaobei
from utils.tools import *

global config


def getconfig():
    global config
    config = global_obj.get_value("config")


class EditInfo(QDialog):
    def __init__(self, parent, info_id):
        super().__init__(parent)
        # 使用ui文件导入定义界面类
        self.ui = Ui_EditInfoDialog()
        # 初始化界面
        self.ui.setupUi(self)
        self.info_id = info_id
        # self.add_info()


class BiaobeiPingce(QDialog):
    def __init__(self, parent, dataset_id):
        super().__init__(parent)
        # 使用ui文件导入定义界面类
        self.ui = Ui_BiaobeiPingceDialog()
        # 初始化界面
        self.ui.setupUi(self)
        self.dataset_id = dataset_id
        self.ui.checkBox_2.setEnabled(False)
        self.add_authorizationinfo()
        self.ui.pushButton_queding.clicked.connect(self.start_pingce)

    def add_authorizationinfo(self):
        results = get_authorizationinfo(DbStr.BiaoBei, DbStr.PingCe)
        for result in results:
            self.ui.comboBox.addItem(result.authorizationinfo_name, result.authorizationinfo_id)

    def start_pingce(self):
        is_skip_done = self.ui.checkBox.isChecked()
        is_skip_ascii = self.ui.checkBox_2.isChecked()
        authorizationinfo_id = self.ui.comboBox.currentData()
        if authorizationinfo_id == None:
            self.ui.label_error.setText("没有可选的授权信息，请在设置页面添加")
            return
        result_a = get_authorizationinfo_by_id(authorizationinfo_id)
        token = result_a[0].authorizationinfo_token
        if not test_biaobei_pingce(token):
            requsetlogger.warning("token校验失败，正在尝试重新获取")
            token = get_biaobei_token(result_a[0].authorizationinfo_APIKey, result_a[0].authorizationinfo_APISecret)
            if not token:
                requsetlogger.error("token重新获取失败，重新输入认证信息")
                return
            else:
                AuthorizationInfo.update(authorizationinfo_token=token).where(
                    AuthorizationInfo.authorizationinfo_id == result_a[0].authorizationinfo_id).execute()
                requsetlogger.warning("token重新获取成功")
        requsetlogger.warning("token校验通过")
        if is_skip_ascii:
            results = get_pingce_info(self.dataset_id, is_skip_done)

            for result in results:
                result: Info
                id = result.info_id
                start = result.info_start_time
                end = result.info_end_time
                text = result.info_text
                file_path = result.info_raw_file_path
                if is_all_chinese(text):
                    response_json = pingce_biaobei(file_path, text, token, start, end)
                    if response_json:
                        acc_score = response_json["result"]["acc_score"]
                        flu_score = response_json["result"]["flu_score"]
                        int_score = response_json["result"]["int_score"]
                        all_score = response_json["result"]["all_score"]
                        mfa_info = {"biaobei": response_json["result"]["word"]}
                        # requsetlogger.info(f"标贝评测成功，文本：{text}，准确度得分：{acc_score}，流利度得分：{flu_score}，完整度得分：{int_score}，总分：{all_score}，")

                        Info.update(
                            info_acc_score=acc_score,
                            info_flu_score=flu_score,
                            info_int_score=int_score,
                            info_all_score=all_score,
                            info_mfa=mfa_info
                        ).where(Info.info_id == id).execute()

                    # print(text)
                    # print(response_json)
                    # return
        else:
            pass


class OutPutSpeaker(QDialog):
    def __init__(self, parent, dataset_id):
        super().__init__(parent)
        # 使用ui文件导入定义界面类
        self.ui = Ui_OutPutSpeakerDialog()
        # 初始化界面
        self.ui.setupUi(self)
        self.dataset_id = dataset_id
        self.add_info()

        # 绑定信号和槽
        self.ui.pushButton_next.clicked.connect(self.output_info)
        self.ui.pushButton_read_preinstall.clicked.connect(self.use_preinstall)
        self.ui.pushButton_back.clicked.connect(self.close)

    def add_info(self):
        """
        添加speaker和文件层级

        """
        self.ui.comboBox_geshi.addItem(f"默认", GeshiStr.default)
        self.ui.comboBox_geshi.addItem(f"AISHELL-3", GeshiStr.aishell3)
        self.ui.comboBox_geshi.addItem(f"VITS", GeshiStr.vits)
        self.ui.comboBox_preinstall.addItem(f"AISHELL-3", GeshiStr.aishell3)
        self.ui.comboBox_preinstall.addItem(f"VITS", GeshiStr.vits)
        self.ui.comboBox_preinstall.setCurrentText(GeshiStr.vits)
        self.use_preinstall()
        result_list = get_speakers(self.dataset_id)
        for line in result_list:
            if line[1] == "shibie_spk":
                text = f"{line[0]}-已识别"
            else:
                text = f"{line[0]}-未识别"
            self.ui.comboBox_speaker.addItem(text, line)
            self.ui.checkBox_auto_skip.setEnabled(False)

    def use_preinstall(self):
        pre_name = self.ui.comboBox_preinstall.currentText()
        if pre_name == GeshiStr.vits:
            self.ui.comboBox_geshi.setCurrentText(GeshiStr.vits)
            self.ui.lineEdit_sample_rate.setText("22050")
            self.ui.comboBox_channel.setCurrentText("1")
            self.ui.lineEdit_guiyihua.setText("-23")
        elif pre_name == GeshiStr.aishell3:
            self.ui.comboBox_geshi.setCurrentText(GeshiStr.aishell3)
            self.ui.lineEdit_sample_rate.setText("44100")
            self.ui.comboBox_channel.setCurrentText("1")
            self.ui.lineEdit_guiyihua.setText("-23")





        pass

    def output_info(self):
        geshi = self.ui.comboBox_geshi.currentData()
        qianzhui = self.ui.lineEdit_qianzhui.text()
        sample_rate = self.ui.lineEdit_sample_rate.text()
        channels = int(self.ui.comboBox_channel.currentText())
        speaker = self.ui.comboBox_speaker.currentData()
        results = get_output_info(self.dataset_id, speaker)
        is_auto_skip = self.ui.checkBox_auto_skip.isChecked()
        normalization = self.ui.lineEdit_guiyihua.text()
        if normalization == "":
            normalization = False
        else:
            try:
                normalization = float(normalization)
                if normalization < -70 or normalization > -5:
                    raise Exception('归一化目标值错误')
            except:
                self.ui.label_error("归一化目标值错误")

        now = datetime.now()
        formatted_time = now.strftime("%Y-%m-%d_%H-%M-%S")
        workspace_path = global_obj.get_value("workspace_path")
        output_path = os.path.join(workspace_path, "output", formatted_time)

        start_time = time.time()

        if geshi == GeshiStr.default:
            out_num = output_like_default(qianzhui, sample_rate, channels, results, output_path, is_auto_skip,
                                          normalization)
        if geshi == GeshiStr.aishell3:
            out_num = output_like_aishell3(qianzhui, sample_rate, channels, results, output_path, is_auto_skip,
                                           normalization)
        if geshi == GeshiStr.vits:
            out_num = output_like_vits(qianzhui, sample_rate, channels, results, output_path, is_auto_skip,
                                       normalization)

        end_time = time.time()
        duration = end_time - start_time

        QMessageBox.information(
            self.parent(),
            '导出成功',
            f'已导出{out_num}条数据\n存放位置：{os.path.abspath(output_path)}')
        guilogger.info(f'已导出{out_num}条数据，耗时{duration:.2f} 秒\n存放位置：{os.path.abspath(output_path)}')

        self.close()


class AddAuthentication(QDialog):
    def __init__(self, parent, company):
        super().__init__(parent)
        # 使用ui文件导入定义界面类
        self.ui = Ui_AddAuthenticationDialog()
        # 初始化界面
        self.ui.setupUi(self)
        self.company = company
        self.add_combobox()

        # 连接信号和槽
        self.ui.pushButton_commit.clicked.connect(self.commit)
        self.ui.pushButton_close.clicked.connect(self.close)

    def add_combobox(self):
        """
        不同的公司实现不同的APP

        :return:
        """
        if self.company == DbStr.BiaoBei:
            self.ui.comboBox_app.addItem(DbStr.PingCe)
        if self.company == DbStr.XunFei:
            self.ui.comboBox_app.addItem(DbStr.ShengWen)

    def commit(self):
        name = self.ui.lineEdit_name.text()
        appid = self.ui.lineEdit_appid.text()
        apisecret = self.ui.lineEdit_apisecret.text()
        apikey = self.ui.lineEdit_apikey.text()
        if name == "":
            self.ui.label_error.setText("请填写名称字段")
            return
        if appid == "":
            self.ui.label_error.setText("请填写appid字段")
            return
        if apisecret == "":
            self.ui.label_error.setText("请填写apisecret字段")
            return
        if apikey == "":
            self.ui.label_error.setText("请填写apikey字段")
            return
        token = get_biaobei_token(apikey, apisecret)
        app = self.ui.comboBox_app.currentText()
        if token:
            AuthorizationInfo.insert({
                "authorizationinfo_name": name,
                "authorizationinfo_APPID": appid,
                "authorizationinfo_APISecret": apisecret,
                "authorizationinfo_APIKey": apikey,
                "authorizationinfo_company": self.company,
                "authorizationinfo_app": app,
                "authorizationinfo_token": token
            }).execute()
            self.close()
        else:
            self.ui.label_error.setText("获取token失败，请检查网络或输入是否有误")


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

        # 连接信号
        self.ui.comboBox.currentIndexChanged.connect(self.change_page_number)
        self.ui.pushButton_add_wav_srt.clicked.connect(self.add_from_file_wav_srt)
        self.ui.pushButton_add_biaobei.clicked.connect(lambda: self.open_add_authorization_dialog(DbStr.BiaoBei))
        self.ui.pushButton_add_xunfei.clicked.connect(lambda: self.open_add_authorization_dialog(DbStr.XunFei))
        self.ui.pushButton_output_speaker.clicked.connect(self.open_output_speaker_dialog)
        self.ui.pushButton_biaobei_pingce.clicked.connect(self.open_biaobei_pingce)

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
