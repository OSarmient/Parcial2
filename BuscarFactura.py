# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BuscarFactura.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_BuscarFactura(object):
    def setupUi(self, BuscarFactura):
        BuscarFactura.setObjectName("BuscarFactura")
        BuscarFactura.resize(401, 194)
        self.centralwidget = QtWidgets.QWidget(BuscarFactura)
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
        self.retranslateUi(BuscarFactura)
        self.CancelarBuscar_2.clicked.connect(BuscarFactura.close)
        QtCore.QMetaObject.connectSlotsByName(BuscarFactura)
        BuscarFactura.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(BuscarFactura)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 401, 21))
        self.menubar.setObjectName("menubar")
        BuscarFactura.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(BuscarFactura)
        self.statusbar.setObjectName("statusbar")
        BuscarFactura.setStatusBar(self.statusbar)

        self.retranslateUi(BuscarFactura)
        self.ConfirmarBuscar_2.clicked.connect(self.IngresoFactura_2.selectAll)
        QtCore.QMetaObject.connectSlotsByName(BuscarFactura)

    def retranslateUi(self, BuscarFactura):
        _translate = QtCore.QCoreApplication.translate
        BuscarFactura.setWindowTitle(_translate("BuscarFactura", "BuscarFactura"))
        self.ConfirmarBuscar_2.setText(_translate("BuscarFactura", "Buscar"))
        self.CancelarBuscar_2.setText(_translate("BuscarFactura", "Cancelar"))
        self.TxtID_2.setText(_translate("BuscarFactura", "No. de Factura"))
