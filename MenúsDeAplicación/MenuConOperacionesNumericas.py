menu = """
**********¡¡¡¡¡BIENVENIDO A LA SECCIÓN DE COMPUERTAS LÓGICAS PARTE 2!!!!!**********

ELIGE UN NÚMERO ENTRE EL 1 Y EL 4.

[1] ES UNA PUERTA LÓGICA "OR".
[2] ES UNA PUERTA LÓGICA "AND".
[3] ES UNA PUERTA LÓGICA "NAND".
[4] ES UNA PUERTA LÓGICA "XOR".

"""
print(menu)

opcion = input('ELIGE UNA OPCIÓN DEL 1 A 4: ')

if opcion == '1':
    print("")
    input("TRUE 'OR' FALSE = TRUE")

elif opcion == '2':
    print("")
    input("TRUE 'AND' FALSE = FALSE")

elif opcion == '3':
    print("")
    input("FALSE 'NAND' FALSE = TRUE")

elif opcion == '4':
    print("")
    input("TRUE 'XOR' TRUE = FALSE")

else:
    print('=-='* 15)
    print('DEBES INGRESAR UN NÚMERO ENTRE EL 1 Y EL 4!!!')
    print('=-='* 15)