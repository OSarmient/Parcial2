# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BorrarServicio.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_BorrarServicio(object):
    def setupUi(self, BorrarServicio):
        BorrarServicio.setObjectName("BorrarServicio")
        BorrarServicio.resize(434, 188)
        self.centralwidget = QtWidgets.QWidget(BorrarServicio)
        self.centralwidget.setObjectName("centralwidget")
        self.IngresoCodigo_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.IngresoCodigo_2.setGeometry(QtCore.QRect(30, 60, 351, 31))
        self.IngresoCodigo_2.setObjectName("IngresoCodigo_2")
        self.CancelarBorrarS_2 = QtWidgets.QPushButton(self.centralwidget)
        self.CancelarBorrarS_2.setGeometry(QtCore.QRect(310, 110, 75, 23))
        self.CancelarBorrarS_2.setObjectName("CancelarBorrarS_2")
        self.ConfirmarBorrarS_2 = QtWidgets.QPushButton(self.centralwidget)
        self.ConfirmarBorrarS_2.setGeometry(QtCore.QRect(220, 110, 75, 23))
        self.ConfirmarBorrarS_2.setObjectName("ConfirmarBorrarS_2")
        self.TxtID_2 = QtWidgets.QLabel(self.centralwidget)
        self.TxtID_2.setGeometry(QtCore.QRect(30, 20, 121, 31))
        self.TxtID_2.setObjectName("TxtID_2")
        self.retranslateUi(BorrarServicio)
        self.CancelarBorrarS_2.clicked.connect(BorrarServicio.close)
        QtCore.QMetaObject.connectSlotsByName(BorrarServicio)
        BorrarServicio.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(BorrarServicio)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 434, 21))
        self.menubar.setObjectName("menubar")
        BorrarServicio.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(BorrarServicio)
        self.statusbar.setObjectName("statusbar")
        BorrarServicio.setStatusBar(self.statusbar)

        self.retranslateUi(BorrarServicio)
        QtCore.QMetaObject.connectSlotsByName(BorrarServicio)

    def retranslateUi(self, BorrarServicio):
        _translate = QtCore.QCoreApplication.translate
        BorrarServicio.setWindowTitle(_translate("BorrarServicio", "BorrarServicio"))
        self.CancelarBorrarS_2.setText(_translate("BorrarServicio", "Cancelar"))
        self.ConfirmarBorrarS_2.setText(_translate("BorrarServicio", "Borrar"))
        self.TxtID_2.setText(_translate("BorrarServicio", "No. de identificacion"))
