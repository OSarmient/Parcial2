# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ListarServicio.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ListarServicio(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(604, 498)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.direccion = QtWidgets.QPushButton(self.centralwidget)
        self.direccion.setGeometry(QtCore.QRect(490, 190, 101, 23))
        self.direccion.setObjectName("direccion")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 10, 461, 401))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 459, 399))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.TablaListaServicios = QtWidgets.QTableView(self.scrollAreaWidgetContents)
        self.TablaListaServicios.setGeometry(QtCore.QRect(0, 0, 461, 401))
        self.TablaListaServicios.setObjectName("TablaListaServicios")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.NoCodigo = QtWidgets.QPushButton(self.centralwidget)
        self.NoCodigo.setGeometry(QtCore.QRect(490, 70, 101, 23))
        self.NoCodigo.setObjectName("NoCodigo")
        self.DatosCliente = QtWidgets.QLabel(self.centralwidget)
        self.DatosCliente.setGeometry(QtCore.QRect(500, 20, 111, 51))
        self.DatosCliente.setObjectName("DatosCliente")
        self.Costo = QtWidgets.QPushButton(self.centralwidget)
        self.Costo.setGeometry(QtCore.QRect(490, 150, 101, 23))
        self.Costo.setObjectName("Costo")
        self.NombreServicio = QtWidgets.QPushButton(self.centralwidget)
        self.NombreServicio.setGeometry(QtCore.QRect(490, 110, 101, 23))
        self.NombreServicio.setObjectName("NombreServicio")
        self.CerrarLista = QtWidgets.QPushButton(self.centralwidget)
        self.CerrarLista.setGeometry(QtCore.QRect(500, 440, 75, 23))
        self.CerrarLista.setObjectName("CerrarLista")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 604, 21))
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
        self.direccion.setText(_translate("MainWindow", "Horas del servicio"))
        self.NoCodigo.setText(_translate("MainWindow", "Codigo de servicio"))
        self.DatosCliente.setText(_translate("MainWindow", "Ordenar Datos:"))
        self.Costo.setText(_translate("MainWindow", "Costo por hora"))
        self.NombreServicio.setText(_translate("MainWindow", "Nombre se servicio"))
        self.CerrarLista.setText(_translate("MainWindow", "Cerrar"))
