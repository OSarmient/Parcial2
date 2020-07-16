from core.module import ModuleBase
from bills import Facturas


class Service(ModuleBase):
    def __init__(self):
        self.database_name = "service"
        self.singularity = "servicio"
        self.singular = "El servicio"
        self.flush_singular = "un servicio"
        self.menu_options = [{
            "display": "Solicitar un servicio",
            "function": Facturas().relation
        }]
        self.main_field = "numero"
        self.properties = [
            {
                "data": "numero",
                "display": "Escriba el codigo que el servicio que deaea: ",
                "value": "",
                "type": "int",
                "ajust": "6"
            },

            {
                "data": "nombre",
                "display": "Escriba el nombre de el servicio que desea: ",
                "value": "",
                "type": "str",
                "ajust": "25"
            },

            {
                "data": "precio",
                "display": "Escriba cuanto cuaesta el servicio por hora: ",
                "value": "",
                "type": "int",
                "ajust": "7"
            },

            {
                "data": "horas",
                "display": "Escriba por cuantas horas quire contratar el servicio: ",
                "value": "",
                "type": "int",
                "ajust": "2"
            }
        ]

        super().__init__()
    
#service = Service()
#service.start()
