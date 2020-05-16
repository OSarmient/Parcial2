import os
import ast

mode = "dev"
databases_path = "databases/"


def create_database(database_name):
    isFile = os.path.isfile(databases_path + database_name + ".txt")
    if os.path.isdir(databases_path) == False:
        os.mkdir("databases")
    if isFile == False:
        open(databases_path + database_name + ".txt", "w")
        return True
    else:
        if mode == "dev":
            print("La base de datos ya existe")
        return False


def get_database(database_name, mode="r"):
    isFile = os.path.isfile(databases_path + database_name + ".txt")
    if isFile == False:
        if mode == "dev":
            print("La base de datos no existe")
        return False
    else:
        return open(databases_path + database_name + ".txt", mode)


def get_data_in_database(database_name):
    database = get_database(database_name, "r")
    separated = []
    database_data = database.read().split("\n")
    for i in range(0, len(database_data) - 1):
        separated.append(ast.literal_eval(database_data[i]))

    return separated


def save_in_database(database_name, data):
    database = get_database(database_name, "a")
    if get_database(database_name, "a") == False:
        create_database(database_name)
        if mode == "dev":
            print("Se creo la base de datos")
    database = get_database(database_name, "a")
    data["uid"] = count_database(database_name)
    database.write(str(data) + "\n")
    return True


def count_database(database_name):
    database = get_database(database_name, "r")
    if database != False:
        all_data = database.read().split("\n")
        return len(all_data) - 1
    else:
        if mode == "dev":
            print("La base de datos no existe")
        return False


def get_by_uid(database_name, uid):
    database = get_database(database_name, "r")
    if database != False:
        all_data = database.read().split("\n")
        for i in range(len(all_data) - 3):
            if ast.literal_eval(all_data[i])["uid"] == uid:
                return ast.literal_eval(all_data[i])
    else:
        if mode == "dev":
            print("la base de datos no existe")
        return False
    return False


def get_by_property(database_name, property="uid", value=""):
    database = get_database(database_name, "r")
    if database != False:
        all_data = database.read().split("\n")
        for i in range(len(all_data) - 1):
            if ast.literal_eval(all_data[i])[property] == value:
                return ast.literal_eval(all_data[i])
    else:
        if mode == "dev":
            print("la base de datos no existe")
        return False
    return False


def get_multi_database_data(database_name, property="uid", value=""):
    database = get_database(database_name, "r")
    return_data = []
    if database != False:
        all_data = database.read().split("\n")
        for i in range(len(all_data) - 1):
            if ast.literal_eval(all_data[i])[property] == value:
                return_data.append(ast.literal_eval(all_data[i]))
        return return_data
    else:
        if mode == "dev":
            print("la base de datos no existe")
        return False
    return False


def delete_data_by_uid(database_name, property="uid", value=" "):
    data_in_database = get_data_in_database(database_name)
    vehicle = get_by_property(database_name, property, value)
    data_in_database.pop(vehicle["uid"])
    write_database = get_database(database_name, "w")
    write_database.write("")
    for i in data_in_database:
        save_in_database(database_name, i)

    # ####Examples

    # ##Create database
    # create_database("customers")

    # ##Include customers in customers database
    # save_in_database("customers", {"id": "1245125", "name": "Sebastian", "lastname": "Torres"})
    # save_in_database("customers", {"id": "1251", "name": "Nicolas", "lastname": "Ochoa"})
    # save_in_database("customers", {"id": "23546", "name": "Margarita", "lastname": "Romero"})
    # save_in_database("customers", {"id": "12512512", "name": "Luz", "lastname": "Beltran"})

    # ##Get data by uid
    # print(get_by_uid("customers", 2))

    # ##Get data with other properties
    # print(get_by_property("customers", "name", "Luz"))
    # print(get_by_property("customers", "id", "1251"))
    # print(get_by_property("customers", "uid", 2))
