# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'select_workspace.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 200)
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(280, 150, 100, 30))
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(160, 150, 100, 30))
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(80, 60, 291, 21))
        font = QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 60, 53, 21))
        self.label.setFont(font)

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(Form.close_program)
        self.pushButton_2.clicked.connect(Form.get_workspace)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u9009\u62e9\u5de5\u4f5c\u533a", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u9000\u51fa", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u786e\u5b9a", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"\u8bf7\u5728\u8fd9\u91cc\u8f93\u5165\u5de5\u4f5c\u533a\u8def\u5f84\uff0c\u652f\u6301\u76f8\u5bf9\u8def\u5f84", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u5de5\u4f5c\u533a\uff1a", None))
    # retranslateUi

