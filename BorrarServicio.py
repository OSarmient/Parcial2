# -*- coding: utf-8 -*-

# BorrarServicio implementation generated from reading ui file 'BorrarServicio.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_BorrarServicio(object):
    def setupUi(self, BorrarServicio):
        BorrarServicio.setObjectName("BorrarServicio")
        BorrarServicio.resize(432, 188)
        self.CancelarBorrarS = QtWidgets.QPushButton(BorrarServicio)
        self.CancelarBorrarS.setGeometry(QtCore.QRect(320, 130, 75, 23))
        self.CancelarBorrarS.setObjectName("CancelarBorrarS")
        self.TxtID = QtWidgets.QLabel(BorrarServicio)
        self.TxtID.setGeometry(QtCore.QRect(40, 40, 121, 31))
        self.TxtID.setObjectName("TxtID")
        self.IngresoCodigo = QtWidgets.QTextEdit(BorrarServicio)
        self.IngresoCodigo.setGeometry(QtCore.QRect(40, 80, 351, 31))
        self.IngresoCodigo.setObjectName("IngresoCodigo")
        self.ConfirmarBorrarS = QtWidgets.QPushButton(BorrarServicio)
        self.ConfirmarBorrarS.setGeometry(QtCore.QRect(230, 130, 75, 23))
        self.ConfirmarBorrarS.setObjectName("ConfirmarBorrarS")

        self.retranslateUi(BorrarServicio)
        QtCore.QMetaObject.connectSlotsByName(BorrarServicio)

    def retranslateUi(self, BorrarServicio):
        _translate = QtCore.QCoreApplication.translate
        BorrarServicio.setWindowTitle(_translate("BorrarServicio", "BorrarServicio"))
        self.CancelarBorrarS.setText(_translate("BorrarServicio", "Cancelar"))
        self.TxtID.setText(_translate("BorrarServicio", "No. de identificacion"))
        self.ConfirmarBorrarS.setText(_translate("BorrarServicio", "Borrar"))
