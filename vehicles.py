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
        "type": "int"
    },
    {
        "data": "placa",
        "display": "Digite el numero de la placa",
        "value": "",
        "type": "int"
    },
    {
        "data": "marca",
        "display": "Digite el nombre de la marca",
        "value": "",
        "type": "string"
    },
    {
        "data": "modelo",
        "display": "Digite el modelo del automovil",
        "value": "",
        "type": "string"
    },
    {
        "data": "cilindrada",
        "display": "Digite la cilindrada",
        "value": "",
        "type": "int"
    },
    {
        "data": "color",
        "display": "Digite el color",
        "value": "",
        "type": "string"
    },
    {
        "data": "tipo",
        "display": "Digite el tipo de automovil (servicio)",
        "value": "",
        "type": "string"
    },
    {
        "data": "combustible",
        "display": "Digite el tipo de combustible",
        "value": "",
        "type": "string"
    },
    {
        "data": "pasajeros",
        "display": "Digite el numero de pasajeros",
        "value": "",
        "type": "int"
    },
    {
        "data": "chasis",
        "display": "Digite el numero de chasis",
        "value": "",
        "type": "int"
    },
    {
        "data": "motor",
        "display": "Digite el numero de motor",
        "value": "",
        "type": "int"
    }
]


def validate_prop(prop):
    error = False
    if prop["type"] == "int" and type(prop["value"]) == prop["type"]:
        print("El valor de " + prop["data"] + " es invalido")
        error = True
    if prop["type"] == "string" and type(prop["value"]) == prop["type"]:
        error = True
        print("El valor de " + prop["data"] + " es invalido")
    return error


def insert():
    data = {}
    for i in props:
        bucle = True
        while bucle:
            i["value"] = input(i["display"] + ": ")
            if validate_prop(i) == False:
                data[i["data"]] = i["value"]
                bucle = False

    database.save_in_database(database_name, data)
    print("Guardado en la base de datos.")


def get_all():
    data = database.get_data_in_database(database_name)
    for i in data:
        keys = i.keys()
        print("----------------")
        for j in keys:
            print(str(j) + ": " + str(i[j]))
        print("----------------")


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
            vehicle_plate = str(input("Digita la placa del vehiculo: "))
            database.delete_data_by_uid(database_name, "placa", vehicle_plate)
        except NameError:
            print(NameError)


def show_menu():
    print()
    print(" ---- Menu (vehiculos) ---- ")
    print()
    print("1. Agregar un carro [1]")
    print("2. Ver todos los carros [2]")
    print("3. Buscar carros de un cliente [3]")
    print("4. Eliminar un vehiculo por su placa [4]")
    print("5. Agregar un carro [5]")
    print("5. Mostrar menú [5]")
    print("6. Salir [6]")
    print()


def start():
    database.create_database(database_name)

    show_menu()

    bucle = True
    while bucle:
        try:
            print("5. Mostrar menú [5]")
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
                show_menu()
            elif option == 6:
                bucle = False
            print()
        except NameError:
            print(NameError)
            print("5. Mostrar menú [5]")
            print("La opción digitada es invalida (debe ser un número en el menú).")
            print()


start()
