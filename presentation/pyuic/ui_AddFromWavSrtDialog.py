# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AddFromWavSrtDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_AddFromWavSrtDialog(object):
    def setupUi(self, AddFromWavSrtDialog):
        if not AddFromWavSrtDialog.objectName():
            AddFromWavSrtDialog.setObjectName(u"AddFromWavSrtDialog")
        AddFromWavSrtDialog.resize(600, 300)
        AddFromWavSrtDialog.setMinimumSize(QSize(600, 300))
        AddFromWavSrtDialog.setMaximumSize(QSize(600, 300))
        font = QFont()
        font.setPointSize(12)
        AddFromWavSrtDialog.setFont(font)
        self.lineEdit_wav = QLineEdit(AddFromWavSrtDialog)
        self.lineEdit_wav.setObjectName(u"lineEdit_wav")
        self.lineEdit_wav.setGeometry(QRect(110, 70, 371, 21))
        self.label = QLabel(AddFromWavSrtDialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 21, 341, 20))
        self.label_2 = QLabel(AddFromWavSrtDialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 70, 81, 16))
        self.lineEdit_srt = QLineEdit(AddFromWavSrtDialog)
        self.lineEdit_srt.setObjectName(u"lineEdit_srt")
        self.lineEdit_srt.setGeometry(QRect(110, 100, 371, 21))
        self.label_3 = QLabel(AddFromWavSrtDialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 100, 81, 16))
        self.pushButton_select_wav = QPushButton(AddFromWavSrtDialog)
        self.pushButton_select_wav.setObjectName(u"pushButton_select_wav")
        self.pushButton_select_wav.setGeometry(QRect(500, 69, 81, 23))
        self.pushButton_select_srt = QPushButton(AddFromWavSrtDialog)
        self.pushButton_select_srt.setObjectName(u"pushButton_select_srt")
        self.pushButton_select_srt.setGeometry(QRect(500, 99, 81, 23))
        self.pushButton_back = QPushButton(AddFromWavSrtDialog)
        self.pushButton_back.setObjectName(u"pushButton_back")
        self.pushButton_back.setGeometry(QRect(500, 210, 81, 24))
        self.pushButton_submit = QPushButton(AddFromWavSrtDialog)
        self.pushButton_submit.setObjectName(u"pushButton_submit")
        self.pushButton_submit.setGeometry(QRect(390, 210, 81, 24))
        self.error_lable = QLabel(AddFromWavSrtDialog)
        self.error_lable.setObjectName(u"error_lable")
        self.error_lable.setGeometry(QRect(30, 190, 541, 16))
        self.error_lable.setFont(font)
        self.error_lable.setStyleSheet(u"color: red;")
        self.lineEdit_spk = QLineEdit(AddFromWavSrtDialog)
        self.lineEdit_spk.setObjectName(u"lineEdit_spk")
        self.lineEdit_spk.setGeometry(QRect(110, 130, 371, 21))
        self.label_4 = QLabel(AddFromWavSrtDialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 130, 81, 16))
        self.checkBox_ismerge = QCheckBox(AddFromWavSrtDialog)
        self.checkBox_ismerge.setObjectName(u"checkBox_ismerge")
        self.checkBox_ismerge.setGeometry(QRect(30, 160, 421, 20))

        self.retranslateUi(AddFromWavSrtDialog)

        QMetaObject.connectSlotsByName(AddFromWavSrtDialog)
    # setupUi

    def retranslateUi(self, AddFromWavSrtDialog):
        AddFromWavSrtDialog.setWindowTitle(QCoreApplication.translate("AddFromWavSrtDialog", u"\u5bfc\u5165\u6587\u4ef6", None))
        self.lineEdit_wav.setText("")
        self.label.setText(QCoreApplication.translate("AddFromWavSrtDialog", u"\u8bf7\u9009\u62e9\u4e00\u4e2a\u97f3\u9891\u6587\u4ef6\u548c\u5b83\u5bf9\u5e94\u7684SRT\u5b57\u5e55\u6587\u4ef6", None))
        self.label_2.setText(QCoreApplication.translate("AddFromWavSrtDialog", u"\u97f3\u9891\u6587\u4ef6\uff1a", None))
        self.lineEdit_srt.setText("")
        self.label_3.setText(QCoreApplication.translate("AddFromWavSrtDialog", u"\u5b57\u5e55\u6587\u4ef6\uff1a", None))
        self.pushButton_select_wav.setText(QCoreApplication.translate("AddFromWavSrtDialog", u"\u9009\u62e9\u6587\u4ef6", None))
        self.pushButton_select_srt.setText(QCoreApplication.translate("AddFromWavSrtDialog", u"\u9009\u62e9\u6587\u4ef6", None))
        self.pushButton_back.setText(QCoreApplication.translate("AddFromWavSrtDialog", u"\u53d6\u6d88", None))
        self.pushButton_submit.setText(QCoreApplication.translate("AddFromWavSrtDialog", u"\u786e\u5b9a", None))
        self.error_lable.setText("")
        self.lineEdit_spk.setText("")
        self.label_4.setText(QCoreApplication.translate("AddFromWavSrtDialog", u"\u53d1\u97f3\u4eba\uff1a", None))
        self.checkBox_ismerge.setText(QCoreApplication.translate("AddFromWavSrtDialog", u"\u81ea\u52a8\u5c06\u76f8\u79bb\u8fc7\u8fd1\u7684\u5b57\u5e55\u5408\u4e3a\u4e00\u4e2a\uff08\u526a\u6620\u5b57\u5e55\u5efa\u8bae\u52fe\u9009\uff09", None))
    # retranslateUi

