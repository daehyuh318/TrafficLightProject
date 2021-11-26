# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\traffic_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1141, 818)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/daehy/.designer/backup/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        MainWindow.setIconSize(QtCore.QSize(100, 100))
        MainWindow.setAnimated(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setToolTipDuration(-1)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setContentsMargins(10, 20, 10, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(-1, -1, 0, 0)
        self.gridLayout.setSpacing(7)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setEnabled(True)
        self.tableWidget.setMinimumSize(QtCore.QSize(450, 500))
        self.tableWidget.setMaximumSize(QtCore.QSize(450, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("QHeaderView::section {background-color:#909090;color:#FFFFFF;}\n"
"section {background-color:#909090;color:#FFFFFF;}")
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(222)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(45)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget.verticalHeader().setDefaultSectionSize(40)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setMinimumSectionSize(40)
        self.gridLayout.addWidget(self.tableWidget, 5, 0, 1, 1)
        self.start_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start_button.sizePolicy().hasHeightForWidth())
        self.start_button.setSizePolicy(sizePolicy)
        self.start_button.setMinimumSize(QtCore.QSize(450, 70))
        self.start_button.setMaximumSize(QtCore.QSize(200, 70))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setBold(True)
        font.setWeight(75)
        self.start_button.setFont(font)
        self.start_button.setObjectName("start_button")
        self.gridLayout.addWidget(self.start_button, 6, 0, 1, 1)
        self.traffic_light_widget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.traffic_light_widget.sizePolicy().hasHeightForWidth())
        self.traffic_light_widget.setSizePolicy(sizePolicy)
        self.traffic_light_widget.setMinimumSize(QtCore.QSize(450, 150))
        self.traffic_light_widget.setMaximumSize(QtCore.QSize(450, 16777215))
        self.traffic_light_widget.setStyleSheet("background-color: rgb(45, 45, 45);")
        self.traffic_light_widget.setObjectName("traffic_light_widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.traffic_light_widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.RED = QtWidgets.QLabel(self.traffic_light_widget)
        self.RED.setMinimumSize(QtCore.QSize(100, 100))
        self.RED.setMaximumSize(QtCore.QSize(100, 100))
        self.RED.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 50px;\n"
"min-height: 100px;\n"
"min-width: 100px;")
        self.RED.setText("")
        self.RED.setObjectName("RED")
        self.horizontalLayout.addWidget(self.RED)
        self.YELLOW = QtWidgets.QLabel(self.traffic_light_widget)
        self.YELLOW.setMaximumSize(QtCore.QSize(100, 100))
        self.YELLOW.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"border-radius: 50px;\n"
"min-height: 100px;\n"
"min-width: 100px;")
        self.YELLOW.setText("")
        self.YELLOW.setObjectName("YELLOW")
        self.horizontalLayout.addWidget(self.YELLOW)
        self.LEFT = QtWidgets.QLabel(self.traffic_light_widget)
        self.LEFT.setMinimumSize(QtCore.QSize(100, 100))
        self.LEFT.setMaximumSize(QtCore.QSize(100, 100))
        self.LEFT.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"border-radius: 50px;\n"
"min-height: 100px;\n"
"min-width: 100px;")
        self.LEFT.setObjectName("LEFT")
        self.horizontalLayout.addWidget(self.LEFT)
        self.GREEN = QtWidgets.QLabel(self.traffic_light_widget)
        self.GREEN.setMinimumSize(QtCore.QSize(100, 100))
        self.GREEN.setMaximumSize(QtCore.QSize(100, 100))
        self.GREEN.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"border-radius: 50px;\n"
"min-height: 100px;\n"
"min-width: 100px;")
        self.GREEN.setText("")
        self.GREEN.setObjectName("GREEN")
        self.horizontalLayout.addWidget(self.GREEN)
        self.gridLayout.addWidget(self.traffic_light_widget, 4, 0, 1, 1)
        self.treeView = QtWidgets.QTreeView(self.centralwidget)
        self.treeView.setMinimumSize(QtCore.QSize(0, 0))
        self.treeView.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.treeView.setLineWidth(1)
        self.treeView.setObjectName("treeView")
        self.gridLayout.addWidget(self.treeView, 5, 3, 1, 2)
        self.delete_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delete_button.sizePolicy().hasHeightForWidth())
        self.delete_button.setSizePolicy(sizePolicy)
        self.delete_button.setMinimumSize(QtCore.QSize(200, 70))
        self.delete_button.setMaximumSize(QtCore.QSize(200, 70))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setBold(True)
        font.setWeight(75)
        self.delete_button.setFont(font)
        self.delete_button.setObjectName("delete_button")
        self.gridLayout.addWidget(self.delete_button, 6, 4, 1, 1)
        self.save_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.save_button.sizePolicy().hasHeightForWidth())
        self.save_button.setSizePolicy(sizePolicy)
        self.save_button.setMinimumSize(QtCore.QSize(200, 70))
        self.save_button.setMaximumSize(QtCore.QSize(200, 70))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setBold(True)
        font.setWeight(75)
        self.save_button.setFont(font)
        self.save_button.setObjectName("save_button")
        self.gridLayout.addWidget(self.save_button, 6, 3, 1, 1)
        self.event_log = QtWidgets.QTextEdit(self.centralwidget)
        self.event_log.setEnabled(False)
        self.event_log.setMinimumSize(QtCore.QSize(0, 0))
        self.event_log.setMaximumSize(QtCore.QSize(16777215, 150))
        self.event_log.setObjectName("event_log")
        self.gridLayout.addWidget(self.event_log, 4, 3, 1, 2)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 4, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "LED"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "TIME"))
        self.start_button.setText(_translate("MainWindow", "시작"))
        self.LEFT.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-family:\'Arial\'; font-size:48pt; font-weight:600;\">←</span></p></body></html>"))
        self.delete_button.setText(_translate("MainWindow", "삭제"))
        self.save_button.setText(_translate("MainWindow", "저장"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
