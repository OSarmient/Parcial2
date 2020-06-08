import vehicles
import service
import clients
from bills import Facturas


class Main():
    def __init__(self):
        bucle = True    
        menu()
        while bucle:
            try:
                option = int(input("Digita la opción que desees ejecutar: "))
                print()
                if option == 1:
                    clients.start()
                    menu()
                elif option == 2:
                    vehicles.start()
                    menu()
                elif option == 3:
                    service.start()
                    menu()
                elif option == 4:
                    facturas.get_allF()
                    menu()
                elif option == 5:
                    facturas.hola()
                    menu()
                elif option == 6:
                    menu()
                elif option == 7:
                    bucle = False

                print()
            except NameError:
                print(NameError)
                print("7. Mostrar menú de modulos [7]")
                print("La opción digitada es invalida (debe ser un número en el menú).")
                print()
    
    def menu(self):
        print("---Menu de modulos----: ")
        print("1. Clientes. [1]")
        print("2. Vehiculos. [2]")
        print("3. Servicios. [3]")
        print("4. Mostar Facturas[4]")
        print("5. Buscar Facturas de un cliente [5]")
        print("6. Mostar menu. [6]")
        print("7. Salir [7]")
    
    inicio = Main()
    inicio.start()


        