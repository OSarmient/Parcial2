# -*- coding: utf-8 -*-

# BorrarVehiculo implementation generated from reading ui file 'BorrarVehiculo.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_BorrarVehiculo(object):
    def setupUi(self, BorrarVehiculo):
        BorrarVehiculo.setObjectName("BorrarVehiculo")
        BorrarVehiculo.resize(430, 192)
        self.CancelarBorrarV = QtWidgets.QPushButton(BorrarVehiculo)
        self.CancelarBorrarV.setGeometry(QtCore.QRect(320, 120, 75, 23))
        self.CancelarBorrarV.setObjectName("CancelarBorrarV")
        self.TxtID = QtWidgets.QLabel(BorrarVehiculo)
        self.TxtID.setGeometry(QtCore.QRect(40, 30, 101, 31))
        self.TxtID.setObjectName("TxtID")
        self.IngresoPlaca = QtWidgets.QTextEdit(BorrarVehiculo)
        self.IngresoPlaca.setGeometry(QtCore.QRect(40, 70, 351, 31))
        self.IngresoPlaca.setObjectName("IngresoPlaca")
        self.ConfirmarBorrarV = QtWidgets.QPushButton(BorrarVehiculo)
        self.ConfirmarBorrarV.setGeometry(QtCore.QRect(230, 120, 75, 23))
        self.ConfirmarBorrarV.setObjectName("ConfirmarBorrarV")

        self.retranslateUi(BorrarVehiculo)
        QtCore.QMetaObject.connectSlotsByName(BorrarVehiculo)

    def retranslateUi(self, BorrarVehiculo):
        _translate = QtCore.QCoreApplication.translate
        BorrarVehiculo.setWindowTitle(_translate("BorrarVehiculo", "BorrarVehiculo"))
        self.CancelarBorrarV.setText(_translate("BorrarVehiculo", "Cancelar"))
        self.TxtID.setText(_translate("BorrarVehiculo", "No. de identificacion"))
        self.ConfirmarBorrarV.setText(_translate("BorrarVehiculo", "Borrar"))
