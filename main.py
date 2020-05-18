import vehicles
import clients
import service
import Facturas


def show_menu():
    print("---Menu de modulos----: ")
    print("1. Clientes. [1]")
    print("2. Vehiculos. [2]")
    print("3. Servicios. [3]")
    print("4. Mostar Facturas[4]")
    print("5. Mostar opciones. [5]")
    print("6. Salir [6]")


bucle = True
show_menu()
while bucle:
    try:
        option = int(input("Digita la opción que desees ejecutar: "))
        print()
        if option == 1:
            clients.start1()
        elif option == 2:
            vehicles.start()
        elif option == 3:
            service.startS()
        elif option == 4:
            Facturas.get_allF()
        elif option == 5:
            show_menu()
        elif option == 6:
            bucle = False
        print()
    except NameError:
        print(NameError)
        print("5. Mostrar menú de modulos [5]")
        print("La opción digitada es invalida (debe ser un número en el menú).")
        print()
