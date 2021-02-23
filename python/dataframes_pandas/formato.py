import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


#FUNCIONES
#lectura csv
def lectura_csv(temp_2018):
     data= pd.read_csv(temp_2018, sep=";", encoding="latin-1",skiprows=[0,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49],
                       usecols=["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"])
     return data

#establecer la cantidad de elementos de la lista
def largo_list(lista_promedio):
     contador= 0
     for x in lista_promedio:
          contador= contador + 1
     return contador

#calcular el promedio del mes escogido
def calculo_prom(lista_promedio):
     suma= 0
     for x in lista_promedio:
         suma = suma + x
     promedio= suma/largo_list(lista_promedio)
     promedio1= round(promedio,2)
     return promedio1

#calcular el valor mínimo del mes escogido
def minimo(lista_promedio):
     menor = lista_promedio[0]
     for n in lista_promedio:
          if n < menor:
               menor = n
     return menor

#calcular el valor máximo del mes escogido
def maximo(lista_promedio):
     mayor = lista_promedio[0]
     for n in lista_promedio:
          if n > mayor:
               mayor = n
     return mayor

#construir lista con número de días del mes
def list_dias(lista_promedio):
     dias_mes = []
     contador= 1
     for x in lista_promedio:
          dias_mes.append(contador)
          contador= contador + 1
     return dias_mes

#archivo
temp_2018= r"C:\Users\nicol\Desktop\Nico Universidad\segundo semestre\FCyP\tarea semana 7\temperatura 2018.csv"

titulo= "Temperaturas año 2018"
print(titulo.center(190, " "))
print(" programa para calcular el promedio, valor más bajo y más alto entre las máximas temperaturas de cada mes, a partir de la siguiente tabla de mediciones diarias")
print("                      ")
#variable retornada desde función lectura dataframe   
df_2018= lectura_csv(temp_2018)

print(df_2018)
#lista con los nombres de cada columna (se elimina la primera, ya que no tenía ningún nombre
lista= df_2018.columns[0:13].values.tolist()
print("                      ")
print("las opciones son: ",lista)
print("                      ")

#selección del mes del que desea realizar el promedio
mes =input("Por favor, digite las 3 letras iniciales del mes que desea promediar:")
#convierte los carácteres de entrada en minúscula
mes_minus= mes.lower()
#convierte el primer carácter de la entrada en mayúscula
mes_prim_mayus= mes_minus.capitalize()

#control de selección de mes (evita inexistencias o faltas ortográficas)
while mes_prim_mayus not in lista: 
     print("NO EXISTEN COINCIDENCIAS")
     mes =input("Por favor, digite las 3 letras iniciales del mes que desea promediar:")
     mes_minus= mes.lower()
     mes_prim_mayus= mes_minus.capitalize()
#muestra selección del mes    
else:
     #diccionario para establecer nombre completo del mes
     meses= {"Ene":"Enero", "Feb":"Febrero", "Mar":"Marzo", "abr":"Abril", "May":"Mayo", "Jun":"Junio", "Jul":"Julio", "Ago":"Agosto", "Sep":"Septiembre", "Oct":"Octubre", "Nov":"Noviembre", "Dic":"Diciembre"}
     print("                      ")
     print("el mes escogido es: ", meses[mes_prim_mayus])

#construye una lista con el mes escogido
lista_promedio_NaN= list(df_2018[mes_prim_mayus])
#filtra los datos nulos dentro de la lista
lista_promedio = [x for x in lista_promedio_NaN if str(x) != 'nan']

#variable retornada desde función largo_list
largo_lista= largo_list(lista_promedio)

#retorno de la función que calcula el promedio
promedio= calculo_prom(lista_promedio)

if mes_prim_mayus in meses:
     mes=(meses[mes_prim_mayus])
print("                      ")
print("el promedio de la temperatura máxima para el mes de ", mes," es de:", promedio,"°")

#retorno de la función que encuentra el valor de la temperatura mínima
temp_minima = minimo(lista_promedio)
print("                      ")
print("la temperatura más baja de las máximas del mes fue de: ",temp_minima,"°")

#retorno de la función que encuentra el valor de la temperatura máxima
temp_maxima = maximo(lista_promedio)
print("                      ")
print("la temperatura máxima del mes fue de: ",temp_maxima,"°")

#retorno de función que crea una lista con la cantidad de elementos del mes a promediar
lista_dias= list_dias(lista_promedio)

#construcción de gráfico de día v/s temperatura
df_grafico={"número de día":lista_dias,"temperatura":lista_promedio}
data_frame=pd.DataFrame(df_grafico)
data_frame.plot(kind="bar", x= "número de día" , y="temperatura",color="red", title="día v/s temperatura")
plt.show()


















