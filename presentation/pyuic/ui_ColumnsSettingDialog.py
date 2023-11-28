# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ColumnsSettingDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QWidget)

class Ui_ColumnsSettingDialog(object):
    def setupUi(self, ColumnsSettingDialog):
        if not ColumnsSettingDialog.objectName():
            ColumnsSettingDialog.setObjectName(u"ColumnsSettingDialog")
        ColumnsSettingDialog.resize(400, 300)
        font = QFont()
        font.setPointSize(12)
        ColumnsSettingDialog.setFont(font)
        self.scrollArea = QScrollArea(ColumnsSettingDialog)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(20, 20, 251, 261))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 249, 259))
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 3, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.pushButton_ok = QPushButton(ColumnsSettingDialog)
        self.pushButton_ok.setObjectName(u"pushButton_ok")
        self.pushButton_ok.setGeometry(QRect(290, 20, 75, 24))
        self.pushButton_cancel = QPushButton(ColumnsSettingDialog)
        self.pushButton_cancel.setObjectName(u"pushButton_cancel")
        self.pushButton_cancel.setGeometry(QRect(290, 60, 75, 24))

        self.retranslateUi(ColumnsSettingDialog)

        QMetaObject.connectSlotsByName(ColumnsSettingDialog)
    # setupUi

    def retranslateUi(self, ColumnsSettingDialog):
        ColumnsSettingDialog.setWindowTitle(QCoreApplication.translate("ColumnsSettingDialog", u"\u81ea\u5b9a\u4e49\u5217", None))
        self.pushButton_ok.setText(QCoreApplication.translate("ColumnsSettingDialog", u"\u786e\u5b9a", None))
        self.pushButton_cancel.setText(QCoreApplication.translate("ColumnsSettingDialog", u"\u53d6\u6d88", None))
    # retranslateUi

