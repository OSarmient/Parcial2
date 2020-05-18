import database
import Servicios_2

mode = "dev"
database_name = "service"
database_nameC = "clients"
database_nameV = "vehicles"
database_nameA = "service_saked"

props = [
    {
        "data": "numero_servicio",
        "display": "Escriba el codigo que el servicio que deaea: ",
        "value": "",
        "type": "int",
        "ajust": "6"
    },

    {
        "data": "nombre_servcio",
        "display": "Escriba el nombre de el servicio que desea: ",
        "value": "",
        "type": "str",
        "ajust": "25"
    },

    {
        "data": "precio_unitario",
        "display": "Escriba cuanto cuaesta el servicio por hora: ",
        "value": "",
        "type": "int",
        "ajust": "7"
    },

    {
        "data": "horas",
        "display": "Escriba por cuantas horas quire contratar el servicio: ",
        "value": "",
        "type": "int",
        "ajust": "2"
    }
]


def validate_props(props):
    error = False
    if props["type"] == "int" and type(props["value"]) == props["type"]:
        print("El valor de " + props["data"] + " no es valido")
        error = True
    if props["type"] == "string" and type(props["value"]) == props["type"]:
        error = True
        print("El valor de " + props["data"] + " es invalido")

    return error


def insertS():
    data = {}
    verify = False
    SC = database.get_data_in_database(database_name)
    for i in props:
        bucle = True
        while bucle:
            i["value"] = input(i["display"] + ": ")
            for a in range(len(SC)):
                if SC[a]["numero_servicio"] == i["value"]:
                    verify = True
            if validate_props(i) == False and verify == False:
                data[i["data"]] = i["value"]
                bucle = False
            else:
                print(
                    "Ya existe un servicio con ese codigo")
                verify = False
    database.save_in_database(database_name, data)
    print("Guardado en la base de datos")


def get1_all():
    print()
    data = database.get_data_in_database(database_name)
    for i in data:
        keys = i.keys()
        print("----------------")
        for j in keys:
            print(str(j) + ": " + str(i[j]))
            print("----------------")



def get_vehicles_service():
    bucle = True
    while bucle:

        print("Digite s en cualquier momento para salir.")
        vehicle_plate = str(
            input("Digite el codigo del servicio: "))

        if vehicle_plate.lower() != "s":
            vehicle_service = database.get_multi_database_data(
                database_name, "numero_servicio", vehicle_plate)

            if type(vehicle_service) == list and len(vehicle_service) > 0:
                print()
                for i in vehicle_service:
                    keys = i.keys()
                    print("----------------")
                    for j in keys:
                        print(str(j) + ": " + str(i[j]))
                    print("----------------")
                print()
            else:
                print()
                print("No existe este servicio.")
                print()
        else:
            bucle = False


def delete_service_by_code():
    bucle = True
    while bucle:
        try:
            print("Digite s en cualquier momento para salir")
            service_code = str(input("Escriba el codigo del servicio: "))

            if service_code.lower() != "s":
                database.delete_data_by_property(
                    database_name, "numero_servicio", service_code)
            else:
                bucle = False
        except NameError:
            print("No es posible eliminar el servicio.")


def show_menu():
    print()
    print("---Menu servicios----: ")
    print()
    print("1. Nuevo servicio. [1]")
    print("2. Buscar servicio. [2]")
    print("3. Eliminar servicio. [3]")
    print("4. Mostrar todos los servicios. [4]")
    print("5. Pedir servicio [5]")
    print("6. Salir. [6]")
    print()


def startS():
    if mode == "dev":
        database.create_database(database_name)

    show_menu()

    bucle = True
    while bucle:

        try:
            print("5, Mostrar menu [5]")
            option = int(input("Digita la opcion que desees ejecutar: "))
            print()
            if option == 1:
                insertS()
            elif option == 2:
                get_vehicles_service()
            elif option == 3:
                delete_service_by_code()
            elif option == 4:
                get1_all()
            elif option == 5:
                Servicios_2.relation()
            elif option == 6:
                bucle = False

        except NameError:
            print(NameError)
            print("5. Mostrar menu [5]")
            print("La excepcion digitada es invalida")
            print()

