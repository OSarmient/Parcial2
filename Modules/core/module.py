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
                "display": "Ordenar todos los datos",
                "function": self.order_by
            }, {
                "display": "Crear " + self.flush_singular,
                "function": self.insert
            }, {
                "display": "Borrar " + self.singularity,
                "function": self.delete_by_uid
            }, {
                "display": "Ver menú",
                "function": self.print_menu
            }, {
                "display": "Salir",
                "function": self.exit
            }
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
        return self.database.get_data_in_database()

    def save(self, data):
        self.database.save_in_database(data)

    def order_by(self):
        order_bucle = True

        while order_bucle:
            print("Digita s para salir en cualquier momento.")
            selected_property = input("Digita la propiedad: ")

            if(selected_property != "s" and selected_property != "S"):
                if selected_property and self.database.validate_prop(selected_property):
                    clean_console()
                    data = self.database.get_orber_by_property(
                        selected_property)
                    self.print_data(data)
                    print()
                else:
                    clean_console()
                    print()
                    print("La propiedad " +
                          str(selected_property) + " no es valida.")
                    print("Selecciona alguna de estas")
                    print()
                    self.database.list_properties()
                    print()
            else:
                order_bucle = False

    def delete(self, dato, property = "uid"):
       return self.database.delete_by_property(property, dato)
        
    def delete_by_uid(self):
        delete_bucle = True

        while delete_bucle:
            print("Digita s para salir en cualquier momento.")
            target_input = input("Digita el identificador unico: ")

            if target_input != "s" and target_input != "S":
                try:
                    target_int = int(target_input)
                    target = self.database.get_by_uid(target_int)
                    clean_console()
                    if target:
                        self.database.delete_by_uid(target_int)
                    else:
                        print(self.singular + " no existe.")
                        print()
                except NameError:
                    print("El indetificador unico no es valido")
            else:
                delete_bucle = False

    def clean(self):
        self.database.clean()

    def print_menu(self):
        print()
        print("-- " + str(self.database_name) + " Menu --")
        print()
        for i in range(0, len(self.options)):
            print(str(i + 1) + ". " + self.options[i]["display"])
        print()

    def validate_prop(self, prop):
        error = False

        if prop["value"] == "":
            print("El valor de " + prop["data"] + " no puede ser nulo")
            error = True

        if prop["type"] == "int" and type(prop["value"]) == prop["type"]:
            print("El valor de " + prop["data"] + " es invalido")
            error = True
        if prop["type"] == "string" and type(prop["value"]) == prop["type"]:
            error = True
            print("El valor de " + prop["data"] + " es invalido")

        if "ajust" in prop and int(prop["ajust"]) < len(prop["value"]):
            print(
                "Superaste el limite de caracteres (Limite: " + prop["ajust"] + ")")
            error = True

        return error
    
    def insert2(self, dato):
        data = {}
        for i in range(len(dato)):
            self.properties[i]["value"] = dato[i]
            data[self.properties[i]["data"]] = self.properties[i]["value"]
        self.save(data)
        
    def insert(self):
        data = {}

        for i in self.properties:
            bucle = True
            while bucle:
                i["value"] = input(i["display"] + ": ")

                if self.validate_prop(i) == False:
                    if i["data"] == self.main_field:
                        if self.database.get_by_property(self.main_field, i["value"]) == False:
                            if i["type"] == "int":
                                data[i["data"]] = int(i["value"])
                            else:
                                data[i["data"]] = i["value"]
                            bucle = False
                        else:
                            print()
                            print("Ya existe "+self.flush_singular +
                                  " con la siguiente propiedad: " + self.main_field)
                            print()
                    else:
                        if i["type"] == "int":
                            data[i["data"]] = int(i["value"])
                        else:
                            data[i["data"]] = i["value"]
                        bucle = False
        self.save(data)
        print("Guardado en la base de datos")

    def exit(self):
        self.main_bucle = False

    def start(self):
        self.print_menu()
        print()

        while self.main_bucle:
            print("Presiona S para salir en cualquier momento.")
            print("Presiona 5 para ver menú.")
            selected_option = str(input("Selecciona una opcion del menú: "))

            if(selected_option == "s" or selected_option == "S"):
                self.main_bucle = False

            if self.main_bucle == True:
                self.options[int(selected_option) - 1]["function"]()
                print()
