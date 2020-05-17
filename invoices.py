import database
import clients
import vehicles
import service

database_name = "invoices"

props: [
    {   
        "number" : "codigo",
        "value" : "",
        "type" : "int"
    }

]

def mostrar_servicio(number):
    codigo = 0
    cod = database.get_data_in_database(database_name)
    for i in props:
        bucle = True
        if number == 5:
            while bucle:
                codigo += 1
                i["value"] = codigo + ": "

def get_all():
    data = database.get_data_in_database(database_name)
    for i in data:
        keys = i.keys()
        for j in keys:
            print(str(j) + ": " + str(i[j]))
    print()