from Modules.core.module import ModuleBase


class Clients(ModuleBase):
    def __init__(self):
        self.database_name = "clients"
        self.singularity = "cliente"
        self.plural = "clientes"
        self.singular = "El cliente"
        self.flush_singular = "un cliente"
        self.menu_options = []
        self.main_field = "noid"
        self.properties = [
            {
                "data": "noid",
                "display": "Digite el número de identificación del cliente",
                "value": "",
                "type": "int",
                "ajust": "12"
            },
            {
                "data": "nombre",
                "display": "Digite el nombre del cliente",
                "value": "",
                "type": "string",
                "ajust": "15"
            },
            {
                "data": "apellido",
                "display": "Digite el apellido del cliente",
                "value": "",
                "type": "string",
                "ajust": "15"
            },
            {
                "data": "direccion",
                "display": "Digite la dirección del cliente",
                "value": "",
                "type": "string",
                "ajust": "30"
            },
            {
                "data": "telefono",
                "display": "Digite el número de telefono del cliente",
                "value": "",
                "type": "int",
                "ajust": "30"
            },
            {
                "data": "ciudad",
                "display": "Digite la ciudad del cliente",
                "value": "",
                "type": "string",
                "ajust": "20"
            },
        ]

        super().__init__()


#clients = Clients()
#clients.start()
