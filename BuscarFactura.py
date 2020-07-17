# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BuscarFactura.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_BuscarF(object):
    def setupUi(self, BuscarFactura):
        BuscarFactura.setObjectName("BuscarFactura")
        BuscarFactura.resize(670, 309)
        self.centralwidget = QtWidgets.QWidget(BuscarFactura)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 140, 631, 121))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.IngresarNo = QtWidgets.QTextEdit(self.centralwidget)
        self.IngresarNo.setGeometry(QtCore.QRect(20, 80, 381, 21))
        self.IngresarNo.setObjectName("IngresarNo")
        self.NoFactura = QtWidgets.QLabel(self.centralwidget)
        self.NoFactura.setGeometry(QtCore.QRect(30, 50, 111, 16))
        self.NoFactura.setObjectName("NoFactura")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(510, 20, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.BuscarB = QtWidgets.QPushButton(self.centralwidget)
        self.BuscarB.setGeometry(QtCore.QRect(510, 70, 75, 23))
        self.BuscarB.setObjectName("BuscarB")
        BuscarFactura.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(BuscarFactura)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 670, 21))
        self.menubar.setObjectName("menubar")
        BuscarFactura.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(BuscarFactura)
        self.statusbar.setObjectName("statusbar")
        BuscarFactura.setStatusBar(self.statusbar)

        self.retranslateUi(BuscarFactura)
        QtCore.QMetaObject.connectSlotsByName(BuscarFactura)

    def retranslateUi(self, BuscarFactura):
        _translate = QtCore.QCoreApplication.translate
        BuscarFactura.setWindowTitle(_translate("BuscarFactura", "BuscarFactura"))
        self.NoFactura.setText(_translate("BuscarFactura", "No. de factura"))
        self.pushButton.setText(_translate("BuscarFactura", "Buscar"))
        self.BuscarB.setText(_translate("BuscarFactura", "Cancelar"))
