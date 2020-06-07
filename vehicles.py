import database
import utils

# vehicles
# placa, marca, modelo, cilindrada, color, tipo de servicio (particular, carga,
# pasajeros), tipo de combustible, capacidad de pasajeros, capacidad de carga, número de chasis y
# número de motor.

# mode = "dev"
database_name = "vehicles"
props = [
    {
        "data": "placa",
        "display": "Digite el numero de la placa",
        "value": "",
        "type": "string",
        "ajust": "6"
    },
    {
        "data": "marca",
        "display": "Digite el nombre de la marca",
        "value": "",
        "type": "string",
        "ajust": "15"
    },
    {
        "data": "modelo",
        "display": "Digite el modelo del automovil",
        "value": "",
        "type": "string",
        "ajust": "15"
    },
    {
        "data": "cilindrada",
        "display": "Digite la cilindrada",
        "value": "",
        "type": "int",
        "ajust": "6"
    },
    {
        "data": "color",
        "display": "Digite el color",
        "value": "",
        "type": "string",
        "ajust": "10"
    },
    {
        "data": "tipo",
        "display": "Digite el tipo de automovil (servicio)",
        "value": "",
        "type": "string",
        "ajust": "30"
    },
    {
        "data": "combustible",
        "display": "Digite el tipo de combustible",
        "value": "",
        "type": "string",
        "ajust": "12"
    },
    {
        "data": "pasajeros",
        "display": "Digite el numero de pasajeros",
        "value": "",
        "type": "int",
        "ajust": "2"
    },
    {
        "data": "chasis",
        "display": "Digite el numero de chasis",
        "value": "",
        "type": "int",
        "ajust": "3"
    },
    {
        "data": "motor",
        "display": "Digite el numero de motor",
        "value": "",
        "type": "int",
        "ajust": "3"
    }
]


def validate_prop(prop):
    error = False

    # validación de propiedades
    # se valida en tipo de propiedad (int, string) y si su valor es valido

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

def insert():

    utils.clean_console()

    data = {}
    for i in props:
        bucle = True
        while bucle:
            i["value"] = input(i["display"] + ": ")

            # Validación de propiedades
            if validate_prop(i) == False:
                if i["data"] == "placa":
                    # Cuando la propiedad sea la placa validar si existe otra igual en la base de datos
                    if database.get_by_property(database_name, "placa", i["value"]) == False:
                        if i["type"] == "int":
                            data[i["data"]] = int(i["value"])
                        else:    
                            data[i["data"]] = i["value"]
                        bucle = False
                    else:
                        print()
                        print("Ya existe un vehiculo con esta placa.")
                        print()
                else:
                    if i["type"] == "int":
                        data[i["data"]] = int(i["value"])
                    else:    
                        data[i["data"]] = i["value"]
                    bucle = False

    database.save_in_database(database_name, data)
    print("Guardado en la base de datos")

def get_all():

    utils.clean_console()

    data = database.get_data_in_database(database_name)
    if len(data) > 0:
        for i in data:
            if i != False:
                keys = i.keys()
                print("----------------")
                for j in keys:
                    print(str(j) + ": " + str(i[j]))
                print("----------------")

def get_all_order_by():

    utils.clean_console()
    bucle = True

    while bucle:


        print("Digite s en cualquier momento para salir.")
        property = str(input("Digita la propiedad para ordenar los vehiculos: "))
        if property.lower() != "s":
            if database.validate_database_props(database_name, property):

                utils.clean_console()
                data = database.get_data_in_database_order_by(database_name, property)
                if len(data) > 0:
                    for i in data:
                        if i != False:
                            keys = i.keys()
                            print("----------------")
                            for j in keys:
                                print(str(j) + ": " + str(i[j]))
                            print("----------------")

            else:
                utils.clean_console()
                print("Las propiedades le los vehiculos son las siguientes: ")
                print()
                database.list_all_properties(database_name)
                print()
        else: 
            bucle = False

def get_one():

    utils.clean_console()

    bucle = True
    while bucle:
        try:
            print("Digite s en cualquier momento para salir.")
            vehicle_plate = str(input("Digita la placa del vehiculo: "))

            if vehicle_plate.lower() != "s":
                vehicle = database.get_by_property(
                    database_name, "placa", vehicle_plate)

                if vehicle != False:
                    utils.clean_console()

                    keys = vehicle.keys()
                    print("----------------")
                    for j in keys:
                        print(str(j) + ": " + str(vehicle[j]))
                    print("----------------")
                else:
                    utils.clean_console()
                    print()
                    print("No existe ningun vehiculo asociado a esta placa. ")
                    print()
            else:
                bucle = False

        except NameError:
            print("No fue posible eliminar el vehiculo.")

def delete_vehicle_by_plate():

    utils.clean_console()

    bucle = True
    while bucle:
        try:
            print("Digite s en cualquier momento para salir.")
            vehicle_plate = str(input("Digita la placa del vehiculo: "))

            if vehicle_plate.lower() != "s":
                database.delete_data_by_property(
                    database_name, "placa", vehicle_plate)
            else:
                bucle = False

        except NameError:
            print("No fue posible eliminar el vehiculo.")

def show_menu():

    utils.clean_console()

    print()
    print(" ---- Menu (vehiculos) ---- ")
    print()
    print("1. Agregar un carro [1]")
    print("2. Ver todos los carros [2]")
    print("3. Eliminar un vehiculo por su placa [3]")
    print("4. Buscar un vehiculo por su placa [4]")
    print("5. Ordenar vehiculos [5]")
    print("6. Mostrar menú [6]")
    print("7. Salir [7]")
    print()

def start():
    database.create_database(database_name)

    show_menu()

    bucle = True
    while bucle:
        try:
            print("6. Mostrar menú [6]")
            option = input("Digita la opción que desees ejecutar: ")
            print()

            if option == "1" or option == "2" or option == "3" or option == "4" or option == "5" or option == "6" or option == "7":

                if option == "1":
                    insert()
                elif option == "2":
                    get_all()
                elif option == "3":
                    delete_vehicle_by_plate()
                elif option == "4":
                    get_one()
                elif option == "5":
                    get_all_order_by()
                elif option == "6":
                    show_menu()
                elif option == "7":
                    bucle = False

            else:
                print("Debes selccionar una opcion del menú.")
            print()

        except NameError:
            print(NameError)
            print("6. Mostrar menú [6]")
            print("La opción digitada es invalida (debe ser un número en el menú).")
            print()
