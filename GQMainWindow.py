from PyQt5 import QtWidgets
from MainWindow import Ui_MainWindow
from VentanaCliente import Ui_VentanaCliente
from VentanaVehiculo import *
from VentanaServicio import *
from BorrarCliente import Ui_BorrarCliente
from BorrarVehiculo import *
from BorrarServicio import *
from ListarCliente import Ui_ListarCliente
from ListarVehiculos import *
from ListarServicio import *
from BuscarFactura import Ui_BuscarFactura
import sys

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.BotonCrearC.clicked.connect(self.abrirCreacionC)
        self.ui.BotonBorrarC.clicked.connect(self.abrirBorrarC)
        self.ui.BotonListarC.clicked.connect(self.abrirListaC)
        self.ui.BotonCrearV.clicked.connect(self.abrirCreacionV)
        self.ui.BotonBorrarV.clicked.connect(self.abrirBorrarV)
        self.ui.BotonListarV.clicked.connect(self.abrirListaV)
        self.ui.BotonCrearS.clicked.connect(self.abrirCreacionS)
        self.ui.BotonBorrarS.clicked.connect(self.abrirBorrarS)
        self.ui.BotonListarS.clicked.connect(self.abrirListaS)
        self.ui.BuscarFactura.clicked.connect(self.buscarFactura)

    def abrirCreacionC(self):
        self.crear = QtWidgets.QMainWindow()
        self.ui = Ui_VentanaCliente()
        self.ui.setupUi(self.crear)
        self.crear.show()
    
    def abrirBorrarC(self):
        self.crear = QtWidgets.QMainWindow()
        self.ui = Ui_BorrarCliente()
        self.ui.setupUi(self.crear)
        self.crear.show()

    def abrirListaC(self):
        self.crear = QtWidgets.QMainWindow()
        self.ui = Ui_ListarCliente()
        self.ui.setupUi(self.crear)
        self.crear.show()

    def abrirCreacionV(self):
        self.crear = QtWidgets.QMainWindow()
        self.ui = Ui_VentanaVehiculos()
        self.ui.setupUi(self.crear)
        self.crear.show()
    
    def abrirBorrarV(self):
        self.crear = QtWidgets.QMainWindow()
        self.ui = Ui_BorrarVehiculo()
        self.ui.setupUi(self.crear)
        self.crear.show()

    def abrirListaV(self):
        self.crear = QtWidgets.QMainWindow()
        self.ui = Ui_ListarVehiculos()
        self.ui.setupUi(self.crear)
        self.crear.show()
    def abrirCreacionS(self):
        self.crear = QtWidgets.QMainWindow()
        self.ui = Ui_VentanaServicio()
        self.ui.setupUi(self.crear)
        self.crear.show()
    
    def abrirBorrarS(self):
        self.crear = QtWidgets.QMainWindow()
        self.ui = Ui_BorrarServicio()
        self.ui.setupUi(self.crear)
        self.crear.show()

    def abrirListaS(self):
        self.crear = QtWidgets.QMainWindow()
        self.ui = Ui_ListarServicio()
        self.ui.setupUi(self.crear)
        self.crear.show()

    def buscarFactura(self):
        self.crear = QtWidgets.QMainWindow()
        self.ui = Ui_BuscarFactura()
        self.ui.setupUi(self.crear)
        self.crear.show()


app = QtWidgets.QApplication([])
application = Window()
application.show()
sys.exit(app.exec())