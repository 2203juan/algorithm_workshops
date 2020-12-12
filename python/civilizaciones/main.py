
def leer_poblacion():
	poblacion = -1

	try:
		poblacion = int(input("Ingrese la cantidad de individuos en la población: "))

		if poblacion <= 0:
			5/0 # se fuerza una excepción para que ingrese los valores adecuados
	except:
		print("Por favor ingresa un entero positivo")
		poblacion = leer_poblacion()

	return poblacion

def leer_recursos():
	recursos = -1

	try:
		recursos = int(input("Ingrese la cantidad de recursos en la población: "))
		if recursos < 0:
			5/0 # se fuerza una excepción para que ingrese los valores adecuados
	except:
		print("Por favor ingresa un entero >= 0")
		recursos = leer_recursos()

	return recursos

def leer_comida():
	comida = -1

	try:
		comida = int(input("Ingrese la cantidad de comida en la población: "))
		if comida < 0:
			5/0 # se fuerza una excepción para que ingrese los valores adecuados
	except:
		print("Por favor ingresa un entero >= 0")
		comida = leer_comida()

	return comida

def leer_nivel():
	nivel = ""

	try:
		nivel = input("Ingrese el nivel de la población (edad media, feudal, castillos o imperial.)  : ")
		nivel = nivel.lower()
		
		if ( nivel != "edad media" and nivel!= "feudal" and nivel!= "castillos" and nivel!="imperial"):
			5/0 # se fuerza una excepción para que ingrese los valores adecuados

	except:
		print("Por favor ingresa un nivel valido: edad media, feudal, castillos o imperial")
		nivel = leer_nivel()

	return nivel

def leer_opcion():
	opcion = -1

	try:
		opcion = int(input("Seleccione una opcion:\n1) Registrar Civilización\n2) Mostrar Civilización con más Recursos\n0) Salir\n"))
		
		if opcion!=0 and opcion!=1 and opcion!=2:
			5/0 # se fuerza una excepción para que ingrese los valores adecuados
	except:
		print("Por favor ingresa un entero de los mostrados anteriormente")
		opcion = leer_opcion()

	return opcion

def registrar_civilizacion():
	nombre = input("Ingrese el nombre de la civilización: ")
	poblacion = leer_poblacion()
	recursos = leer_recursos()
	comida = leer_comida()
	nivel = leer_nivel()

	nombre_archivo = input("Ingrese el nombre que quiere que tenga el archivo (ejemplo -> archivo_1) : ")

	civilizacion = {"Nombre": nombre, "Poblacion": poblacion, "Recursos": recursos, "Comida": comida, "Nivel": nivel}
	
	f = open(nombre_archivo + ".txt","w")
	f.write( str(civilizacion) )
	f.close()

def cargar_civilizacion(civilizacion):

	file = open(civilizacion + ".txt", "r")

	contents = file.read()

	contents = eval(contents) # para que python reconozca el diccionario guardado en el archivo

	return contents




def leer_dos_civilizaciones():
	civilizacion_1 = input("Ingrese el nombre de la civilización 1 (ejemplo -> archivo_1) : ")
	civilizacion_2 = input("Ingrese el nombre de la civilización 2 (ejemplo -> archivo_2) : ")

	civilizacion_1 = cargar_civilizacion(civilizacion_1)
	civilizacion_2 = cargar_civilizacion(civilizacion_2)

	print("El nombre y la cantidad de poblaciond de la civilizacion que posee mayor cantidad de recursos es:\n")

	nombre_civ = civilizacion_1["Nombre"]
	cantidad_pob = int(civilizacion_1["Poblacion"])

	if int(civilizacion_1["Recursos"]) < int(civilizacion_2["Recursos"]):
		nombre_civ = civilizacion_2["Nombre"]
		cantidad_pob = int(civilizacion_2["Poblacion"])

	print(nombre_civ, cantidad_pob)

def menu():
	opcion = 1
	print("Bienvenido a Ages of Empires")
	
	while opcion != 0:
	
		opcion = leer_opcion()

		if opcion == 1:
			registrar_civilizacion()
		
		if opcion == 2:
			leer_dos_civilizaciones()
menu()


 