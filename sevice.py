import database

#mode = "dev"
database_name = "service"

props = [
    {
        "data": "numero_servicio",
        "display": "Escriba el codigo que el servicio que deaea: ",
        "value": "",
        "type": "int"
    },

    {
        "data": "nombre_servcio",
        "display": "Escriba el nombre de el servicio que desea: ",
        "value": "",
        "type": "str"
    },

    {
        "data": "precio_unitario",
        "display": "Escriba cuanto cuaesta el servicio por hora: ",
        "value": "",
        "type": "int"
    },

    {
        "data": "Horas",
        "display": "Escriba por cuantas horas quire contratar el servicio: ",
        "value": "",
        "type": "int"
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

    if "ajust" in prop and int(prop["ajust"]) < len(prop["value"]):
        print("Supero el limite de caracteres")
    return error


def insert():
    data = {}

    for i in props:
        bucle = True
        while bucle:
            i["value"] = input(i["display"] + ": ")
            if validate_props(i) == False:
                data[i["data"]] = i["value"]
                bucle = False

        print("Guardado en la base de datos")
        database.save_in_database(database_name, data)


def get_all():
    data = database.get_data_in_database(database_name)
    for i in data:
        keys = i.keys()
        for j in keys:
            print(str(j) + ": " + str(i[j]))
    print()


def get_vehicles_service():
    bucle = True
    while bucle:

        print("Digite \"+\" en cualquier momento para salir.")
        vehicle_plate = str(
            input("Digite la placa de su vehiculo: "))

        if vehicle_plate.lower() != "+":
            vehicles_service = database.get_multi_database_data(
                database_name, "vehicle", vehicle_plate)

            if type(vehicles_service) == list and len(vehicles_service) > 0:
                print()
                print("Existen " + str(len(vehicles_service)) +
                      " servicios asociados a ese vehiculo.")
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
    print("5. Mostar opciones. [5]")
    print("6. Salir [6]")


def start():

    show_menu()

    bucle = True
    while bucle:

        try:
            option = int(input("Digita laopcion que desees ejecutar: "))
            if option == 1:
                insert()
            elif option == 2:
                get_vehicles_service()
            elif option == 3:
                delete_service_by_code()
            elif option == 4:
                get_all()
            elif option == 5:
                show_menu()
            elif option == 6:
                bucle = False

        except:
            print("La excepcion digitada es invalida")
