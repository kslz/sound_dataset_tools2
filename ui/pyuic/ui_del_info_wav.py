# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'del_info_wav.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QLabel,
    QPushButton, QSizePolicy, QWidget)

class Ui_del_info_wav_Dialog(object):
    def setupUi(self, del_info_wav_Dialog):
        if not del_info_wav_Dialog.objectName():
            del_info_wav_Dialog.setObjectName(u"del_info_wav_Dialog")
        del_info_wav_Dialog.resize(600, 250)
        del_info_wav_Dialog.setMinimumSize(QSize(600, 250))
        del_info_wav_Dialog.setMaximumSize(QSize(600, 250))
        font = QFont()
        font.setPointSize(12)
        del_info_wav_Dialog.setFont(font)
        self.label = QLabel(del_info_wav_Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 21, 561, 20))
        self.label_2 = QLabel(del_info_wav_Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 70, 81, 16))
        self.pushButton_back = QPushButton(del_info_wav_Dialog)
        self.pushButton_back.setObjectName(u"pushButton_back")
        self.pushButton_back.setGeometry(QRect(500, 200, 81, 24))
        self.pushButton_submit = QPushButton(del_info_wav_Dialog)
        self.pushButton_submit.setObjectName(u"pushButton_submit")
        self.pushButton_submit.setGeometry(QRect(390, 200, 81, 24))
        self.error_lable = QLabel(del_info_wav_Dialog)
        self.error_lable.setObjectName(u"error_lable")
        self.error_lable.setGeometry(QRect(30, 170, 541, 16))
        self.error_lable.setFont(font)
        self.error_lable.setStyleSheet(u"color: red;")
        self.comboBox_files = QComboBox(del_info_wav_Dialog)
        self.comboBox_files.setObjectName(u"comboBox_files")
        self.comboBox_files.setGeometry(QRect(130, 70, 381, 22))

        self.retranslateUi(del_info_wav_Dialog)

        QMetaObject.connectSlotsByName(del_info_wav_Dialog)
    # setupUi

    def retranslateUi(self, del_info_wav_Dialog):
        del_info_wav_Dialog.setWindowTitle(QCoreApplication.translate("del_info_wav_Dialog", u"\u5220\u9664\u6570\u636e", None))
        self.label.setText(QCoreApplication.translate("del_info_wav_Dialog", u"\u9009\u62e9\u4e00\u4e2a\u4e4b\u524d\u5bfc\u5165\u7684\u97f3\u9891\u6587\u4ef6\uff0c\u5220\u9664\u4e0e\u6b64\u6587\u4ef6\u5173\u8054\u7684\u6570\u636e", None))
        self.label_2.setText(QCoreApplication.translate("del_info_wav_Dialog", u"\u97f3\u9891\u6587\u4ef6\uff1a", None))
        self.pushButton_back.setText(QCoreApplication.translate("del_info_wav_Dialog", u"\u53d6\u6d88", None))
        self.pushButton_submit.setText(QCoreApplication.translate("del_info_wav_Dialog", u"\u786e\u5b9a", None))
        self.error_lable.setText("")
    # retranslateUi

