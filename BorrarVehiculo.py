# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BorrarVehiculo.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_BorrarVehiculo(object):
    def setupUi(self, BorrarVehiculo):
        BorrarVehiculo.setObjectName("BorrarVehiculo")
        BorrarVehiculo.resize(430, 193)
        self.centralwidget = QtWidgets.QWidget(BorrarVehiculo)
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
        self.CancelarBorrarV.clicked.connect(BorrarVehiculo.close)
        QtCore.QMetaObject.connectSlotsByName(BorrarVehiculo)
        BorrarVehiculo.setCentralWidget(self.centralwidget)
        BorrarVehiculo.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(BorrarVehiculo)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 430, 21))
        self.menubar.setObjectName("menubar")
        BorrarVehiculo.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(BorrarVehiculo)
        self.statusbar.setObjectName("statusbar")
        BorrarVehiculo.setStatusBar(self.statusbar)

        self.retranslateUi(BorrarVehiculo)
        self.ConfirmarBorrarV.clicked.connect(self.IngresoPlaca.selectAll)
        QtCore.QMetaObject.connectSlotsByName(BorrarVehiculo)

    def retranslateUi(self, BorrarVehiculo):
        _translate = QtCore.QCoreApplication.translate
        BorrarVehiculo.setWindowTitle(_translate("BorrarVehiculo", "BorrarVehiculo"))
        self.ConfirmarBorrarV.setText(_translate("BorrarVehiculo", "Borrar"))
        self.CancelarBorrarV.setText(_translate("BorrarVehiculo", "Cancelar"))
        self.TxtID.setText(_translate("BorrarVehiculo", "No. de identificacion"))
