import database

#servicios 2

database_name = "clients"
database_name2 = "vehicles"
database_name3 = "service"
database_name4 = "Facturas"


def relation():
    data = []
    bucle = True
    while bucle:

        print("Digite s en cualquier momento para salir.")
        client1 = str(
            input("Digite el numero de identificación del cliente: "))

        if client1.lower() != "s":
            client4 = database.get_multi_database_data(
                database_name, "noid1", client1)
            if type(client4) == list and len(client4) > 0:
                serv(database_name3)
                get_vehicles1(database_name2, client1)
                plate1 = input("Digite la placa del vehiculo que desea realizar el servicio: ")
                placa(database_name2, client1, plate1, data)
                
                bucle = False
            else:
                print()
                print("No existe un cliente asociado a este numero de identificación.")
                print()
        else:
            bucle = False
            
def get_vehicles1(database_name, customer_id):
    bucle = True
    while bucle:

        if customer_id.lower() != "s":
            customer_vehicles = database.get_multi_database_data(
                database_name, "cliente", customer_id.ljust(12))
            if type(customer_vehicles) == list and len(customer_vehicles) > 0:
                print()
                print("Existen " + str(len(customer_vehicles)) +
                      " vehiculos asociados a este numero de indentificación.")
                for i in customer_vehicles:
                    print("----------------")
                    print(str([i][0]["marca"]) + ": " + str([i][0]["placa"]))
                    print("----------------")
                print()
                bucle = False
            else:
                print()
                print("No existen vehiculos asociados a este numero de identificación.")
                print()
                customer_id = str(
                    input("Digite el numero de identificación del cliente: "))
        else:
            bucle = False
            
def placa(database_name, customer_id, plate, data):
    bucle = True
    while bucle:
        customer_vehicles = database.get_multi_database_data(
        database_name, "cliente", customer_id.ljust(12))
        customer_plate = "s"
        for i in range(len(customer_vehicles)): 
            customer_plate = customer_vehicles[i]["placa"]
            vehicle_list = customer_vehicles[i]
            if plate == customer_plate:
                print()
                print("Transacción confirmada")
                print()
                bucle = False
                break
        if plate!=customer_plate:
            print()
            print("No existen vehiculos asociados a esta placa")
            print()
            plate = input("Digite la placa del vehiculo que desea realizar el servicio: ")
    del vehicle_list["cliente"]
    insert_list(vehicle_list, data)
    print(data)
    
def serv(database_name):
    get_all(database_name)
    bucle = True
    while bucle:
        service1 = input("Digite el codigo del servicio que desea: ")
        vehicles_service = database.get_multi_database_data(
                database_name, "numero_servicio", service1)
        if type(vehicles_service) == list and len(vehicles_service) > 0:
            print()
            bucle = False
        else:
            print()
            print("No existe un servicio asociado a este codigo. ")
            print()
        
def insert_list(lista, data):
    for i in lista:
        keys = i.keys()
        for j in keys:
            data.append(str(j) + ": " + str(i[j]))

def get_all(database_name):
    data = database.get_data_in_database(database_name)
    print()
    for i in data:
        keys = i.keys()
        for j in keys:
            print(str(j) + ": " + str(i[j]))
    print()
            
relation()

    
