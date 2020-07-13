# -*- coding: utf-8 -*-

# ListarVehiculos implementation generated from reading ui file 'ListarVehiculos.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ListarVehiculos(object):
    def setupUi(self, ListarVehiculos):
        ListarVehiculos.setObjectName("ListarVehiculos")
        ListarVehiculos.resize(606, 496)
        self.Cilindraje = QtWidgets.QPushButton(ListarVehiculos)
        self.Cilindraje.setGeometry(QtCore.QRect(500, 190, 75, 23))
        self.Cilindraje.setObjectName("Cilindraje")
        self.Marca = QtWidgets.QPushButton(ListarVehiculos)
        self.Marca.setGeometry(QtCore.QRect(500, 110, 75, 23))
        self.Marca.setObjectName("Marca")
        self.Modelo = QtWidgets.QPushButton(ListarVehiculos)
        self.Modelo.setGeometry(QtCore.QRect(500, 150, 75, 23))
        self.Modelo.setObjectName("Modelo")
        self.scrollArea = QtWidgets.QScrollArea(ListarVehiculos)
        self.scrollArea.setGeometry(QtCore.QRect(10, 10, 461, 401))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 459, 399))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.TablaListaVehiculo = QtWidgets.QTableView(self.scrollAreaWidgetContents)
        self.TablaListaVehiculo.setGeometry(QtCore.QRect(0, 0, 461, 401))
        self.TablaListaVehiculo.setObjectName("TablaListaVehiculo")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.NoPlaca = QtWidgets.QPushButton(ListarVehiculos)
        self.NoPlaca.setGeometry(QtCore.QRect(500, 70, 75, 23))
        self.NoPlaca.setObjectName("NoPlaca")
        self.Color = QtWidgets.QPushButton(ListarVehiculos)
        self.Color.setGeometry(QtCore.QRect(500, 230, 75, 23))
        self.Color.setObjectName("Color")
        self.CerrarLista = QtWidgets.QPushButton(ListarVehiculos)
        self.CerrarLista.setGeometry(QtCore.QRect(500, 460, 75, 23))
        self.CerrarLista.setObjectName("CerrarLista")
        self.TipoServicio = QtWidgets.QPushButton(ListarVehiculos)
        self.TipoServicio.setGeometry(QtCore.QRect(500, 270, 81, 23))
        self.TipoServicio.setObjectName("TipoServicio")
        self.DatosVehiculo = QtWidgets.QLabel(ListarVehiculos)
        self.DatosVehiculo.setGeometry(QtCore.QRect(500, 20, 111, 51))
        self.DatosVehiculo.setObjectName("DatosVehiculo")
        self.Combustible = QtWidgets.QPushButton(ListarVehiculos)
        self.Combustible.setGeometry(QtCore.QRect(500, 310, 75, 23))
        self.Combustible.setObjectName("Combustible")
        self.Pasajeros = QtWidgets.QPushButton(ListarVehiculos)
        self.Pasajeros.setGeometry(QtCore.QRect(500, 350, 75, 23))
        self.Pasajeros.setObjectName("Pasajeros")
        self.Chasis = QtWidgets.QPushButton(ListarVehiculos)
        self.Chasis.setGeometry(QtCore.QRect(500, 390, 75, 23))
        self.Chasis.setObjectName("Chasis")
        self.pushButton_4 = QtWidgets.QPushButton(ListarVehiculos)
        self.pushButton_4.setGeometry(QtCore.QRect(500, 430, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")

        self.retranslateUi(ListarVehiculos)
        QtCore.QMetaObject.connectSlotsByName(ListarVehiculos)

    def retranslateUi(self, ListarVehiculos):
        _translate = QtCore.QCoreApplication.translate
        ListarVehiculos.setWindowTitle(_translate("ListarVehiculos", "ListarVehiculos"))
        self.Cilindraje.setText(_translate("ListarVehiculos", "Cilindraje"))
        self.Marca.setText(_translate("ListarVehiculos", "Marca"))
        self.Modelo.setText(_translate("ListarVehiculos", "Modelo"))
        self.NoPlaca.setText(_translate("ListarVehiculos", "No de Placa"))
        self.Color.setText(_translate("ListarVehiculos", "Color"))
        self.CerrarLista.setText(_translate("ListarVehiculos", "Cerrar"))
        self.TipoServicio.setText(_translate("ListarVehiculos", "Tipo de servicio"))
        self.DatosVehiculo.setText(_translate("ListarVehiculos", "Ordenar Datos:"))
        self.Combustible.setText(_translate("ListarVehiculos", "Combustible"))
        self.Pasajeros.setText(_translate("ListarVehiculos", "Pasajeros"))
        self.Chasis.setText(_translate("ListarVehiculos", "Chasis"))
        self.pushButton_4.setText(_translate("ListarVehiculos", "Motor"))
