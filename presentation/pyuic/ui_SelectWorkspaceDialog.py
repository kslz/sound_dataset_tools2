# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SelectWorkspaceDialog.ui'
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

class Ui_SelectWorkspaceDialog(object):
    def setupUi(self, SelectWorkspaceDialog):
        if not SelectWorkspaceDialog.objectName():
            SelectWorkspaceDialog.setObjectName(u"SelectWorkspaceDialog")
        SelectWorkspaceDialog.resize(400, 200)
        self.lineEdit = QLineEdit(SelectWorkspaceDialog)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(80, 60, 291, 21))
        font = QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.label = QLabel(SelectWorkspaceDialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 60, 53, 21))
        self.label.setFont(font)
        self.cancel_button = QPushButton(SelectWorkspaceDialog)
        self.cancel_button.setObjectName(u"cancel_button")
        self.cancel_button.setGeometry(QRect(280, 150, 100, 30))
        self.submit_button = QPushButton(SelectWorkspaceDialog)
        self.submit_button.setObjectName(u"submit_button")
        self.submit_button.setGeometry(QRect(160, 150, 100, 30))

        self.retranslateUi(SelectWorkspaceDialog)

        QMetaObject.connectSlotsByName(SelectWorkspaceDialog)
    # setupUi

    def retranslateUi(self, SelectWorkspaceDialog):
        SelectWorkspaceDialog.setWindowTitle(QCoreApplication.translate("SelectWorkspaceDialog", u"Dialog", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("SelectWorkspaceDialog", u"\u8bf7\u5728\u8fd9\u91cc\u8f93\u5165\u5de5\u4f5c\u533a\u8def\u5f84\uff0c\u652f\u6301\u76f8\u5bf9\u8def\u5f84", None))
        self.label.setText(QCoreApplication.translate("SelectWorkspaceDialog", u"\u5de5\u4f5c\u533a\uff1a", None))
        self.cancel_button.setText(QCoreApplication.translate("SelectWorkspaceDialog", u"\u9000\u51fa", None))
        self.submit_button.setText(QCoreApplication.translate("SelectWorkspaceDialog", u"\u786e\u5b9a", None))
    # retranslateUi

