from core.module import ModuleBase


class Vehicles(ModuleBase):
    def __init__(self):
        self.database_name = "vehicles"
        super().__init__()


vehicles = Vehicles()