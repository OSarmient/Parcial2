import database
import Facturas
import utils

#servicios 2

database_name = "clients"
database_name2 = "vehicles"
database_name3 = "service"
database_name4 = "service_asked"


def relation():
    bucle = True
    while bucle:

        print("Digite s en cualquier momento para salir.")
        client1 = str(
            input("Digite el numero de identificación del cliente: "))

        if client1.lower() != "s":
            client4 = database.get_multi_database_data(
                database_name, "noid1", client1)
            if type(client4) == list and len(client4) > 0:
                placa(database_name2, client4)
                serv(database_name3, client4)
                ciclo(database_name3, client4)
                print("Transacción confirmada")
                bucle = False
            else:
                print()
                print("No existe un cliente asociado a este numero de identificación.")
                print()
        else:
            bucle = False
            
            
def placa(database_name, client):

    utils.clean_console()
    
    get_all(database_name)
    print()
    bucle = True
    while bucle:
        plate = input("Digite la placa del vehiculo que desea realizar el servicio: ")
        customer_vehicles = database.get_multi_database_data(
        database_name, "placa", plate)
        if type(customer_vehicles) == list and len(customer_vehicles) > 0:
            client[0].update(customer_vehicles[0])
            bucle = False
        else:
            print()
            print("No existe un vehiculo asociado a esta placa. ")
            print()
            
def serv(database_name, client):

    utils.clean_console()
    
    get_all(database_name)
    bucle = True
    while bucle:
        service1 = input("Digite el codigo del servicio que desea: ")
        vehicles_service = database.get_multi_database_data(
                database_name, "numero", service1)
        if type(vehicles_service) == list and len(vehicles_service) > 0:
            client[0].update(vehicles_service[0])
            bucle = False
        else:
            print()
            print("No existe un servicio asociado a este codigo. ")
            print()
    del client[0]["uid"]
    database.save_in_database(database_name4, client[0])
    Facturas.get_bills(client)

def ciclo(database_name, client):
    loop = True
    while loop:
        ask = input("Desea agregar otro servicio, Si o No? ")
        if ask.lower() == "si":
            serv(database_name, client)
        elif ask.lower() == "no":
            loop = False
        else:
            print("Debe responder Si o No")

def get_all(database_name):

    utils.clean_console()
    
    data = database.get_data_in_database(database_name)
    print()
    for i in data:
        keys = i.keys()
        for j in keys:
            print(str(j) + ": " + str(i[j]))
        print()
