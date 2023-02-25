# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dataset_view.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QGroupBox,
    QHeaderView, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTabWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_DatasetMainWindow(object):
    def setupUi(self, DatasetMainWindow):
        if not DatasetMainWindow.objectName():
            DatasetMainWindow.setObjectName(u"DatasetMainWindow")
        DatasetMainWindow.resize(1200, 800)
        DatasetMainWindow.setMinimumSize(QSize(1200, 800))
        DatasetMainWindow.setMaximumSize(QSize(1200, 800))
        self.centralwidget = QWidget(DatasetMainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 10, 1181, 681))
        font = QFont()
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_2 = QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget_2 = QWidget(self.tab)
        self.widget_2.setObjectName(u"widget_2")
        self.tableWidget = QTableWidget(self.widget_2)
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
        if (self.tableWidget.rowCount() < 10):
            self.tableWidget.setRowCount(10)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, __qtablewidgetitem14)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 10, 1141, 421))
        self.tableWidget.setFont(font)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setMinimumSectionSize(20)
        self.comboBox = QComboBox(self.widget_2)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(10, 440, 201, 31))
        font1 = QFont()
        font1.setPointSize(10)
        self.comboBox.setFont(font1)
        self.pushButton_add_wav_srt = QPushButton(self.widget_2)
        self.pushButton_add_wav_srt.setObjectName(u"pushButton_add_wav_srt")
        self.pushButton_add_wav_srt.setGeometry(QRect(230, 440, 231, 31))
        self.pushButton_add_wav_srt_2 = QPushButton(self.widget_2)
        self.pushButton_add_wav_srt_2.setObjectName(u"pushButton_add_wav_srt_2")
        self.pushButton_add_wav_srt_2.setGeometry(QRect(920, 440, 231, 31))

        self.verticalLayout_2.addWidget(self.widget_2)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout = QVBoxLayout(self.tab_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(self.tab_2)
        self.widget.setObjectName(u"widget")

        self.verticalLayout.addWidget(self.widget)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.label = QLabel(self.tab_3)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 271, 21))
        self.label.setFont(font)
        self.tabWidget_2 = QTabWidget(self.tab_3)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setGeometry(QRect(20, 50, 1141, 601))
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.groupBox = QGroupBox(self.tab_4)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 1111, 271))
        self.tableWidget_biaobei = QTableWidget(self.groupBox)
        if (self.tableWidget_biaobei.columnCount() < 6):
            self.tableWidget_biaobei.setColumnCount(6)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget_biaobei.setHorizontalHeaderItem(0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget_biaobei.setHorizontalHeaderItem(1, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget_biaobei.setHorizontalHeaderItem(2, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget_biaobei.setHorizontalHeaderItem(3, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget_biaobei.setHorizontalHeaderItem(4, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget_biaobei.setHorizontalHeaderItem(5, __qtablewidgetitem20)
        self.tableWidget_biaobei.setObjectName(u"tableWidget_biaobei")
        self.tableWidget_biaobei.setGeometry(QRect(20, 20, 961, 231))
        self.tableWidget_biaobei.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_biaobei.verticalHeader().setVisible(False)
        self.pushButton_add_biaobei = QPushButton(self.groupBox)
        self.pushButton_add_biaobei.setObjectName(u"pushButton_add_biaobei")
        self.pushButton_add_biaobei.setGeometry(QRect(990, 20, 111, 41))
        self.groupBox_2 = QGroupBox(self.tab_4)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 290, 1111, 271))
        self.pushButton_add_xunfei = QPushButton(self.groupBox_2)
        self.pushButton_add_xunfei.setObjectName(u"pushButton_add_xunfei")
        self.pushButton_add_xunfei.setGeometry(QRect(990, 20, 111, 41))
        self.tableWidget_xunfei = QTableWidget(self.groupBox_2)
        if (self.tableWidget_xunfei.columnCount() < 6):
            self.tableWidget_xunfei.setColumnCount(6)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget_xunfei.setHorizontalHeaderItem(0, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget_xunfei.setHorizontalHeaderItem(1, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget_xunfei.setHorizontalHeaderItem(2, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget_xunfei.setHorizontalHeaderItem(3, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget_xunfei.setHorizontalHeaderItem(4, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableWidget_xunfei.setHorizontalHeaderItem(5, __qtablewidgetitem26)
        self.tableWidget_xunfei.setObjectName(u"tableWidget_xunfei")
        self.tableWidget_xunfei.setGeometry(QRect(20, 20, 961, 231))
        self.tableWidget_xunfei.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_xunfei.verticalHeader().setVisible(False)
        self.tabWidget_2.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.tabWidget_2.addTab(self.tab_5, "")
        self.tabWidget.addTab(self.tab_3, "")
        DatasetMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(DatasetMainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1200, 22))
        DatasetMainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(DatasetMainWindow)
        self.statusbar.setObjectName(u"statusbar")
        DatasetMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(DatasetMainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(DatasetMainWindow)
    # setupUi

    def retranslateUi(self, DatasetMainWindow):
        DatasetMainWindow.setWindowTitle(QCoreApplication.translate("DatasetMainWindow", u"\u6570\u636e\u96c6", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("DatasetMainWindow", u"\u5e8f\u53f7", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("DatasetMainWindow", u"\u6807\u6ce8\u6587\u672c", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("DatasetMainWindow", u"\u53d1\u97f3\u4eba", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("DatasetMainWindow", u"\u6807\u7b7e", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("DatasetMainWindow", u"\u64cd\u4f5c", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("DatasetMainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("DatasetMainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("DatasetMainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem8 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("DatasetMainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem9 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("DatasetMainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem10 = self.tableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("DatasetMainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem11 = self.tableWidget.verticalHeaderItem(6)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("DatasetMainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem12 = self.tableWidget.verticalHeaderItem(7)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("DatasetMainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem13 = self.tableWidget.verticalHeaderItem(8)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("DatasetMainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem14 = self.tableWidget.verticalHeaderItem(9)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("DatasetMainWindow", u"\u65b0\u5efa\u884c", None));
        self.pushButton_add_wav_srt.setText(QCoreApplication.translate("DatasetMainWindow", u"\u4ece\u6587\u4ef6\u5bfc\u5165\uff08\u97f3\u9891+\u5b57\u5e55\uff09", None))
        self.pushButton_add_wav_srt_2.setText(QCoreApplication.translate("DatasetMainWindow", u"\u5bfc\u51fa\u6570\u636e\u96c6", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("DatasetMainWindow", u"\u6570\u636e\u96c6\u6982\u89c8", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("DatasetMainWindow", u"\u6570\u636e\u5904\u7406", None))
        self.label.setText(QCoreApplication.translate("DatasetMainWindow", u"\u6ce8\u610f\uff1a\u672c\u9875\u8bbe\u7f6e\u5728\u672c\u5de5\u4f5c\u533a\u4e0b\u901a\u7528", None))
        self.groupBox.setTitle(QCoreApplication.translate("DatasetMainWindow", u"\u6807\u8d1d", None))
        ___qtablewidgetitem15 = self.tableWidget_biaobei.horizontalHeaderItem(0)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("DatasetMainWindow", u"id", None));
        ___qtablewidgetitem16 = self.tableWidget_biaobei.horizontalHeaderItem(1)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("DatasetMainWindow", u"\u540d\u79f0", None));
        ___qtablewidgetitem17 = self.tableWidget_biaobei.horizontalHeaderItem(2)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("DatasetMainWindow", u"APP\u7c7b\u578b", None));
        ___qtablewidgetitem18 = self.tableWidget_biaobei.horizontalHeaderItem(3)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("DatasetMainWindow", u"APPID", None));
        ___qtablewidgetitem19 = self.tableWidget_biaobei.horizontalHeaderItem(4)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("DatasetMainWindow", u"APISecret\uff08client_secret\uff09", None));
        ___qtablewidgetitem20 = self.tableWidget_biaobei.horizontalHeaderItem(5)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("DatasetMainWindow", u"APIKey\uff08client_id\uff09", None));
        self.pushButton_add_biaobei.setText(QCoreApplication.translate("DatasetMainWindow", u"\u6dfb\u52a0", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("DatasetMainWindow", u"\u8baf\u98de", None))
        self.pushButton_add_xunfei.setText(QCoreApplication.translate("DatasetMainWindow", u"\u6dfb\u52a0", None))
        ___qtablewidgetitem21 = self.tableWidget_xunfei.horizontalHeaderItem(0)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("DatasetMainWindow", u"id", None));
        ___qtablewidgetitem22 = self.tableWidget_xunfei.horizontalHeaderItem(1)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("DatasetMainWindow", u"\u540d\u79f0", None));
        ___qtablewidgetitem23 = self.tableWidget_xunfei.horizontalHeaderItem(2)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("DatasetMainWindow", u"APP\u7c7b\u578b", None));
        ___qtablewidgetitem24 = self.tableWidget_xunfei.horizontalHeaderItem(3)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("DatasetMainWindow", u"APPID", None));
        ___qtablewidgetitem25 = self.tableWidget_xunfei.horizontalHeaderItem(4)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("DatasetMainWindow", u"APISecret\uff08client_secret\uff09", None));
        ___qtablewidgetitem26 = self.tableWidget_xunfei.horizontalHeaderItem(5)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("DatasetMainWindow", u"APIKey\uff08client_id\uff09", None));
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), QCoreApplication.translate("DatasetMainWindow", u"\u6388\u6743\u7ba1\u7406", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), QCoreApplication.translate("DatasetMainWindow", u"\u5168\u5c40\u8bbe\u7f6e", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("DatasetMainWindow", u"\u8f6f\u4ef6\u8bbe\u7f6e", None))
    # retranslateUi

