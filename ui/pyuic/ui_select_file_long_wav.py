# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'select_file_long_wav.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_select_file_long_wav_Dialog(object):
    def setupUi(self, select_file_long_wav_Dialog):
        if not select_file_long_wav_Dialog.objectName():
            select_file_long_wav_Dialog.setObjectName(u"select_file_long_wav_Dialog")
        select_file_long_wav_Dialog.resize(600, 250)
        select_file_long_wav_Dialog.setMinimumSize(QSize(600, 250))
        select_file_long_wav_Dialog.setMaximumSize(QSize(600, 250))
        font = QFont()
        font.setPointSize(12)
        select_file_long_wav_Dialog.setFont(font)
        self.lineEdit_wav = QLineEdit(select_file_long_wav_Dialog)
        self.lineEdit_wav.setObjectName(u"lineEdit_wav")
        self.lineEdit_wav.setGeometry(QRect(110, 70, 371, 21))
        self.label = QLabel(select_file_long_wav_Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 21, 341, 20))
        self.label_2 = QLabel(select_file_long_wav_Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 70, 81, 16))
        self.pushButton_select_wav = QPushButton(select_file_long_wav_Dialog)
        self.pushButton_select_wav.setObjectName(u"pushButton_select_wav")
        self.pushButton_select_wav.setGeometry(QRect(500, 69, 81, 23))
        self.pushButton_back = QPushButton(select_file_long_wav_Dialog)
        self.pushButton_back.setObjectName(u"pushButton_back")
        self.pushButton_back.setGeometry(QRect(500, 200, 81, 24))
        self.pushButton_submit = QPushButton(select_file_long_wav_Dialog)
        self.pushButton_submit.setObjectName(u"pushButton_submit")
        self.pushButton_submit.setGeometry(QRect(390, 200, 81, 24))
        self.error_lable = QLabel(select_file_long_wav_Dialog)
        self.error_lable.setObjectName(u"error_lable")
        self.error_lable.setGeometry(QRect(30, 170, 541, 16))
        self.error_lable.setFont(font)
        self.error_lable.setStyleSheet(u"color: red;")
        self.lineEdit_spk = QLineEdit(select_file_long_wav_Dialog)
        self.lineEdit_spk.setObjectName(u"lineEdit_spk")
        self.lineEdit_spk.setGeometry(QRect(110, 100, 371, 21))
        self.label_4 = QLabel(select_file_long_wav_Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 100, 81, 16))
        self.label_5 = QLabel(select_file_long_wav_Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 130, 141, 16))
        self.lineEdit_min_silence_len = QLineEdit(select_file_long_wav_Dialog)
        self.lineEdit_min_silence_len.setObjectName(u"lineEdit_min_silence_len")
        self.lineEdit_min_silence_len.setGeometry(QRect(170, 130, 101, 21))
        self.lineEdit_non_silence_thresh = QLineEdit(select_file_long_wav_Dialog)
        self.lineEdit_non_silence_thresh.setObjectName(u"lineEdit_non_silence_thresh")
        self.lineEdit_non_silence_thresh.setGeometry(QRect(430, 130, 101, 21))
        self.label_6 = QLabel(select_file_long_wav_Dialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(290, 130, 131, 16))

        self.retranslateUi(select_file_long_wav_Dialog)

        QMetaObject.connectSlotsByName(select_file_long_wav_Dialog)
    # setupUi

    def retranslateUi(self, select_file_long_wav_Dialog):
        select_file_long_wav_Dialog.setWindowTitle(QCoreApplication.translate("select_file_long_wav_Dialog", u"\u5bfc\u5165\u6587\u4ef6", None))
        self.lineEdit_wav.setText("")
        self.label.setText(QCoreApplication.translate("select_file_long_wav_Dialog", u"\u8bf7\u9009\u62e9\u4e00\u4e2a\u97f3\u9891\u6587\u4ef6\u548c\u5b83\u5bf9\u5e94\u7684SRT\u5b57\u5e55\u6587\u4ef6", None))
        self.label_2.setText(QCoreApplication.translate("select_file_long_wav_Dialog", u"\u97f3\u9891\u6587\u4ef6\uff1a", None))
        self.pushButton_select_wav.setText(QCoreApplication.translate("select_file_long_wav_Dialog", u"\u9009\u62e9\u6587\u4ef6", None))
        self.pushButton_back.setText(QCoreApplication.translate("select_file_long_wav_Dialog", u"\u53d6\u6d88", None))
        self.pushButton_submit.setText(QCoreApplication.translate("select_file_long_wav_Dialog", u"\u786e\u5b9a", None))
        self.error_lable.setText("")
        self.lineEdit_spk.setText("")
        self.label_4.setText(QCoreApplication.translate("select_file_long_wav_Dialog", u"\u53d1\u97f3\u4eba\uff1a", None))
        self.label_5.setText(QCoreApplication.translate("select_file_long_wav_Dialog", u"\u6700\u77ed\u9759\u97f3\u957f\u5ea6(ms)\uff1a", None))
        self.lineEdit_min_silence_len.setText("")
        self.lineEdit_non_silence_thresh.setText("")
        self.label_6.setText(QCoreApplication.translate("select_file_long_wav_Dialog", u"\u9759\u97f3\u9608\u503c(dBFS)\uff1a", None))
    # retranslateUi

