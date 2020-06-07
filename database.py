import os
import ast

# Dependencied OS https://docs.python.org/3/library/os.html

# Dependencies AST https://docs.python.org/3/library/ast.html
# Use: ast.literal_eval(string)
# Solo se uso la función literal_eval() para pasar de un string en modo dict a una clase dict de python

mode = "dev"
databases_path = "databases/"


def create_database(database_name):
    # param database_name (String)
    # return (Bool) si el archivo existe devuelve false : true

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
    # param database_name (String)
    # return (Array) Información formateada en la base de datos

    database = get_database(database_name, "r")
    separated = []
    database_data = database.read().split("\n")
    for i in range(0, len(database_data) - 1):
        separated.append(ast.literal_eval(database_data[i]))

    return separated


def save_in_database(database_name, data):
    # Agregar elemento en la base de datos
    # param database_name (String)
    # return (Array) info in database

    database = get_database(database_name, "a")
    if get_database(database_name, "a") == False:
        create_database(database_name)
        if mode == "dev":
            print("Se creo la base de datos")
    database = get_database(database_name, "a")
    data["uid"] = count_database(database_name)

    try:
        database.write(str(data) + "\n")
        return True
    except NameError:
        print(NameError)
        return False


def save_in_database2(database_name, data):
    # Agregar elemento en la base de datos
    # param database_name (String)
    # return (Boolean) agregar informacion

    database = get_database(database_name, "a")
    if get_database(database_name, "a") == False:
        create_database(database_name)
        if mode == "dev":
            print("Se creo la base de datos")
    database = get_database(database_name, "a")

    try:
        database.write(str(data) + "\n")
        return True
    except NameError:
        print(NameError)
        return False


def count_database(database_name):
    # Contar información en la base de datos
    # param database_name (String)
    # return (Int) and (Boolean)

    database = get_database(database_name, "r")
    if database != False:
        all_data = database.read().split("\n")
        return len(all_data) - 1
    else:
        if mode == "dev":
            print("La base de datos no existe")
        return False


def get_by_uid(database_name, uid):

    # Obtener información basado en su uid
    # param database_name (String)
    # param uid (Int)
    # return (Boolean) or (Dict)

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

    # Obtener informaciónde una fila basado en el valor de una propiedad
    # param database_name (String)
    # param property (String)
    # param value (String)
    # return (Boolean) or (Dict)

    database = get_database(database_name, "r")
    if database != False:
        all_data = database.read().split("\n")
        for i in range(len(all_data) - 1):
            if ast.literal_eval(all_data[i])[property].strip() == value:
                return ast.literal_eval(all_data[i])
    else:
        if mode == "dev":
            print("la base de datos no existe")
        return False
    return False


def get_multi_database_data(database_name, property="uid", value=""):

    # Obtener información de todas las filas basado en el valor de una propiedad
    # param database_name (String)
    # param property (String)
    # param value (String) or (Int)
    # return (Boolean) or (List)

    database = get_database(database_name, "r")
    return_data = []
    if database != False:
        all_data = database.read().split("\n")
        for i in range(len(all_data) - 1):
            if ast.literal_eval(all_data[i])[property].strip() == value:
                return_data.append(ast.literal_eval(all_data[i]))
        return return_data
    else:
        if mode == "dev":
            print("la base de datos no existe")
        return False
    return False


def get_multi_database_data2(database_name, property="uid", value=""):

    # Obtener información de todas las filas basado en el valor de una propiedad
    # param database_name (String)
    # param property (String)
    # param value (String) or (Int)
    # return (Boolean) or (List)

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


def delete_data_by_property(database_name, property="uid", value=" "):

    # Borrar fila en la base de datos basado en sus propiedades
    # param database_name (String)
    # param property (String)
    # param value (String) or (Int)

    data_in_database = get_data_in_database(database_name)
    row = get_by_property(database_name, property, value)
    if row != False:
        data_in_database.pop(row["uid"])
        write_database = get_database(database_name, "w")
        write_database.write("")
        for i in data_in_database:
            save_in_database(database_name, i)
    else:
        print("No existe en la base de datos.")


def delete_data_by_uid(database_name, property="uid", value=" "):

    # Borrar fila en la base de datos basado en sus propiedades
    # param database_name (String)
    # param property (String)
    # param value (String) or (Int)

    data_in_database = get_data_in_database(database_name)
    vehicle = get_by_property(database_name, property, value)
    if vehicle != False:
        data_in_database.pop(vehicle["uid"])
        write_database = get_database(database_name, "w")
        write_database.write("")
        for i in data_in_database:
            save_in_database(database_name, i)
    else:
        print("No existe en la base de datos.")


def get_data_in_database_order_by(database_name, property="uid"):

    # Obtener información de todas las filas y ordenarla segun la propiedad
    # param database_name (String)
    # param property (String)
    # return (Boolean) or (List)

    database = get_database(database_name, "r")

    if database != False:
        all_data = database.read().split("\n")
        big_data = []

        for i in range(len(all_data) - 1):
            big_data.append(ast.literal_eval(all_data[i]))
        return sorted(big_data, key=lambda i: i[property])

    else:
        if mode == "dev":
            print("la base de datos no existe")
        return False
    return False


def validate_database_props(database_name, prop):
    in_array = False

    properties = get_all_properties(database_name)
    for i in properties:
        if i == prop:
            in_array = True
    return in_array


def list_all_properties(database_name):
    database = get_database(database_name, "r")
    if database != False:
        keys = get_all_properties(database_name)
        for i in range(len(keys) - 1):
            print(str(i + 1) + ":" + keys[i])
    else:
        if mode == "dev":
            print("la base de datos no existe")
        return False
    return False


def get_all_properties(database_name):
    database = get_database(database_name, "r")
    if database != False:
        all_data = database.read().split("\n")
        data = ast.literal_eval(all_data[0])
        return list(data.keys())
    else:
        if mode == "dev":
            print("la base de datos no existe")
        return False
    return False

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
