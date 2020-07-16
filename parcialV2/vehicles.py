from .core. module import ModuleBase


class Vehicles(ModuleBase):
    def __init__(self):
        self.database_name = "vehicles"
        self.singularity = "vehiculo"
        self.singular = "El vehiculo"
        self.flush_singular = "un vehiculo"
        self.menu_options = [{
            "display": "Custom menu action",
            "function": self.exit
        }]
        self.main_field = "placa"
        self.properties = [
            {
                "data": "placa",
                "display": "Digite el numero de la placa",
                "value": "",
                "type": "string",
                "ajust": "6"
            },
            {
                "data": "marca",
                "display": "Digite el nombre de la marca",
                "value": "",
                "type": "string",
                "ajust": "15"
            },
            {
                "data": "modelo",
                "display": "Digite el modelo del automovil",
                "value": "",
                "type": "string",
                "ajust": "15"
            },
            {
                "data": "cilindrada",
                "display": "Digite la cilindrada",
                "value": "",
                "type": "int",
                "ajust": "6"
            },
            {
                "data": "color",
                "display": "Digite el color",
                "value": "",
                "type": "string",
                "ajust": "10"
            },
            {
                "data": "tipo",
                "display": "Digite el tipo de automovil (servicio)",
                "value": "",
                "type": "string",
                "ajust": "30"
            },
            {
                "data": "combustible",
                "display": "Digite el tipo de combustible",
                "value": "",
                "type": "string",
                "ajust": "12"
            },
            {
                "data": "pasajeros",
                "display": "Digite el numero de pasajeros",
                "value": "",
                "type": "int",
                "ajust": "2"
            },
            {
                "data": "chasis",
                "display": "Digite el numero de chasis",
                "value": "",
                "type": "int",
                "ajust": "3"
            },
            {
                "data": "motor",
                "display": "Digite el numero de motor",
                "value": "",
                "type": "int",
                "ajust": "3"
            }
        ]

        super().__init__()


#vehicles = Vehicles()
#vehicles.start()
