import os
import ast

databases_path = "databases/"

def create_database(database_name):
    isFile = os.path.isfile(databases_path + database_name + ".txt")
    if os.path.isdir(databases_path) == False:
        os.mkdir("databases")
    if isFile == False:
        open(databases_path + database_name + ".txt", "w")
        return True
    else: 
        print("La base de datos ya existe")
        return False

def get_database(database_name, mode):
    isFile = os.path.isfile(databases_path + database_name + ".txt")
    if isFile == False:
        print("La base de datos no existe")
        return False
    else: 
        return open(databases_path + database_name + ".txt", mode)

def save_in_database(database_name, data):
    database = get_database(database_name, "a")
    if get_database(database_name, "a") == False:
        create_database(database_name)
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
        print("La base de datos no existe")
        return False

def get_by_uid(database_name, uid):
    data = {}
    database = get_database(database_name, "r")
    if database != False:
        all_data = database.read().split("\n")
        for i in range(len(all_data) - 3):
            if ast.literal_eval(all_data[i])["uid"] == uid:
                return ast.literal_eval(all_data[i])
    else: 
        print("la base de datos no existe")
        return False
    return False

def get_by_property(database_name, property, value):
    data = {}
    database = get_database(database_name, "r")
    if database != False:
        all_data = database.read().split("\n")
        for i in range(len(all_data) - 3):
            if ast.literal_eval(all_data[i])[property] == value:
                return ast.literal_eval(all_data[i])
    else: 
        print("la base de datos no existe")
        return False
    return False

####EXamples

create_database("customers")
save_in_database("customers", {"id": "1245125", "name": "Sebastian", "lastname": "Torres"})