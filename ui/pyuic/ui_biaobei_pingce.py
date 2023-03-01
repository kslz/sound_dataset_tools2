# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'biaobei_pingce.ui'
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
    QLabel, QPushButton, QSizePolicy, QWidget)

class Ui_BiaobeiPingceDialog(object):
    def setupUi(self, BiaobeiPingceDialog):
        if not BiaobeiPingceDialog.objectName():
            BiaobeiPingceDialog.setObjectName(u"BiaobeiPingceDialog")
        BiaobeiPingceDialog.resize(400, 300)
        font = QFont()
        font.setPointSize(12)
        BiaobeiPingceDialog.setFont(font)
        self.checkBox = QCheckBox(BiaobeiPingceDialog)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(30, 30, 221, 20))
        self.checkBox_2 = QCheckBox(BiaobeiPingceDialog)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setGeometry(QRect(30, 60, 281, 20))
        self.checkBox_2.setCheckable(True)
        self.checkBox_2.setChecked(True)
        self.pushButton_quxiao = QPushButton(BiaobeiPingceDialog)
        self.pushButton_quxiao.setObjectName(u"pushButton_quxiao")
        self.pushButton_quxiao.setGeometry(QRect(310, 260, 75, 24))
        self.pushButton_queding = QPushButton(BiaobeiPingceDialog)
        self.pushButton_queding.setObjectName(u"pushButton_queding")
        self.pushButton_queding.setGeometry(QRect(220, 260, 75, 24))
        self.comboBox = QComboBox(BiaobeiPingceDialog)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(160, 90, 131, 22))
        self.label = QLabel(BiaobeiPingceDialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 90, 111, 16))
        self.label_error = QLabel(BiaobeiPingceDialog)
        self.label_error.setObjectName(u"label_error")
        self.label_error.setGeometry(QRect(30, 230, 351, 16))
        self.label_error.setStyleSheet(u"color:red")

        self.retranslateUi(BiaobeiPingceDialog)

        QMetaObject.connectSlotsByName(BiaobeiPingceDialog)
    # setupUi

    def retranslateUi(self, BiaobeiPingceDialog):
        BiaobeiPingceDialog.setWindowTitle(QCoreApplication.translate("BiaobeiPingceDialog", u"\u6807\u8d1d\u8bed\u97f3\u8bc4\u6d4b", None))
        self.checkBox.setText(QCoreApplication.translate("BiaobeiPingceDialog", u"\u53ea\u5bf9\u672a\u6253\u5206\u7684\u6570\u636e\u8fdb\u884c\u8bc4\u6d4b", None))
        self.checkBox_2.setText(QCoreApplication.translate("BiaobeiPingceDialog", u"\u53ea\u5bf9\u652f\u6301\u7684\u6570\u636e\u8fdb\u884c\u8bc4\u6d4b\uff08\u7eaf\u4e2d\u6587\uff09", None))
        self.pushButton_quxiao.setText(QCoreApplication.translate("BiaobeiPingceDialog", u"\u53d6\u6d88", None))
        self.pushButton_queding.setText(QCoreApplication.translate("BiaobeiPingceDialog", u"\u786e\u5b9a", None))
        self.label.setText(QCoreApplication.translate("BiaobeiPingceDialog", u"\u9009\u62e9\u6388\u6743\u4fe1\u606f\uff1a", None))
        self.label_error.setText("")
    # retranslateUi

