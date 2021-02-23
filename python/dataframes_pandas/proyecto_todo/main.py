import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# parte 1
###############################################################3

#lectura csv
def lectura_csv_1(dataset):
     data = pd.read_csv(dataset,encoding="latin-1", sep  =",", header=0)
     return data

# Promedio
def promedio_1(lista):
     n = len(lista)
     suma = 0

     for elem in lista:
          suma +=elem
     return round(suma/n,2)

# Mínimo
def minimo_1(lista_promedio):
     menor = lista_promedio[0]
     for n in lista_promedio:
          if n < menor:
               menor = n
     return menor

# Máximo
def maximo_1(lista_promedio):
     mayor = lista_promedio[0]
     for n in lista_promedio:
          if n > mayor:
               mayor = n
     return mayor

df = lectura_csv_1("API_EN.ATM.CO2E.KT_DS2_es_csv_v2_1942967.csv")

df.rename(columns = {'ï»¿"Country Name"':'Country Name'}, inplace = True) 
#print(df.head())

chile = df.loc[df["Country Name"] == "Chile"]
#print(chile.columns)
years = list()
for i in range(4,len(chile.columns)-1):
    years +=list(chile[chile.columns[i]])

# se calcula el promedio para reemplazarlo en los años NaN
prom = promedio_1(years[:len(years)-4])

for i in range(len(years)-4,len(years)):
    years[i] = prom

# Se hacen las operaciones requeridas para Chile
# Se obtiene el promedio
prom = promedio_1(years)
print("El promedio de emición de CO2 desde 1960 hasta la actualidad es: ", prom)

# Se obtiene el máximo
maximo_valor = maximo_1(years)
print("El valor máximo de emición de CO2 registrado desde 1960 hasta la actualidad es: ", maximo_valor)

# Se obtiene el mínimo
minimo_valor = minimo_1(list(years))
print("El valor mínimo de emición de CO2 registrado desde 1960 hasta la actualidad es: ", minimo_valor)

name_years = [str(i) for i in range(1960,2021)]

df_grafico ={"Year":name_years, "Ema":years}
data_frame = pd.DataFrame(df_grafico)
data_frame.plot(kind ="bar", x= "Year" , y="Ema",color="red", title="Emanación vs Año", rot = -90)
plt.show()

# parte 2
#####################################################################################################
import pandas as pd
import matplotlib.pyplot as plt


##################  FUNCIONES TEMPERATURA  #######################


#Lectura de csv
def lectura_csv(temp_2020):
     data= pd.read_csv(temp_2020, sep=";", encoding="UTF-8", skiprows=[0,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49],
                       usecols= ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"])
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

###############################################FUNCIONES EMISIONES##############################################################

#lectura csv emisiones
def lectura_csv1(dataset):
     data= pd.read_csv(dataset,encoding="latin-1", sep  =",", header=0)
     return data


# Promedio emisiones
def promedio1(lista):
     n = len(lista)
     suma = 0

     for elem in lista:
          suma +=elem
     return round(suma/n,2)

# Mínimo emisiones
def minimo1(lista_promedio):
     menor = lista_promedio[0]
     for n in lista_promedio:
          if n < menor:
               menor = n
     return menor

# Máximo emesiones
def maximo1(lista_promedio):
     mayor = lista_promedio[0]
     for n in lista_promedio:
          if n > mayor:
               mayor = n
     return mayor


#########################################MAIN###############################################################

#ENTRADAS

#TEMPERATURAS
#entradas por cada región de Chile
temp_2020_1 = r"csv_proyecto\temperatura\Tarapacá\2020\2021-01-24T20_14_05.701Z.csv"
temp_2020_2 = r"csv_proyecto\temperatura\Antofagasta\2020\2021-01-24T20_18_18.397Z.csv"
temp_2020_3 = r"csv_proyecto\temperatura\Atacama\2020\2021-01-24T20_25_16.090Z.csv"
temp_2020_4 = r"csv_proyecto\temperatura\Coquimbo\2020\2021-01-24T22_17_51.802Z.csv"
temp_2020_5 = r"csv_proyecto\temperatura\Valparaiso\2020\2021-01-24T22_52_01.967Z.csv"
temp_2020_6 = r"csv_proyecto\temperatura\O'higgins\2020\2021-01-25T17_38_50.555Z.csv"
temp_2020_7 = r"csv_proyecto\temperatura\Maule\2020\2021-01-24T23_03_37.253Z.csv"
temp_2020_8 = r"csv_proyecto\temperatura\Bio Bio\2020\2021-01-24T22_47_32.069Z.csv"
temp_2020_9 = r"csv_proyecto\temperatura\Araucania\2020\2021-01-24T22_59_20.968Z.csv"
temp_2020_10 = r"csv_proyecto\temperatura\Los Lagos\2020\2021-01-24T23_07_37.125Z.csv"
temp_2020_11 = r"csv_proyecto\temperatura\Aysen\2020\2021-01-24T22_43_10.079Z.csv"
temp_2020_12 = r"csv_proyecto\temperatura\Magallanes\2020\2021-01-24T22_54_28.471Z.csv"
temp_2020_13 = r"csv_proyecto\temperatura\metropolitana\2020\2021-01-23T20_26_16.323Z.csv"
temp_2020_14 = r"csv_proyecto\temperatura\Los Rios\2020\2021-01-24T23_06_38.555Z.csv"
temp_2020_15 = r"csv_proyecto\temperatura\Arica_parinacota\2020\2021-01-24T22_45_23.883Z.csv"
temp_2020_16 = r"csv_proyecto\temperatura\Ñuble\2020\2021-01-24T22_32_38.936Z.csv"

#EMISIONES
emisiones = r"factores_de_emision.csv"


#Título
titulo= "Temperaturas Y Emisiones dioxido de carbono año 2020"
print(titulo.center(190, " "))
#descripción del programa
print(" programa para calcular el promedio, valor más bajo y más alto entre las máximas de temperaturas y emisiones de cada mes del año 2020")
print("                      ")

print(" Sus opciones para visualizar son: \n"
      "1.- región de Tarapacá \n"
      "2.- región de Antofagasta \n"
      "3.- región de Atacama \n"
      "4.- región de Coquimbo \n"
      "5.- región de Valparaiso \n"
      "6.- región del Libertador General Bernardo O'Higgins \n"
      "7.- región del Maule \n"
      "8.- región del Biobío \n"
      "9.- región de la Araucanía \n"
      "10.- región de los lagos \n"
      "11.- región de Aysén del General Carlos Ibáñez del Campo \n"
      "12.- región de Magallanes y de la Antártica Chilena \n"
      "13.- región Metropolitana de Santiago \n"
      "14.- región de Los Ríos \n"
      "15.- región de de Arica y Parinacota \n"
      "16.- región del Ñuble \n")


seleccionar_region = input("Bienvenido, Para comenzar digite el número de la región que desea obtener información y luego presione ENTER: ")

#control de selección de mes (evita inexistencias o faltas ortográficas)
lista_regiones = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16"]
while seleccionar_region not in lista_regiones:
     
     print("DEBE INGRESAR UN NÚMERO ENTRE 1 Y 16")
     seleccionar_region = input("Por favor, digite el número de la región que desea visualizar y luego presione ENTER: ")
    
#muestra selección de la región    
else:
     #diccionario para establecer nombre completo de la región
     diccionario_region= {"1":"región de Tarapacá", "2":"región de Antofagasta", "3":"región de Atacama", "4":"región de Coquimbo", "5":"región de Valparaiso",
             "6":"región del Libertador General Bernardo O'Higgins", "7":"región del Maule", "8":"región del Biobío", "9":"región de la Araucanía",
             "10":"región de los lagos", "11":"región de Aysén del General Carlos Ibáñez del Campo", "12":"región de Magallanes y de la Antártica Chilena",
             "13":"región Metropolitana de Santiago", "14":"región de Los Ríos", "15":"región de de Arica y Parinacota", "16":"región del Ñuble"}
     print("                      ")
     print("la región escogida es: ", diccionario_region[seleccionar_region])
     df_region = seleccionar_region

if df_region == "1":
     df_2020= lectura_csv(temp_2020_1)
elif df_region == "2":
     df_2020= lectura_csv(temp_2020_2)
elif df_region == "3":
     df_2020= lectura_csv(temp_2020_3)
elif df_region == "4":
     df_2020= lectura_csv(temp_2020_4)
elif df_region == "5":
     df_2020= lectura_csv(temp_2020_5)
elif df_region == "6":
     df_2020= lectura_csv(temp_2020_6)
elif df_region == "7":
     df_2020= lectura_csv(temp_2020_7)
elif df_region == "8":
     df_2020= lectura_csv(temp_2020_8)
elif df_region == "9":
     df_2020= lectura_csv(temp_2020_9)
elif df_region == "10":
     df_2020= lectura_csv(temp_2020_10)
elif df_region == "11":
     df_2020= lectura_csv(temp_2020_11)
elif df_region == "12":
     df_2020= lectura_csv(temp_2020_12)
elif df_region == "13":
     df_2020= lectura_csv(temp_2020_13)
elif df_region == "14":
     df_2020= lectura_csv(temp_2020_14)
elif df_region == "15":
     df_2020= lectura_csv(temp_2020_15)
elif df_region == "16":
     df_2020= lectura_csv(temp_2020_16)
     


#variable retornada desde función lectura dataframe   
df_emisiones = lectura_csv1(emisiones)
print("  ")
print("mediciones diarias de temperatura máxima año 2020")
print("  ")
print(df_2020)
print("  ")
print("tabla emsiones CO2 año 2018")
print("  ")
print(df_emisiones)
#lista con los nombres de cada columna (se elimina la primera, ya que no tenía ningún nombre
lista= df_2020.columns[0:13].values.tolist()
#print(lista)

print("                      ")
#realiza un print con las opciones disponibles para que el usuario escoja un mes
print("las opciones para visualizar son: ",str(lista[0])+",",str(lista[1])+",",str(lista[2])+",",str(lista[3])+",",str(lista[4])+",",str(lista[5])+",",str(lista[6])+",",
      str(lista[7])+",",str(lista[8])+",",str(lista[9])+",",str(lista[10])+",",str(lista[11]))
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
     mes =input("Por favor, digite las 3 letras iniciales del mes que desea obtener información:")
     mes_minus= mes.lower()
     mes_prim_mayus= mes_minus.capitalize()
#muestra selección del mes    
else:
     #diccionario para establecer nombre completo del mes
     meses= {"Ene":"Enero", "Feb":"Febrero", "Mar":"Marzo", "abr":"Abril", "May":"Mayo", "Jun":"Junio", "Jul":"Julio", "Ago":"Agosto", "Sep":"Septiembre", "Oct":"Octubre", "Nov":"Noviembre", "Dic":"Diciembre"}
     print("                      ")
     print("el mes escogido es: ", meses[mes_prim_mayus])

#construye una lista con el mes escogido
lista_promedio_NaN= list(df_2020[mes_prim_mayus])
#filtra los datos nulos dentro de la lista
lista_promedio = [x for x in lista_promedio_NaN if str(x) != 'nan']

#variable retornada desde función largo_list Temperaturas
largo_lista= largo_list(lista_promedio)


#retorno de la función que calcula el promedio Temperaturas
promedio= calculo_prom(lista_promedio)

if mes_prim_mayus in meses:
     mes=(meses[mes_prim_mayus])
print("                      ")
print("el promedio de la temperatura máxima para el mes de ", mes," fue de:", str(promedio)+"°")

#retorno de la función que encuentra el valor de la temperatura mínima
temp_minima = minimo(lista_promedio)
print("                      ")
print("la temperatura más baja de las máximas del mes fue de: ",str(temp_minima)+"°")
#retorno de la función que encuentra el valor de la temperatura máxima
temp_maxima = maximo(lista_promedio)
print("                      ")
print("la temperatura máxima del mes fue de: ",str(temp_maxima)+"°")

#retorno de función que crea una lista con la cantidad de elementos del mes a promediar
lista_dias= list_dias(lista_promedio)

#############################EMANASIONES######################################

# Se obtiene la columna de emisión de C02
emisionCO2 = df_emisiones["emisionCO2"]

#Separación de datos
print("  ")

# Se obtiene el promedio
prom = promedio1(list(emisionCO2))
print("El promedio de emisión de CO2 para el año 2018 es: ", str(prom))

#Separación de datos
print("  ")

# Se obtiene el máximo de las emanasiones
maximo_valor = maximo1(list(emisionCO2))
print("El valor máximo de emisión de CO2 registrado para el año 2018 es: ", str(maximo_valor))
#Separación de datos
print("  ")
# Se obtiene el mínimo de las emanasiones
minimo_valor = minimo1(list(emisionCO2))
print("El valor mínimo de emisión de CO2 registrado para el año 2018 es: ", str(minimo_valor))

# Grafica de la emisión de C02 para todos los meses
meses = list()
emision = list()
for i in range(1, 13):
     meses.append(i)
     mes = df_emisiones[df_emisiones["mes"] == i]
     emision_mes = list(mes["emisionCO2"])
     emision.append(promedio1(emision_mes))
     
#separación
print("  ")     
#pausa hasta que el usuario de una entrada por teclado para que el gráfico se muestre luego de que se haya podido leer la información
mostrar_grafico= input("presione la tecla enter para visualizar los gráficos de emisiones y temperaturas del mes escogido ")

#construcción de gráfico de emisiones
df_grafico ={"Mes":meses,"co2":emision}
data_frame = pd.DataFrame(df_grafico)
data_frame.plot(kind ="bar", x= "Mes" , y="co2",color="red", title="Promedio de Emisión de CO2 por mes", rot = 0)
plt.show()


#construcción de gráfico de día v/s temperatura
df_grafico={"número de día":lista_dias,"temperatura":lista_promedio}
data_frame=pd.DataFrame(df_grafico)
data_frame.plot(kind="bar", x= "número de día" , y="temperatura",color="red", title="día v/s temperatura")
plt.show()



















# parte 3
#####################################################################################################
from os import lstat
import pandas as pd
import matplotlib.pyplot as plt


##################  FUNCIONES TEMPERATURA  #######################



archivos = ['metropolitana_act.csv', 'atacama_80.csv', 'arica_parinacota_act.csv', 'valparaiso_act.csv', 'tarapaca_act.csv', 'los_rios_act.csv', 'o_higgins_80.csv', 'antofagasta_act.csv', 'magallanes_80.csv', 'coquimbo_act.csv', 'biobio_80.csv', 'biobio_act.csv', 'arica_parinacota_80.csv', 'coquimbo_80.csv', 'antofagasta_80.csv', 'maule_80.csv', 'araucania_act.csv', 'araucania_80.csv', 'magallanes_act.csv', 'atacama_act.csv', 'o_higgins_act.csv', 'valparaiso_80.csv', 'aysen_act.csv', 'tarapaca_80.csv', 'los_lagos_act.csv', 'aysen_80.csv', 'los_rios_80.csv', 'metropolitana_80.csv', 'los_lagos_80.csv', 'maule_act.csv']



#lectura csv
def lectura_csv_3(dataset):
     data= pd.read_csv(dataset,encoding="latin-1", sep  =";", header=0)
     return data

# Promedio
def promedio_3(lista):
     n = len(lista)
     suma = 0
     
     for elem in lista:
          if str(elem)!="nan":
               suma +=float(elem)
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

#print(df.columns)

df_mes = list(df[mes_op])[:31]

for i in range(len(df_mes)):
        if str(df_mes[i]) != "nan":
                df_mes[i] = float(df_mes[i].replace(",","."))
        
        

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


