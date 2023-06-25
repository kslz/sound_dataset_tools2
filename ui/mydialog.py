# -*- coding: utf-8 -*-
"""
    @Time : 2023/4/10/010 10:39
    @Author : 李子
    @Url : https://github.com/kslz
"""
from PySide6.QtCore import QRect, Signal
from PySide6.QtWidgets import QDialog, QMessageBox, QFileDialog

from ui.mywidget import AudioButton, AudioNowButton
from ui.pyuic.ui_add_authorizationinfo import Ui_AddAuthenticationDialog
from ui.pyuic.ui_biaobei_pingce import Ui_BiaobeiPingceDialog
from ui.pyuic.ui_del_info_wav import Ui_del_info_wav_Dialog
from ui.pyuic.ui_edit_info import Ui_EditInfoDialog
from ui.pyuic.ui_output_dataset_speaker import Ui_OutPutSpeakerDialog
from ui.pyuic.ui_pingce_jindutiao import Ui_PingcejinduDialog
from ui.pyuic.ui_select_file_long_wav import Ui_select_file_long_wav_Dialog
from ui.pyuic.ui_select_file_wav_srt import Ui_select_file_wav_srt_Dialog

from utils.log import *
from utils.request_tools import *
from utils.tools import *


class Pingcejiindu(QDialog):
    start = Signal()
    pause = Signal()
    stop = Signal()
    def __init__(self, parent, dataset_id):
        super().__init__(parent)
        # 使用ui文件导入定义界面类
        self.ui = Ui_PingcejinduDialog()
        # 初始化界面
        self.ui.setupUi(self)
        # self.ui.progressBar.setRange(0, 5)
        # self.ui.progressBar.setValue(3)
        self.ui.progressBar.setStyleSheet('''
            QProgressBar {
                text-align: center;
            }
            ''')

    def


class EditInfo(QDialog):
    windowClosed = Signal()

    def __init__(self, parent, info_id):
        super().__init__(parent)
        # 使用ui文件导入定义界面类
        self.ui = Ui_EditInfoDialog()
        # 初始化界面
        self.ui.setupUi(self)
        self.info_id = info_id
        self.add_info()
        self.ui.pushButton_3.clicked.connect(self.update_info)
        self.ui.pushButton_2.clicked.connect(self.close)

    def add_info(self):
        info = Info.get_by_id(self.info_id)
        wav_path = info.info_raw_file_path
        start_time = str(info.info_start_time)
        end_time = str(info.info_end_time)
        text = info.info_text
        info_id = str(info.info_id)
        speaker = info.info_speaker

        self.ui.lineEdit_info_text.setText(text)
        self.ui.lineEdit_info_starttime.setText(start_time)
        self.ui.lineEdit_info_endtime.setText(end_time)
        self.ui.label_info_id.setText(info_id)
        self.ui.label_info_speaker.setText(speaker)

        # self.btn_shiting = PlayNowSoundBTN('试听', self)
        self.btn_shiting = AudioNowButton(wav_path, int(start_time), int(end_time), self)
        self.btn_shiting.clicked.connect(self.shiting)
        # btn_sc.clicked.connect(lambda: self.del_dataset(dataset_id, dataset_name))
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
        self.ui.label_error.setText("")
        if authorizationinfo_id == None:
            self.ui.label_error.setText("没有可选的授权信息，请在设置页面添加")
            return
        result_a = get_authorizationinfo_by_id(authorizationinfo_id)
        token = result_a[0].authorizationinfo_token
        try:
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
        except requests.exceptions.SSLError:
            self.ui.label_error.setText("SSLError 请关闭代理在尝试进行评测")
            requsetlogger.error("SSLError 请关闭代理在尝试进行评测")

        if is_skip_ascii:
            results = get_pingce_info(self.dataset_id, is_skip_done)
            self.ui.label_error.setText("正在运行中，窗口可能卡死，请勿关闭窗口")
            requsetlogger.error("正在运行中，窗口可能卡死，请勿关闭窗口")
            output_speaker_dialog = Pingcejiindu(self, self.dataset_id)
            output_speaker_dialog.exec_()

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
                        # mfa_info = {"biaobei": response_json["result"]["word"]}
                        requsetlogger.info(
                            f"标贝评测成功，文本：{text}，准确度得分：{acc_score}，流利度得分：{flu_score}，完整度得分：{int_score}，总分：{all_score}，")

                        create_or_update_biaobeipingceinfo(id, acc_score, flu_score, int_score, all_score,
                                                           response_json)
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
        self.ui.comboBox_geshi.currentIndexChanged.connect(self.auto_skip_change_enable)

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
        self.auto_skip_change_enable()
        result_list = get_speakers(self.dataset_id)
        for line in result_list:
            if line[1] == "shibie_spk":
                text = f"{line[0]}-已识别"
            else:
                text = f"{line[0]}-未识别"
            self.ui.comboBox_speaker.addItem(text, line)
            # self.ui.checkBox_auto_skip.setEnabled(False)

    def auto_skip_change_enable(self):
        self.ui.checkBox_auto_skip.setEnabled(True)
        self.ui.checkBox_auto_skip.setChecked(False)
        now_geshi = self.ui.comboBox_geshi.currentData()
        if now_geshi == GeshiStr.aishell3:
            self.ui.checkBox_auto_skip.setChecked(True)
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


class DelInfoByWav(QDialog):
    def __init__(self, parent, dataset_id):
        super().__init__(parent)
        # 使用ui文件导入定义界面类
        self.ui = Ui_del_info_wav_Dialog()
        # 初始化界面
        self.ui.setupUi(self)
        self.dataset_id = dataset_id
        self.add_file_select()
        self.ui.pushButton_submit.clicked.connect(self.del_info_and_file)
        self.ui.pushButton_back.clicked.connect(self.close)

    def add_file_select(self):
        self.ui.comboBox_files.clear()
        results = get_file_raw_path_by_dataset_id(self.dataset_id)
        for result in results:
            file_path = result.info_raw_file_path
            file_name = os.path.basename(file_path)
            file_name = os.path.splitext(file_name)[0]
            self.ui.comboBox_files.addItem(file_name, file_path)

    def del_info_and_file(self):
        file_path = self.ui.comboBox_files.currentData()
        print(f"删除{file_path}")
        try:
            del_info_by_raw_file_path(file_path)
        except:
            guilogger.error(f"文件 {file_path} 关联的数据删除失败")
        else:
            guilogger.info(f"文件 {file_path} 关联的数据已被删除")
            if os.path.exists(file_path):
                try:
                    os.remove(file_path)
                    guilogger.info(f"文件 {file_path} 已被删除")
                except:
                    guilogger.error(f"文件 {file_path} 删除失败")
        self.add_file_select()
        self.parent().refresh_table()
        self.close()


class SelectLongWavFile(QDialog):
    def __init__(self, parent, dataset_id):
        super().__init__(parent)
        # 使用ui文件导入定义界面类
        self.ui = Ui_select_file_long_wav_Dialog()
        # 初始化界面
        self.ui.setupUi(self)
        self.ui.lineEdit_wav.setReadOnly(True)
        self.file_paths = {}
        self.dataset_id = dataset_id
        self.ui.pushButton_select_wav.clicked.connect(self.select_file_wav)
        self.ui.pushButton_submit.clicked.connect(self.save_to_dataset)
        self.ui.pushButton_back.clicked.connect(self.close)
        self.ui.lineEdit_min_silence_len.setText(str(1000))
        self.ui.lineEdit_non_silence_thresh.setText(str(-40))

    def select_file_wav(self):
        filePath, _ = QFileDialog.getOpenFileName(
            self,  # 父窗口对象
            "选择你要导入的音频文件",  # 标题
            r"./",  # 起始目录
            "音频文件 (*)"  # 选择类型过滤项，过滤内容在括号中
        )
        self.file_paths["wav"] = filePath
        self.ui.lineEdit_wav.setText(filePath)

    def save_to_dataset(self):
        wav_path = self.file_paths["wav"]
        workspace_path = global_obj.get_value("workspace_path")
        wav_path = copy_file_to_workspace(wav_path, os.path.join(workspace_path, "sounds"))
        speaker = self.ui.lineEdit_spk.text()
        min_silence_len = int(self.ui.lineEdit_min_silence_len.text())
        non_silent_ranges = int(self.ui.lineEdit_non_silence_thresh.text())
        # is_better = self.ui.checkBox.isChecked()
        is_better = True
        seek_step = 10

        if wav_path.strip() == "" or None:
            self.ui.error_lable.setText("输入音频路径为空")
            return
        if speaker.strip() == "" or None:
            self.ui.error_lable.setText("输入发音人为空")
            return

        if os.path.isfile(wav_path):
            try:
                duration = get_audio_duration(wav_path)
            except Exception as e:
                self.ui.error_lable.setText("音频文件解析失败，请检查所选文件是否正确")
                guilogger.error(f"音频文件 {wav_path} 解析失败，请检查所选文件是否正确")
                print(e)
                return
            sound = AudioSegment.from_file(wav_path)
            if add_info_by_file_long_wav(self.dataset_id, wav_path, speaker, min_silence_len, non_silent_ranges,
                                         seek_step, is_better, sound):
                self.parent().refresh_table()
                self.close()


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
            # if add_info_by_file_wav_srt(self.dataset_id, wav_path, srt_path, speaker):
            sound = AudioSegment.from_file(wav_path)
            if add_info_by_file_wav_srt_better(self.dataset_id, wav_path, srt_path, speaker, sound, is_merge_srt):
                self.parent().refresh_table()
                self.close()




        else:
            self.ui.error_lable.setText("音频文件或字幕文件不存在！")
            guilogger.error(f"音频文件 {wav_path} 或字幕文件 {srt_path} 不存在")
        pass

    def go_back(self):
        self.close()
