import math
# punto 4

nombre = input("Ingrese el nombre: ")
nem = float(input("Ingrese el NEM: "))
rank = float(input("Ingrese el Ranking: "))
psu_leng = float(input("Ingrese su puntaje en PSU Lenguaje y Comunicación: "))
psu_mat = float(input("Ingrese su puntaje en PSU Matemáticas: "))
psu_cien = float(input("Ingrese su puntaje en PSU CIENCIAS: "))
print()
print("Nombre: ", nombre)
pond = nem*0.1 + rank*0.2 + psu_leng*0.1 + psu_mat*0.5 + psu_cien*0.1
print("Puntaje ponderado con el que se postula: ", pond)