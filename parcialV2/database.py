import os
import ast
import random


class Database:

    def __init__(self, database_name):
        self.__database_folder = "databases"
        self.__database_name = database_name
        self.__database_mode = "pro"
        self.__database_path = self.__database_folder + \
            "/" + self.__database_name + ".txt"

        self.__create_database()

    def __create_database(self):
        isFile = os.path.isfile(self.__database_path)

        # Validate database folder
        if os.path.isdir(self.__database_folder) == False:
            os.mkdir("databases")

        # Crete database file
        if isFile == False:
            open(self.__database_path, "w")
            return True
        else:
            if self.__database_mode == "dev":
                print("La base de datos ya existe")
            return False

    def _get_database(self, mode):
        isFile = os.path.isfile(self.__database_path)

        # Validate if the database exists
        if isFile == False:
            if self.__database_mode == "dev":
                print("La base de datos no existe")
            self.__create_database()
            return False
        else:
            return open(self.__database_path, mode)

    def _count_database(self):
        return len(self.get_data_in_database())

    def get_data_in_database(self):
        database = self._get_database("r")
        separated = []
        database_data = database.read().split("\n")

        if database_data:
            for i in range(0, len(database_data) - 1):
                separated.append(ast.literal_eval(database_data[i]))

        return separated

    def save_in_database(self, data):
        database = self._get_database("a")

        if database == False:
            self.__create_database()
            if self.__database_mode == "dev":
                print("Se creo la base de datos")

        database = self._get_database("a")
        data["uid"] = self._count_database() + 1

        if self.__database_mode:
            data["random"] = random.randrange(0, 100)

        try:
            database.write(str(data) + "\n")
            return True
        except NameError:
            print(NameError)
            return False

    def get_by_uid(self, uid):
        database_data = self.get_data_in_database()
        output_data = False

        if database_data:
            if len(database_data) > 0:
                for i in range(len(database_data)):
                    if int(database_data[i]["uid"]) == int(uid):
                        output_data = database_data[i]

                if output_data == False:
                    print("No existe el uid " + uid + " en la base de datos.")
                    return False
                else:
                    return output_data
            else:
                print("La base de datos está vacia.")
                return False
        else:
            if self.__database_mode == "dev":
                print("La base de datos no existe")
            return False
        return False

    def get_by_property(self, property="uid", value=""):
        database_data = self.get_data_in_database()
        output_data = False
        loaded = False

        if database_data:
            if len(database_data) > 0:
                for i in range(len(database_data)):
                    if database_data[i][property] == value and loaded == False:
                        output_data = database_data[i]
                        loaded = True

                if output_data == False:
                    print("No existe la propiedad (" + str(property) +
                          ") con el valor: " + str(value) + " en la base de datos.")

                    return False
                else:
                    return output_data
            else:
                print("La base de datos está vacia.")
                return False
        else:
            if self.__database_mode == "dev":
                print("La base de datos no existe")
            return False
        return False

    def get_multi_by_property(self, property="uid", value=""):
        database_data = self.get_data_in_database()
        output_data = []

        if database_data:
            if len(database_data) > 0:
                for i in range(len(database_data)):
                    if database_data[i][property] == value:
                        output_data.append(database_data[i])

                if output_data == False:
                    print("No existe la propiedad (" + property +
                          ") con el valor: " + value + " en la base de datos.")

                    return False
                else:
                    return output_data
            else:
                print("La base de datos está vacia.")
                return False
        else:
            if self.__database_mode == "dev":
                print("La base de datos no existe")
            return False
        return False

    def delete_by_uid(self, uid):
        data_in_database = self.get_data_in_database()
        deleted = False
        if len(data_in_database) > 0:
            if uid and data_in_database[uid - 1]:
                try:
                    data_in_database.pop(uid - 1)
                    write_database = self._get_database("w")
                    write_database.write("")
                    for i in data_in_database:
                        self.save_in_database(i)
                    deleted = True
                except NameError:
                    print(NameError)

                return deleted
            else:
                print("El identificador unico no es valido.")
                return False
        else:
            print("La base de datos esta vacia.")
            return False

    def delete_by_property(self, property="uid", value=""):
        data_in_database = self.get_data_in_database()
        deleted = False
        flush = self.get_by_property(property, value)

        if len(data_in_database) > 0:
            if flush and flush[property]:
                try:
                    data_in_database.pop(flush["uid"] - 1)
                    write_database = self._get_database("w")
                    write_database.write("")
                    for i in data_in_database:
                        self.save_in_database(i)
                    deleted = True
                except NameError:
                    print(NameError)

                return deleted
            else:
                print("El valor o la propiedad no es valido.")
                return False
        else:
            print("La base de datos esta vacia.")
            return False

    def get_orber_by_property(self, property):
        all_data = self.get_data_in_database()
        big_data = []

        if len(all_data) > 0:
            return sorted(all_data, key=lambda i: i[property])

    def get_properties(self):
        database_data = self.get_data_in_database()[0]
        return list(database_data.keys())

    def list_properties(self):
        keys = self.get_properties()
        for i in range(0, len(keys)):
            print(str(i + 1) + ":" + keys[i])

    def validate_prop(self, prop):
        in_array = False

        properties = self.get_properties()
        for i in properties:
            if i == prop:
                in_array = True
        return in_array


# database = Database("vehicles")
# data = {"name": "sebastian"}
# for i in range(0,200):
#     database.save_in_database(data)
# print(database.delete_by_property("uid", 1))
# print(database.get_orber_by_property("random"))
# print(database.list_properties())
# print(database.validate_prop("lol"))
