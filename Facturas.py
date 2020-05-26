import database
import utils

database_name4 = "service_asked"
database_name5 = "Facturas"

def get_bills(client):
    BD = database.count_database(database_name5)
    if BD == False:
        dic = {"No. Factura" : 0}
    else:
        dic = {"No. Factura" : BD}
    dic.update(client[0])
    database.save_in_database2(database_name5, dic)
    
def get_allF():
    
    utils.clean_console()
    
    data = database.get_data_in_database(database_name5)
    for i in data:
        print("-----------------")
        print (i)
        print("-----------------")

def hola():
    
    utils.clean_console()
    
    bill1 = database.get_data_in_database(database_name5)
    loop = True
    while loop:
        iden = input("Digite su número de identificación: ")
        for i in bill1:
            if i["noid1"] == iden:
                keys = i.keys()
                for j in keys:
                    print(str(j) + ": " + str(i[j]))
                print()
                loop = False
            else:
                print("No existe una factura asociada a este cliente")
                break
