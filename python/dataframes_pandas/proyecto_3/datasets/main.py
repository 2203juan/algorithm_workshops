from os import lstat
import pandas as pd
import matplotlib.pyplot as plt


##################  FUNCIONES TEMPERATURA  #######################


archivos = ['metropolitana_act.xls', 'atacama_80.xls', 'arica_parinacota_act.xls', 'valparaiso_act.xls', 'tarapaca_act.xls', 'los_rios_act.xls', 'o_higgins_80.xls', 'antofagasta_act.xls', 'magallanes_80.xls', 'coquimbo_act.xls', 'biobio_80.xls', 'biobio_act.xls', 'arica_parinacota_80.xls', 'coquimbo_80.xls', 'antofagasta_80.xls', 'maule_80.xls', 'araucania_act.xls', 'araucania_80.xls', 'magallanes_act.xls', 'atacama_act.xls', 'o_higgins_act.xls', 'valparaiso_80.xls', 'aysen_act.xls', 'tarapaca_80.xls', 'los_lagos_act.xls', 'aysen_80.xls', 'los_rios_80.xls', 'metropolitana_80.xls', 'los_lagos_80.xls', 'maule_act.xls']




#lectura csv
def lectura_csv_3(dataset):
     data= pd.read_csv(dataset,encoding="latin-1", sep  =",", header=0)
     return data

# Promedio
def promedio_3(lista):
     n = len(lista)
     suma = 0

     for elem in lista:
          if str(elem)!="nan":
               suma +=elem
     return round(suma/n,2)

def reemplazar_nan_3(lista, valor):
     for i in range(len(lista)):
          if str(lista[i]) == "nan":
               lista[i] = valor
     return lista               

# Mínimo
def minimo_3(lista_promedio):
     menor = lista_promedio[0]
     for n in lista_promedio:
          if n < menor:
               menor = n
     return menor

# Máximo
def maximo_3(lista_promedio):
     mayor = lista_promedio[0]
     for n in lista_promedio:
          if n > mayor:
               mayor = n
     return mayor


op = 1
print("Hola, por favor selecciona un archivo a procesar")

for i in range(len(archivos)):
     print(i,"-->",archivos[i])

op = int(input())

file = archivos[op]

meses = ["ENE","FEB","MAR","ABR","MAY","JUN","JUL","AGO","SEP","OCT","NOV","DIC"]

mes_op = "ENE"

print("Seleccione el mes de interes: ")

for i in range(len(meses)):
     print(i,"-->",meses[i])

mes_op = meses[int(input())]


df = lectura_csv_3(file)

df_mes = list(df[mes_op])

# buscamos el promedio 
prom = promedio_3(df_mes)

# en caso de que haya nans se actualizan con el promedio
df_mes = reemplazar_nan_3(df_mes, prom)

# ahora ya se asegura que no hay nan, podemos hacer todos los calculos normal

# Se obtiene el promedio
prom = promedio_3(df_mes)
print("El promedio es: ", prom)

# Se obtiene el máximo
maximo_valor = maximo_3(df_mes)
print("El valor máximo es: ", maximo_valor)

# Se obtiene el mínimo
minimo_valor = minimo_3(df_mes)
print("El valor mínimo es: ", minimo_valor)

# grafico precipitaciones vs dias del mes
lista_dias = [ i+1 for i in range(len(df_mes))]
df_grafico = {"número de día":lista_dias,"prec":df_mes}
data_frame = pd.DataFrame(df_grafico)
data_frame.plot(kind = "bar", x = "número de día" , y ="prec",color = "green", title="día v/s precipitacion")
plt.show()


op = print("Desea leer un txt?")
print("1) Si\n2) No")
op = int(input())
if op == 1:
     try:
          print("La informacion del archivo es:")
          print()
          f = open(input("Ingrese el nombre del archivo: ")+".txt","r")
          for line in f:
               print(line)
     except:
          print("El archivo no existe")



