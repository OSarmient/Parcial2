# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ListarVehiculos.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ListarVehiculos(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(606, 541)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Combustible = QtWidgets.QPushButton(self.centralwidget)
        self.Combustible.setGeometry(QtCore.QRect(500, 300, 75, 23))
        self.Combustible.setObjectName("Combustible")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(500, 430, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.CerrarLista = QtWidgets.QPushButton(self.centralwidget)
        self.CerrarLista.setGeometry(QtCore.QRect(500, 470, 75, 23))
        self.CerrarLista.setObjectName("CerrarLista")
        self.Marca = QtWidgets.QPushButton(self.centralwidget)
        self.Marca.setGeometry(QtCore.QRect(500, 100, 75, 23))
        self.Marca.setObjectName("Marca")
        self.DatosVehiculo = QtWidgets.QLabel(self.centralwidget)
        self.DatosVehiculo.setGeometry(QtCore.QRect(500, 10, 111, 51))
        self.DatosVehiculo.setObjectName("DatosVehiculo")
        self.NoPlaca = QtWidgets.QPushButton(self.centralwidget)
        self.NoPlaca.setGeometry(QtCore.QRect(500, 60, 75, 23))
        self.NoPlaca.setObjectName("NoPlaca")
        self.Chasis = QtWidgets.QPushButton(self.centralwidget)
        self.Chasis.setGeometry(QtCore.QRect(500, 380, 75, 23))
        self.Chasis.setObjectName("Chasis")
        self.TipoServicio = QtWidgets.QPushButton(self.centralwidget)
        self.TipoServicio.setGeometry(QtCore.QRect(500, 260, 81, 23))
        self.TipoServicio.setObjectName("TipoServicio")
        self.Pasajeros = QtWidgets.QPushButton(self.centralwidget)
        self.Pasajeros.setGeometry(QtCore.QRect(500, 340, 75, 23))
        self.Pasajeros.setObjectName("Pasajeros")
        self.Cilindraje = QtWidgets.QPushButton(self.centralwidget)
        self.Cilindraje.setGeometry(QtCore.QRect(500, 180, 75, 23))
        self.Cilindraje.setObjectName("Cilindraje")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 0, 461, 401))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 459, 399))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.TablaListaVehiculo = QtWidgets.QTableView(self.scrollAreaWidgetContents)
        self.TablaListaVehiculo.setGeometry(QtCore.QRect(0, 0, 461, 401))
        self.TablaListaVehiculo.setObjectName("TablaListaVehiculo")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.Modelo = QtWidgets.QPushButton(self.centralwidget)
        self.Modelo.setGeometry(QtCore.QRect(500, 140, 75, 23))
        self.Modelo.setObjectName("Modelo")
        self.Color = QtWidgets.QPushButton(self.centralwidget)
        self.Color.setGeometry(QtCore.QRect(500, 220, 75, 23))
        self.Color.setObjectName("Color")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 606, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Combustible.setText(_translate("MainWindow", "Combustible"))
        self.pushButton_4.setText(_translate("MainWindow", "Motor"))
        self.CerrarLista.setText(_translate("MainWindow", "Cerrar"))
        self.Marca.setText(_translate("MainWindow", "Marca"))
        self.DatosVehiculo.setText(_translate("MainWindow", "Ordenar Datos:"))
        self.NoPlaca.setText(_translate("MainWindow", "No de Placa"))
        self.Chasis.setText(_translate("MainWindow", "Chasis"))
        self.TipoServicio.setText(_translate("MainWindow", "Tipo de servicio"))
        self.Pasajeros.setText(_translate("MainWindow", "Pasajeros"))
        self.Cilindraje.setText(_translate("MainWindow", "Cilindraje"))
        self.Modelo.setText(_translate("MainWindow", "Modelo"))
        self.Color.setText(_translate("MainWindow", "Color"))
