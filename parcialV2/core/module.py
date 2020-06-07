from .database import Database
from .utils import clean_console


class ModuleBase:
    def __init__(self):
        self.database = Database(self.database_name)
        self.main_bucle = True
        self.options = []
        self.add_options()

    def add_options(self):

        self.default_options = [
            {
                "display": "Listar todos los datos",
                "function": self.get_all
            }, {
                "display": "Ver menú",
                "function": self.print_menu
            }, {
                "display": "Salir",
                "function": self.exit
            },
        ]

        for i in self.default_options:
            self.options.append(i)

        if len(self.menu_options) > 0:
            for i in self.menu_options:
                self.options.append(i)

    def print_data(self, data):
        for i in data:
            keys = i.keys()
            print()
            print("------------")
            for j in keys:
                print(str(j) + " : " + str(i[j]))
            print("------------")

    def get_all(self):
        clean_console()
        data = self.database.get_data_in_database()
        self.print_data(data)

    def save(self, data):
        self.database.save_in_database(data)

    def order_by(self, property):
        clean_console()
        data = self.database.get_orber_by_property(property)
        self.print_data(data)

    def delete(self, uid):
        self.database.delete_by_uid(uid)

    def clean(self):
        self.database.clean()

    def print_menu(self):
        clean_console()
        print()
        print("-- " + str(self.database_name) + " Menu --")
        print()
        for i in range(0, len(self.options)):
            print(str(i + 1) + ". " + self.options[i]["display"])
        print()

    def exit(self):
        self.main_bucle = False

    def start(self):
        self.print_menu()
        print()

        while self.main_bucle:
            print("Presiona S para salir en cualquier momento.")
            print("Presiona 2 para ver menú.")
            selected_option = str(input("Selecciona una opcion del menú: "))

            if(selected_option == "s" or selected_option == "S"):
                self.main_bucle = False

            if self.main_bucle == True:
                self.options[int(selected_option) - 1]["function"]()
                print()
