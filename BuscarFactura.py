# -*- coding: utf-8 -*-

# BuscarFactura implementation generated from reading ui file 'BuscarFactura.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_BuscarFactura(object):
    def setupUi(self, BuscarFactura):
        BuscarFactura.setObjectName("BuscarFactura")
        BuscarFactura.resize(400, 192)
        self.CancelarBuscar = QtWidgets.QPushButton(BuscarFactura)
        self.CancelarBuscar.setGeometry(QtCore.QRect(300, 120, 75, 23))
        self.CancelarBuscar.setObjectName("CancelarBuscar")
        self.TxtID = QtWidgets.QLabel(BuscarFactura)
        self.TxtID.setGeometry(QtCore.QRect(20, 30, 101, 31))
        self.TxtID.setObjectName("TxtID")
        self.IngresoFactura = QtWidgets.QTextEdit(BuscarFactura)
        self.IngresoFactura.setGeometry(QtCore.QRect(20, 70, 351, 31))
        self.IngresoFactura.setObjectName("IngresoFactura")
        self.ConfirmarBuscar = QtWidgets.QPushButton(BuscarFactura)
        self.ConfirmarBuscar.setGeometry(QtCore.QRect(210, 120, 75, 23))
        self.ConfirmarBuscar.setObjectName("ConfirmarBuscar")

        self.retranslateUi(BuscarFactura)
        QtCore.QMetaObject.connectSlotsByName(BuscarFactura)

    def retranslateUi(self, BuscarFactura):
        _translate = QtCore.QCoreApplication.translate
        BuscarFactura.setWindowTitle(_translate("BuscarFactura", "BuscarFactura"))
        self.CancelarBuscar.setText(_translate("BuscarFactura", "Cancelar"))
        self.TxtID.setText(_translate("BuscarFactura", "No. de Factura"))
        self.ConfirmarBuscar.setText(_translate("BuscarFactura", "Buscar"))
