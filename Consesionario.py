#try:
Archivo = open("Clientes.txt","w")
Archivo.write("Puto el que lo lea")
#finally:
Archivo.close()

with open("Clientes.txt","a") as Archivo:
    Archivo.write("\nEste es un texto de  prueva")

with open("Clientes.txt","r") as Archivo:
#=====================================#
#print(Archivo.readlines())
#=====================================#
    print(Archivo.read())
#=====================================#
#for linea in Archivo:  
#    print(linea)
#=====================================#
#    Archivo.close()
#=====================================#
def inputCliente():
    ID = input("Ingrese su numero de cedula: ") #El usuario ingresa su propiainformacion correspondiente
    ID=ID.ljust(12)
    name = input("Ingrese su primer nombre: ")
    name = name.ljust(10)
    lastname = input("Ingrese su primer apellido: ")
    lastname = lastname.ljust(11)
    address = input("Ingrese su direccion (Solo la de su calle):")
    address = address.ljust(20)
    phone = input("Ingrese su numero telefonico: ")
    phone = phone.ljust(10)
    city = input("Ingrese su ciudad de recidencia: ")
    client = ID + name + lastname + address + phone + city
    return client

def inputVehiculo():
    plate = input("Ingrese la placa de su vehiculo: ")
    plate = plate.ljust(7)



