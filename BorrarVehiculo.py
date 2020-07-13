# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BorrarVehiculo.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_BorrarVehiculo(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(430, 193)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ConfirmarBorrarV = QtWidgets.QPushButton(self.centralwidget)
        self.ConfirmarBorrarV.setGeometry(QtCore.QRect(230, 110, 75, 23))
        self.ConfirmarBorrarV.setObjectName("ConfirmarBorrarV")
        self.IngresoPlaca = QtWidgets.QTextEdit(self.centralwidget)
        self.IngresoPlaca.setGeometry(QtCore.QRect(40, 60, 351, 31))
        self.IngresoPlaca.setObjectName("IngresoPlaca")
        self.CancelarBorrarV = QtWidgets.QPushButton(self.centralwidget)
        self.CancelarBorrarV.setGeometry(QtCore.QRect(320, 110, 75, 23))
        self.CancelarBorrarV.setObjectName("CancelarBorrarV")
        self.TxtID = QtWidgets.QLabel(self.centralwidget)
        self.TxtID.setGeometry(QtCore.QRect(40, 20, 101, 31))
        self.TxtID.setObjectName("TxtID")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 430, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ConfirmarBorrarV.setText(_translate("MainWindow", "Borrar"))
        self.CancelarBorrarV.setText(_translate("MainWindow", "Cancelar"))
        self.TxtID.setText(_translate("MainWindow", "No. de identificacion"))
