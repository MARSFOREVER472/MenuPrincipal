# ESTE ES LA VERSIÓN 2 DEL MENÚ PRINCIPAL.

import os

def main():
    """
    FUNCIÓN QUE LIMPIA LA PANTALLA Y MUESTRA EL MAIN
    """
    os.system('cls') # SUGERENCIA: Para Windows 10 u 11 tienes que cambiarlo a 'clear' por un 'cls'
    print("INGRESE UNA OPCIÓN: ")
    print("\t1 - Opción 1 - BALAZO ES CON 'B' DE BURRO")
    print("\t2 - Opción 2 - VASO ES CON 'V' CORTA")
    print("\t3 - SALIR")

while True:
    # MOSTRAREMOS EL MAIN PRINCIPAL:

    main()

    # SOLICITAREMOS UNA OPCIÓN AL USUARIO:

    mainOptions = input("INGRESE UN NÚMERO >> ")

    if mainOptions == "1":
        print("")
        input("OPCIÓN 1 - FALSO\nPRESS ANOTHER KEY TO CONTINUE...")
    elif mainOptions == "2":
        print("")
        input("OPCIÓN 2 - VERDADERO\nPRESS ANOTHER KEY TO CONTINUE...")
    elif mainOptions == "3":
        break
    else:
        print("")
        input("PARÁMETROS INCORRECTOS...\nTRY AGAIN!!!")