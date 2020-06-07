from .database import Database
from .utils import clean_console


class ModuleBase:
    def __init__(self):
        self.database = Database(self.database_name)

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
