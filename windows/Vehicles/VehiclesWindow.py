from PyQt5 import QtWidgets

from parcialV2.vehicles import Vehicles
from windows.Vehicles.BorrarVehiculo import Ui_BorrarVehiculo
from windows.Vehicles.VentanaVehiculo import Ui_VentanaVehiculos
from windows.Vehicles.ListarVehiculos import Ui_ListarVehiculos

class VehiclesWindow:
    def __init__(self, ui):
        self.ui = ui
        self.vehicles = Vehicles()

        self.uis = {
            "list": Ui_ListarVehiculos(),
            "delete": Ui_BorrarVehiculo(),
            "create": Ui_VentanaVehiculos(),
        }

        self.table_header = []

        self.windows = {}
        self.create_windows()

        ui.BotonCrearV.clicked.connect(self.show_list)
        ui.BotonBorrarV.clicked.connect(self.show_list)
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
