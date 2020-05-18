import database

database_name4 = "service_asked"
database_name5 = "Facturas"

def hola():
    price = 0
    bill = database.get_data_in_database(database_name4)
    iden = input("Digite su número de identificación: ")
    for i in bill:
        for j in i:
            if j == ("noid1: " + iden):
                for x in i:
                    a = x[0:6]
                    if a == ("precio"):
                        price += (int(x[8:len(x)]))
                price=("Valor Total = " + str(price))
                i.append(price)
                print(i)
                database.save_in_database2(database_name5, i)
                price = 0
                
hola()
