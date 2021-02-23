def main():

	estudiantes = list()

	estudiantes_con_grupo = list()

	grupos_3_4 = list()

	f = open ('alumnos.txt','r')

	for line in f:
		estudiantes.append(line.strip())

	f.close()

	f2 = open ('grupos.txt','r')

	for line in f2:
		tmp = line.strip().split(";")
		n = len(tmp)-1

		if n < 3 or n > 4:
			grupos_3_4.append(tmp[0])

		for i in range(1,len(tmp)):
			if tmp[i] not in estudiantes_con_grupo:
				estudiantes_con_grupo.append(tmp[i])

	f2.close()

	grupos_3_4.sort()

	estudiantes_sin_grupo = list()

	for est in estudiantes:
		if est not in estudiantes_con_grupo:
			estudiantes_sin_grupo.append(est)

	estudiantes_sin_grupo.sort()

	print("Grupos sin 3 o 4 integrantes:")

	for grupo in grupos_3_4:
		print(grupo)

	print("Alumnos sin grupo:")

	for est in estudiantes_sin_grupo:
		print(est)

main()







