class Vehicle:

    __database_name = "vehicles"

    def __show_menu(self):
        print()
        print(" ---- Menu (vehiculos) ---- ")
        print()
        print("1. Agregar un carro [1]")
        print("2. Ver todos los carros [2]")
        print("3. Buscar carros de un cliente [3]")
        print("4. Eliminar un vehiculo por su placa [4]")
        print("5. Mostrar menú [5]")
        print("6. Salir [6]")
        print()

    def start(self):
        print("start")


vehicle = Vehicle()
vehicle.start()
