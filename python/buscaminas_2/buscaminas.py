import random #para generar las bombas de  manera aleatoria
import pickle #para guardar y cargar archivos de manera estructurada
import time #para dar efecto de retardo cuando se gana o se pierde

def construirTablero(filas,columnas,bombas):
	"""
	Esta funcion construye el tablero que se le
	muestra al usuario y tambien el tablero
	interno donde se tienen ubicadas las bombas
	"""
	tablero = []

	for i in range(filas+1):
		tmp = []
	
		for j in range(columnas+1):
			if i==0:
				tmp.append(str(j))
			
			else:
				if j==0:
					tmp.append(str(i))
				else:
					tmp.append("#")
		tablero.append(tmp)

	tableroInterno = [[0 for i in range(filas)] for j in range(columnas)]
	listaBombas = []

	for k in range(bombas):
		nuevaBomba = (random.randint(0,filas-1),random.randint(0,columnas-1))
		
		while nuevaBomba in listaBombas:
			nuevaBomba = (random.randint(0,filas-1),random.randint(0,columnas-1))
		
		listaBombas.append(nuevaBomba)

	for x,y in listaBombas:
		tableroInterno[x][y] = 1
	return tablero,tableroInterno

def mostrarTablero(tablero):
	"""
	Esta funcion imprime el tablero que
	se le muestra al usuario
	"""
	for row in tablero:
		print(row)

def guardarPartida(vidas,bombas,tablero,tableroInterno,aciertos
	,totalSize,puntos,primeraGanada,destapadas):

	"""
	Esta funcion guarda la partida de un usuario
	en un archivo de texto llamado data.txt
	"""
	data = {}
	data["vidas"] = vidas
	data["bombas"] = bombas
	data["tablero"] = tablero
	data["tableroInterno"] = tableroInterno
	data["aciertos"] = aciertos
	data["totalSize"] = totalSize
	data["puntos"] = puntos
	data["primeraGanada"] = primeraGanada
	data["destapadas"] = destapadas

	archivo = open("data.txt","wb")
	pickle.dump(data,archivo)
	archivo.close()

def cargarPartida():
	"""
	Esta funcion carga los datos necesarios
	para reanudar la partida de un usuario
	desde el archivo data.txt
	"""
	archivo = open("data.txt","rb")
	data = pickle.load(archivo)
	#print(data)
	archivo.close()
	return (data["vidas"],
	data["bombas"],
	data["tablero"],
	data["tableroInterno"],
	data["aciertos"],
	data["totalSize"],
	data["puntos"],
	data["primeraGanada"],
	data["destapadas"] )


def iniciarJuego(nivel,nombre,cargar):
	"""
	Esta funcion tiene la lógica del juego
	"""
	if cargar==2:
		vidas,bombas,tablero,tableroInterno,aciertos,totalSize,puntos,primeraGanada,destapadas = cargarPartida()
	else:
		tablero = None
		bombas = None
		if nivel==1:
			bombas = 6
			n = 5
			tablero,tableroInterno = construirTablero(n,n,bombas)

		if nivel==2:
			bombas = 10
			n = 7
			tablero,tableroInterno = construirTablero(n,n,bombas)

		if nivel==3:
			n = 9
			bombas = 14
			tablero,tableroInterno = construirTablero(n,n,bombas)


		vidas = 3
		aciertos = 0
		totalSize = n*n
		destapadas = []
		puntos = 10
		primeraGanada = True

		guardarPartida(vidas,bombas,tablero,tableroInterno,aciertos
			,totalSize,puntos,primeraGanada,destapadas)

	n = len(tableroInterno)
	while (aciertos!=totalSize-bombas) and vidas > 0:
		mostrarTablero(tablero)

		fila = int(input("Selecciona la fila que deseas destapar:\n"))
		while fila < 1 or fila > n:
			print("Ingresa una posicion valida: entre {} y {}".format(1,n))
			fila = int(input("Selecciona la fila que deseas destapar:\n"))

		columna = int(input("Selecciona la columna que deseas destapar:\n"))
		while columna < 1 or columna > n:
			print("Ingresa una posicion valida: entre {} y {}".format(1,n))
			columna = int(input("Selecciona la columna que deseas destapar:\n"))

		if (fila,columna) not in destapadas:
			destapadas.append((fila,columna))

			gana = False
			if tableroInterno[fila-1][columna-1]==1:
				tablero[fila][columna] = ":("
			else:
				tablero[fila][columna] = "O"
				gana = True


			mostrarTablero(tablero)
			if gana:
				if primeraGanada==False:
					puntos = puntos + (puntos*1.1)
				primeraGanada = False
				print("--->BIEN JUGADO,CONTINUAS CON {} VIDAS<---".format(vidas))
				print("°°°° TU PUNTAJE ES: {}".format(puntos))
				aciertos +=1

			else:
				vidas -=1
				if vidas==0:
					print("\n\n")
					print(":( :( Se han acabado las vidas y con ello el juego :( :(")
					time.sleep(3)
					print("Así quedó tu tablero")
					mostrarTablero(tablero)
					print()
				else:
					print("--->BOMBAAA,TIENES {} VIDAS<---".format(vidas))
			guardarPartida(vidas,bombas,tablero,tableroInterno,aciertos
			,totalSize,puntos,primeraGanada,destapadas)
		else:
			print("Esa ya la destapaste, destapa otra")

	if vidas>0:
		print("\n\n")
		print(":) :) Felicitaciones  Ganaste :) :)")
		time.sleep(3)
		print("Así quedó tu tablero")
		mostrarTablero(tablero)
		print()




def menu():
	"""
	Esta función implementa el 
	menu de inicio del juego
	"""
	print("----Bienvenido a BuscaminasLab----")
	nombre = input("-------¿Cual es tu nombre?--------\n")
	print("--Genial {}, es hora de jugar!!----- \n".format(nombre))
	opcion = int(input("Selecciona el nivel: \n 1) Bajo\n 2) Medio\n 3) Alto\n"))
	
	while opcion!=0:
		cargar = int(input("1) Nueva Partida\n2) Cargar Partida\n"))
		iniciarJuego(opcion,nombre,cargar)
		print("Bienvenido a BuscaminasLab")
		nombre = input("¿Cual es tu nombre?\n")
		opcion = int(input("Selecciona el nivel o marca 0 para salir: \n 1) Bajo\n 2) Medio\n 3) Alto\n"))
		
menu()