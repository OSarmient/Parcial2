from core.module import ModuleBase
from core.database import Database
from core.utils import clean_console

class Facturas(ModuleBase):  
    def __init__(self):
        self.database = Database("facturas")
        self.main_bucle = True
        self.main_field = "No Factura"
        
    def get_bills(self,client):
        self.database = Database("facturas")
        BD = self.database._count_database()
        if BD == False:
            BD = 0
        dic = {"No. Factura" : BD}
        dic.update(client[0])
        self.save(dic)
        print()
        print("Factura No " + str(BD) + " generada")
        print()     

    def hola(self):
        clean_console()
        self.database = Database("facturas")
        bill1 = self.database.get_data_in_database()
        loop = True
        v = True
        while loop:
            try: 
                iden = int(input("Digite el número de factura: "))
                print()
                for i in bill1:
                    if i["No. Factura"] == iden:
                        keys = i.keys()
                        for j in keys:
                            print(str(j) + ": " + str(i[j]))
                        print()
                        v = True
                        loop = False
                        break
                    else:
                        v = False
                if v == False:
                    print("No existe una factura registrada a este número")
            except:
                print("Vuelva a digitar el número de factura")
                
    def relation(self):
        bucle = True
        self.database = Database("clients")
        while bucle:

            print("Digite s en cualquier momento para salir.")
            client1 = str(
                input("Digite el numero de identificación del cliente: "))

            if client1.lower() != "s":
                client = int(client1)
                client4 = self.database.get_multi_by_property("No ID", client)
                if type(client4) == list and len(client4) > 0:
                    self.placa(client4)
                    self.serv(client4)
                    self.ciclo(client4)
                    print("Transacción confirmada")
                    bucle = False
                else:
                    print()
                    print("No existe un cliente asociado a este numero de identificación.")
                    print()
            else:
                bucle = False
                
                
    def placa(self, client):

        self.database = Database("vehicles")
        self.get_all()
        print()
        bucle = True
        while bucle:
            plate = input("Digite la placa del vehiculo que desea realizar el servicio: ")
            customer_vehicles = self.database.get_multi_by_property("placa", plate)
            if type(customer_vehicles) == list and len(customer_vehicles) > 0:
                client[0].update(customer_vehicles[0])
                bucle = False
            else:
                print()
                print("No existe un vehiculo asociado a esta placa. ")
                print()
                
    def serv(self, client):

        self.database = Database("service")
        self.get_all()
        bucle = True
        while bucle:
            service1 = int(input("Digite el codigo del servicio que desea: "))
            vehicles_service = self.database.get_multi_by_property("numero", service1)
            if type(vehicles_service) == list and len(vehicles_service) > 0:
                client[0].update(vehicles_service[0])
                bucle = False
            else:
                print()
                print("No existe un servicio asociado a este codigo. ")
                print()
        del client[0]["uid"]
        self.database = Database("service_asked")
        self.save(client[0])
        self.get_bills(client)

    def ciclo(self, client):
        loop = True
        while loop:
            ask = input("Desea agregar otro servicio, Si o No? ")
            if ask.lower() == "si":
                self.serv(client)
            elif ask.lower() == "no":
                loop = False
            else:
                print("Debe responder Si o No")