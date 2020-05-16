import database

#clientes

mode = "dev"
database_name = "client"

props1 = [{"data": "noid1",
          "display": "Digite el número de identificación del cliente",
          "value": "",
           "type": "string"
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
    if props1["type"]=="string" and type(props1["value"]) == props1["type"]:
        error = True
        print("El valor de " + props1["data"] + " es invalido")

    return error

def insert1 ():
    data = {}
    for i in props1:
        bucle = True
        while bucle:
            i["value"] = input(i["display"] + ": ")
            if validate_props1(i) == False:
                data[i["data"]] = i["value"]
                bucle = False
                
    print("Guardado en la base de datos")
    database.save_in_database(database_name, data)
    
def get1_all():
    print()
    data = database.get_data_in_database(database_name)
    for i in data:
        keys = i.keys()
        print("----------------")
        for j in keys:
            print(str(j) + ": " + str(i[j]))
            print("----------------")
            print()
    
def show_ops():
    print()
    print("------Opciones (clientes)------")
    print()
    print("1. Registrar un cliente [1]")
    print("2. Ver la lista de clientes [2]")
    print("3. Buscar un cliente [3]")
    print("4. Mostrar opciones [4]")
    print("5. Salir [5]")
    print()
    
def start1():
    if mode == "dev":
        database.create_database(database_name)
        
    show_ops()
    
    bucle = True
    while bucle:
        try:
            print("4. Mostrar Menú [4]")
            option = int(input("Digita la opción que desees ejecutar: "))
            if option == 1:
                insert1()
            elif option == 2:
                get1_all()
            elif option == 4:
                show_ops()
            elif option == 5:
                bucle = False
        except NameError:
            print(NameError)
            print("4. Mostrar Menú [4]")
            print("La opción digitada es invalida (debe ser número en las opciones)")
            print()

start1()
