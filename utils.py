from os import system
import platform

def clean_console():
    if platform.system() == "Linux":
        system("clear")
    else:
        system("cls")
