from core.module import ModuleBase


class Vehicles(ModuleBase):
    def __init__(self):
        self.database_name = "vehicles"
        self.menu_options = [
            {
                "display": "Borrar",
                "function": self.get_all
            }
        ]

        super().__init__()


vehicles = Vehicles()
vehicles.start()
