
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
    mark = input("Ingrese la marca del vehiculo: ")
    mark = mark.ljust(13)
    model = input("Ingrese el modelo del vehiculo")
    model = model.ljust(20)
    displacement = input("Ingrese el cilindraje del vehiculo: ")
    displacement = displacement.ljust(5)
    color = input("Ingrese el color de su vehiculo: ")
    color = color.ljust(15)
    serviceV = input("Ingrese que tipo de servicio presta su vehiculo (particular/publico): ")
    serviceV = serviceV.ljust(11)
    NPassengers = input("Ingrese cuanta capasidad de pasajeros tiene su vehiculo: ")
    NPassengers= NPassengers.ljust(2)
    LCapacity = input("Ingrese cuanta caraga puede soportar el vehiculo (Toneladas): ")
    LCapacity = LCapacity.ljust(2)
    NChassis = input("Ingrese el numero correspondiente al chasis de su vehiculo: ")
    NChassis = NChassis.ljust(17)
    NMotor = input("Ingrese el numero correspondiente al motor de su vehiculo: ")
    NMotor = NMotor.ljust(6)
    vehicle = plate + mark + model + displacement + color +serviceV + NPassengers + LCapacity + NChassis + NMotor
    return vehicle

def inputServicio():
    #check =""
    #while check != ("c" or "n"):
        #check = input("¿Usted conoce el codigo o sabe el nombre del servio que va a pedir? (C[codigo]/N[nombre])")
        #if check.lower() == "c":
    CServicio = input("Ingrese el codigo correspondiente al servicio que desea \n|654321|\n|214365|\n|123456|\n|563412|\n|162534|\n")
    CServicio = CServicio.ljust(6)
            #break
        #elif check.lower() == "n":
    NServicio = input("Ingrese el nombre del servicio que desea \n| Cambio de Aceite |\n| Mantenimiento Mecanico |\n| Electricidad Automotriz |\n| Frenos |\n| Latoneria y Puntura |\n")
    NServicio = NServicio.ljust(25)
            #break
        #else:
            #print("Por favor hagalo de nuevo.")                     
    PUnitario = input("Ingrese el precio por hora del servicio solicitado: ")
    PUnitario = PUnitario.ljust(7)
    HServicio = input("Ingrese por cuantas horas va a soliitar el servicio: ")
    HServicio = HServicio.ljust(2)

