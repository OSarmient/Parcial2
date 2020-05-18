import database

database_name4 = "service_asked"
database_name5 = "Facturas"

def hola():
    price = 0                                               #Precio es 0
    bill = database.get_data_in_database(database_name4)    #llama un archivo
    iden = input("Digite su número de identificación: ")    #Mete el id
    for i in bill:                                          #Pasa por cada uno de los elementos del archivo
        for j in i:                                         #Pasa por los items de los elementos del archivo
            if j == ("noid1: " + iden):                     #Si el item es igual que el ID
                for x in i:                                 #Recorre lositems de los elementos del archivo
                     a = x[0:6]                              #
                     if a == ("precio"):
                        price += (int(x[8:len(x)]))
                price=("Valor Total = " + str(price))
                i.append(price)
                print(i)
                database.save_in_database2(database_name5, i)
                price = 0
                break
            else:
                print("No hay facturas registradas para este cliente")
                break
def get_allF():
    print()
    data = database.get_data_in_database(database_name5)
    for i in data:
        keys = i.keys()
        print("-----------------")
        for j in keys:
            print(str(j) + ": " + str(i[j]))
            print("-------------------")

#def fin_servicio(archivo):
#    data = {}
#    v
