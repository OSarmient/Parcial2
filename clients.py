import database

# clientes

mode = "dev"
database_name = "clients"

props1 = [{"data": "noid1",
           "display": "Digite el número de identificación del cliente",
           "value": "",
           "type": "int",
           "ajust" : "12"
           },
          {"data": "name1",
           "display": "Digite el nombre",
           "value": "",
           "type": "string",
           "ajust" : "15"
           },
          {"data": "lastname1",
           "display": "Digite el apellido",
           "value": "",
           "type": "string",
           "ajust" : "15"
           },
          {"data": "address1",
           "display": "Digite la dirección",
           "value": "",
           "type": "string",
           "ajust" : "30"
           },
          {"data": "phone1",
           "display": "Digite el número de telefono",
           "value": "",
           "type": "int",
           "ajust" : "20"
           },
          {"data": "city1",
           "display": "Digite la ciudad",
           "value": "",
           "type": "string",
           "ajust" : "20"
           }
          ]


def validate_props1(props1):
    error = False

    # validación de propiedades
    # se valida en tipo de propiedad (int, string) y si su valor es valido

    if props1["value"] == "":
        print("El valor de " + props1["data"] + " no puede ser nulo")
        error = True

    if props1["type"] == "int" and type(props1["value"]) == props1["type"]:
        print("El valor de " + prop["data"] + " es invalido")
        error = True
    if props1["type"] == "string" and type(props1["value"]) == props1["type"]:
        error = True
        print("El valor de " + props1["data"] + " es invalido")

    if "ajust" in props1 and int(props1["ajust"]) < len(props1["value"]):
        print(
            "Superaste el limite de caracteres (Limite: " + props1["ajust"] + ")")
        error = True

    return error


def insert1():
    
    utils.clean_console()
    
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
    
    utils.clean_console()
    
    data = database.get_data_in_database(database_name)
    for i in data:
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
        property = str(input("Digita la propiedad para ordenar los clientes: "))
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
                print("Las propiedades de los clientes son las siguientes: ")
                print()
                database.list_all_properties(database_name)
                print()
        else: 
            bucle = False

def get1_client():
    
    utils.clean_console()
    
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

    utils.clean_console()
    
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
            print("No fue posible eliminar al cliente")


def show_ops():

    utils.clean_console()
    
    print()
    print("------Opciones (clientes)------")
    print()
    print("1. Registrar un cliente [1]")
    print("2. Ver la lista de clientes [2]")
    print("3. Buscar un cliente [3]")
    print("4. Borrar un cliente [4]")
    print("5. Ordenar clientes [5]")
    print("6. Mostrar opciones [6]")
    print("7. Salir [7]")
    print()


def start1():
    if mode == "dev":
        database.create_database(database_name)

    show_ops()

    bucle = True
    while bucle:
        try:
            print("6. Mostrar Menú [6]")
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
                get_all_order_by()
            elif option == 6:
                show_ops()
            elif option == 7:
                bucle = False
            else:
                print("Debes selccionar una opcion del menú.")
            print()
        except NameError:
            print(NameError)
            print("6. Mostrar Menú [6]")
            print("La opción digitada es invalida (debe ser número en las opciones)")
            print()

