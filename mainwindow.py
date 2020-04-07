# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!
import datetime

from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QWidget, QGridLayout, QTextBrowser, QLineEdit, QPushButton, QTabWidget, QTableWidget, QMenuBar, QMenu, QStatusBar, QAbstractItemView, QAction

class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		if not MainWindow.objectName():
			MainWindow.setObjectName(u"MainWindow")
		MainWindow.resize(1000, 800)
		self.centralwidget = QWidget(MainWindow)
		self.centralwidget.setObjectName(u"centralwidget")
		
		self.gridLayout = QGridLayout(self.centralwidget)
		self.gridLayout.setSpacing(5)
		self.gridLayout.setObjectName(u"gridLayout")
		self.gridLayout.setContentsMargins(10, 10, 10, 10)
		
		self.textBrowserDec = QTextBrowser(self.centralwidget)
		self.textBrowserDec.setObjectName(u"textBrowserDec")
		self.gridLayout.addWidget(self.textBrowserDec, 7, 0, 1, 1)
		
		self.lineEdit = QLineEdit(self.centralwidget)
		self.lineEdit.setObjectName(u"lineEdit")
		regex = QtCore.QRegExp("^[0-9A-Za-z]{4}( [0-9A-Za-z]{4})*")
		validator = QtGui.QRegExpValidator(regex)
		self.lineEdit.setValidator(validator)
		self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)
		
		self.getMETAR = QPushButton(self.centralwidget)
		self.getMETAR.setObjectName(u"getMETAR")
		self.gridLayout.addWidget(self.getMETAR, 0, 1, 1, 1)
		
		self.clearButton = QPushButton(self.centralwidget)
		self.clearButton.setObjectName(u"clearButton")
		self.gridLayout.addWidget(self.clearButton, 0, 2, 1, 1)
	# Maintab
		self.tabWidget = QTabWidget(self.centralwidget)
		self.tabWidget.setObjectName(u"tabWidget")
		#Tab METAR
		self.tab_1 = QWidget()
		self.tab_1.setObjectName(u"tab_1")
		self.gridLayout_2 = QGridLayout(self.tab_1)
		self.gridLayout_2.setObjectName(u"gridLayout_2")
		self.tableWidget = QTableWidget(self.tab_1)
		self.tableWidget.setObjectName(u"tableWidget")
		self.tableWidget.setColumnCount(3)
		self.tableWidget.setRowCount(0)
		self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
		self.tableWidget.horizontalHeader().setVisible(True)
		self.tableWidget.verticalHeader().setVisible(False)
		self.tableWidget.setHorizontalHeaderLabels([u"ICAO", u"TIME", u"METAR CODE"])
		self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
		self.gridLayout_2.addWidget(self.tableWidget, 0, 0, 1, 1)
		self.tabWidget.addTab(self.tab_1, "")
		#Tab_METAR_END
		
		self.tab_2 = QWidget()
		self.tab_2.setObjectName(u"tab_2")
		self.gridLayout_3 = QGridLayout(self.tab_2)
		self.gridLayout_3.setObjectName(u"gridLayout_3")
		self.tableWidget_2 = QTableWidget(self.tab_2)
		self.tableWidget_2.setObjectName(u"tableWidget_2")
		self.gridLayout_3.addWidget(self.tableWidget_2, 0, 0, 1, 1)
		self.tabWidget.addTab(self.tab_2, "")
		self.tab_3 = QWidget()
		self.tab_3.setObjectName(u"tab_3")
		self.gridLayout_4 = QGridLayout(self.tab_3)
		self.gridLayout_4.setObjectName(u"gridLayout_4")
		self.tableWidget_3 = QTableWidget(self.tab_3)
		self.tableWidget_3.setObjectName(u"tableWidget_3")
		self.gridLayout_4.addWidget(self.tableWidget_3, 0, 0, 1, 1)
		self.tabWidget.addTab(self.tab_3, "")
		self.gridLayout.addWidget(self.tabWidget, 2, 0, 1, 1)
	#Maintab_END

		self.verticalLayout = QtWidgets.QVBoxLayout()
		self.verticalLayout.setObjectName("verticalLayout")
		self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
		self.checkBox.setEnabled(True)
		self.checkBox.setStatusTip("")
		self.checkBox.setChecked(True)
		self.checkBox.setTristate(False)
		self.checkBox.setObjectName("checkBox")
		self.verticalLayout.addWidget(self.checkBox)
		self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
		self.checkBox_2.setObjectName("checkBox_2")
		self.verticalLayout.addWidget(self.checkBox_2)
		self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
		self.checkBox_3.setObjectName("checkBox_3")
		self.verticalLayout.addWidget(self.checkBox_3)
		self.gridLayout.addLayout(self.verticalLayout, 2, 1, 1, 2)

		#WIP
		self.checkBox.setChecked(True)
		self.checkBox.setDisabled(True)
		self.checkBox_2.setDisabled(True)
		self.checkBox_3.setDisabled(True)
		#END_WIP
		
		MainWindow.setCentralWidget(self.centralwidget)
		self.menubar = QMenuBar(MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 294, 29))
		self.menubar.setObjectName("menubar")
		self.menuFile = QMenu(self.menubar)
		self.menuFile.setObjectName("menuFile")
		MainWindow.setMenuBar(self.menubar)
		self.statusbar = QStatusBar(MainWindow)
		self.statusbar.setObjectName("statusbar")
		MainWindow.setStatusBar(self.statusbar)
		self.actionQuit = QAction(MainWindow)
		self.actionQuit.setObjectName("actionQuit")
		self.menuFile.addAction(self.actionQuit)
		self.menubar.addAction(self.menuFile.menuAction())

		self.retranslateUi(MainWindow)
		self.actionQuit.triggered.connect(MainWindow.close)
		self.tabWidget.setCurrentIndex(0)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)
		


	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "METAR"))
		self.menuFile.setTitle(_translate("MainWindow", "Fi&le"))
		self.actionQuit.setText(_translate("MainWindow", "&Quit"))
		self.getMETAR.setText(QCoreApplication.translate("MainWindow", u"GET", None))
		self.clearButton.setText(QCoreApplication.translate("MainWindow", u"CLEAR", None))
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), QCoreApplication.translate("MainWindow", u"METAR", None))
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"TAF", None))
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"NOTAM", None))
		self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"TAF", None))
		self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"NOTAM", None))
		self.checkBox.setText(QCoreApplication.translate("MainWindow", u"METAR", None))
		
