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
    print("5. Buscar Factura [5]")
    print("6. Mostar menu. [6]")
    print("7. Salir [7]")


bucle = True
show_menu()
while bucle:
    try:
        option = int(input("Digita la opción que desees ejecutar: "))
        print()
        if option == 1:
            clients.start1()
            show_menu()
        elif option == 2:
            vehicles.start()
            show_menu()
        elif option == 3:
            service.startS()
            show_menu()
        elif option == 4:
            Facturas.get_allF()
            show_menu()
        elif option == 5:
            Facturas.hola()
            show_menu()
        elif option == 6:
            show_menu()
        elif option == 7:
            bucle = False

        print()
    except NameError:
        print(NameError)
        print("7. Mostrar menú de modulos [7]")
        print("La opción digitada es invalida (debe ser un número en el menú).")
        print()
