def main():

	f = open ('grupos_arreglados.txt','r')
	grupos = list()
	
	for line in f:
		grupos.append(line.strip().split(";"))


	f2 = open ('notas_grupos.txt','r')
	notas = list()

	for line in f2:
		grupo_nota = line.strip().split(";")

		for grupo in grupos:
			if grupo[0] == grupo_nota[0]:
				for i in range(1, len(grupo)):
					notas.append((grupo[i], float(grupo_nota[1])))

	notas = sorted(notas, key=lambda tup: (tup[1], tup[0]))

	f3 = open ('notas.txt','w')
	#f3.write("Contenidos del archivo notas.txt\n")
	for x,y in notas:
		f3.write(x+";"+str(y)+"\n")
	f3.close()

main()