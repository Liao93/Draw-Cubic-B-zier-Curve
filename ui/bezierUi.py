# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bezier.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(273, 423)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.p1_info = QtWidgets.QLabel(self.centralwidget)
        self.p1_info.setGeometry(QtCore.QRect(80, 120, 111, 21))
        self.p1_info.setText("")
        self.p1_info.setObjectName("p1_info")
        self.p2_info = QtWidgets.QLabel(self.centralwidget)
        self.p2_info.setGeometry(QtCore.QRect(80, 150, 111, 21))
        self.p2_info.setText("")
        self.p2_info.setObjectName("p2_info")
        self.p3_info = QtWidgets.QLabel(self.centralwidget)
        self.p3_info.setGeometry(QtCore.QRect(80, 180, 111, 21))
        self.p3_info.setText("")
        self.p3_info.setObjectName("p3_info")
        self.p4_info = QtWidgets.QLabel(self.centralwidget)
        self.p4_info.setGeometry(QtCore.QRect(80, 210, 111, 21))
        self.p4_info.setText("")
        self.p4_info.setObjectName("p4_info")
        self.resetButton = QtWidgets.QPushButton(self.centralwidget)
        self.resetButton.setGeometry(QtCore.QRect(90, 260, 93, 28))
        self.resetButton.setObjectName("resetButton")
        self.drawButton = QtWidgets.QPushButton(self.centralwidget)
        self.drawButton.setGeometry(QtCore.QRect(90, 300, 93, 28))
        self.drawButton.setObjectName("drawButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 273, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Bézier curve"))
        self.resetButton.setText(_translate("MainWindow", "Reset"))
        self.drawButton.setText(_translate("MainWindow", "Draw"))

