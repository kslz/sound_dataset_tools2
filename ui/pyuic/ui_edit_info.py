# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_info.ui'
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

class Ui_EditInfoDialog(object):
    def setupUi(self, EditInfoDialog):
        if not EditInfoDialog.objectName():
            EditInfoDialog.setObjectName(u"EditInfoDialog")
        EditInfoDialog.resize(400, 300)
        font = QFont()
        font.setPointSize(12)
        EditInfoDialog.setFont(font)
        self.label = QLabel(EditInfoDialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 111, 20))
        self.label_info_id = QLabel(EditInfoDialog)
        self.label_info_id.setObjectName(u"label_info_id")
        self.label_info_id.setGeometry(QRect(150, 20, 111, 20))
        self.label_3 = QLabel(EditInfoDialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 50, 111, 20))
        self.lineEdit_info_text = QLineEdit(EditInfoDialog)
        self.lineEdit_info_text.setObjectName(u"lineEdit_info_text")
        self.lineEdit_info_text.setGeometry(QRect(150, 50, 231, 21))
        self.pushButton = QPushButton(EditInfoDialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(290, 20, 91, 24))
        self.label_4 = QLabel(EditInfoDialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 80, 111, 20))
        self.comboBox = QComboBox(EditInfoDialog)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(150, 80, 231, 22))
        self.pushButton_2 = QPushButton(EditInfoDialog)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(320, 260, 75, 24))
        self.pushButton_3 = QPushButton(EditInfoDialog)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(230, 260, 75, 24))

        self.retranslateUi(EditInfoDialog)

        QMetaObject.connectSlotsByName(EditInfoDialog)
    # setupUi

    def retranslateUi(self, EditInfoDialog):
        EditInfoDialog.setWindowTitle(QCoreApplication.translate("EditInfoDialog", u"\u6570\u636e\u7f16\u8f91", None))
        self.label.setText(QCoreApplication.translate("EditInfoDialog", u"\u6570\u636eid:", None))
        self.label_info_id.setText(QCoreApplication.translate("EditInfoDialog", u"\u6570\u636eid", None))
        self.label_3.setText(QCoreApplication.translate("EditInfoDialog", u"\u6807\u6ce8\u6587\u672c\uff1a", None))
        self.lineEdit_info_text.setText("")
        self.pushButton.setText(QCoreApplication.translate("EditInfoDialog", u"\u8bd5\u542c", None))
        self.label_4.setText(QCoreApplication.translate("EditInfoDialog", u"\u53d1\u97f3\u4eba\uff1a", None))
        self.pushButton_2.setText(QCoreApplication.translate("EditInfoDialog", u"\u53d6\u6d88", None))
        self.pushButton_3.setText(QCoreApplication.translate("EditInfoDialog", u"\u786e\u5b9a", None))
    # retranslateUi

