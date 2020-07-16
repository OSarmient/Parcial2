from PyQt5 import QtWidgets
from MainWindow import Ui_MainWindow
from VentanaCliente import Ui_VentanaCliente
from VentanaVehiculo import Ui_VentanaVehiculos
from VentanaServicio import Ui_VentanaServicio
from VentanaFactura import Ui_VentanaFactura
from BorrarCliente import Ui_BorrarCliente
from BorrarVehiculo import Ui_BorrarVehiculo
from BorrarServicio import Ui_BorrarServicio
from ListarCliente import Ui_ListarCliente
from ListarVehiculos import Ui_ListarVehiculos
from ListarServicio import Ui_ListarServicio
from BuscarFactura import Ui_BuscarFactura
from PyQt5.uic import loadUi
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
        self.ui.CrearFactura.clicked.connect(self.crearF)

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

    def crearF(self):
        self.crear = QtWidgets.QMainWindow()
        self.ui = Ui_VentanaFactura()
        self.ui.setupUi(self.crear)
        self.crear.show()
    
    def Cancelar(self):
        self.close()
    

app = QtWidgets.QApplication([])
application = Window()
application.show()
sys.exit(app.exec())