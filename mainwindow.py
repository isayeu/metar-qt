# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!
import datetime

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 783)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 294, 29))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())
        
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        regex = QtCore.QRegExp("^[A-Za-z]{4}( [A-Za-z]{4})*")
        validator = QtGui.QRegExpValidator(regex)
        self.lineEdit.setValidator(validator)
        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)
                
        self.getMETAR = QtWidgets.QPushButton(self.centralwidget)
        self.getMETAR.setObjectName(u"getMETAR")
        self.gridLayout.addWidget(self.getMETAR, 0, 1, 1, 1)
        
        self.clearButton = QtWidgets.QPushButton(self.centralwidget)
        self.clearButton.setObjectName(u"clearButton")
        self.gridLayout.addWidget(self.clearButton, 0, 2, 1, 1)
        

        
        self.textBrowserDec = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowserDec.setObjectName(u"textBrowserDec")
        self.gridLayout.addWidget(self.textBrowserDec, 2, 0, 1, 1)
        
      
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName(u"tableWidget")
        self.gridLayout.addWidget(self.tableWidget, 1, 0, 1, 1)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setVisible(True)
        self.tableWidget.setHorizontalHeaderLabels([u"ICAO", u"TIME", u"METAR CODE"])
        
      
        self.retranslateUi(MainWindow)
        self.actionQuit.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        

        
    

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "METAR"))
        self.menuFile.setTitle(_translate("MainWindow", "Fi&le"))
        self.actionQuit.setText(_translate("MainWindow", "&Quit"))
        self.getMETAR.setText(QCoreApplication.translate("MainWindow", u"GET", None))
        self.clearButton.setText(QCoreApplication.translate("MainWindow", u"CLEAR", None))

