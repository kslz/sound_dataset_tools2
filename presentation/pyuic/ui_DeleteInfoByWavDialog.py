# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DeleteInfoByWavDialog.ui'
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

class Ui_DeleteInfoByWavDialog(object):
    def setupUi(self, DeleteInfoByWavDialog):
        if not DeleteInfoByWavDialog.objectName():
            DeleteInfoByWavDialog.setObjectName(u"DeleteInfoByWavDialog")
        DeleteInfoByWavDialog.resize(600, 250)
        DeleteInfoByWavDialog.setMinimumSize(QSize(600, 250))
        DeleteInfoByWavDialog.setMaximumSize(QSize(600, 250))
        font = QFont()
        font.setPointSize(12)
        DeleteInfoByWavDialog.setFont(font)
        self.label = QLabel(DeleteInfoByWavDialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 21, 561, 20))
        self.label_2 = QLabel(DeleteInfoByWavDialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 70, 81, 16))
        self.pushButton_back = QPushButton(DeleteInfoByWavDialog)
        self.pushButton_back.setObjectName(u"pushButton_back")
        self.pushButton_back.setGeometry(QRect(500, 200, 81, 24))
        self.pushButton_submit = QPushButton(DeleteInfoByWavDialog)
        self.pushButton_submit.setObjectName(u"pushButton_submit")
        self.pushButton_submit.setGeometry(QRect(390, 200, 81, 24))
        self.error_lable = QLabel(DeleteInfoByWavDialog)
        self.error_lable.setObjectName(u"error_lable")
        self.error_lable.setGeometry(QRect(30, 170, 541, 16))
        self.error_lable.setFont(font)
        self.error_lable.setStyleSheet(u"color: red;")
        self.comboBox_files = QComboBox(DeleteInfoByWavDialog)
        self.comboBox_files.setObjectName(u"comboBox_files")
        self.comboBox_files.setGeometry(QRect(130, 70, 381, 22))

        self.retranslateUi(DeleteInfoByWavDialog)

        QMetaObject.connectSlotsByName(DeleteInfoByWavDialog)
    # setupUi

    def retranslateUi(self, DeleteInfoByWavDialog):
        DeleteInfoByWavDialog.setWindowTitle(QCoreApplication.translate("DeleteInfoByWavDialog", u"\u5220\u9664\u6570\u636e", None))
        self.label.setText(QCoreApplication.translate("DeleteInfoByWavDialog", u"\u9009\u62e9\u4e00\u4e2a\u4e4b\u524d\u5bfc\u5165\u7684\u97f3\u9891\u6587\u4ef6\uff0c\u5220\u9664\u4e0e\u6b64\u6587\u4ef6\u5173\u8054\u7684\u6570\u636e", None))
        self.label_2.setText(QCoreApplication.translate("DeleteInfoByWavDialog", u"\u97f3\u9891\u6587\u4ef6\uff1a", None))
        self.pushButton_back.setText(QCoreApplication.translate("DeleteInfoByWavDialog", u"\u53d6\u6d88", None))
        self.pushButton_submit.setText(QCoreApplication.translate("DeleteInfoByWavDialog", u"\u786e\u5b9a", None))
        self.error_lable.setText("")
    # retranslateUi

