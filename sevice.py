import database

mode = "dev"
database_name = "service"

props = [
    {
        "data": "codigo_servicio", 
        "display": "Escriba el codigo que el servicio que deaea: ", 
        "value": "",
        "type": "int"
    },

    {
        "data": "numero_servcio", 
        "display": "Escriba el nombre de el servicio que desea: ", 
        "value":"", 
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
    return error

def insert ():
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

def show_menu():
    print("---Menu servicios----: ")
    print("1. Cambio de aceite. [1]")
    print("2. Mantenimiento mecanico. [2")
    print("3. Electicidad aoutomotriz. [3]")
    print("4. Frenos. [4]")
    print("5. Latoneria y pintura. [5]")
    print("6. Salir [6]")

def start():
    if mode == "dev":
        database.create_database(database_name)
    
    show_menu()
    

    bucle = True
    while bucle:
 
        try:
            option = int(input("Digita laopcion que desees ejecutar: "))
            if option == 1: insert()
            elif option == 2: get_all()
            elif option == 5: show_menu()
            elif option == 6: bucle = False

        except:
            print("La excepcion digitada es invalida")

start()
