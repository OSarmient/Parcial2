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

    def set_table_data(self, order = ""):
        if len(self.vehicles.get_all()) > 0:

            all_vehicles = []
            
            if order == "": all_vehicles = self.vehicles.get_all()
            else: all_vehicles = self.vehicles.get_ordered_by(order)

            validate_header = []

            for i in all_vehicles[0]:
                validate_header.append(i.title()) 

            if validate_header != self.table_header:
                self.table_header = validate_header
                self.uis["list"].tableWidget.setColumnCount(len(self.table_header))
                self.uis["list"].tableWidget.setHorizontalHeaderLabels(self.table_header)

            self.uis["list"].tableWidget.setRowCount(len(all_vehicles))

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

    def set_combox_box_data(self):
        combo_box_data = list(self.table_header)
        combo_box_data.insert(0, " - Ninguno - ")
        self.uis["list"].comboBox.addItems(combo_box_data)
        self.uis["list"].comboBox.currentIndexChanged.connect(self.order_data)

    def order_data(self):
        order_value_index = self.uis["list"].comboBox.currentIndex()
        order_value_text = self.uis["list"].comboBox.currentText()
        if order_value_index == 0: self.set_table_data()
        else: self.set_table_data(order_value_text.lower())

    def show_list(self):
        _translate = QtCore.QCoreApplication.translate

        self.set_table_data()
        self.set_combox_box_data()

        if self.vehicles.plural: self.uis["list"].label.setText(_translate("List", self.vehicles.plural))
        else: self.uis["list"].label.setText(_translate("List", self.vehicles.database_name))

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
        form_properties = self.vehicles.properties
        counter= 0

        complete_box_layout = QtWidgets.QVBoxLayout()

        for i in form_properties:
            input_group = QtWidgets.QGroupBox()
            input_group.setFixedHeight(55)
            input_group.setTitle(i["data"].title())
            layout = QtWidgets.QVBoxLayout()
            text_element = QtWidgets.QTextEdit()
            text_element.setObjectName(i["data"].title())
            text_element.setFixedHeight(20)
            layout.addWidget(text_element)
            input_group.setLayout(layout)
            complete_box_layout.addWidget(input_group)
            counter += 1 

        self.uis["create"].scrollArea.setLayout(complete_box_layout)
        self.windows["create"].show()   
