# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ListarCliente.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ListarCliente(object):
    def setupUi(self, ListarCliente):
        ListarCliente.setObjectName("ListarCliente")
        ListarCliente.resize(677, 496)
        self.centralwidget = QtWidgets.QWidget(ListarCliente)
        self.centralwidget.setObjectName("centralwidget")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 0, 461, 401))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 459, 399))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.TablaListaCliente = QtWidgets.QTableView(self.scrollAreaWidgetContents)
        self.TablaListaCliente.setGeometry(QtCore.QRect(0, 0, 461, 401))
        self.TablaListaCliente.setObjectName("TablaListaCliente")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.DatosCliente = QtWidgets.QLabel(self.centralwidget)
        self.DatosCliente.setGeometry(QtCore.QRect(500, 10, 111, 51))
        self.DatosCliente.setObjectName("DatosCliente")
        self.No_ID = QtWidgets.QPushButton(self.centralwidget)
        self.No_ID.setGeometry(QtCore.QRect(500, 60, 75, 23))
        self.No_ID.setObjectName("No_ID")
        self.Nombre = QtWidgets.QPushButton(self.centralwidget)
        self.Nombre.setGeometry(QtCore.QRect(500, 100, 75, 23))
        self.Nombre.setObjectName("Nombre")
        self.Apellido = QtWidgets.QPushButton(self.centralwidget)
        self.Apellido.setGeometry(QtCore.QRect(500, 140, 75, 23))
        self.Apellido.setObjectName("Apellido")
        self.direccion = QtWidgets.QPushButton(self.centralwidget)
        self.direccion.setGeometry(QtCore.QRect(500, 180, 75, 23))
        self.direccion.setObjectName("direccion")
        self.Telefono = QtWidgets.QPushButton(self.centralwidget)
        self.Telefono.setGeometry(QtCore.QRect(500, 220, 75, 23))
        self.Telefono.setObjectName("Telefono")
        self.Ciudad = QtWidgets.QPushButton(self.centralwidget)
        self.Ciudad.setGeometry(QtCore.QRect(500, 260, 75, 23))
        self.Ciudad.setObjectName("Ciudad")
        self.CerrarLista = QtWidgets.QPushButton(self.centralwidget)
        self.CerrarLista.setGeometry(QtCore.QRect(580, 410, 75, 23))
        self.CerrarLista.setObjectName("CerrarLista")
        ListarCliente.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ListarCliente)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 677, 21))
        self.menubar.setObjectName("menubar")
        ListarCliente.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ListarCliente)
        self.statusbar.setObjectName("statusbar")
        ListarCliente.setStatusBar(self.statusbar)

        self.retranslateUi(ListarCliente)
        QtCore.QMetaObject.connectSlotsByName(ListarCliente)

    def retranslateUi(self, ListarCliente):
        _translate = QtCore.QCoreApplication.translate
        ListarCliente.setWindowTitle(_translate("ListarCliente", "MainWindow"))
        self.DatosCliente.setText(_translate("ListarCliente", "Ordenar Datos:"))
        self.No_ID.setText(_translate("ListarCliente", "No de ID"))
        self.Nombre.setText(_translate("ListarCliente", "Nombre"))
        self.Apellido.setText(_translate("ListarCliente", "Apellido"))
        self.direccion.setText(_translate("ListarCliente", "Direnccion"))
        self.Telefono.setText(_translate("ListarCliente", "Telefono"))
        self.Ciudad.setText(_translate("ListarCliente", "Ciudad"))
        self.CerrarLista.setText(_translate("ListarCliente", "Cerrar"))
