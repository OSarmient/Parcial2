# -*- coding: utf-8 -*-

# ListarServicio implementation generated from reading ui file 'ListarServicio.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ListarServicio(object):
    def setupUi(self, ListarServicio):
        ListarServicio.setObjectName("ListarServicio")
        ListarServicio.resize(605, 498)
        self.direccion = QtWidgets.QPushButton(ListarServicio)
        self.direccion.setGeometry(QtCore.QRect(490, 190, 101, 23))
        self.direccion.setObjectName("direccion")
        self.NombreServicio = QtWidgets.QPushButton(ListarServicio)
        self.NombreServicio.setGeometry(QtCore.QRect(490, 110, 101, 23))
        self.NombreServicio.setObjectName("NombreServicio")
        self.Costo = QtWidgets.QPushButton(ListarServicio)
        self.Costo.setGeometry(QtCore.QRect(490, 150, 101, 23))
        self.Costo.setObjectName("Costo")
        self.scrollArea = QtWidgets.QScrollArea(ListarServicio)
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
        self.NoCodigo = QtWidgets.QPushButton(ListarServicio)
        self.NoCodigo.setGeometry(QtCore.QRect(490, 70, 101, 23))
        self.NoCodigo.setObjectName("NoCodigo")
        self.CerrarLista = QtWidgets.QPushButton(ListarServicio)
        self.CerrarLista.setGeometry(QtCore.QRect(500, 440, 75, 23))
        self.CerrarLista.setObjectName("CerrarLista")
        self.DatosCliente = QtWidgets.QLabel(ListarServicio)
        self.DatosCliente.setGeometry(QtCore.QRect(500, 20, 111, 51))
        self.DatosCliente.setObjectName("DatosCliente")

        self.retranslateUi(ListarServicio)
        QtCore.QMetaObject.connectSlotsByName(ListarServicio)

    def retranslateUi(self, ListarServicio):
        _translate = QtCore.QCoreApplication.translate
        ListarServicio.setWindowTitle(_translate("ListarServicio", "ListarServicio"))
        self.direccion.setText(_translate("ListarServicio", "Horas del servicio"))
        self.NombreServicio.setText(_translate("ListarServicio", "Nombre se servicio"))
        self.Costo.setText(_translate("ListarServicio", "Costo por hora"))
        self.NoCodigo.setText(_translate("ListarServicio", "Codigo de servicio"))
        self.CerrarLista.setText(_translate("ListarServicio", "Cerrar"))
        self.DatosCliente.setText(_translate("ListarServicio", "Ordenar Datos:"))
