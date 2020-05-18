import database

database_name4 = "service_asked"
database_name5 = "Facturas"

def get_bills(iden):
    price = 0                                               #Precio es 0
    BD = 0
    bill = database.get_data_in_database(database_name4)    #llama un archivo
    for i in bill:                                          #Pasa por cada uno de los elementos del archivo
        for j in i:                                         #Pasa por los items de los elementos del archivo
            if j == ("noid1: " + iden):                     #Si el item es igual que el ID
                for x in i:                                 #Recorre lositems de los elementos del archivo
                     a = x[0:6]                              #
                     if a == ("precio"):
                        price += (int(x[8:len(x)]))
                price=("Valor Total = " + str(price))
                i.append(price)
                BD = database.count_database(database_name5)
                i.insert(0, ("Factura No. " + str(BD)))
                database.save_in_database2(database_name5, i)
                price = 0
                break
        break
    
def get_allF():
    print()
    data = database.get_data_in_database(database_name5)
    for i in data:
        print("-----------------")
        print (i)
        print("-----------------")

def hola():
    iden = input("Digite su número de identificación: ")
    bill1 = database.get_data_in_database(database_name5)
    loop = True
    for i in bill1:
        while loop:
            for j in i:
                 if j == ("noid1: " + iden):
                    print(i)
                    loop = False
                    break
                 else:
                    loop = True
            break
        break
    if loop == True:
        print("No exite una factura asociada a este cliente")

#def fin_servicio(archivo):
#    data = {}
#    v
