# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'final.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QSplitter, QStackedWidget, QTabWidget,
    QTableWidget, QTableWidgetItem, QTextEdit, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.ApplicationModal)
        MainWindow.resize(812, 439)
        MainWindow.setTabShape(QTabWidget.Rounded)
        MainWindow.setDockNestingEnabled(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.mainMenu = QStackedWidget(self.centralwidget)
        self.mainMenu.setObjectName(u"mainMenu")
        font = QFont()
        font.setPointSize(8)
        self.mainMenu.setFont(font)
        self.mainMenu.setFrameShape(QFrame.NoFrame)
        self.mainMenu.setFrameShadow(QFrame.Plain)
        self.Connection = QWidget()
        self.Connection.setObjectName(u"Connection")
        self.gridLayout = QGridLayout(self.Connection)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox_2 = QGroupBox(self.Connection)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setStyleSheet(u"border-radius:10px;\n"
"background-color:rgb(31,149,239);\n"
"color:white;\n"
"QGroupBox {\n"
"\n"
"}")
        self.CAN1_tick = QCheckBox(self.groupBox_2)
        self.CAN1_tick.setObjectName(u"CAN1_tick")
        self.CAN1_tick.setGeometry(QRect(30, 0, 161, 20))
        font1 = QFont()
        font1.setPointSize(10)
        self.CAN1_tick.setFont(font1)
        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(50, 90, 51, 20))
        self.label_6.setFont(font1)
        self.Speed_1 = QComboBox(self.groupBox_2)
        self.Speed_1.addItem("")
        self.Speed_1.addItem("")
        self.Speed_1.addItem("")
        self.Speed_1.setObjectName(u"Speed_1")
        self.Speed_1.setGeometry(QRect(100, 90, 69, 22))

        self.gridLayout.addWidget(self.groupBox_2, 0, 0, 1, 1)

        self.groupBox_3 = QGroupBox(self.Connection)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setStyleSheet(u"border-radius:10px;\n"
"background-color:rgb(31,149,239);\n"
"color:white;\n"
"QGroupBox {\n"
"\n"
"}")
        self.CAN2_tick = QCheckBox(self.groupBox_3)
        self.CAN2_tick.setObjectName(u"CAN2_tick")
        self.CAN2_tick.setGeometry(QRect(30, 0, 171, 20))
        self.CAN2_tick.setFont(font1)
        self.label_5 = QLabel(self.groupBox_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(50, 90, 55, 21))
        self.label_5.setFont(font1)
        self.Speed_2 = QComboBox(self.groupBox_3)
        self.Speed_2.addItem("")
        self.Speed_2.addItem("")
        self.Speed_2.addItem("")
        self.Speed_2.setObjectName(u"Speed_2")
        self.Speed_2.setGeometry(QRect(90, 90, 69, 22))

        self.gridLayout.addWidget(self.groupBox_3, 0, 1, 1, 1)

        self.groupBox_5 = QGroupBox(self.Connection)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setStyleSheet(u"border-radius:10px;\n"
"background-color:rgb(31,149,239);\n"
"color:white;\n"
"QGroupBox {\n"
"\n"
"}")
        self.CAN3_tick = QCheckBox(self.groupBox_5)
        self.CAN3_tick.setObjectName(u"CAN3_tick")
        self.CAN3_tick.setGeometry(QRect(30, 0, 171, 20))
        self.CAN3_tick.setFont(font1)
        self.label_7 = QLabel(self.groupBox_5)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(50, 90, 55, 21))
        self.label_7.setFont(font1)
        self.Speed_3 = QComboBox(self.groupBox_5)
        self.Speed_3.addItem("")
        self.Speed_3.addItem("")
        self.Speed_3.addItem("")
        self.Speed_3.setObjectName(u"Speed_3")
        self.Speed_3.setGeometry(QRect(100, 90, 69, 22))

        self.gridLayout.addWidget(self.groupBox_5, 0, 2, 1, 1)

        self.groupBox_7 = QGroupBox(self.Connection)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setStyleSheet(u"border-radius:10px;\n"
"background-color:rgb(31,149,239);\n"
"color:white;\n"
"QGroupBox {\n"
"\n"
"}")
        self.CAN4_tick = QCheckBox(self.groupBox_7)
        self.CAN4_tick.setObjectName(u"CAN4_tick")
        self.CAN4_tick.setGeometry(QRect(30, 0, 161, 20))
        self.CAN4_tick.setFont(font1)
        self.label_8 = QLabel(self.groupBox_7)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(50, 90, 55, 21))
        self.label_8.setFont(font1)
        self.Speed_4 = QComboBox(self.groupBox_7)
        self.Speed_4.addItem("")
        self.Speed_4.addItem("")
        self.Speed_4.addItem("")
        self.Speed_4.setObjectName(u"Speed_4")
        self.Speed_4.setGeometry(QRect(90, 90, 69, 22))

        self.gridLayout.addWidget(self.groupBox_7, 1, 0, 1, 1)

        self.groupBox_9 = QGroupBox(self.Connection)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.groupBox_9.setStyleSheet(u"border-radius:10px;\n"
"background-color:rgb(31,149,239);\n"
"color:white;\n"
"QGroupBox {\n"
"\n"
"}")
        self.CAN5_tick = QCheckBox(self.groupBox_9)
        self.CAN5_tick.setObjectName(u"CAN5_tick")
        self.CAN5_tick.setGeometry(QRect(30, 0, 161, 20))
        self.CAN5_tick.setFont(font1)
        self.label_19 = QLabel(self.groupBox_9)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(50, 90, 55, 21))
        self.label_19.setFont(font1)
        self.Speed_5 = QComboBox(self.groupBox_9)
        self.Speed_5.addItem("")
        self.Speed_5.addItem("")
        self.Speed_5.addItem("")
        self.Speed_5.setObjectName(u"Speed_5")
        self.Speed_5.setGeometry(QRect(90, 90, 69, 22))

        self.gridLayout.addWidget(self.groupBox_9, 1, 1, 1, 1)

        self.groupBox_11 = QGroupBox(self.Connection)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.groupBox_11.setStyleSheet(u"border-radius:10px;\n"
"background-color:rgb(31,149,239);\n"
"color:white;\n"
"QGroupBox {\n"
"\n"
"}")
        self.OBD = QCheckBox(self.groupBox_11)
        self.OBD.setObjectName(u"OBD")
        self.OBD.setGeometry(QRect(70, 0, 81, 20))
        self.OBD.setFont(font1)

        self.gridLayout.addWidget(self.groupBox_11, 1, 2, 1, 1)

        self.mainMenu.addWidget(self.Connection)
        self.Overview = QWidget()
        self.Overview.setObjectName(u"Overview")
        self.gridLayout_3 = QGridLayout(self.Overview)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_18 = QLabel(self.Overview)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_3.addWidget(self.label_18, 0, 0, 1, 1)

        self.textEdit_2 = QTextEdit(self.Overview)
        self.textEdit_2.setObjectName(u"textEdit_2")

        self.gridLayout_3.addWidget(self.textEdit_2, 1, 0, 1, 4)

        self.label_17 = QLabel(self.Overview)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_3.addWidget(self.label_17, 2, 0, 1, 1)

        self.textEdit = QTextEdit(self.Overview)
        self.textEdit.setObjectName(u"textEdit")

        self.gridLayout_3.addWidget(self.textEdit, 3, 0, 1, 4)

        self.checkBox = QCheckBox(self.Overview)
        self.checkBox.setObjectName(u"checkBox")

        self.gridLayout_3.addWidget(self.checkBox, 4, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(200, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 4, 1, 1, 1)

        self.label_20 = QLabel(self.Overview)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_3.addWidget(self.label_20, 4, 2, 1, 1)

        self.textEdit_3 = QTextEdit(self.Overview)
        self.textEdit_3.setObjectName(u"textEdit_3")

        self.gridLayout_3.addWidget(self.textEdit_3, 4, 3, 1, 1)

        self.mainMenu.addWidget(self.Overview)
        self.CAN = QWidget()
        self.CAN.setObjectName(u"CAN")
        self.verticalLayout_2 = QVBoxLayout(self.CAN)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tableWidget = QTableWidget(self.CAN)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.tableWidget.rowCount() < 11):
            self.tableWidget.setRowCount(11)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setItem(1, 0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setItem(1, 1, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setItem(1, 3, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget.setItem(2, 0, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget.setItem(2, 1, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget.setItem(2, 3, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget.setItem(3, 0, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget.setItem(3, 1, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget.setItem(3, 3, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget.setItem(4, 0, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget.setItem(4, 1, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableWidget.setItem(4, 3, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tableWidget.setItem(5, 0, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tableWidget.setItem(5, 1, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tableWidget.setItem(5, 3, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tableWidget.setItem(6, 0, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tableWidget.setItem(6, 1, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tableWidget.setItem(6, 3, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tableWidget.setItem(7, 0, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tableWidget.setItem(7, 1, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tableWidget.setItem(7, 3, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.tableWidget.setItem(8, 0, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.tableWidget.setItem(8, 1, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.tableWidget.setItem(8, 3, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.tableWidget.setItem(9, 0, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.tableWidget.setItem(9, 1, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.tableWidget.setItem(9, 3, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.tableWidget.setItem(10, 0, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.tableWidget.setItem(10, 1, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.tableWidget.setItem(10, 3, __qtablewidgetitem44)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout_2.addWidget(self.tableWidget)

        self.comboBox = QComboBox(self.CAN)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.verticalLayout_2.addWidget(self.comboBox)

        self.mainMenu.addWidget(self.CAN)
        self.Diag = QWidget()
        self.Diag.setObjectName(u"Diag")
        self.horizontalLayout_6 = QHBoxLayout(self.Diag)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.tableWidget_2 = QTableWidget(self.Diag)
        if (self.tableWidget_2.columnCount() < 2):
            self.tableWidget_2.setColumnCount(2)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem46)
        if (self.tableWidget_2.rowCount() < 7):
            self.tableWidget_2.setRowCount(7)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(2, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(3, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(4, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(5, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(6, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        self.tableWidget_2.setItem(0, 0, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        self.tableWidget_2.setItem(0, 1, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        self.tableWidget_2.setItem(1, 0, __qtablewidgetitem56)
        __qtablewidgetitem57 = QTableWidgetItem()
        self.tableWidget_2.setItem(1, 1, __qtablewidgetitem57)
        __qtablewidgetitem58 = QTableWidgetItem()
        self.tableWidget_2.setItem(2, 0, __qtablewidgetitem58)
        __qtablewidgetitem59 = QTableWidgetItem()
        self.tableWidget_2.setItem(2, 1, __qtablewidgetitem59)
        __qtablewidgetitem60 = QTableWidgetItem()
        self.tableWidget_2.setItem(3, 0, __qtablewidgetitem60)
        __qtablewidgetitem61 = QTableWidgetItem()
        self.tableWidget_2.setItem(3, 1, __qtablewidgetitem61)
        __qtablewidgetitem62 = QTableWidgetItem()
        self.tableWidget_2.setItem(4, 0, __qtablewidgetitem62)
        __qtablewidgetitem63 = QTableWidgetItem()
        self.tableWidget_2.setItem(4, 1, __qtablewidgetitem63)
        __qtablewidgetitem64 = QTableWidgetItem()
        self.tableWidget_2.setItem(5, 0, __qtablewidgetitem64)
        __qtablewidgetitem65 = QTableWidgetItem()
        self.tableWidget_2.setItem(5, 1, __qtablewidgetitem65)
        __qtablewidgetitem66 = QTableWidgetItem()
        self.tableWidget_2.setItem(6, 0, __qtablewidgetitem66)
        __qtablewidgetitem67 = QTableWidgetItem()
        self.tableWidget_2.setItem(6, 1, __qtablewidgetitem67)
        self.tableWidget_2.setObjectName(u"tableWidget_2")

        self.horizontalLayout_6.addWidget(self.tableWidget_2)

        self.mainMenu.addWidget(self.Diag)
        self.Setting = QWidget()
        self.Setting.setObjectName(u"Setting")
        self.gridLayout_6 = QGridLayout(self.Setting)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.tableWidget_3 = QTableWidget(self.Setting)
        if (self.tableWidget_3.columnCount() < 5):
            self.tableWidget_3.setColumnCount(5)
        __qtablewidgetitem68 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, __qtablewidgetitem68)
        __qtablewidgetitem69 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, __qtablewidgetitem69)
        __qtablewidgetitem70 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, __qtablewidgetitem70)
        __qtablewidgetitem71 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(3, __qtablewidgetitem71)
        __qtablewidgetitem72 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(4, __qtablewidgetitem72)
        if (self.tableWidget_3.rowCount() < 5):
            self.tableWidget_3.setRowCount(5)
        __qtablewidgetitem73 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(0, __qtablewidgetitem73)
        __qtablewidgetitem74 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(1, __qtablewidgetitem74)
        __qtablewidgetitem75 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(2, __qtablewidgetitem75)
        __qtablewidgetitem76 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(3, __qtablewidgetitem76)
        __qtablewidgetitem77 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(4, __qtablewidgetitem77)
        __qtablewidgetitem78 = QTableWidgetItem()
        self.tableWidget_3.setItem(0, 0, __qtablewidgetitem78)
        self.tableWidget_3.setObjectName(u"tableWidget_3")

        self.gridLayout_6.addWidget(self.tableWidget_3, 0, 0, 1, 1)

        self.mainMenu.addWidget(self.Setting)

        self.gridLayout_2.addWidget(self.mainMenu, 0, 2, 2, 3)

        self.onlyicon = QWidget(self.centralwidget)
        self.onlyicon.setObjectName(u"onlyicon")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.onlyicon.sizePolicy().hasHeightForWidth())
        self.onlyicon.setSizePolicy(sizePolicy)
        self.onlyicon.setMinimumSize(QSize(55, 0))
        self.onlyicon.setMaximumSize(QSize(100, 16777215))
        self.onlyicon.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.onlyicon.setStyleSheet(u"QWidget{\n"
"	background-color:rgb(31,149,239);\n"
"}\n"
"QPushButton {\n"
"	color: white;\n"
"	text-align:middle;\n"
"	height: 30px;\n"
"	border:none;\n"
"	border-top-left-radius:10px;\n"
"	border-bottom-left-radius:10px;\n"
"	border-top-right-radius:10px;\n"
"	border-bottom-right-radius:10px;\n"
"}\n"
"QLabel {\n"
"	color:white;\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: #F5FAFE;\n"
"	color:#1F95EF;\n"
"	font-weight:bold;\n"
"}")
        self.gridLayout_4 = QGridLayout(self.onlyicon)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(5, -1, 5, -1)
        self.label = QLabel(self.onlyicon)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(15)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.connectbut_1 = QPushButton(self.onlyicon)
        self.connectbut_1.setObjectName(u"connectbut_1")
        icon = QIcon()
        icon.addFile(u":/images/Connection_white.png", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/images/Connection.png", QSize(), QIcon.Normal, QIcon.On)
        self.connectbut_1.setIcon(icon)
        self.connectbut_1.setCheckable(True)
        self.connectbut_1.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.connectbut_1)

        self.sendbut_1 = QPushButton(self.onlyicon)
        self.sendbut_1.setObjectName(u"sendbut_1")
        icon1 = QIcon()
        icon1.addFile(u":/images/send_white.png", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u":/images/send.png", QSize(), QIcon.Normal, QIcon.On)
        self.sendbut_1.setIcon(icon1)
        self.sendbut_1.setCheckable(True)
        self.sendbut_1.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.sendbut_1)

        self.snifferbut_1 = QPushButton(self.onlyicon)
        self.snifferbut_1.setObjectName(u"snifferbut_1")
        self.snifferbut_1.setStyleSheet(u"font-weight:bold;")
        icon2 = QIcon()
        icon2.addFile(u":/images/CAN_white.png", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u":/images/CAN.png", QSize(), QIcon.Normal, QIcon.On)
        self.snifferbut_1.setIcon(icon2)
        self.snifferbut_1.setIconSize(QSize(24, 24))
        self.snifferbut_1.setCheckable(True)
        self.snifferbut_1.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.snifferbut_1)

        self.diagbut_1 = QPushButton(self.onlyicon)
        self.diagbut_1.setObjectName(u"diagbut_1")
        icon3 = QIcon()
        icon3.addFile(u":/images/diag_white.png", QSize(), QIcon.Normal, QIcon.Off)
        icon3.addFile(u":/images/diag.png", QSize(), QIcon.Normal, QIcon.On)
        icon3.addFile(u":/images/diag.png", QSize(), QIcon.Disabled, QIcon.Off)
        self.diagbut_1.setIcon(icon3)
        self.diagbut_1.setIconSize(QSize(18, 18))
        self.diagbut_1.setCheckable(True)
        self.diagbut_1.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.diagbut_1)

        self.settingbut_1 = QPushButton(self.onlyicon)
        self.settingbut_1.setObjectName(u"settingbut_1")
        icon4 = QIcon()
        icon4.addFile(u":/images/settings_white.png", QSize(), QIcon.Normal, QIcon.Off)
        icon4.addFile(u":/images/settings.png", QSize(), QIcon.Normal, QIcon.On)
        self.settingbut_1.setIcon(icon4)
        self.settingbut_1.setCheckable(True)
        self.settingbut_1.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.settingbut_1)


        self.gridLayout_4.addLayout(self.verticalLayout_4, 1, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(19, 234, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_3, 2, 0, 1, 1)

        self.pushButton_9 = QPushButton(self.onlyicon)
        self.pushButton_9.setObjectName(u"pushButton_9")
        icon5 = QIcon()
        icon5.addFile(u":/images/log_out_white.png", QSize(), QIcon.Normal, QIcon.Off)
        icon5.addFile(u":/images/log_out.png", QSize(), QIcon.Normal, QIcon.On)
        self.pushButton_9.setIcon(icon5)
        self.pushButton_9.setCheckable(True)
        self.pushButton_9.setAutoExclusive(True)

        self.gridLayout_4.addWidget(self.pushButton_9, 3, 0, 1, 1)


        self.gridLayout_2.addWidget(self.onlyicon, 0, 0, 3, 1)

        self.pushButton_16 = QPushButton(self.centralwidget)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setStyleSheet(u"QPushButton{\n"
"    font-family: \"Segoe UI\";\n"
"    font-size: 8pt;\n"
"    border: 1px solid;\n"
"    border-color: rgb(31,149,239);\n"
"    border-radius: 3px; \n"
"    background-color: rgb(31,149,239);\n"
"    color: white;\n"
"    font: bold;\n"
"\n"
"	margin: 1px;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 1px solid;\n"
"    border-radius: 3px;\n"
"    border-color: rgb(33, 77, 115);\n"
"}\n"
"QPushButton:focus {\n"
"    outline-color: transparent;\n"
"    border: 2px solid;\n"
"    border-color: rgb(151, 195, 243);\n"
"	margin: 0px;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(52, 113, 173);\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/images/menu_white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_16.setIcon(icon6)
        self.pushButton_16.setIconSize(QSize(24, 24))
        self.pushButton_16.setCheckable(True)
        self.pushButton_16.setAutoExclusive(True)

        self.gridLayout_2.addWidget(self.pushButton_16, 2, 2, 1, 1)

        self.StatusBar = QStackedWidget(self.centralwidget)
        self.StatusBar.setObjectName(u"StatusBar")
        sizePolicy.setHeightForWidth(self.StatusBar.sizePolicy().hasHeightForWidth())
        self.StatusBar.setSizePolicy(sizePolicy)
        self.StatusBar.setMaximumSize(QSize(16777215, 60))
        self.StatusBar.setStyleSheet(u"border:none;")
        self.Overview_2 = QWidget()
        self.Overview_2.setObjectName(u"Overview_2")
        self.horizontalLayout_21 = QHBoxLayout(self.Overview_2)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalSpacer_16 = QSpacerItem(44, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_16)

        self.Stream_2 = QPushButton(self.Overview_2)
        self.Stream_2.setObjectName(u"Stream_2")
        self.Stream_2.setStyleSheet(u"QPushButton{\n"
"    font-family: \"Segoe UI\";\n"
"    font-size: 8pt;\n"
"    border: 1px solid;\n"
"    border-color: rgb(31,149,239);\n"
"    border-radius: 3px; \n"
"    padding-right: 10px; \n"
"    padding-left: 10px;\n"
"    padding-top: 5px;\n"
"    padding-bottom: 5px;\n"
"    background-color: rgb(31,149,239);\n"
"    color: white;\n"
"    font: bold;\n"
"    width: 64px;\n"
"	margin: 1px;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 1px solid;\n"
"    border-radius: 3px;\n"
"    border-color: rgb(33, 77, 115);\n"
"}\n"
"QPushButton:focus {\n"
"    outline-color: transparent;\n"
"    border: 2px solid;\n"
"    border-color: rgb(151, 195, 243);\n"
"	margin: 0px;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(52, 113, 173);\n"
"}")

        self.horizontalLayout_21.addWidget(self.Stream_2)

        self.Setting_CAN_2 = QPushButton(self.Overview_2)
        self.Setting_CAN_2.setObjectName(u"Setting_CAN_2")
        self.Setting_CAN_2.setStyleSheet(u"QPushButton{\n"
"    font-family: \"Segoe UI\";\n"
"    font-size: 8pt;\n"
"    border: 1px solid;\n"
"    border-color: rgb(31,149,239);\n"
"    border-radius: 3px; \n"
"    padding-right: 10px; \n"
"    padding-left: 10px;\n"
"    padding-top: 5px;\n"
"    padding-bottom: 5px;\n"
"    background-color: rgb(31,149,239);\n"
"    color: white;\n"
"    font: bold;\n"
"    width: 64px;\n"
"	margin: 1px;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 1px solid;\n"
"    border-radius: 3px;\n"
"    border-color: rgb(33, 77, 115);\n"
"}\n"
"QPushButton:focus {\n"
"    outline-color: transparent;\n"
"    border: 2px solid;\n"
"    border-color: rgb(151, 195, 243);\n"
"	margin: 0px;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(52, 113, 173);\n"
"}")

        self.horizontalLayout_21.addWidget(self.Setting_CAN_2)

        self.horizontalSpacer_15 = QSpacerItem(98, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_15)

        self.splitter_5 = QSplitter(self.Overview_2)
        self.splitter_5.setObjectName(u"splitter_5")
        self.splitter_5.setAutoFillBackground(False)
        self.splitter_5.setStyleSheet(u"QWidget{\n"
"border: 1px solid;\n"
"}")
        self.splitter_5.setFrameShape(QFrame.NoFrame)
        self.splitter_5.setLineWidth(10)
        self.splitter_5.setOrientation(Qt.Vertical)
        self.layoutWidget_9 = QWidget(self.splitter_5)
        self.layoutWidget_9.setObjectName(u"layoutWidget_9")
        self.horizontalLayout_19 = QHBoxLayout(self.layoutWidget_9)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.label_15 = QLabel(self.layoutWidget_9)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_19.addWidget(self.label_15)

        self.status_connect_4 = QPushButton(self.layoutWidget_9)
        self.status_connect_4.setObjectName(u"status_connect_4")
        icon7 = QIcon()
        icon7.addFile(u":/images/yellow_status.png", QSize(), QIcon.Normal, QIcon.Off)
        icon7.addFile(u":/images/green_status.png", QSize(), QIcon.Normal, QIcon.On)
        self.status_connect_4.setIcon(icon7)
        self.status_connect_4.setIconSize(QSize(12, 12))

        self.horizontalLayout_19.addWidget(self.status_connect_4)

        self.splitter_5.addWidget(self.layoutWidget_9)
        self.layoutWidget_10 = QWidget(self.splitter_5)
        self.layoutWidget_10.setObjectName(u"layoutWidget_10")
        self.horizontalLayout_20 = QHBoxLayout(self.layoutWidget_10)
        self.horizontalLayout_20.setSpacing(6)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.label_16 = QLabel(self.layoutWidget_10)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_20.addWidget(self.label_16)

        self.battery_percent_7 = QLabel(self.layoutWidget_10)
        self.battery_percent_7.setObjectName(u"battery_percent_7")

        self.horizontalLayout_20.addWidget(self.battery_percent_7)

        self.splitter_5.addWidget(self.layoutWidget_10)

        self.horizontalLayout_21.addWidget(self.splitter_5)

        self.horizontalSpacer_17 = QSpacerItem(24, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_17)

        self.StatusBar.addWidget(self.Overview_2)
        self.CAN_2 = QWidget()
        self.CAN_2.setObjectName(u"CAN_2")
        self.horizontalLayout_18 = QHBoxLayout(self.CAN_2)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalSpacer_13 = QSpacerItem(44, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_13)

        self.Stream = QPushButton(self.CAN_2)
        self.Stream.setObjectName(u"Stream")
        self.Stream.setStyleSheet(u"QPushButton{\n"
"    font-family: \"Segoe UI\";\n"
"    font-size: 8pt;\n"
"    border: 1px solid;\n"
"    border-color: rgb(31,149,239);\n"
"    border-radius: 3px; \n"
"    padding-right: 10px; \n"
"    padding-left: 10px;\n"
"    padding-top: 5px;\n"
"    padding-bottom: 5px;\n"
"    background-color: rgb(31,149,239);\n"
"    color: white;\n"
"    font: bold;\n"
"    width: 64px;\n"
"	margin: 1px;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 1px solid;\n"
"    border-radius: 3px;\n"
"    border-color: rgb(33, 77, 115);\n"
"}\n"
"QPushButton:focus {\n"
"    outline-color: transparent;\n"
"    border: 2px solid;\n"
"    border-color: rgb(151, 195, 243);\n"
"	margin: 0px;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(52, 113, 173);\n"
"}")

        self.horizontalLayout_18.addWidget(self.Stream)

        self.Pause = QPushButton(self.CAN_2)
        self.Pause.setObjectName(u"Pause")
        self.Pause.setStyleSheet(u"QPushButton{\n"
"    font-family: \"Segoe UI\";\n"
"    font-size: 8pt;\n"
"    border: 1px solid;\n"
"    border-color: rgb(31,149,239);\n"
"    border-radius: 3px; \n"
"    padding-right: 10px; \n"
"    padding-left: 10px;\n"
"    padding-top: 5px;\n"
"    padding-bottom: 5px;\n"
"    background-color: rgb(31,149,239);\n"
"    color: white;\n"
"    font: bold;\n"
"    width: 64px;\n"
"	margin: 1px;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 1px solid;\n"
"    border-radius: 3px;\n"
"    border-color: rgb(33, 77, 115);\n"
"}\n"
"QPushButton:focus {\n"
"    outline-color: transparent;\n"
"    border: 2px solid;\n"
"    border-color: rgb(151, 195, 243);\n"
"	margin: 0px;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(52, 113, 173);\n"
"}")

        self.horizontalLayout_18.addWidget(self.Pause)

        self.Save_to_CSV = QPushButton(self.CAN_2)
        self.Save_to_CSV.setObjectName(u"Save_to_CSV")
        self.Save_to_CSV.setStyleSheet(u"QPushButton{\n"
"    font-family: \"Segoe UI\";\n"
"    font-size: 8pt;\n"
"    border: 1px solid;\n"
"    border-color: rgb(31,149,239);\n"
"    border-radius: 3px; \n"
"    padding-right: 10px; \n"
"    padding-left: 10px;\n"
"    padding-top: 5px;\n"
"    padding-bottom: 5px;\n"
"    background-color: rgb(31,149,239);\n"
"    color: white;\n"
"    font: bold;\n"
"    width: 64px;\n"
"	margin: 1px;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 1px solid;\n"
"    border-radius: 3px;\n"
"    border-color: rgb(33, 77, 115);\n"
"}\n"
"QPushButton:focus {\n"
"    outline-color: transparent;\n"
"    border: 2px solid;\n"
"    border-color: rgb(151, 195, 243);\n"
"	margin: 0px;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(52, 113, 173);\n"
"}")

        self.horizontalLayout_18.addWidget(self.Save_to_CSV)

        self.Stop_Save = QPushButton(self.CAN_2)
        self.Stop_Save.setObjectName(u"Stop_Save")
        self.Stop_Save.setStyleSheet(u"QPushButton{\n"
"    font-family: \"Segoe UI\";\n"
"    font-size: 8pt;\n"
"    border: 1px solid;\n"
"    border-color: rgb(31,149,239);\n"
"    border-radius: 3px; \n"
"    padding-right: 10px; \n"
"    padding-left: 10px;\n"
"    padding-top: 5px;\n"
"    padding-bottom: 5px;\n"
"    background-color: rgb(31,149,239);\n"
"    color: white;\n"
"    font: bold;\n"
"    width: 64px;\n"
"	margin: 1px;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 1px solid;\n"
"    border-radius: 3px;\n"
"    border-color: rgb(33, 77, 115);\n"
"}\n"
"QPushButton:focus {\n"
"    outline-color: transparent;\n"
"    border: 2px solid;\n"
"    border-color: rgb(151, 195, 243);\n"
"	margin: 0px;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(52, 113, 173);\n"
"}")

        self.horizontalLayout_18.addWidget(self.Stop_Save)

        self.horizontalSpacer_12 = QSpacerItem(98, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_12)

        self.splitter_4 = QSplitter(self.CAN_2)
        self.splitter_4.setObjectName(u"splitter_4")
        self.splitter_4.setAutoFillBackground(False)
        self.splitter_4.setStyleSheet(u"QWidget{\n"
"border: 1px solid;\n"
"}")
        self.splitter_4.setFrameShape(QFrame.NoFrame)
        self.splitter_4.setLineWidth(10)
        self.splitter_4.setOrientation(Qt.Vertical)
        self.layoutWidget_7 = QWidget(self.splitter_4)
        self.layoutWidget_7.setObjectName(u"layoutWidget_7")
        self.horizontalLayout_16 = QHBoxLayout(self.layoutWidget_7)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.layoutWidget_7)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_16.addWidget(self.label_13)

        self.status_connect_3 = QPushButton(self.layoutWidget_7)
        self.status_connect_3.setObjectName(u"status_connect_3")
        self.status_connect_3.setIcon(icon7)
        self.status_connect_3.setIconSize(QSize(12, 12))

        self.horizontalLayout_16.addWidget(self.status_connect_3)

        self.splitter_4.addWidget(self.layoutWidget_7)
        self.layoutWidget_8 = QWidget(self.splitter_4)
        self.layoutWidget_8.setObjectName(u"layoutWidget_8")
        self.horizontalLayout_17 = QHBoxLayout(self.layoutWidget_8)
        self.horizontalLayout_17.setSpacing(6)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.label_14 = QLabel(self.layoutWidget_8)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_17.addWidget(self.label_14)

        self.battery_percent_6 = QLabel(self.layoutWidget_8)
        self.battery_percent_6.setObjectName(u"battery_percent_6")

        self.horizontalLayout_17.addWidget(self.battery_percent_6)

        self.splitter_4.addWidget(self.layoutWidget_8)

        self.horizontalLayout_18.addWidget(self.splitter_4)

        self.horizontalSpacer_14 = QSpacerItem(24, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_14)

        self.StatusBar.addWidget(self.CAN_2)
        self.Diag_2 = QWidget()
        self.Diag_2.setObjectName(u"Diag_2")
        self.horizontalLayout_5 = QHBoxLayout(self.Diag_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_6 = QSpacerItem(336, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_6)

        self.splitter = QSplitter(self.Diag_2)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Vertical)
        self.layoutWidget = QWidget(self.splitter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.pushButton_11 = QPushButton(self.layoutWidget)
        self.pushButton_11.setObjectName(u"pushButton_11")
        icon8 = QIcon()
        icon8.addFile(u":/images/yellow_status.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_11.setIcon(icon8)
        self.pushButton_11.setIconSize(QSize(12, 12))

        self.horizontalLayout_3.addWidget(self.pushButton_11)

        self.splitter.addWidget(self.layoutWidget)
        self.layoutWidget1 = QWidget(self.splitter)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.horizontalLayout_4 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.layoutWidget1)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.battery_percent = QLabel(self.layoutWidget1)
        self.battery_percent.setObjectName(u"battery_percent")

        self.horizontalLayout_4.addWidget(self.battery_percent)

        self.splitter.addWidget(self.layoutWidget1)

        self.horizontalLayout_5.addWidget(self.splitter)

        self.horizontalSpacer_3 = QSpacerItem(24, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.StatusBar.addWidget(self.Diag_2)
        self.Setting_2 = QWidget()
        self.Setting_2.setObjectName(u"Setting_2")
        self.horizontalLayout_13 = QHBoxLayout(self.Setting_2)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_9)

        self.Save_seting = QPushButton(self.Setting_2)
        self.Save_seting.setObjectName(u"Save_seting")
        self.Save_seting.setStyleSheet(u"QPushButton{\n"
"    font-family: \"Segoe UI\";\n"
"    font-size: 8pt;\n"
"    border: 1px solid;\n"
"    border-color: rgb(31,149,239);\n"
"    border-radius: 3px; \n"
"    padding-right: 10px; \n"
"    padding-left: 10px;\n"
"    padding-top: 5px;\n"
"    padding-bottom: 5px;\n"
"    background-color: rgb(31,149,239);\n"
"    color: white;\n"
"    font: bold;\n"
"    width: 64px;\n"
"	margin: 1px;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 1px solid;\n"
"    border-radius: 3px;\n"
"    border-color: rgb(33, 77, 115);\n"
"}\n"
"QPushButton:focus {\n"
"    outline-color: transparent;\n"
"    border: 2px solid;\n"
"    border-color: rgb(151, 195, 243);\n"
"	margin: 0px;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(52, 113, 173);\n"
"}")

        self.horizontalLayout_13.addWidget(self.Save_seting)

        self.horizontalSpacer_10 = QSpacerItem(188, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_10)

        self.splitter_3 = QSplitter(self.Setting_2)
        self.splitter_3.setObjectName(u"splitter_3")
        self.splitter_3.setAutoFillBackground(False)
        self.splitter_3.setStyleSheet(u"QWidget{\n"
"border: 1px solid;\n"
"}")
        self.splitter_3.setFrameShape(QFrame.NoFrame)
        self.splitter_3.setLineWidth(10)
        self.splitter_3.setOrientation(Qt.Vertical)
        self.layoutWidget_3 = QWidget(self.splitter_3)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.horizontalLayout_11 = QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.layoutWidget_3)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_11.addWidget(self.label_9)

        self.status_connect = QPushButton(self.layoutWidget_3)
        self.status_connect.setObjectName(u"status_connect")
        self.status_connect.setIcon(icon7)
        self.status_connect.setIconSize(QSize(12, 12))

        self.horizontalLayout_11.addWidget(self.status_connect)

        self.splitter_3.addWidget(self.layoutWidget_3)
        self.layoutWidget_4 = QWidget(self.splitter_3)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.horizontalLayout_12 = QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout_12.setSpacing(6)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.layoutWidget_4)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_12.addWidget(self.label_10)

        self.battery_percent_4 = QLabel(self.layoutWidget_4)
        self.battery_percent_4.setObjectName(u"battery_percent_4")

        self.horizontalLayout_12.addWidget(self.battery_percent_4)

        self.splitter_3.addWidget(self.layoutWidget_4)

        self.horizontalLayout_13.addWidget(self.splitter_3)

        self.horizontalSpacer_11 = QSpacerItem(24, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_11)

        self.StatusBar.addWidget(self.Setting_2)
        self.Connection_2 = QWidget()
        self.Connection_2.setObjectName(u"Connection_2")
        self.horizontalLayout_2 = QHBoxLayout(self.Connection_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_20 = QSpacerItem(183, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_20)

        self.Connect = QPushButton(self.Connection_2)
        self.Connect.setObjectName(u"Connect")
        self.Connect.setStyleSheet(u"QPushButton{\n"
"    font-family: \"Segoe UI\";\n"
"    font-size: 8pt;\n"
"    border: 1px solid;\n"
"    border-color: rgb(31,149,239);\n"
"    border-radius: 3px; \n"
"    padding-right: 10px; \n"
"    padding-left: 10px;\n"
"    padding-top: 5px;\n"
"    padding-bottom: 5px;\n"
"    background-color: rgb(31,149,239);\n"
"    color: white;\n"
"    font: bold;\n"
"    width: 64px;\n"
"	margin: 1px;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 1px solid;\n"
"    border-radius: 3px;\n"
"    border-color: rgb(33, 77, 115);\n"
"}\n"
"QPushButton:focus {\n"
"    outline-color: transparent;\n"
"    border: 2px solid;\n"
"    border-color: rgb(151, 195, 243);\n"
"	margin: 0px;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(52, 113, 173);\n"
"}")

        self.horizontalLayout_2.addWidget(self.Connect)

        self.Reset = QPushButton(self.Connection_2)
        self.Reset.setObjectName(u"Reset")
        self.Reset.setStyleSheet(u"QPushButton{\n"
"    font-family: \"Segoe UI\";\n"
"    font-size: 8pt;\n"
"    border: 1px solid;\n"
"    border-color: rgb(31,149,239);\n"
"    border-radius: 3px; \n"
"    padding-right: 10px; \n"
"    padding-left: 10px;\n"
"    padding-top: 5px;\n"
"    padding-bottom: 5px;\n"
"    background-color: rgb(31,149,239);\n"
"    color: white;\n"
"    font: bold;\n"
"    width: 64px;\n"
"	margin: 1px;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 1px solid;\n"
"    border-radius: 3px;\n"
"    border-color: rgb(33, 77, 115);\n"
"}\n"
"QPushButton:focus {\n"
"    outline-color: transparent;\n"
"    border: 2px solid;\n"
"    border-color: rgb(151, 195, 243);\n"
"	margin: 0px;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(52, 113, 173);\n"
"}")

        self.horizontalLayout_2.addWidget(self.Reset)

        self.horizontalSpacer_19 = QSpacerItem(144, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_19)

        self.splitter_6 = QSplitter(self.Connection_2)
        self.splitter_6.setObjectName(u"splitter_6")
        self.splitter_6.setAutoFillBackground(False)
        self.splitter_6.setStyleSheet(u"QWidget{\n"
"border: 1px solid;\n"
"}")
        self.splitter_6.setFrameShape(QFrame.NoFrame)
        self.splitter_6.setLineWidth(10)
        self.splitter_6.setOrientation(Qt.Vertical)
        self.layoutWidget_5 = QWidget(self.splitter_6)
        self.layoutWidget_5.setObjectName(u"layoutWidget_5")
        self.horizontalLayout_14 = QHBoxLayout(self.layoutWidget_5)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.layoutWidget_5)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_14.addWidget(self.label_11)

        self.status_connect_2 = QPushButton(self.layoutWidget_5)
        self.status_connect_2.setObjectName(u"status_connect_2")
        icon9 = QIcon()
        icon9.addFile(u":/images/red_status.png", QSize(), QIcon.Normal, QIcon.Off)
        icon9.addFile(u":/images/green_status.png", QSize(), QIcon.Normal, QIcon.On)
        self.status_connect_2.setIcon(icon9)
        self.status_connect_2.setIconSize(QSize(12, 12))

        self.horizontalLayout_14.addWidget(self.status_connect_2)

        self.splitter_6.addWidget(self.layoutWidget_5)
        self.layoutWidget_6 = QWidget(self.splitter_6)
        self.layoutWidget_6.setObjectName(u"layoutWidget_6")
        self.horizontalLayout_15 = QHBoxLayout(self.layoutWidget_6)
        self.horizontalLayout_15.setSpacing(6)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.layoutWidget_6)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_15.addWidget(self.label_12)

        self.battery_percent_5 = QLabel(self.layoutWidget_6)
        self.battery_percent_5.setObjectName(u"battery_percent_5")

        self.horizontalLayout_15.addWidget(self.battery_percent_5)

        self.splitter_6.addWidget(self.layoutWidget_6)

        self.horizontalLayout_2.addWidget(self.splitter_6)

        self.horizontalSpacer_18 = QSpacerItem(24, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_18)

        self.StatusBar.addWidget(self.Connection_2)

        self.gridLayout_2.addWidget(self.StatusBar, 2, 3, 1, 1)

        self.fullmenu = QWidget(self.centralwidget)
        self.fullmenu.setObjectName(u"fullmenu")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.fullmenu.sizePolicy().hasHeightForWidth())
        self.fullmenu.setSizePolicy(sizePolicy1)
        self.fullmenu.setMinimumSize(QSize(150, 0))
        self.fullmenu.setMaximumSize(QSize(130, 16777215))
        self.fullmenu.setBaseSize(QSize(150, 445))
        self.fullmenu.setMouseTracking(False)
        self.fullmenu.setAutoFillBackground(False)
        self.fullmenu.setStyleSheet(u"QWidget{\n"
"	background-color:rgb(31,149,239);\n"
"}\n"
"QPushButton {\n"
"	font-family: \"Segoe UI\";\n"
"	color: white;\n"
"	text-align:left;\n"
"	height: 30px;\n"
"	border:none;\n"
"	border-top-left-radius:10px;\n"
"	border-bottom-left-radius:10px;\n"
"}\n"
"QLabel {\n"
"	color:white;\n"
"	font-family: \"Segoe UI\";\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: #F5FAFE;\n"
"	color:#1F95EF;\n"
"	font-weight:bold;\n"
"}")
        self.gridLayout_5 = QGridLayout(self.fullmenu)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(5, -1, 0, -1)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(15, -1, 15, -1)
        self.horizontalSpacer_4 = QSpacerItem(13, 13, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.label_2 = QLabel(self.fullmenu)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.horizontalSpacer_2 = QSpacerItem(13, 13, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.gridLayout_5.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, -1, 0, -1)
        self.connectbut = QPushButton(self.fullmenu)
        self.connectbut.setObjectName(u"connectbut")
        self.connectbut.setIcon(icon)
        self.connectbut.setCheckable(True)
        self.connectbut.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.connectbut)

        self.sendbut = QPushButton(self.fullmenu)
        self.sendbut.setObjectName(u"sendbut")
        self.sendbut.setIcon(icon1)
        self.sendbut.setCheckable(True)
        self.sendbut.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.sendbut)

        self.snifferbut = QPushButton(self.fullmenu)
        self.snifferbut.setObjectName(u"snifferbut")
        self.snifferbut.setIcon(icon2)
        self.snifferbut.setIconSize(QSize(24, 24))
        self.snifferbut.setCheckable(True)
        self.snifferbut.setAutoRepeat(False)
        self.snifferbut.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.snifferbut)

        self.diagbut = QPushButton(self.fullmenu)
        self.diagbut.setObjectName(u"diagbut")
        icon10 = QIcon()
        icon10.addFile(u":/images/diag_white.png", QSize(), QIcon.Normal, QIcon.Off)
        icon10.addFile(u":/images/diag.png", QSize(), QIcon.Normal, QIcon.On)
        self.diagbut.setIcon(icon10)
        self.diagbut.setIconSize(QSize(18, 18))
        self.diagbut.setCheckable(True)
        self.diagbut.setAutoExclusive(True)
        self.diagbut.setFlat(False)

        self.verticalLayout.addWidget(self.diagbut)

        self.settingbut = QPushButton(self.fullmenu)
        self.settingbut.setObjectName(u"settingbut")
        self.settingbut.setStyleSheet(u"")
        self.settingbut.setIcon(icon4)
        self.settingbut.setCheckable(True)
        self.settingbut.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.settingbut)


        self.gridLayout_5.addLayout(self.verticalLayout, 1, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(19, 143, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_4, 2, 0, 1, 1)

        self.pushButton_10 = QPushButton(self.fullmenu)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setIcon(icon5)
        self.pushButton_10.setCheckable(True)
        self.pushButton_10.setAutoExclusive(True)

        self.gridLayout_5.addWidget(self.pushButton_10, 3, 0, 1, 1)


        self.gridLayout_2.addWidget(self.fullmenu, 0, 1, 3, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton_16.toggled.connect(self.onlyicon.setHidden)
        self.pushButton_16.toggled.connect(self.fullmenu.setVisible)
        self.settingbut_1.toggled.connect(self.settingbut.setChecked)
        self.diagbut_1.toggled.connect(self.diagbut.setChecked)
        self.snifferbut_1.toggled.connect(self.snifferbut.setChecked)
        self.sendbut_1.toggled.connect(self.sendbut.setChecked)
        self.pushButton_9.toggled.connect(self.pushButton_10.setChecked)
        self.settingbut.toggled.connect(self.settingbut_1.setChecked)
        self.diagbut.toggled.connect(self.diagbut_1.setChecked)
        self.snifferbut.toggled.connect(self.snifferbut_1.setChecked)
        self.sendbut.toggled.connect(self.sendbut_1.setChecked)
        self.pushButton_10.toggled.connect(self.pushButton_9.setChecked)
        self.connectbut.toggled.connect(self.connectbut_1.toggle)
        self.pushButton_10.toggled.connect(MainWindow.close)
        self.pushButton_9.toggled.connect(MainWindow.close)

        self.mainMenu.setCurrentIndex(2)
        self.StatusBar.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox_2.setTitle("")
        self.CAN1_tick.setText(QCoreApplication.translate("MainWindow", u"CAN bus channel 1", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Speed", None))
        self.Speed_1.setItemText(0, QCoreApplication.translate("MainWindow", u"500000", None))
        self.Speed_1.setItemText(1, QCoreApplication.translate("MainWindow", u"100000", None))
        self.Speed_1.setItemText(2, QCoreApplication.translate("MainWindow", u"FD", None))

        self.groupBox_3.setTitle("")
        self.CAN2_tick.setText(QCoreApplication.translate("MainWindow", u"CAN bus channel 2", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Speed", None))
        self.Speed_2.setItemText(0, QCoreApplication.translate("MainWindow", u"500000", None))
        self.Speed_2.setItemText(1, QCoreApplication.translate("MainWindow", u"100000", None))
        self.Speed_2.setItemText(2, QCoreApplication.translate("MainWindow", u"FD", None))

        self.groupBox_5.setTitle("")
        self.CAN3_tick.setText(QCoreApplication.translate("MainWindow", u"CAN bus channel 3", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Speed", None))
        self.Speed_3.setItemText(0, QCoreApplication.translate("MainWindow", u"500000", None))
        self.Speed_3.setItemText(1, QCoreApplication.translate("MainWindow", u"100000", None))
        self.Speed_3.setItemText(2, QCoreApplication.translate("MainWindow", u"FD", None))

        self.groupBox_7.setTitle("")
        self.CAN4_tick.setText(QCoreApplication.translate("MainWindow", u"CAN bus channel 4", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Speed", None))
        self.Speed_4.setItemText(0, QCoreApplication.translate("MainWindow", u"500000", None))
        self.Speed_4.setItemText(1, QCoreApplication.translate("MainWindow", u"100000", None))
        self.Speed_4.setItemText(2, QCoreApplication.translate("MainWindow", u"FD", None))

        self.groupBox_9.setTitle("")
        self.CAN5_tick.setText(QCoreApplication.translate("MainWindow", u"CAN bus channel 5", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Speed", None))
        self.Speed_5.setItemText(0, QCoreApplication.translate("MainWindow", u"500000", None))
        self.Speed_5.setItemText(1, QCoreApplication.translate("MainWindow", u"100000", None))
        self.Speed_5.setItemText(2, QCoreApplication.translate("MainWindow", u"FD", None))

        self.groupBox_11.setTitle("")
        self.OBD.setText(QCoreApplication.translate("MainWindow", u"OBD II", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Data", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Loop", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Frequency (s)", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Timestamp", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"DLC", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Data", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem8 = self.tableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem9 = self.tableWidget.verticalHeaderItem(6)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem10 = self.tableWidget.verticalHeaderItem(7)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"7", None));
        ___qtablewidgetitem11 = self.tableWidget.verticalHeaderItem(8)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"8", None));
        ___qtablewidgetitem12 = self.tableWidget.verticalHeaderItem(9)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"9", None));
        ___qtablewidgetitem13 = self.tableWidget.verticalHeaderItem(10)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"10", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"<select channel>", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"All", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"CAN1", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"CAN2", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"CAN3", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"CAN4", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"CAN5", None))

        ___qtablewidgetitem14 = self.tableWidget_2.verticalHeaderItem(0)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem15 = self.tableWidget_2.verticalHeaderItem(1)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem16 = self.tableWidget_2.verticalHeaderItem(2)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem17 = self.tableWidget_2.verticalHeaderItem(3)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem18 = self.tableWidget_2.verticalHeaderItem(4)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem19 = self.tableWidget_2.verticalHeaderItem(5)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem20 = self.tableWidget_2.verticalHeaderItem(6)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"7", None));

        __sortingEnabled1 = self.tableWidget_2.isSortingEnabled()
        self.tableWidget_2.setSortingEnabled(False)
        ___qtablewidgetitem21 = self.tableWidget_2.item(0, 0)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Engine speed (RPM)", None));
        ___qtablewidgetitem22 = self.tableWidget_2.item(1, 0)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Engine load", None));
        ___qtablewidgetitem23 = self.tableWidget_2.item(2, 0)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Coolant temperature ", None));
        ___qtablewidgetitem24 = self.tableWidget_2.item(3, 0)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"Throttle position", None));
        ___qtablewidgetitem25 = self.tableWidget_2.item(4, 0)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"Battery voltage", None));
        ___qtablewidgetitem26 = self.tableWidget_2.item(5, 0)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"Speed", None));
        ___qtablewidgetitem27 = self.tableWidget_2.item(6, 0)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"...", None));
        self.tableWidget_2.setSortingEnabled(__sortingEnabled1)

        ___qtablewidgetitem28 = self.tableWidget_3.horizontalHeaderItem(0)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"CAN1", None));
        ___qtablewidgetitem29 = self.tableWidget_3.horizontalHeaderItem(1)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"CAN2", None));
        ___qtablewidgetitem30 = self.tableWidget_3.horizontalHeaderItem(2)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"CAN3", None));
        ___qtablewidgetitem31 = self.tableWidget_3.horizontalHeaderItem(3)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"CAN4", None));
        ___qtablewidgetitem32 = self.tableWidget_3.horizontalHeaderItem(4)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"C\u1ea0N5", None));
        ___qtablewidgetitem33 = self.tableWidget_3.verticalHeaderItem(0)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem34 = self.tableWidget_3.verticalHeaderItem(1)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"Size", None));
        ___qtablewidgetitem35 = self.tableWidget_3.verticalHeaderItem(2)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"Path", None));
        ___qtablewidgetitem36 = self.tableWidget_3.verticalHeaderItem(3)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"Last update", None));
        ___qtablewidgetitem37 = self.tableWidget_3.verticalHeaderItem(4)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"Status", None));

        __sortingEnabled2 = self.tableWidget_3.isSortingEnabled()
        self.tableWidget_3.setSortingEnabled(False)
        self.tableWidget_3.setSortingEnabled(__sortingEnabled2)

        self.label.setText(QCoreApplication.translate("MainWindow", u"BK-AUTO", None))
        self.connectbut_1.setText("")
        self.sendbut_1.setText("")
        self.snifferbut_1.setText("")
        self.diagbut_1.setText("")
        self.settingbut_1.setText("")
        self.pushButton_9.setText("")
        self.pushButton_16.setText("")
        self.Stream_2.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.Setting_CAN_2.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Connection status:", None))
        self.status_connect_4.setText("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"HW battery:", None))
        self.battery_percent_7.setText(QCoreApplication.translate("MainWindow", u"NaN", None))
        self.Stream.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.Pause.setText(QCoreApplication.translate("MainWindow", u"Pause", None))
        self.Save_to_CSV.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.Stop_Save.setText(QCoreApplication.translate("MainWindow", u"Stop Save", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Connection status:", None))
        self.status_connect_3.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"HW battery:", None))
        self.battery_percent_6.setText(QCoreApplication.translate("MainWindow", u"NaN", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Connection status:", None))
        self.pushButton_11.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"HW battery:", None))
        self.battery_percent.setText(QCoreApplication.translate("MainWindow", u"NaN", None))
        self.Save_seting.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Connection status:", None))
        self.status_connect.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"HW battery:", None))
        self.battery_percent_4.setText(QCoreApplication.translate("MainWindow", u"NaN", None))
        self.Connect.setText(QCoreApplication.translate("MainWindow", u"Check DTC", None))
        self.Reset.setText(QCoreApplication.translate("MainWindow", u"Reset DTC", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Connection status:", None))
        self.status_connect_2.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"HW battery:", None))
        self.battery_percent_5.setText(QCoreApplication.translate("MainWindow", u"NaN", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"BK-AUTO", None))
        self.connectbut.setText(QCoreApplication.translate("MainWindow", u"Connection", None))
        self.sendbut.setText(QCoreApplication.translate("MainWindow", u"Send CAN message", None))
        self.snifferbut.setText(QCoreApplication.translate("MainWindow", u"CAN Sniffer", None))
        self.diagbut.setText(QCoreApplication.translate("MainWindow", u"Diagnotics", None))
        self.settingbut.setText(QCoreApplication.translate("MainWindow", u"Setting", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"Shut down", None))
    # retranslateUi

