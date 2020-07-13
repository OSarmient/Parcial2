# -*- coding: utf-8 -*-

# VentanaServicio implementation generated from reading ui file 'VentanaServicio.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_VentanaServicio(object):
    def setupUi(self, VentanaServicio):
        VentanaServicio.setObjectName("VentanaServicio")
        VentanaServicio.resize(469, 361)
        self.NombreServicio = QtWidgets.QLabel(VentanaServicio)
        self.NombreServicio.setGeometry(QtCore.QRect(10, 80, 101, 31))
        self.NombreServicio.setObjectName("NombreServicio")
        self.IngresarCodigo = QtWidgets.QTextEdit(VentanaServicio)
        self.IngresarCodigo.setGeometry(QtCore.QRect(10, 50, 351, 31))
        self.IngresarCodigo.setObjectName("IngresarCodigo")
        self.CodigoServicio = QtWidgets.QLabel(VentanaServicio)
        self.CodigoServicio.setGeometry(QtCore.QRect(10, 20, 101, 31))
        self.CodigoServicio.setObjectName("CodigoServicio")
        self.Horas = QtWidgets.QLabel(VentanaServicio)
        self.Horas.setGeometry(QtCore.QRect(10, 200, 91, 31))
        self.Horas.setObjectName("Horas")
        self.IngresarHoras = QtWidgets.QTextEdit(VentanaServicio)
        self.IngresarHoras.setGeometry(QtCore.QRect(10, 230, 351, 31))
        self.IngresarHoras.setObjectName("IngresarHoras")
        self.CostoXHora = QtWidgets.QLabel(VentanaServicio)
        self.CostoXHora.setGeometry(QtCore.QRect(10, 140, 141, 31))
        self.CostoXHora.setObjectName("CostoXHora")
        self.IngresarCosto = QtWidgets.QTextEdit(VentanaServicio)
        self.IngresarCosto.setGeometry(QtCore.QRect(10, 170, 351, 31))
        self.IngresarCosto.setObjectName("IngresarCosto")
        self.textEdit_7 = QtWidgets.QTextEdit(VentanaServicio)
        self.textEdit_7.setGeometry(QtCore.QRect(10, 110, 351, 31))
        self.textEdit_7.setObjectName("textEdit_7")
        self.AceptarInfoS = QtWidgets.QPushButton(VentanaServicio)
        self.AceptarInfoS.setGeometry(QtCore.QRect(280, 300, 75, 23))
        self.AceptarInfoS.setObjectName("AceptarInfoS")
        self.CancelarInfoS = QtWidgets.QPushButton(VentanaServicio)
        self.CancelarInfoS.setGeometry(QtCore.QRect(370, 300, 75, 23))
        self.CancelarInfoS.setObjectName("CancelarInfoS")

        self.retranslateUi(VentanaServicio)
        QtCore.QMetaObject.connectSlotsByName(VentanaServicio)

    def retranslateUi(self, VentanaServicio):
        _translate = QtCore.QCoreApplication.translate
        VentanaServicio.setWindowTitle(_translate("VentanaServicio", "VentanaServicio"))
        self.NombreServicio.setText(_translate("VentanaServicio", "Nombre del servicio"))
        self.CodigoServicio.setText(_translate("VentanaServicio", "Codigo del Servicio"))
        self.Horas.setText(_translate("VentanaServicio", "Horas del servicio"))
        self.CostoXHora.setText(_translate("VentanaServicio", "Costo por hora del servicio"))
        self.AceptarInfoS.setText(_translate("VentanaServicio", "Aceptar"))
        self.CancelarInfoS.setText(_translate("VentanaServicio", "Cancelar"))
