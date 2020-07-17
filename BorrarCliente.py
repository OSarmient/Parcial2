# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BorrarCliente.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from clients import Clients

class Ui_BorrarCliente(object):
    def setupUi(self, BorrarCliente):
        BorrarCliente.setObjectName("BorrarCliente")
        BorrarCliente.resize(433, 189)
        self.centralwidget = QtWidgets.QWidget(BorrarCliente)
        self.centralwidget.setObjectName("centralwidget")
        self.IngresoID = QtWidgets.QTextEdit(self.centralwidget)
        self.IngresoID.setGeometry(QtCore.QRect(40, 70, 351, 31))
        self.IngresoID.setObjectName("IngresoID")
        self.TxtID = QtWidgets.QLabel(self.centralwidget)
        self.TxtID.setGeometry(QtCore.QRect(40, 30, 101, 31))
        self.TxtID.setObjectName("TxtID")
        self.CancelarBorrarC = QtWidgets.QPushButton(self.centralwidget)
        self.CancelarBorrarC.setGeometry(QtCore.QRect(320, 120, 75, 23))
        self.CancelarBorrarC.setObjectName("CancelarBorrarC")
        self.ConfirmarBorrarC = QtWidgets.QPushButton(self.centralwidget)
        self.ConfirmarBorrarC.setGeometry(QtCore.QRect(230, 120, 75, 23))
        self.ConfirmarBorrarC.setObjectName("ConfirmarBorrarC")
        self.retranslateUi(BorrarCliente)
        self.CancelarBorrarC.clicked.connect(BorrarCliente.close)
        QtCore.QMetaObject.connectSlotsByName(BorrarCliente)
        BorrarCliente.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(BorrarCliente)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 433, 21))
        self.menubar.setObjectName("menubar")
        BorrarCliente.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(BorrarCliente)
        self.statusbar.setObjectName("statusbar")
        BorrarCliente.setStatusBar(self.statusbar)

        self.retranslateUi(BorrarCliente)
        self.ConfirmarBorrarC.clicked.connect(self.erase)
        self.ConfirmarBorrarC.clicked.connect(BorrarCliente.close)
        QtCore.QMetaObject.connectSlotsByName(BorrarCliente)

    def retranslateUi(self, BorrarCliente):
        _translate = QtCore.QCoreApplication.translate
        BorrarCliente.setWindowTitle(_translate("BorrarCliente", "MainWindow"))
        self.TxtID.setText(_translate("BorrarCliente", "No. de identificacion"))
        self.CancelarBorrarC.setText(_translate("BorrarCliente", "Cancelar"))
        self.ConfirmarBorrarC.setText(_translate("BorrarCliente", "Borrar"))

    def erase(self, VentanaCliente):
        data = self.IngresoID.toPlainText()
        clients = Clients()
        clients.delete(data, property="No ID")
