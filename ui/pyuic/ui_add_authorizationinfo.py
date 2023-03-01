# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_authorizationinfo.ui'
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
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_AddAuthenticationDialog(object):
    def setupUi(self, AddAuthenticationDialog):
        if not AddAuthenticationDialog.objectName():
            AddAuthenticationDialog.setObjectName(u"AddAuthenticationDialog")
        AddAuthenticationDialog.resize(400, 500)
        font = QFont()
        font.setPointSize(12)
        AddAuthenticationDialog.setFont(font)
        self.label = QLabel(AddAuthenticationDialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 181, 21))
        self.lineEdit_name = QLineEdit(AddAuthenticationDialog)
        self.lineEdit_name.setObjectName(u"lineEdit_name")
        self.lineEdit_name.setGeometry(QRect(20, 50, 351, 21))
        self.label_2 = QLabel(AddAuthenticationDialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 90, 191, 21))
        self.label_3 = QLabel(AddAuthenticationDialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 160, 201, 21))
        self.label_4 = QLabel(AddAuthenticationDialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 230, 141, 21))
        self.lineEdit_appid = QLineEdit(AddAuthenticationDialog)
        self.lineEdit_appid.setObjectName(u"lineEdit_appid")
        self.lineEdit_appid.setGeometry(QRect(20, 120, 351, 21))
        self.lineEdit_apisecret = QLineEdit(AddAuthenticationDialog)
        self.lineEdit_apisecret.setObjectName(u"lineEdit_apisecret")
        self.lineEdit_apisecret.setGeometry(QRect(20, 190, 351, 21))
        self.lineEdit_apikey = QLineEdit(AddAuthenticationDialog)
        self.lineEdit_apikey.setObjectName(u"lineEdit_apikey")
        self.lineEdit_apikey.setGeometry(QRect(20, 260, 351, 21))
        self.label_error = QLabel(AddAuthenticationDialog)
        self.label_error.setObjectName(u"label_error")
        self.label_error.setGeometry(QRect(20, 390, 351, 21))
        self.label_error.setStyleSheet(u"color: red;")
        self.pushButton_close = QPushButton(AddAuthenticationDialog)
        self.pushButton_close.setObjectName(u"pushButton_close")
        self.pushButton_close.setGeometry(QRect(264, 440, 111, 24))
        self.pushButton_commit = QPushButton(AddAuthenticationDialog)
        self.pushButton_commit.setObjectName(u"pushButton_commit")
        self.pushButton_commit.setGeometry(QRect(130, 440, 111, 24))
        self.comboBox_app = QComboBox(AddAuthenticationDialog)
        self.comboBox_app.setObjectName(u"comboBox_app")
        self.comboBox_app.setGeometry(QRect(20, 330, 111, 22))
        self.label_5 = QLabel(AddAuthenticationDialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 300, 141, 21))

        self.retranslateUi(AddAuthenticationDialog)

        QMetaObject.connectSlotsByName(AddAuthenticationDialog)
    # setupUi

    def retranslateUi(self, AddAuthenticationDialog):
        AddAuthenticationDialog.setWindowTitle(QCoreApplication.translate("AddAuthenticationDialog", u"\u6dfb\u52a0\u6388\u6743\u4fe1\u606f", None))
        self.label.setText(QCoreApplication.translate("AddAuthenticationDialog", u"\u540d\u79f0", None))
        self.label_2.setText(QCoreApplication.translate("AddAuthenticationDialog", u"APPID", None))
        self.label_3.setText(QCoreApplication.translate("AddAuthenticationDialog", u"APISecret\uff08client_secret\uff09", None))
        self.label_4.setText(QCoreApplication.translate("AddAuthenticationDialog", u"APIKey\uff08client_id\uff09", None))
        self.label_error.setText("")
        self.pushButton_close.setText(QCoreApplication.translate("AddAuthenticationDialog", u"\u53d6\u6d88", None))
        self.pushButton_commit.setText(QCoreApplication.translate("AddAuthenticationDialog", u"\u63d0\u4ea4", None))
        self.label_5.setText(QCoreApplication.translate("AddAuthenticationDialog", u"\u5e94\u7528\u7c7b\u578b", None))
    # retranslateUi

