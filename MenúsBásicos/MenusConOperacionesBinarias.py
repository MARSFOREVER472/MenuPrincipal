main = """
**********¡¡¡¡¡BIENVENIDO A LA SECCIÓN DE COMPUERTAS LÓGICAS PARTE 1!!!!!**********

ELIGE UN NÚMERO ENTRE EL 1 Y EL 3.

[1] ES UNA PUERTA LÓGICA "OR".
[2] ES UNA PUERTA LÓGICA "AND".
[3] ES UNA PUERTA LÓGICA "NAND".

"""
print(main)

option = input('ENTER A OPTION 1 TO 3: ')

if option == '1':
    print("")
    input("TRUE 'OR' FALSE = TRUE")

elif option == '2':
    print("")
    input("TRUE 'AND' FALSE = FALSE")

elif option == '3':
    print("")
    input("FALSE 'NAND' FALSE = TRUE")

else:
    print('=-='* 20)
    print('YOU MUST ENTER A NUMBER BETWEEN 1 A 3!!!')
    print('=-='* 20)