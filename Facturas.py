import database
import utils

database_name4 = "service_asked"
database_name5 = "Facturas"

def get_bills(client):
    BD = database.count_database(database_name5)
    if BD == False:
        BD = 0
    dic = {"No. Factura" : BD}
    dic.update(client[0])
    database.save_in_database2(database_name5, dic)
    print()
    print("Factura No " + str(BD) + " generada")
    print()
def get_allF():
    
    utils.clean_console()
    
    data = database.get_data_in_database(database_name5)
    for i in data:
        keys = i.keys()
        for j in keys:
            print(str(j) + ": " + str(i[j]))
        print("-----------------")

def hola():
    
    utils.clean_console()
    
    bill1 = database.get_data_in_database(database_name5)
    loop = True
    while loop:
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
