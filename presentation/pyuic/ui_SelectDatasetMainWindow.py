# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SelectDatasetMainWindow.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHeaderView, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_SelectDatasetMainWindow(object):
    def setupUi(self, SelectDatasetMainWindow):
        if not SelectDatasetMainWindow.objectName():
            SelectDatasetMainWindow.setObjectName(u"SelectDatasetMainWindow")
        SelectDatasetMainWindow.resize(800, 600)
        SelectDatasetMainWindow.setMinimumSize(QSize(800, 600))
        SelectDatasetMainWindow.setMaximumSize(QSize(800, 600))
        self.centralwidget = QWidget(SelectDatasetMainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(50, 50, 701, 441))
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(50, 510, 101, 31))
        font = QFont()
        font.setPointSize(11)
        self.pushButton.setFont(font)
        SelectDatasetMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(SelectDatasetMainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        SelectDatasetMainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(SelectDatasetMainWindow)
        self.statusbar.setObjectName(u"statusbar")
        SelectDatasetMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SelectDatasetMainWindow)

        QMetaObject.connectSlotsByName(SelectDatasetMainWindow)
    # setupUi

    def retranslateUi(self, SelectDatasetMainWindow):
        SelectDatasetMainWindow.setWindowTitle(QCoreApplication.translate("SelectDatasetMainWindow", u"\u9009\u62e9\u6570\u636e\u96c6", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("SelectDatasetMainWindow", u"\u6570\u636e\u96c6\u540d", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("SelectDatasetMainWindow", u"\u521b\u5efa\u65f6\u95f4", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("SelectDatasetMainWindow", u"\u4e0a\u6b21\u4f7f\u7528\u65f6\u95f4", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("SelectDatasetMainWindow", u"\u5907\u6ce8", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("SelectDatasetMainWindow", u"\u64cd\u4f5c", None));
        self.pushButton.setText(QCoreApplication.translate("SelectDatasetMainWindow", u"\u6dfb\u52a0\u6570\u636e\u96c6", None))
    # retranslateUi

