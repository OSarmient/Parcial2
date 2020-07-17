# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VentanaFactura.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_VentanaFactura(object):
    def setupUi(self, VentanaFactura):
        VentanaFactura.setObjectName("VentanaFactura")
        VentanaFactura.resize(387, 502)
        self.centralwidget = QtWidgets.QWidget(VentanaFactura)
        self.centralwidget.setObjectName("centralwidget")
        self.IDClienteF = QtWidgets.QLabel(self.centralwidget)
        self.IDClienteF.setGeometry(QtCore.QRect(20, 10, 81, 31))
        self.IDClienteF.setObjectName("IDClienteF")
        self.IngresoCodigoF = QtWidgets.QTextEdit(self.centralwidget)
        self.IngresoCodigoF.setGeometry(QtCore.QRect(20, 160, 351, 31))
        self.IngresoCodigoF.setObjectName("IngresoCodigoF")
        self.IngresoPlacaF = QtWidgets.QTextEdit(self.centralwidget)
        self.IngresoPlacaF.setGeometry(QtCore.QRect(20, 100, 351, 31))
        self.IngresoPlacaF.setObjectName("IngresoPlacaF")
        self.CodigoSF = QtWidgets.QLabel(self.centralwidget)
        self.CodigoSF.setGeometry(QtCore.QRect(20, 130, 181, 31))
        self.CodigoSF.setObjectName("CodigoSF")
        self.IngresoID_F = QtWidgets.QTextEdit(self.centralwidget)
        self.IngresoID_F.setGeometry(QtCore.QRect(20, 40, 351, 31))
        self.IngresoID_F.setObjectName("IngresoID_F")
        self.PlacaF = QtWidgets.QLabel(self.centralwidget)
        self.PlacaF.setGeometry(QtCore.QRect(20, 70, 181, 31))
        self.PlacaF.setObjectName("PlacaF")
        self.CancelarF = QtWidgets.QPushButton(self.centralwidget)
        self.CancelarF.setGeometry(QtCore.QRect(300, 430, 75, 23))
        self.CancelarF.setObjectName("CancelarF")
        self.AceptarF = QtWidgets.QPushButton(self.centralwidget)
        self.AceptarF.setGeometry(QtCore.QRect(210, 430, 75, 23))
        self.AceptarF.setObjectName("AceptarF")
        VentanaFactura.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(VentanaFactura)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 387, 21))
        self.menubar.setObjectName("menubar")
        VentanaFactura.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(VentanaFactura)
        self.statusbar.setObjectName("statusbar")
        VentanaFactura.setStatusBar(self.statusbar)

        self.retranslateUi(VentanaFactura)
        self.AceptarF.clicked.connect(self.IngresoID_F.selectAll)
        self.AceptarF.clicked.connect(self.IngresoPlacaF.selectAll)
        self.AceptarF.clicked.connect(self.IngresoCodigoF.selectAll)
        QtCore.QMetaObject.connectSlotsByName(VentanaFactura)

    def retranslateUi(self, VentanaFactura):
        _translate = QtCore.QCoreApplication.translate
        VentanaFactura.setWindowTitle(_translate("VentanaFactura", "MainWindow"))
        self.IDClienteF.setText(_translate("VentanaFactura", "ID del Cliente"))
        self.CodigoSF.setText(_translate("VentanaFactura", "No. del cogido del servicio solicitado"))
        self.PlacaF.setText(_translate("VentanaFactura", "No. de la placa del vehiculo asociado"))
        self.CancelarF.setText(_translate("VentanaFactura", "Cancelar"))
        self.AceptarF.setText(_translate("VentanaFactura", "Aceptar"))
