# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'output_dataset_speaker.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QStackedWidget, QVBoxLayout,
    QWidget)

class Ui_OutPutSpeakerDialog(object):
    def setupUi(self, OutPutSpeakerDialog):
        if not OutPutSpeakerDialog.objectName():
            OutPutSpeakerDialog.setObjectName(u"OutPutSpeakerDialog")
        OutPutSpeakerDialog.resize(540, 581)
        font = QFont()
        font.setPointSize(12)
        OutPutSpeakerDialog.setFont(font)
        self.stackedWidget = QStackedWidget(OutPutSpeakerDialog)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(20, 10, 511, 371))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.label_2 = QLabel(self.page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 131, 131, 16))
        self.lineEdit_sample_rate = QLineEdit(self.page)
        self.lineEdit_sample_rate.setObjectName(u"lineEdit_sample_rate")
        self.lineEdit_sample_rate.setGeometry(QRect(290, 170, 191, 21))
        self.comboBox_geshi = QComboBox(self.page)
        self.comboBox_geshi.setObjectName(u"comboBox_geshi")
        self.comboBox_geshi.setGeometry(QRect(290, 90, 191, 22))
        self.label_3 = QLabel(self.page)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 171, 131, 16))
        self.label = QLabel(self.page)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 90, 221, 20))
        self.lineEdit_qianzhui = QLineEdit(self.page)
        self.lineEdit_qianzhui.setObjectName(u"lineEdit_qianzhui")
        self.lineEdit_qianzhui.setGeometry(QRect(290, 130, 191, 21))
        self.label_9 = QLabel(self.page)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(20, 250, 131, 16))
        self.comboBox_speaker = QComboBox(self.page)
        self.comboBox_speaker.setObjectName(u"comboBox_speaker")
        self.comboBox_speaker.setGeometry(QRect(290, 250, 191, 22))
        self.groupBox_2 = QGroupBox(self.page)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 10, 491, 71))
        self.pushButton_read_preinstall = QPushButton(self.groupBox_2)
        self.pushButton_read_preinstall.setObjectName(u"pushButton_read_preinstall")
        self.pushButton_read_preinstall.setGeometry(QRect(280, 30, 111, 24))
        self.pushButton_read_preinstall.setFont(font)
        self.comboBox_preinstall = QComboBox(self.groupBox_2)
        self.comboBox_preinstall.setObjectName(u"comboBox_preinstall")
        self.comboBox_preinstall.setGeometry(QRect(10, 30, 211, 22))
        self.label_4 = QLabel(self.page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 211, 131, 16))
        self.comboBox_channel = QComboBox(self.page)
        self.comboBox_channel.addItem("")
        self.comboBox_channel.addItem("")
        self.comboBox_channel.setObjectName(u"comboBox_channel")
        self.comboBox_channel.setGeometry(QRect(290, 210, 191, 22))
        self.checkBox_auto_skip = QCheckBox(self.page)
        self.checkBox_auto_skip.setObjectName(u"checkBox_auto_skip")
        self.checkBox_auto_skip.setGeometry(QRect(290, 290, 111, 20))
        self.checkBox_auto_skip.setChecked(True)
        self.label_5 = QLabel(self.page)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 290, 201, 16))
        self.label_guiyihua = QLabel(self.page)
        self.label_guiyihua.setObjectName(u"label_guiyihua")
        self.label_guiyihua.setGeometry(QRect(20, 330, 261, 41))
        self.label_guiyihua.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.lineEdit_guiyihua = QLineEdit(self.page)
        self.lineEdit_guiyihua.setObjectName(u"lineEdit_guiyihua")
        self.lineEdit_guiyihua.setGeometry(QRect(290, 330, 191, 21))
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.groupBox = QGroupBox(self.page_2)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(0, 30, 501, 231))
        self.label_cengji = QLabel(self.groupBox)
        self.label_cengji.setObjectName(u"label_cengji")
        self.label_cengji.setGeometry(QRect(10, 50, 231, 141))
        self.label_cengji.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_geshi = QLabel(self.groupBox)
        self.label_geshi.setObjectName(u"label_geshi")
        self.label_geshi.setGeometry(QRect(260, 50, 231, 141))
        self.label_geshi.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 26, 151, 16))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.label_6.setFont(font1)
        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(260, 26, 151, 16))
        self.label_7.setFont(font1)
        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 200, 141, 20))
        self.label_file_num = QLabel(self.groupBox)
        self.label_file_num.setObjectName(u"label_file_num")
        self.label_file_num.setGeometry(QRect(160, 200, 151, 20))
        self.stackedWidget.addWidget(self.page_2)
        self.pushButton_next = QPushButton(OutPutSpeakerDialog)
        self.pushButton_next.setObjectName(u"pushButton_next")
        self.pushButton_next.setGeometry(QRect(430, 540, 75, 24))
        self.pushButton_back = QPushButton(OutPutSpeakerDialog)
        self.pushButton_back.setObjectName(u"pushButton_back")
        self.pushButton_back.setGeometry(QRect(320, 540, 75, 24))
        self.label_error = QLabel(OutPutSpeakerDialog)
        self.label_error.setObjectName(u"label_error")
        self.label_error.setGeometry(QRect(40, 520, 271, 16))
        self.label_error.setFont(font)
        self.label_error.setStyleSheet(u"color:red")
        self.groupBox_3 = QGroupBox(OutPutSpeakerDialog)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(30, 390, 491, 131))
        self.comboBox_pingce = QComboBox(self.groupBox_3)
        self.comboBox_pingce.setObjectName(u"comboBox_pingce")
        self.comboBox_pingce.setGeometry(QRect(10, 30, 211, 22))
        self.horizontalLayoutWidget = QWidget(self.groupBox_3)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(240, 20, 241, 101))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_left = QVBoxLayout()
        self.verticalLayout_left.setObjectName(u"verticalLayout_left")

        self.horizontalLayout.addLayout(self.verticalLayout_left)

        self.verticalLayout_right = QVBoxLayout()
        self.verticalLayout_right.setObjectName(u"verticalLayout_right")

        self.horizontalLayout.addLayout(self.verticalLayout_right)

        self.label_10 = QLabel(self.groupBox_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(10, 60, 211, 61))
        self.label_10.setWordWrap(True)

        self.retranslateUi(OutPutSpeakerDialog)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(OutPutSpeakerDialog)
    # setupUi

    def retranslateUi(self, OutPutSpeakerDialog):
        OutPutSpeakerDialog.setWindowTitle(QCoreApplication.translate("OutPutSpeakerDialog", u"\u5bfc\u51fa\u6570\u636e\u96c6", None))
        self.label_2.setText(QCoreApplication.translate("OutPutSpeakerDialog", u"\u6dfb\u52a0\u97f3\u9891\u6587\u4ef6\u524d\u7f00", None))
        self.lineEdit_sample_rate.setText("")
        self.label_3.setText(QCoreApplication.translate("OutPutSpeakerDialog", u"\u97f3\u9891\u6587\u4ef6\u91c7\u6837\u7387", None))
        self.label.setText(QCoreApplication.translate("OutPutSpeakerDialog", u"\u8f93\u51fa\u6587\u4ef6\u5c42\u7ea7\u548c\u6807\u6ce8\u6587\u4ef6\u683c\u5f0f", None))
        self.lineEdit_qianzhui.setText("")
        self.label_9.setText(QCoreApplication.translate("OutPutSpeakerDialog", u"\u53d1\u97f3\u4eba", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("OutPutSpeakerDialog", u"\u9884\u8bbe", None))
        self.pushButton_read_preinstall.setText(QCoreApplication.translate("OutPutSpeakerDialog", u"\u8bfb\u53d6\u6240\u9009\u9884\u8bbe", None))
        self.label_4.setText(QCoreApplication.translate("OutPutSpeakerDialog", u"\u58f0\u9053\u6570", None))
        self.comboBox_channel.setItemText(0, QCoreApplication.translate("OutPutSpeakerDialog", u"1", None))
        self.comboBox_channel.setItemText(1, QCoreApplication.translate("OutPutSpeakerDialog", u"2", None))

        self.checkBox_auto_skip.setText(QCoreApplication.translate("OutPutSpeakerDialog", u"\u662f", None))
        self.label_5.setText(QCoreApplication.translate("OutPutSpeakerDialog", u"\u81ea\u52a8\u8df3\u8fc7\u542b\u6709\u975e\u4e2d\u6587\u7684\u6570\u636e", None))
        self.label_guiyihua.setText(QCoreApplication.translate("OutPutSpeakerDialog", u"\u5f52\u4e00\u5316\uff08\u7559\u7a7a\u4e3a\u4e0d\u8fdb\u884c\u5f52\u4e00\u5316\uff09\n"
"\u8303\u56f4\u4e3a-70~-5", None))
        self.lineEdit_guiyihua.setText(QCoreApplication.translate("OutPutSpeakerDialog", u"-23", None))
        self.groupBox.setTitle(QCoreApplication.translate("OutPutSpeakerDialog", u"\u9884\u89c8", None))
        self.label_cengji.setText(QCoreApplication.translate("OutPutSpeakerDialog", u"sounds\n"
"    - 1.wav\n"
"    - 2.wav\n"
"    ......\n"
"labels.txt", None))
        self.label_geshi.setText(QCoreApplication.translate("OutPutSpeakerDialog", u"1.wav|\u4f60\u597d\u4e16\u754c\n"
"2.wav|\u4e16\u754c\u4f60\u597d\n"
"......", None))
        self.label_6.setText(QCoreApplication.translate("OutPutSpeakerDialog", u"\u6587\u4ef6\u5c42\u7ea7\uff1a", None))
        self.label_7.setText(QCoreApplication.translate("OutPutSpeakerDialog", u"\u6807\u6ce8\u6587\u4ef6\u5185\u5bb9\uff1a", None))
        self.label_8.setText(QCoreApplication.translate("OutPutSpeakerDialog", u"\u9884\u8ba1\u5bfc\u51fa\u6587\u4ef6\u6570\u91cf\uff1a", None))
        self.label_file_num.setText("")
        self.pushButton_next.setText(QCoreApplication.translate("OutPutSpeakerDialog", u"\u4e0b\u4e00\u6b65", None))
        self.pushButton_back.setText(QCoreApplication.translate("OutPutSpeakerDialog", u"\u4e0a\u4e00\u6b65", None))
        self.label_error.setText("")
        self.groupBox_3.setTitle(QCoreApplication.translate("OutPutSpeakerDialog", u"\u8bc4\u6d4b\u76f8\u5173", None))
        self.comboBox_pingce.setPlaceholderText("")
        self.label_10.setText(QCoreApplication.translate("OutPutSpeakerDialog", u"\u9009\u62e9\u8bc4\u6d4b\u4f9d\u636e\u540e\u53ef\u4ee5\u8fc7\u6ee4\u5bfc\u51fa\u7684\u6570\u636e\uff0c\u53ea\u4f1a\u5bfc\u51fa\u6307\u5b9a\u5206\u6570\u8d85\u8fc7\u9650\u5b9a\u503c\u7684\u6570\u636e\u3002", None))
    # retranslateUi

