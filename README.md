# Menú principal

En este repositorio les voy a mostrar cómo se hace un algoritmo de menú sencillo para desplegar por pantalla el resultado:
```
import os
 
def menu():
	"""
	Función que limpia la pantalla y muestra nuevamente el menu
	"""
	os.system('cls') # NOTA para windows tienes que cambiar clear por cls
	print ("Selecciona una opción")
	print ("\t1 - Opción 1")
	print ("\t2 - Opción 2")
	print ("\t3 - Opción 3")
	print ("\t9 - Salir")
 
 
while True:
	# Mostraremos el menú principal:
	
	menu()
 
	# Solicitamos una opción al usuario:

	opcionMenu = input("INGRESE CUALQUIER NÚMERO >> ")
 
	if opcionMenu == "1":
		print ("")
		input("Has pulsado la opción 1...\nPresione cualquier tecla para continuar")
	elif opcionMenu == "2":
		print ("")
		input("Has pulsado la opción 2...\nPresione cualquier tecla para continuar")
	elif opcionMenu == "3":
		print ("")
		input("Has pulsado la opción 3...\nPreisone cualquier tecla para continuar")
	elif opcionMenu == "9":
		break
	else:
		print ("")
		input("Opción Inválida...\nPresione cualquier tecla para continuar")
```
