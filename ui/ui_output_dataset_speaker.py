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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QGroupBox,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QStackedWidget, QWidget)

class Ui_OutPutSpeakerDialog(object):
    def setupUi(self, OutPutSpeakerDialog):
        if not OutPutSpeakerDialog.objectName():
            OutPutSpeakerDialog.setObjectName(u"OutPutSpeakerDialog")
        OutPutSpeakerDialog.resize(540, 400)
        font = QFont()
        font.setPointSize(12)
        OutPutSpeakerDialog.setFont(font)
        self.stackedWidget = QStackedWidget(OutPutSpeakerDialog)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(20, 10, 511, 321))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.pushButton_save_preinstall = QPushButton(self.page)
        self.pushButton_save_preinstall.setObjectName(u"pushButton_save_preinstall")
        self.pushButton_save_preinstall.setGeometry(QRect(320, 50, 161, 24))
        self.pushButton_save_preinstall.setFont(font)
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
        self.comboBox_preinstall = QComboBox(self.page)
        self.comboBox_preinstall.setObjectName(u"comboBox_preinstall")
        self.comboBox_preinstall.setGeometry(QRect(20, 50, 231, 22))
        self.label = QLabel(self.page)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 90, 221, 20))
        self.lineEdit_qianzhui = QLineEdit(self.page)
        self.lineEdit_qianzhui.setObjectName(u"lineEdit_qianzhui")
        self.lineEdit_qianzhui.setGeometry(QRect(290, 130, 191, 21))
        self.label_9 = QLabel(self.page)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(20, 210, 131, 16))
        self.comboBox_speaker = QComboBox(self.page)
        self.comboBox_speaker.setObjectName(u"comboBox_speaker")
        self.comboBox_speaker.setGeometry(QRect(290, 210, 191, 22))
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
        self.pushButton_next.setGeometry(QRect(430, 360, 75, 24))
        self.pushButton_back = QPushButton(OutPutSpeakerDialog)
        self.pushButton_back.setObjectName(u"pushButton_back")
        self.pushButton_back.setGeometry(QRect(320, 360, 75, 24))

        self.retranslateUi(OutPutSpeakerDialog)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(OutPutSpeakerDialog)
    # setupUi

    def retranslateUi(self, OutPutSpeakerDialog):
        OutPutSpeakerDialog.setWindowTitle(QCoreApplication.translate("OutPutSpeakerDialog", u"\u5bfc\u51fa\u6570\u636e\u96c6", None))
        self.pushButton_save_preinstall.setText(QCoreApplication.translate("OutPutSpeakerDialog", u"\u4fdd\u5b58\u5f53\u524d\u9009\u9879\u4e3a\u9884\u8bbe", None))
        self.label_2.setText(QCoreApplication.translate("OutPutSpeakerDialog", u"\u6dfb\u52a0\u97f3\u9891\u6587\u4ef6\u524d\u7f00", None))
        self.lineEdit_sample_rate.setText("")
        self.label_3.setText(QCoreApplication.translate("OutPutSpeakerDialog", u"\u97f3\u9891\u6587\u4ef6\u91c7\u6837\u7387", None))
        self.label.setText(QCoreApplication.translate("OutPutSpeakerDialog", u"\u8f93\u51fa\u6587\u4ef6\u5c42\u7ea7\u548c\u6807\u6ce8\u6587\u4ef6\u683c\u5f0f", None))
        self.lineEdit_qianzhui.setText("")
        self.label_9.setText(QCoreApplication.translate("OutPutSpeakerDialog", u"\u53d1\u97f3\u4eba", None))
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
    # retranslateUi

