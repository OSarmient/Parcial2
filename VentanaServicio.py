# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VentanaServicio.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_VentanaServicio(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(468, 361)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
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
        self.textEdit_7 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_7.setGeometry(QtCore.QRect(20, 100, 351, 31))
        self.textEdit_7.setObjectName("textEdit_7")
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
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 468, 21))
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
        self.CostoXHora.setText(_translate("MainWindow", "Costo por hora del servicio"))
        self.Horas.setText(_translate("MainWindow", "Horas del servicio"))
        self.CodigoServicio.setText(_translate("MainWindow", "Codigo del Servicio"))
        self.CancelarInfoS.setText(_translate("MainWindow", "Cancelar"))
        self.NombreServicio.setText(_translate("MainWindow", "Nombre del servicio"))
        self.AceptarInfoS.setText(_translate("MainWindow", "Aceptar"))
