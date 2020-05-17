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
    verify = False
    noid2 = database.get_data_in_database(database_name)
    for i in props:
        bucle = True
        while bucle:
            i["value"] = input(i["display"] + ": ")
            for a in range(len(noid2)):
                if noid2[a]["placa"].strip() == i["value"]:
                    verify = True
                    print("Esta placa ya esta registrada")
            if validate_prop(i) == False and verify == False:
                if "ajust" in i:
                    data[i["data"]] = i["value"].ljust(int(i["ajust"]))
                else:
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
            print("Digite s en cualquier momento para salir.")
            vehicle_plate = str(input("Digita la placa del vehiculo: "))

            if vehicle_plate.lower() == "s":
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
