# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ListarServicio.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from service import Service


class Ui_ListarServicio(object):
    def setupUi(self, ListarServicio):
        ListarServicio.setObjectName("ListarServicio")
        ListarServicio.resize(604, 498)
        self.centralwidget = QtWidgets.QWidget(ListarServicio)
        self.centralwidget.setObjectName("centralwidget")
        self.direccion = QtWidgets.QPushButton(self.centralwidget)
        self.direccion.setGeometry(QtCore.QRect(490, 190, 101, 23))
        self.direccion.setObjectName("direccion")
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
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 10, 461, 401))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 459, 399))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.tableWidget = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 461, 401))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(100)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.retranslateUi(ListarServicio)
        self.CerrarLista.clicked.connect(ListarServicio.close)
        QtCore.QMetaObject.connectSlotsByName(ListarServicio)
        ListarServicio.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ListarServicio)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 604, 21))
        self.menubar.setObjectName("menubar")
        ListarServicio.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ListarServicio)
        self.statusbar.setObjectName("statusbar")
        ListarServicio.setStatusBar(self.statusbar)

        self.retranslateUi(ListarServicio)
        self.NoCodigo.clicked.connect(self.get_service)
        QtCore.QMetaObject.connectSlotsByName(ListarServicio)

    def retranslateUi(self, ListarServicio):
        _translate = QtCore.QCoreApplication.translate
        ListarServicio.setWindowTitle(_translate("ListarServicio", "MainWindow"))
        self.direccion.setText(_translate("ListarServicio", "Horas del servicio"))
        self.NoCodigo.setText(_translate("ListarServicio", "Codigo de servicio"))
        self.DatosCliente.setText(_translate("ListarServicio", "Ordenar Datos:"))
        self.Costo.setText(_translate("ListarServicio", "Costo por hora"))
        self.NombreServicio.setText(_translate("ListarServicio", "Nombre se servicio"))
        self.CerrarLista.setText(_translate("ListarServicio", "Cerrar"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("ListarServicio", "Código"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("ListarServicio", "Nombre"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("ListarServicio", "Costo"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("ListarServicio", "Tiempo (Horas)"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("ListarServicio", "Uid"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("ListarServicio", "Random"))

    def get_service(self, ListarServicio):
        service=Service()
        data =service.get_all()
        row = 0
        for i in data:
            col = 0
            keys = i.keys()
            for j in keys:
                item = QtWidgets.QTableWidgetItem(str(i[j]))
                self.tableWidget.setItem(row, col, item)
                col+=1
            row +=1
