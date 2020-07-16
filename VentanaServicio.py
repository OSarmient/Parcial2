# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VentanaServicio.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from service import Service


class Ui_VentanaServicio(object):
    def setupUi(self, VentanaServicio):
        VentanaServicio.setObjectName("VentanaServicio")
        VentanaServicio.resize(468, 361)
        self.centralwidget = QtWidgets.QWidget(VentanaServicio)
        self.centralwidget.setObjectName("centralwidget")
        self.IngresarCosto = QtWidgets.QTextEdit(self.centralwidget)
        self.IngresarCosto.setGeometry(QtCore.QRect(20, 160, 351, 31))
        self.IngresarCosto.setObjectName("IngresarCosto")
        self.CostoXHora = QtWidgets.QLabel(self.centralwidget)
        self.CostoXHora.setGeometry(QtCore.QRect(20, 130, 141, 31))
        self.CostoXHora.setObjectName("CostoXHora")
        self.Horas = QtWidgets.QLabel(self.centralwidget)
        self.Horas.setGeometry(QtCore.QRect(20, 190, 91, 31))
        self.Horas.setObjectName("Horas")
        self.CodigoServicio = QtWidgets.QLabel(self.centralwidget)
        self.CodigoServicio.setGeometry(QtCore.QRect(20, 10, 101, 31))
        self.CodigoServicio.setObjectName("CodigoServicio")
        self.CancelarInfoS = QtWidgets.QPushButton(self.centralwidget)
        self.CancelarInfoS.setGeometry(QtCore.QRect(380, 290, 75, 23))
        self.CancelarInfoS.setObjectName("CancelarInfoS")
        self.IngresarNombre = QtWidgets.QTextEdit(self.centralwidget)
        self.IngresarNombre.setGeometry(QtCore.QRect(20, 100, 351, 31))
        self.IngresarNombre.setObjectName("IngresarNombre")
        self.NombreServicio = QtWidgets.QLabel(self.centralwidget)
        self.NombreServicio.setGeometry(QtCore.QRect(20, 70, 101, 31))
        self.NombreServicio.setObjectName("NombreServicio")
        self.IngresarCodigo = QtWidgets.QTextEdit(self.centralwidget)
        self.IngresarCodigo.setGeometry(QtCore.QRect(20, 40, 351, 31))
        self.IngresarCodigo.setObjectName("IngresarCodigo")
        self.IngresarHoras = QtWidgets.QTextEdit(self.centralwidget)
        self.IngresarHoras.setGeometry(QtCore.QRect(20, 220, 351, 31))
        self.IngresarHoras.setObjectName("IngresarHoras")
        self.AceptarInfoS = QtWidgets.QPushButton(self.centralwidget)
        self.AceptarInfoS.setGeometry(QtCore.QRect(290, 290, 75, 23))
        self.AceptarInfoS.setObjectName("AceptarInfoS")
        self.retranslateUi(VentanaServicio)
        self.CancelarInfoS.clicked.connect(VentanaServicio.close)
        QtCore.QMetaObject.connectSlotsByName( VentanaServicio)
        VentanaServicio.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(VentanaServicio)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 468, 21))
        self.menubar.setObjectName("menubar")
        VentanaServicio.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(VentanaServicio)
        self.statusbar.setObjectName("statusbar")
        VentanaServicio.setStatusBar(self.statusbar)

        self.retranslateUi(VentanaServicio)
        self.AceptarInfoS.clicked.connect(self.insert1)
        self.AceptarInfoS.clicked.connect(VentanaServicio.close)
        QtCore.QMetaObject.connectSlotsByName(VentanaServicio)

        self.retranslateUi(VentanaServicio)
        self.AceptarInfoS.clicked.connect(self.IngresarCodigo.selectAll)
        self.AceptarInfoS.clicked.connect(self.IngresarNombre.selectAll)
        self.AceptarInfoS.clicked.connect(self.IngresarCosto.selectAll)
        self.AceptarInfoS.clicked.connect(self.IngresarHoras.selectAll)
        QtCore.QMetaObject.connectSlotsByName(VentanaServicio)

    def retranslateUi(self, VentanaServicio):
        _translate = QtCore.QCoreApplication.translate
        VentanaServicio.setWindowTitle(_translate("VentanaServicio", "MainWindow"))
        self.CostoXHora.setText(_translate("VentanaServicio", "Costo por hora del servicio"))
        self.Horas.setText(_translate("VentanaServicio", "Horas del servicio"))
        self.CodigoServicio.setText(_translate("VentanaServicio", "Codigo del Servicio"))
        self.CancelarInfoS.setText(_translate("VentanaServicio", "Cancelar"))
        self.NombreServicio.setText(_translate("VentanaServicio", "Nombre del servicio"))
        self.AceptarInfoS.setText(_translate("VentanaServicio", "Aceptar"))

    def insert1(self, VentanaServicio):
        data = []
        data.append(self.IngresarCodigo.toPlainText())
        data.append(self.IngresarNombre.toPlainText())
        data.append(self.IngresarCosto.toPlainText())
        data.append(self.IngresarHoras.toPlainText())
        service = Service()
        service.insert2(data)