import random

def crear_tablero_numerado(n, m, tablero):
 	"""
	Esta funcion sirve para contar la cantidad de minas alrededor de una casilla que no es bomba
	y armar un tablero de referencia que va a servir para desarrollar la logica del juego	
 	"""
 	for fila in range(n):
 		for columna in range(m):
 			# si hay una mina no hay necesidad de contar esa celda
 			if tablero[fila][columna] != "b":
 				# revisar arriba
 				if fila > 0 and tablero[fila-1][columna] == "b":
 					tablero[fila][columna] = tablero[fila][columna] + 1
 				# revisar abajo    
 				if fila < n-1  and tablero[fila+1][columna] == "b":
 					tablero[fila][columna] = tablero[fila][columna] + 1
 				# revisar a la izquierda
 				if columna > 0 and tablero[fila][columna-1] == "b":
 					tablero[fila][columna] = tablero[fila][columna] + 1
 				# revisar a la derecha
 				if columna < m-1 and tablero[fila][columna+1] == "b":
 					tablero[fila][columna] = tablero[fila][columna] + 1
 				# revisar la esquina superior izquierda    
 				if fila > 0 and columna > 0 and tablero[fila-1][columna-1] == "b":
 					tablero[fila][columna] = tablero[fila][columna] + 1
 				# revisar la esquina superior derecha
 				if fila > 0 and columna < m-1 and tablero[fila-1][columna+1]== "b":
 					tablero[fila][columna] = tablero[fila][columna] + 1
 				# revisar la esquina inferior izquierda
 				if fila < n-1 and columna > 0 and tablero[fila+1][columna-1] == "b":
 					tablero[fila][columna] = tablero[fila][columna] + 1
 				# revisar la esquina inferior derecha
 				if fila < n-1 and columna< m-1 and tablero[fila+1][columna+1]== "b":
 					tablero[fila][columna] = tablero[fila][columna] + 1
 	return tablero

def iniciar_tablero(filas, columnas, cantidad_minas):
	"""
	Esta funcion recibe por parametro la cantidad de filas, columnas y minas que debe tener el tablero,
	retorna una matriz que se compone de 1's y 0's, donde 1 representa que en esa posicion existe una mina
	y 0 que no
	"""

	tablero = list() # matriz que representa el tablero del juego

	# En este ciclo inicializamos el tablero en 0 (fila por fila)
	for i in range(filas):
		lista_temporal = list()
		for j in range(columnas):
			lista_temporal.append(0)
		tablero.append(lista_temporal)

	# mientras haya minas por asignar
	while cantidad_minas > 0:
		posicion_x = random.randint(0, filas - 1) # fila en la que se va a poner la mina
		posicion_y = random.randint(0, columnas - 1) # columna en la que se va a poner la mina
		
		while tablero[posicion_x][posicion_y] == "b": # mientras se genere  una fila y columna que ya tienen mina
			posicion_x = random.randint(0, filas - 1)
			posicion_y = random.randint(0, columnas - 1) 
		
		tablero[posicion_x][posicion_y] = "b" # se asigna la mina
		cantidad_minas -=1 # se cuenta una mina menos por asignar

	return tablero


def jugar(tablero, filas, columnas, numero_jugadas):
	fin_juego = False
	bomba = False
	minas_encontradas = 0
	jugadas = numero_jugadas
	tablero_usuario = list()

	# creamos el tablero que se le va a mostrar al usuario mientras juega
	for i in range(filas):
		tmp = list()
		for j in range(columnas):
			tmp.append("*") 
		tablero_usuario.append(tmp)

	print("Bienvenido al juego de Buscaminas")
	print()
	imprimir_tablero(tablero_usuario)

	# mientras aun tenga jugadas y no haya encontrado ninguna mina
	while not fin_juego and not bomba:
		fila, columna = int(input("Ingrese la fila entre {} y {}\n".format(0, filas - 1))), int(input("Ingrese la columna entre {} y {}\n".format(0,columnas - 1)))

		if tablero_usuario[fila][columna] != "*":# si hay algo diferente a * entonces ya la destapo
			print("Esa celda ya la destapaste!!")
		else:
			if tablero[fila][columna] == "b":
				print("LÁSTIMA, CAÍSTE EN UNA BOMBA!!")
				imprimir_tablero(tablero)
				print("-----GAME OVER--------")

				bomba = True
			else:
				tablero_usuario[fila][columna] = tablero[fila][columna] # copio el valor del tablero en el tablero del usuario ( para mostrarle la cantidad de minas que tiene alrededor)
				jugadas -=1

				fin_juego = jugadas == 0

				mostrar = int(input("Quiere ver el tablero? \n1) Si\n2) No\n"))

				if mostrar == 1:
					imprimir_tablero(tablero_usuario)

	if jugadas >= 0 and not bomba:
		print("Felicitaciones, ganaste!!")
	guardar_tablero(tablero_usuario)


def imprimir_tablero(tablero):
	"""
	Esta funcion sirve para imprimir el tablero que se recibe por parametro
	"""
	for i in range(len(tablero)):
		for j in range(len(tablero[i])):
			print(tablero[i][j], end = "\t")
		print()

def guardar_tablero(tablero):
	"""
	Esta funcion sirve para guardar el tablero del usuario en un archivo de texto
	lla,ado juego.txt
	"""
	archivo = open('juego.txt', 'w')
	cadena = ""
	
	for fila in tablero:
		cadena += (str(fila)+"\n")
	archivo.write(cadena)

	archivo.close()
def main():
	filas = int(input("Ingrese la cantidad de filas del tablero\n"))
	columnas = int(input("Ingrese la cantidad de columnas del tablero\n"))
	cantidad_minas = int(input("Ingrese la cantidad de minas que desea\n"))
	numero_jugadas = int(input("Ingrese la cantidad de jugadas que desea realizar\n"))


	tablero_con_minas = iniciar_tablero(filas, columnas, cantidad_minas)
	tablero_numerado = crear_tablero_numerado(filas, columnas, tablero_con_minas)

	jugar(tablero_numerado, filas, columnas, numero_jugadas)

main()