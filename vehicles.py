import database

# vehicles
# placa, marca, modelo, cilindrada, color, tipo de servicio (particular, carga,
# pasajeros), tipo de combustible, capacidad de pasajeros, capacidad de carga, número de chasis y
# número de motor.

mode = "dev"
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

    print("Guardado en la base de datos")
    database.save_in_database(database_name, data)


def get_all():
    print()
    data = database.get_data_in_database(database_name)
    for i in data:
        keys = i.keys()
        print("----------------")
        for j in keys:
            print(str(j) + ": " + str(i[j]))
        print("----------------")
        print()


def show_menu():
    print()
    print(" ---- Menu (vehiculos) ---- ")
    print()
    print("1. Agregar un carro [1]")
    print("2. Ver todos los carros [2]")
    print("3. Buscar carro por su placa [3]")
    print("4. Agregar un carro [4]")
    print("5. Agregar un carro [5]")
    print("5. Mostrar menú [5]")
    print("6. Salir [6]")
    print()


def start():
    if mode == "dev":
        database.create_database(database_name)

    show_menu()

    bucle = True
    while bucle:
        try:
            print("5. Mostrar menú [5]")
            option = int(input("Digita la opción que desees ejecutar: "))
            if option == 1:
                insert()
            elif option == 2:
                get_all()
            elif option == 5:
                show_menu()
            elif option == 6:
                bucle = False
        except NameError:
            print(NameError)
            print("5. Mostrar menú [5]")
            print("La opción digitada es invalida (debe ser un número en el menú).")
            print()


start()
