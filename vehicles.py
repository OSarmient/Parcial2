import database

# vehicles
# placa, marca, modelo, cilindrada, color, tipo de servicio (particular, carga,
# pasajeros), tipo de combustible, capacidad de pasajeros, capacidad de carga, número de chasis y
# número de motor.

# mode = "dev"
database_name = "vehicles"
props = [
    {
        "data": "cliente",
        "display": "Digite el numero de identificación del cliente",
        "value": "",
        "type": "string",
        "ajust": "12"
    },
    {
        "data": "placa",
        "display": "Digite el numero de la placa",
        "value": "",
        "type": "int",
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
                        data[i["data"]] = i["value"].ljust(int(i["ajust"]))
                        bucle = False
                    else:
                        print()
                        print("Ya existe un vehiculo con esta placa.")
                        print()
                else:
                    data[i["data"]] = i["value"].ljust(int(i["ajust"]))
                    bucle = False

    database.save_in_database(database_name, data)
    print("Guardado en la base de datos")


def get_all():
    data = database.get_data_in_database(database_name)
    if len(data) > 0:
        for i in data:
            if i != False:
                keys = i.keys()
                print("----------------")
                for j in keys:
                    print(str(j) + ": " + str(i[j]))
                print("----------------")


def get_one():
    bucle = True
    while bucle:
        try:
            print("Digite s en cualquier momento para salir.")
            vehicle_plate = str(input("Digita la placa del vehiculo: "))

            if vehicle_plate.lower() != "s":
                vehicle = database.get_by_property(
                    database_name, "placa", vehicle_plate)

                if vehicle != False:
                    keys = vehicle.keys()
                    print("----------------")
                    for j in keys:
                        print(str(j) + ": " + str(vehicle[j]))
                    print("----------------")
                else:
                    print()
                    print("No existe ningun vehiculo asociado a esta placa. ")
                    print()
            else:
                bucle = False

        except NameError:
            print("No due posible eliminar el vehiculo.")


def get_customer_vehicles():
    bucle = True
    while bucle:

        print("Digite s en cualquier momento para salir.")
        customer_id = str(
            input("Digite el numero de identificación del cliente: "))

        if customer_id.lower() != "s":
            customer_vehicles = database.get_multi_database_data(
                database_name, "cliente", customer_id)

            if type(customer_vehicles) == list and len(customer_vehicles) > 0:
                print()
                print("Existen " + str(len(customer_vehicles)) +
                      " vehiculos asociados a este numero de indentificación.")
                for i in customer_vehicles:
                    keys = i.keys()
                    print("----------------")
                    for j in keys:
                        print(str(j) + ": " + str(i[j]))
                    print("----------------")
                print()
            else:
                print()
                print("No existen vehiculos asociados a este numero de identificación.")
                print()
        else:
            bucle = False


def delete_vehicle_by_plate():
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
            print("No due posible eliminar el vehiculo.")


def show_menu():
    print()
    print(" ---- Menu (vehiculos) ---- ")
    print()
    print("1. Agregar un carro [1]")
    print("2. Ver todos los carros [2]")
    print("3. Buscar carros de un cliente [3]")
    print("4. Eliminar un vehiculo por su placa [4]")
    print("5. Buscar un vehiculo por su placa [5]")
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
            option = int(input("Digita la opción que desees ejecutar: "))
            print()
            if option == 1:
                insert()
            elif option == 2:
                get_all()
            elif option == 3:
                get_customer_vehicles()
            elif option == 4:
                delete_vehicle_by_plate()
            elif option == 5:
                get_one()
            elif option == 6:
                show_menu()
            elif option == 7:
                bucle = False
            print()

        except NameError:
            print(NameError)
            print("6. Mostrar menú [6]")
            print("La opción digitada es invalida (debe ser un número en el menú).")
            print()


start()
