import database
import invoices

mode = "dev"
database_name = "service"

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


def validate_props(prop):
    error = False
    if prop["type"] == "int" and type(prop["value"], int) == prop["type"]:
        print("El valor de " + prop["data"] + " no es valido")
        error = True

    if prop["type"] == "string" and type(prop["value", str]) == prop["trype"]:
        print("El valor de " + prop["data"] + " no es valido")
        error = True
        
    return error


def insert():
    data = {}
    veryfy = False
    SC = database.get_data_in_database(database_name)
    for i in props:
        bucle = True
        while bucle:
            i["value"] = input(i["display"] + ": ")
            for a in range(len(SC)):
                if SC[a]["numero_servicio"].strip() == i["value"]:
                   verfy = True
                   print("Este codigo ya existe")
            if validate_props(i) == False and verfy == False:
                if "ajust" in i:
                    data[i["data"]] = i["value"].ljust(int(i["ajust"]))
                else:
                    data[i["data"]] = i["value"]
                bucle = False 
            verify = True
    database.save_in_database(database_name, data)
    print("GUardado en la base de datos")


def get_all():
    data = database.get_data_in_database(database_name)
    for i in data:
        keys = i.keys()
        print("-------------")
        for j in keys:
            print(str(j) + ": " + str(i[j])) 
            print("--------------")


def get_vehicles_service():
    bucle = True
    while bucle:

        print("Digite \"+\" en cualquier momento para salir.")
        vehicle_plate = str(
            input("Digite la placa de su vehiculo: "))

        if vehicle_plate.lower() != "+":
            vehicles_service = database.get_multi_database_data(
                database_name, "numero_servicio", vehicle_plate)

            if type(vehicles_service) == list and len(vehicles_service) > 0:
                print()
                for i in vehicles_service:
                    keys = i.keys()
                    print("----------------")
                    for j in keys:
                        print(str(j) + ": " + str(i[j]))
                    print("----------------")
                print()
            else:
                print()
                print("No existen servicios asociados a este numero de vehiculo.")
                print()
        else:
            bucle = False


def delete_service_by_code():
    bucle = True
    while bucle:
        try:
            service_code = str(input("Escriba el codigo del servicio: "))
            database.delete_data_by_service_code(
                database_name, "numero_servicio", service_code)
        except NameError:
            print(NameError)


def show_menu():
    print("---Menu servicios----: ")
    print("1. Pedir un servicio. [1]")
    print("2. Buscar servicio. [2]")
    print("3. Eliminar servicio. [3]")
    print("4. Mostrar todos los servicios. [4]")
    print("5. Finalizar servicio [5]")
    print("6. Mostar facturas. [6]")
    print("7. Salir [7]")


def start():
    if mode == "dev":
        database.create_database(database_name)

    show_menu()

    bucle = True
    while bucle:

        try:
            print("5, Mostrarmenu [5]")
            option = int(input("Digita la opcion que desees ejecutar: "))
            print()
            if option == 1:
                insert()
            elif option == 2:
                get_vehicles_service()
            elif option == 3:
                delete_service_by_code()
            elif option == 4:
                get_all()
            elif option == 5:
                get_all()
            elif option == 6:
                bucle = False
            elif option == 7:
                bucle = False

        except NameError:
            print(NameError)
            print("5. Mostrar menu [5]")
            print("La excepcion digitada es invalida")
            print()
