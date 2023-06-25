# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pingce_jindutiao.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QProgressBar, QPushButton,
    QSizePolicy, QWidget)

class Ui_PingcejinduDialog(object):
    def setupUi(self, PingcejinduDialog):
        if not PingcejinduDialog.objectName():
            PingcejinduDialog.setObjectName(u"PingcejinduDialog")
        PingcejinduDialog.resize(371, 111)
        self.progressBar = QProgressBar(PingcejinduDialog)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(20, 20, 311, 23))
        font = QFont()
        font.setPointSize(12)
        self.progressBar.setFont(font)
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(0)
        self.progressBar.setValue(0)
        self.progressBar.setTextDirection(QProgressBar.TopToBottom)
        self.pushButton_queding = QPushButton(PingcejinduDialog)
        self.pushButton_queding.setObjectName(u"pushButton_queding")
        self.pushButton_queding.setGeometry(QRect(20, 60, 75, 24))
        self.pushButton_queding.setFont(font)
        self.pushButton_queding_2 = QPushButton(PingcejinduDialog)
        self.pushButton_queding_2.setObjectName(u"pushButton_queding_2")
        self.pushButton_queding_2.setGeometry(QRect(140, 60, 75, 24))
        self.pushButton_queding_2.setFont(font)
        self.pushButton_queding_3 = QPushButton(PingcejinduDialog)
        self.pushButton_queding_3.setObjectName(u"pushButton_queding_3")
        self.pushButton_queding_3.setGeometry(QRect(260, 60, 75, 24))
        self.pushButton_queding_3.setFont(font)

        self.retranslateUi(PingcejinduDialog)

        QMetaObject.connectSlotsByName(PingcejinduDialog)
    # setupUi

    def retranslateUi(self, PingcejinduDialog):
        PingcejinduDialog.setWindowTitle(QCoreApplication.translate("PingcejinduDialog", u"\u8bed\u97f3\u8bc4\u6d4b", None))
        self.progressBar.setFormat(QCoreApplication.translate("PingcejinduDialog", u"%v/%m", None))
        self.pushButton_queding.setText(QCoreApplication.translate("PingcejinduDialog", u"\u5f00\u59cb", None))
        self.pushButton_queding_2.setText(QCoreApplication.translate("PingcejinduDialog", u"\u6682\u505c", None))
        self.pushButton_queding_3.setText(QCoreApplication.translate("PingcejinduDialog", u"\u505c\u6b62", None))
    # retranslateUi

