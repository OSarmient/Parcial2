import database

#servicios 2

database_name = "clients"
database_name2 = "vehicles"
database_name3 = "service"
database_name4 = "service_asked"


def relation():
    data = []
    bucle = True
    while bucle:

        print("Digite s en cualquier momento para salir.")
        client1 = str(
            input("Digite el numero de identificación del cliente: "))

        if client1.lower() != "s":
            client4 = database.get_multi_database_data2(
                database_name, "noid1", client1)
            if type(client4) == list and len(client4) > 0:
                insert_list(client4, data)
                get_vehicles1(database_name2, client1)
                plate1 = input("Digite la placa del vehiculo que desea realizar el servicio: ")
                placa(database_name2, client1, plate1, data)
                serv(database_name3, data)
                ciclo(database_name3,data)
                print("Transacción confirmada")
                database.save_in_database2(database_name4, data)
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
            customer_vehicles = database.get_multi_database_data2(
                database_name, "cliente", customer_id)
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
        customer_vehicles = database.get_multi_database_data2(
        database_name, "cliente", customer_id)
        customer_plate = "s"
        for i in range(len(customer_vehicles)): 
            customer_plate = customer_vehicles[i]["placa"]
            vehicle_list = customer_vehicles[i]
            if plate == customer_plate:
                print()
                bucle = False
                break
        if plate!=customer_plate:
            print()
            print("No existen vehiculos asociados a esta placa")
            print()
            plate = input("Digite la placa del vehiculo que desea realizar el servicio: ")
    del vehicle_list["cliente"]
    ve_li=[]
    ve_li.append(vehicle_list)
    insert_list(ve_li, data)
    
def serv(database_name, data):
    get_all(database_name)
    bucle = True
    while bucle:
        service1 = input("Digite el codigo del servicio que desea: ")
        vehicles_service = database.get_multi_database_data2(
                database_name, "numero_servicio", service1)
        if type(vehicles_service) == list and len(vehicles_service) > 0:
            print()
            bucle = False
        else:
            print()
            print("No existe un servicio asociado a este codigo. ")
            print()
    insert_list(vehicles_service, data)

def ciclo(database_name, data):
    loop = True
    while loop:
        ask = input("Desea agregar otro servicio, Si o No? ")
        if ask.lower() == "si":
            serv(database_name, data)
        elif ask.lower() == "no":
            loop = False
        else:
            print("Debe responder Si o No")
            ask = input("Desea agregar otro servicio, Si o No? ")

def insert_list(lista, data):
    for i in lista:
        keys = i.keys()
        for j in keys:
            data.append(str(j) + ": " + str(i[j]))
    data.pop()

def get_all(database_name):
    data = database.get_data_in_database(database_name)
    print()
    for i in data:
        keys = i.keys()
        for j in keys:
            print(str(j) + ": " + str(i[j]))
    print()
            
relation()
