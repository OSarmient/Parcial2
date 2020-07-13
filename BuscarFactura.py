# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BuscarFactura.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_BuscarFactura(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(401, 194)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.IngresoFactura_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.IngresoFactura_2.setGeometry(QtCore.QRect(20, 60, 351, 31))
        self.IngresoFactura_2.setObjectName("IngresoFactura_2")
        self.ConfirmarBuscar_2 = QtWidgets.QPushButton(self.centralwidget)
        self.ConfirmarBuscar_2.setGeometry(QtCore.QRect(210, 110, 75, 23))
        self.ConfirmarBuscar_2.setObjectName("ConfirmarBuscar_2")
        self.CancelarBuscar_2 = QtWidgets.QPushButton(self.centralwidget)
        self.CancelarBuscar_2.setGeometry(QtCore.QRect(300, 110, 75, 23))
        self.CancelarBuscar_2.setObjectName("CancelarBuscar_2")
        self.TxtID_2 = QtWidgets.QLabel(self.centralwidget)
        self.TxtID_2.setGeometry(QtCore.QRect(20, 20, 101, 31))
        self.TxtID_2.setObjectName("TxtID_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 401, 21))
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
        self.ConfirmarBuscar_2.setText(_translate("MainWindow", "Buscar"))
        self.CancelarBuscar_2.setText(_translate("MainWindow", "Cancelar"))
        self.TxtID_2.setText(_translate("MainWindow", "No. de Factura"))
