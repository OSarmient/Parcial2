import os
import franchisee


class DataMan(franchisee.Franchisee):

    __database_name = ""
    __database_path = "databases/"
    __relative_path = ""

    def __init__(self, database_name):
        self.__database_name = database_name
        self.__relative_path = self.__create_path()
        self.__create_dir()
        self.__create()

    def __create_path(self):
        return self.__database_path + self.__database_name + ".txt"

    def __validate_database_file(self):
        return os.path.isfile(self.__relative_path)

    def __create_database_file(self):
        try:
            open(self.__relative_path + ".txt", "w")
        except NameError:
            print(NameError)

    def __create_dir(self):
        if os.path.isdir(self.__database_path) == False:
            os.mkdir(self.__database_path)

    def __create(self):
        print()
        if self.__validate_database_file() != False:
            self.__create_database_file()


database = DataMan("vehicles")
