# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DatasetViewMainWindow.ui'
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
    QHBoxLayout, QHeaderView, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QTabWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_DatasetViewMainWindow(object):
    def setupUi(self, DatasetViewMainWindow):
        if not DatasetViewMainWindow.objectName():
            DatasetViewMainWindow.setObjectName(u"DatasetViewMainWindow")
        DatasetViewMainWindow.resize(1200, 800)
        DatasetViewMainWindow.setMinimumSize(QSize(1200, 700))
        self.centralwidget = QWidget(DatasetViewMainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_6 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        font = QFont()
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.tab1NewView = QWidget()
        self.tab1NewView.setObjectName(u"tab1NewView")
        self.verticalLayout_8 = QVBoxLayout(self.tab1NewView)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.groupBox_operate = QGroupBox(self.tab1NewView)
        self.groupBox_operate.setObjectName(u"groupBox_operate")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_operate)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_input = QPushButton(self.groupBox_operate)
        self.pushButton_input.setObjectName(u"pushButton_input")

        self.horizontalLayout_2.addWidget(self.pushButton_input)

        self.pushButton_search = QPushButton(self.groupBox_operate)
        self.pushButton_search.setObjectName(u"pushButton_search")

        self.horizontalLayout_2.addWidget(self.pushButton_search)

        self.pushButton_output = QPushButton(self.groupBox_operate)
        self.pushButton_output.setObjectName(u"pushButton_output")

        self.horizontalLayout_2.addWidget(self.pushButton_output)

        self.pushButton_columns_setting = QPushButton(self.groupBox_operate)
        self.pushButton_columns_setting.setObjectName(u"pushButton_columns_setting")

        self.horizontalLayout_2.addWidget(self.pushButton_columns_setting)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout_8.addWidget(self.groupBox_operate)

        self.groupBox_dataset = QGroupBox(self.tab1NewView)
        self.groupBox_dataset.setObjectName(u"groupBox_dataset")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_dataset.sizePolicy().hasHeightForWidth())
        self.groupBox_dataset.setSizePolicy(sizePolicy)
        self.verticalLayout_9 = QVBoxLayout(self.groupBox_dataset)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.tableWidget_info_show = QTableWidget(self.groupBox_dataset)
        self.tableWidget_info_show.setObjectName(u"tableWidget_info_show")

        self.verticalLayout_9.addWidget(self.tableWidget_info_show)

        self.widget_page_info = QWidget(self.groupBox_dataset)
        self.widget_page_info.setObjectName(u"widget_page_info")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_page_info)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.widget_page_size = QWidget(self.widget_page_info)
        self.widget_page_size.setObjectName(u"widget_page_size")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_page_size)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_page_info = QLabel(self.widget_page_size)
        self.label_page_info.setObjectName(u"label_page_info")

        self.horizontalLayout_4.addWidget(self.label_page_info)

        self.label_page_size_1 = QLabel(self.widget_page_size)
        self.label_page_size_1.setObjectName(u"label_page_size_1")

        self.horizontalLayout_4.addWidget(self.label_page_size_1)

        self.comboBox_page_size = QComboBox(self.widget_page_size)
        self.comboBox_page_size.setObjectName(u"comboBox_page_size")

        self.horizontalLayout_4.addWidget(self.comboBox_page_size)

        self.label_page_size_2 = QLabel(self.widget_page_size)
        self.label_page_size_2.setObjectName(u"label_page_size_2")

        self.horizontalLayout_4.addWidget(self.label_page_size_2)


        self.horizontalLayout_6.addWidget(self.widget_page_size)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)

        self.widget_page_change = QWidget(self.widget_page_info)
        self.widget_page_change.setObjectName(u"widget_page_change")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_page_change)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.pushButton_page_last = QPushButton(self.widget_page_change)
        self.pushButton_page_last.setObjectName(u"pushButton_page_last")

        self.horizontalLayout_5.addWidget(self.pushButton_page_last)

        self.pushButton_page_next = QPushButton(self.widget_page_change)
        self.pushButton_page_next.setObjectName(u"pushButton_page_next")

        self.horizontalLayout_5.addWidget(self.pushButton_page_next)


        self.horizontalLayout_6.addWidget(self.widget_page_change)


        self.verticalLayout_9.addWidget(self.widget_page_info)


        self.verticalLayout_8.addWidget(self.groupBox_dataset)

        self.tabWidget.addTab(self.tab1NewView, "")
        self.tab1View = QWidget()
        self.tab1View.setObjectName(u"tab1View")
        self.verticalLayout_2 = QVBoxLayout(self.tab1View)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget_2 = QWidget(self.tab1View)
        self.widget_2.setObjectName(u"widget_2")
        self.tableWidget = QTableWidget(self.widget_2)
        if (self.tableWidget.rowCount() < 10):
            self.tableWidget.setRowCount(10)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, __qtablewidgetitem9)
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
        self.pushButton_output_speaker = QPushButton(self.widget_2)
        self.pushButton_output_speaker.setObjectName(u"pushButton_output_speaker")
        self.pushButton_output_speaker.setGeometry(QRect(920, 440, 231, 31))
        self.pushButton_add_long_wav = QPushButton(self.widget_2)
        self.pushButton_add_long_wav.setObjectName(u"pushButton_add_long_wav")
        self.pushButton_add_long_wav.setGeometry(QRect(230, 490, 231, 31))
        self.pushButton_del_by_raw_wav = QPushButton(self.widget_2)
        self.pushButton_del_by_raw_wav.setObjectName(u"pushButton_del_by_raw_wav")
        self.pushButton_del_by_raw_wav.setGeometry(QRect(580, 440, 231, 31))

        self.verticalLayout_2.addWidget(self.widget_2)

        self.tabWidget.addTab(self.tab1View, "")
        self.tab2SearchOutput = QWidget()
        self.tab2SearchOutput.setObjectName(u"tab2SearchOutput")
        self.verticalLayout_3 = QVBoxLayout(self.tab2SearchOutput)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tbl_widget = QWidget(self.tab2SearchOutput)
        self.tbl_widget.setObjectName(u"tbl_widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(5)
        sizePolicy1.setHeightForWidth(self.tbl_widget.sizePolicy().hasHeightForWidth())
        self.tbl_widget.setSizePolicy(sizePolicy1)
        self.verticalLayout_4 = QVBoxLayout(self.tbl_widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.tableWidget_2 = QTableWidget(self.tbl_widget)
        self.tableWidget_2.setObjectName(u"tableWidget_2")

        self.verticalLayout_4.addWidget(self.tableWidget_2)


        self.verticalLayout_3.addWidget(self.tbl_widget)

        self.btn_widget = QWidget(self.tab2SearchOutput)
        self.btn_widget.setObjectName(u"btn_widget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(2)
        sizePolicy2.setHeightForWidth(self.btn_widget.sizePolicy().hasHeightForWidth())
        self.btn_widget.setSizePolicy(sizePolicy2)
        self.horizontalLayout = QHBoxLayout(self.btn_widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox_3 = QGroupBox(self.btn_widget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(1)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy3)
        self.verticalLayout_7 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.comboBox_2 = QComboBox(self.groupBox_3)
        self.comboBox_2.setObjectName(u"comboBox_2")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.comboBox_2.sizePolicy().hasHeightForWidth())
        self.comboBox_2.setSizePolicy(sizePolicy4)

        self.verticalLayout_7.addWidget(self.comboBox_2)


        self.horizontalLayout.addWidget(self.groupBox_3)

        self.widget_3 = QWidget(self.btn_widget)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(4)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy5)

        self.horizontalLayout.addWidget(self.widget_3)


        self.verticalLayout_3.addWidget(self.btn_widget)

        self.tabWidget.addTab(self.tab2SearchOutput, "")
        self.tab3DataProcessing = QWidget()
        self.tab3DataProcessing.setObjectName(u"tab3DataProcessing")
        self.verticalLayout = QVBoxLayout(self.tab3DataProcessing)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(self.tab3DataProcessing)
        self.widget.setObjectName(u"widget")
        self.pushButton_biaobei_pingce = QPushButton(self.widget)
        self.pushButton_biaobei_pingce.setObjectName(u"pushButton_biaobei_pingce")
        self.pushButton_biaobei_pingce.setGeometry(QRect(20, 20, 211, 51))

        self.verticalLayout.addWidget(self.widget)

        self.tabWidget.addTab(self.tab3DataProcessing, "")
        self.tab4Settings = QWidget()
        self.tab4Settings.setObjectName(u"tab4Settings")
        self.verticalLayout_5 = QVBoxLayout(self.tab4Settings)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label = QLabel(self.tab4Settings)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.verticalLayout_5.addWidget(self.label)

        self.tabWidget_2 = QTabWidget(self.tab4Settings)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.groupBox = QGroupBox(self.tab_4)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 1111, 271))
        self.tableWidget_biaobei = QTableWidget(self.groupBox)
        if (self.tableWidget_biaobei.columnCount() < 6):
            self.tableWidget_biaobei.setColumnCount(6)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_biaobei.setHorizontalHeaderItem(0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_biaobei.setHorizontalHeaderItem(1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_biaobei.setHorizontalHeaderItem(2, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget_biaobei.setHorizontalHeaderItem(3, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget_biaobei.setHorizontalHeaderItem(4, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget_biaobei.setHorizontalHeaderItem(5, __qtablewidgetitem15)
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
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget_xunfei.setHorizontalHeaderItem(0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget_xunfei.setHorizontalHeaderItem(1, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget_xunfei.setHorizontalHeaderItem(2, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget_xunfei.setHorizontalHeaderItem(3, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget_xunfei.setHorizontalHeaderItem(4, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget_xunfei.setHorizontalHeaderItem(5, __qtablewidgetitem21)
        self.tableWidget_xunfei.setObjectName(u"tableWidget_xunfei")
        self.tableWidget_xunfei.setGeometry(QRect(20, 20, 961, 231))
        self.tableWidget_xunfei.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_xunfei.verticalHeader().setVisible(False)
        self.tabWidget_2.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.tabWidget_2.addTab(self.tab_5, "")

        self.verticalLayout_5.addWidget(self.tabWidget_2)

        self.tabWidget.addTab(self.tab4Settings, "")

        self.verticalLayout_6.addWidget(self.tabWidget)

        DatasetViewMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(DatasetViewMainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1200, 22))
        DatasetViewMainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(DatasetViewMainWindow)
        self.statusbar.setObjectName(u"statusbar")
        DatasetViewMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(DatasetViewMainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(DatasetViewMainWindow)
    # setupUi

    def retranslateUi(self, DatasetViewMainWindow):
        DatasetViewMainWindow.setWindowTitle(QCoreApplication.translate("DatasetViewMainWindow", u"\u6570\u636e\u96c6", None))
        self.groupBox_operate.setTitle(QCoreApplication.translate("DatasetViewMainWindow", u"\u64cd\u4f5c", None))
        self.pushButton_input.setText(QCoreApplication.translate("DatasetViewMainWindow", u"\u5bfc\u5165", None))
        self.pushButton_search.setText(QCoreApplication.translate("DatasetViewMainWindow", u"\u641c\u7d22", None))
        self.pushButton_output.setText(QCoreApplication.translate("DatasetViewMainWindow", u"\u5bfc\u51fa", None))
        self.pushButton_columns_setting.setText(QCoreApplication.translate("DatasetViewMainWindow", u"\u5217\u8bbe\u7f6e", None))
        self.groupBox_dataset.setTitle(QCoreApplication.translate("DatasetViewMainWindow", u"\u6570\u636e\u96c6", None))
        self.label_page_info.setText(QCoreApplication.translate("DatasetViewMainWindow", u"\u5f53\u524d1\u523015\uff0c\u51711234\u6761\u6570\u636e", None))
        self.label_page_size_1.setText(QCoreApplication.translate("DatasetViewMainWindow", u"\u6bcf\u9875", None))
        self.label_page_size_2.setText(QCoreApplication.translate("DatasetViewMainWindow", u"\u884c", None))
        self.pushButton_page_last.setText(QCoreApplication.translate("DatasetViewMainWindow", u"\u2190", None))
        self.pushButton_page_next.setText(QCoreApplication.translate("DatasetViewMainWindow", u"\u2192", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1NewView), QCoreApplication.translate("DatasetViewMainWindow", u"\u65b0\u6570\u636e\u96c6\u6982\u89c8", None))
        ___qtablewidgetitem = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("DatasetViewMainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem1 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("DatasetViewMainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem2 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("DatasetViewMainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem3 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("DatasetViewMainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("DatasetViewMainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("DatasetViewMainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("DatasetViewMainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("DatasetViewMainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem8 = self.tableWidget.verticalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("DatasetViewMainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem9 = self.tableWidget.verticalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("DatasetViewMainWindow", u"\u65b0\u5efa\u884c", None));
        self.pushButton_add_wav_srt.setText(QCoreApplication.translate("DatasetViewMainWindow", u"\u4ece\u6587\u4ef6\u5bfc\u5165\uff08\u97f3\u9891+\u5b57\u5e55\uff09", None))
        self.pushButton_output_speaker.setText(QCoreApplication.translate("DatasetViewMainWindow", u"\u5bfc\u51fa\u6570\u636e\u96c6\uff08\u5355\u53d1\u97f3\u4eba\uff09", None))
        self.pushButton_add_long_wav.setText(QCoreApplication.translate("DatasetViewMainWindow", u"\u4ece\u6587\u4ef6\u5bfc\u5165\uff08\u957f\u97f3\u9891\uff09", None))
        self.pushButton_del_by_raw_wav.setText(QCoreApplication.translate("DatasetViewMainWindow", u"\u6839\u636e\u6e90\u97f3\u9891\u5220\u9664\u6570\u636e", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1View), QCoreApplication.translate("DatasetViewMainWindow", u"\u6570\u636e\u96c6\u6982\u89c8", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("DatasetViewMainWindow", u"\u6570\u636e\u5c55\u793a", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2SearchOutput), QCoreApplication.translate("DatasetViewMainWindow", u"\u7b5b\u9009\u548c\u5bfc\u51fa", None))
        self.pushButton_biaobei_pingce.setText(QCoreApplication.translate("DatasetViewMainWindow", u"\u6807\u8d1d\u8bed\u97f3\u8bc4\u6d4b", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab3DataProcessing), QCoreApplication.translate("DatasetViewMainWindow", u"\u6570\u636e\u5904\u7406", None))
        self.label.setText(QCoreApplication.translate("DatasetViewMainWindow", u"\u6ce8\u610f\uff1a\u672c\u9875\u8bbe\u7f6e\u5728\u672c\u5de5\u4f5c\u533a\u4e0b\u901a\u7528", None))
        self.groupBox.setTitle(QCoreApplication.translate("DatasetViewMainWindow", u"\u6807\u8d1d", None))
        ___qtablewidgetitem10 = self.tableWidget_biaobei.horizontalHeaderItem(0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("DatasetViewMainWindow", u"id", None));
        ___qtablewidgetitem11 = self.tableWidget_biaobei.horizontalHeaderItem(1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("DatasetViewMainWindow", u"\u540d\u79f0", None));
        ___qtablewidgetitem12 = self.tableWidget_biaobei.horizontalHeaderItem(2)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("DatasetViewMainWindow", u"APP\u7c7b\u578b", None));
        ___qtablewidgetitem13 = self.tableWidget_biaobei.horizontalHeaderItem(3)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("DatasetViewMainWindow", u"APPID", None));
        ___qtablewidgetitem14 = self.tableWidget_biaobei.horizontalHeaderItem(4)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("DatasetViewMainWindow", u"APISecret\uff08client_secret\uff09", None));
        ___qtablewidgetitem15 = self.tableWidget_biaobei.horizontalHeaderItem(5)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("DatasetViewMainWindow", u"APIKey\uff08client_id\uff09", None));
        self.pushButton_add_biaobei.setText(QCoreApplication.translate("DatasetViewMainWindow", u"\u6dfb\u52a0", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("DatasetViewMainWindow", u"\u8baf\u98de", None))
        self.pushButton_add_xunfei.setText(QCoreApplication.translate("DatasetViewMainWindow", u"\u6dfb\u52a0", None))
        ___qtablewidgetitem16 = self.tableWidget_xunfei.horizontalHeaderItem(0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("DatasetViewMainWindow", u"id", None));
        ___qtablewidgetitem17 = self.tableWidget_xunfei.horizontalHeaderItem(1)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("DatasetViewMainWindow", u"\u540d\u79f0", None));
        ___qtablewidgetitem18 = self.tableWidget_xunfei.horizontalHeaderItem(2)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("DatasetViewMainWindow", u"APP\u7c7b\u578b", None));
        ___qtablewidgetitem19 = self.tableWidget_xunfei.horizontalHeaderItem(3)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("DatasetViewMainWindow", u"APPID", None));
        ___qtablewidgetitem20 = self.tableWidget_xunfei.horizontalHeaderItem(4)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("DatasetViewMainWindow", u"APISecret\uff08client_secret\uff09", None));
        ___qtablewidgetitem21 = self.tableWidget_xunfei.horizontalHeaderItem(5)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("DatasetViewMainWindow", u"APIKey\uff08client_id\uff09", None));
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), QCoreApplication.translate("DatasetViewMainWindow", u"\u6388\u6743\u7ba1\u7406", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), QCoreApplication.translate("DatasetViewMainWindow", u"\u5168\u5c40\u8bbe\u7f6e", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab4Settings), QCoreApplication.translate("DatasetViewMainWindow", u"\u8f6f\u4ef6\u8bbe\u7f6e", None))
    # retranslateUi

