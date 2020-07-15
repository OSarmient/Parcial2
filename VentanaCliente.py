# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VentanaCliente.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_VentanaCliente(object):
    def setupUi(self, VentanaCliente):
        VentanaCliente.setObjectName("VentanaCliente")
        VentanaCliente.resize(686, 481)
        self.centralwidget = QtWidgets.QWidget(VentanaCliente)
        self.centralwidget.setObjectName("centralwidget")
        self.IngresoID_C = QtWidgets.QTextEdit(self.centralwidget)
        self.IngresoID_C.setGeometry(QtCore.QRect(150, 40, 351, 31))
        self.IngresoID_C.setObjectName("IngresoID_C")
        self.IngresoNombre = QtWidgets.QTextEdit(self.centralwidget)
        self.IngresoNombre.setGeometry(QtCore.QRect(150, 100, 351, 31))
        self.IngresoNombre.setObjectName("IngresoNombre")
        self.IngresoTelefono = QtWidgets.QTextEdit(self.centralwidget)
        self.IngresoTelefono.setGeometry(QtCore.QRect(150, 280, 351, 31))
        self.IngresoTelefono.setObjectName("IngresoTelefono")
        self.IngresoCiudad = QtWidgets.QTextEdit(self.centralwidget)
        self.IngresoCiudad.setGeometry(QtCore.QRect(150, 340, 351, 31))
        self.IngresoCiudad.setObjectName("IngresoCiudad")
        self.IngresoApellido = QtWidgets.QTextEdit(self.centralwidget)
        self.IngresoApellido.setGeometry(QtCore.QRect(150, 160, 351, 31))
        self.IngresoApellido.setObjectName("IngresoApellido")
        self.IngrsoDireccion = QtWidgets.QTextEdit(self.centralwidget)
        self.IngrsoDireccion.setGeometry(QtCore.QRect(150, 220, 351, 31))
        self.IngrsoDireccion.setObjectName("IngrsoDireccion")
        self.TxtNombre = QtWidgets.QLabel(self.centralwidget)
        self.TxtNombre.setGeometry(QtCore.QRect(150, 70, 71, 31))
        self.TxtNombre.setObjectName("TxtNombre")
        self.TxtApellido = QtWidgets.QLabel(self.centralwidget)
        self.TxtApellido.setGeometry(QtCore.QRect(150, 130, 71, 31))
        self.TxtApellido.setObjectName("TxtApellido")
        self.TxtID = QtWidgets.QLabel(self.centralwidget)
        self.TxtID.setGeometry(QtCore.QRect(150, 10, 101, 31))
        self.TxtID.setObjectName("TxtID")
        self.TxtDireccion = QtWidgets.QLabel(self.centralwidget)
        self.TxtDireccion.setGeometry(QtCore.QRect(150, 190, 71, 31))
        self.TxtDireccion.setObjectName("TxtDireccion")
        self.TxtTelefono = QtWidgets.QLabel(self.centralwidget)
        self.TxtTelefono.setGeometry(QtCore.QRect(150, 250, 101, 31))
        self.TxtTelefono.setObjectName("TxtTelefono")
        self.TxtCiudad = QtWidgets.QLabel(self.centralwidget)
        self.TxtCiudad.setGeometry(QtCore.QRect(150, 310, 71, 31))
        self.TxtCiudad.setObjectName("TxtCiudad")
        self.AceptarInfoC = QtWidgets.QPushButton(self.centralwidget)
        self.AceptarInfoC.setGeometry(QtCore.QRect(500, 400, 75, 23))
        self.AceptarInfoC.setObjectName("AceptarInfoC")
        self.CancelarInfoC = QtWidgets.QPushButton(self.centralwidget)
        self.CancelarInfoC.setGeometry(QtCore.QRect(590, 400, 75, 23))
        self.CancelarInfoC.setObjectName("CancelarInfoC")
        self.retranslateUi(VentanaCliente)
        self.CancelarInfoC.clicked.connect(VentanaCliente.close)
        QtCore.QMetaObject.connectSlotsByName(VentanaCliente)
        VentanaCliente.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(VentanaCliente)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 686, 21))
        self.menubar.setObjectName("menubar")
        VentanaCliente.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(VentanaCliente)
        self.statusbar.setObjectName("statusbar")
        VentanaCliente.setStatusBar(self.statusbar)

        self.retranslateUi(VentanaCliente)
        self.AceptarInfoC.clicked.connect(self.IngresoID_C.selectAll)
        self.AceptarInfoC.clicked.connect(self.IngresoNombre.selectAll)
        self.AceptarInfoC.clicked.connect(self.IngresoApellido.selectAll)
        self.AceptarInfoC.clicked.connect(self.IngrsoDireccion.selectAll)
        self.AceptarInfoC.clicked.connect(self.IngresoTelefono.selectAll)
        self.AceptarInfoC.clicked.connect(self.IngresoCiudad.selectAll)
        QtCore.QMetaObject.connectSlotsByName(VentanaCliente)

    def retranslateUi(self, VentanaCliente):
        _translate = QtCore.QCoreApplication.translate
        VentanaCliente.setWindowTitle(_translate("VentanaCliente", "MainWindow"))
        self.TxtNombre.setText(_translate("VentanaCliente", "Nombre"))
        self.TxtApellido.setText(_translate("VentanaCliente", "Apellido"))
        self.TxtID.setText(_translate("VentanaCliente", "No de identificacion"))
        self.TxtDireccion.setText(_translate("VentanaCliente", "Direccion"))
        self.TxtTelefono.setText(_translate("VentanaCliente", "Numero de telefono"))
        self.TxtCiudad.setText(_translate("VentanaCliente", "Ciudad"))
        self.AceptarInfoC.setText(_translate("VentanaCliente", "Aceptar"))
        self.CancelarInfoC.setText(_translate("VentanaCliente", "Cancelar"))
