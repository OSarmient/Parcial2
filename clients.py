import database

# clientes

mode = "dev"
database_name = "clients"

props1 = [{"data": "noid1",
           "display": "Digite el número de identificación del cliente",
           "value": "",
           "type": "int"
           },
          {"data": "name1",
           "display": "Digite el nombre",
           "value": "",
           "type": "string"
           },
          {"data": "lastname1",
           "display": "Digite el apellido",
           "value": "",
           "type": "string"
           },
          {"data": "address1",
           "display": "Digite la dirección",
           "value": "",
           "type": "string"
           },
          {"data": "phone1",
           "display": "Digite el número de telefono",
           "value": "",
           "type": "int"
           },
          {"data": "city1",
           "display": "Digite la ciudad",
           "value": "",
           "type": "string"
           }
          ]


def validate_props1(props1):
    error = False
    if props1["type"] == "int" and type(props1["value"]) == props1["type"]:
        print("El valor de " + props1["data"] + " no es valido")
        error = True
    if props1["type"] == "string" and type(props1["value"]) == props1["type"]:
        error = True
        print("El valor de " + props1["data"] + " es invalido")

    return error


def insert1():
    data = {}
    verify = False
    noid2 = database.get_data_in_database(database_name)
    for i in props1:
        bucle = True
        while bucle:
            i["value"] = input(i["display"] + ": ")
            for a in range(len(noid2)):
                if noid2[a]["noid1"] == i["value"]:
                    verify = True
            if validate_props1(i) == False and verify == False:
                data[i["data"]] = i["value"]
                bucle = False
            else:
                print(
                    "Ya existe un cliente asociado a este número de identificación")
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


def get1_client():
    bucle = True
    while bucle:

        print("Digite s en cualquier momento para salir.")
        client1 = str(
            input("Digite el numero de identificación del cliente: "))

        if client1.lower() != "s":
            client4 = database.get_multi_database_data(
                database_name, "noid1", client1)

            if type(client4) == list and len(client4) > 0:
                print()
                for i in client4:
                    keys = i.keys()
                    print("----------------")
                    for j in keys:
                        print(str(j) + ": " + str(i[j]))
                    print("----------------")
                print()
            else:
                print()
                print("No existe un cliente asociado a este numero de identificación.")
                print()
        else:
            bucle = False


def delete_client1():
    bucle = True
    while bucle:
        try:
            print("Digite s en cualquier momento para salir.")
            client1 = str(input("Digita el número de identificación del cliente: "))
            
            if client1.lower() != "s": 
                database.delete_data_by_uid(database_name, "noid1", client1)
            else:
                bucle = False
        except NameError:
            print(NameError)


def show_ops():
    print()
    print("------Opciones (clientes)------")
    print()
    print("1. Registrar un cliente [1]")
    print("2. Ver la lista de clientes [2]")
    print("3. Buscar un cliente [3]")
    print("4. Borrar un cliente [4]")
    print("5. Mostrar opciones [5]")
    print("6. Salir [6]")
    print()


def start1():
    if mode == "dev":
        database.create_database(database_name)

    show_ops()

    bucle = True
    while bucle:
        try:
            print("5. Mostrar Menú [5]")
            option = int(input("Digita la opción que desees ejecutar: "))
            print()
            if option == 1:
                insert1()
            elif option == 2:
                get1_all()
            elif option == 3:
                get1_client()
            elif option == 4:
                delete_client1()
            elif option == 5:
                show_ops()
            elif option == 6:
                bucle = False
        except NameError:
            print(NameError)
            print("5. Mostrar Menú [5]")
            print("La opción digitada es invalida (debe ser número en las opciones)")
            print()

