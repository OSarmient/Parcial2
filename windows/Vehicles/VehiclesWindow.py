from PyQt5 import QtWidgets, QtCore

from Modules.vehicles import Vehicles
from windows.Base.Delete import Ui_Delete
from windows.Base.Create import Ui_Create
from windows.Base.List import Ui_List

class VehiclesWindow:
    def __init__(self, ui):
        self.ui = ui
        self.vehicles = Vehicles()

        self.uis = {
            "list": Ui_List(),
            "delete": Ui_Delete(),
            "create": Ui_Create(),
        }

        self.delete_props = {
            "title": "Eliminar " + self.vehicles.singularity,
            "prop": "Digite el numero de la placa",
        }

        self.table_header = []

        self.windows = {}
        self.create_windows()

        ui.BotonCrearV.clicked.connect(self.show_create)
        ui.BotonBorrarV.clicked.connect(self.show_delete)
        ui.BotonListarV.clicked.connect(self.show_list)

    def set_table_data(self):
        if len(self.vehicles.get_all()) > 0:

            all_vehicles = self.vehicles.get_all()

            ## set header

            for i in all_vehicles[0]:
                self.table_header.append(i.title())

            self.uis["list"].tableWidget.setColumnCount(len(self.table_header))
            self.uis["list"].tableWidget.setHorizontalHeaderLabels(self.table_header)
            self.uis["list"].tableWidget.setRowCount(len(all_vehicles))

            ## set and format data
            
            for i in range(0, len(all_vehicles)):
                for j in range(0, len(self.table_header)):
                    data = QtWidgets.QTableWidgetItem(str(all_vehicles[i][self.table_header[j].lower()]))
                    self.uis["list"].tableWidget.setItem(i, j, data)

            self.uis["list"].tableWidget.resizeColumnsToContents()
            self.uis["list"].tableWidget.resizeRowsToContents()

    def create_windows(self):
        for key in self.uis:
            self.windows[key] = QtWidgets.QMainWindow()
            self.uis[key].setupUi(self.windows[key])

    def show_list(self):
        self.set_table_data()
        self.windows["list"].show()

    def show_delete(self):
        _translate = QtCore.QCoreApplication.translate
        self.uis["delete"].Title.setText(_translate("Delete", self.delete_props["title"] ))
        self.uis["delete"].TxtID.setText(_translate("Delete", self.delete_props["prop"]))
        self.uis["delete"].ConfirmarBorrarV.clicked.connect(self.delete)
        self.uis["delete"].CancelarBorrarV.clicked.connect(self.close_delete)
        self.windows["delete"].show()

    def delete(self):
        delete = self.vehicles.delete(self.uis["delete"].UniqueProp.toPlainText(), "placa")

        if delete == False: print("No existe u vehiculo con esta placa")
        else: print("Vehiculo eliminado")   
    
    def close_delete(self):
        self.windows["delete"].close()

    def show_create(self):
        self.windows["create"].show()   
