
def buscar_horizontal_y_vertical(sopa, palabras):
	ans = list()



	for palabra in palabras:
		
		# busqueda horizontal
		for i in range(len(sopa)):
			#print(palabra, sopa[i])
			if palabra in "".join(sopa[i]):
				a_buscar = palabra[0]
				for j in range(len(sopa[i])):
					if sopa[i][j] == a_buscar and sopa[i][j+1] == palabra[1]:
						ans.append([i,j])
						break

		
		# busqueda vertical
		for j in range(len(sopa)):
			col = list()
			for i in range(len(sopa[j])):
				col.append(sopa[i][j])

			if palabra in "".join(col):
				for i in range(len(col)):
					if col[i] == palabra[0] and col[i+1] == palabra[1]:
						ans.append([i,j])
						break

	return ans






def main():
	sopas = [['P', 'O', 'P', 'F', 'C', 'E', 'N'],
			 ['Y', 'U', 'U', 'R', 'U', 'O', 'O'],
			 ['T', 'A', 'P', 'T', 'I', 'R', 'U'],
			 ['H', 'P', 'T', 'C', 'P', 'N', 'T'],
			 ['O', 'U', 'N', 'E', 'C', 'U', 'T'],
			 ['N', 'U', 'Y', 'A', 'U', 'P', 'T'],
			 ['F', 'R', 'E', 'T', 'U', 'R', 'N']
		    ]

	palabras = ["PYTHON", 
				"PRINT",
				"OUTPUT",
				"RETURN",
				"FUNCION"]
	print(buscar_horizontal_y_vertical(sopas, palabras))
main()