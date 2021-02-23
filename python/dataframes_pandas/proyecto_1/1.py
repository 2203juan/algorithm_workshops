import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#lectura csv
def lectura_csv(dataset):
     data = pd.read_csv(dataset,encoding="latin-1", sep  =",", header=0)
     return data

# Promedio
def promedio(lista):
     n = len(lista)
     suma = 0

     for elem in lista:
          suma +=elem
     return round(suma/n,2)

# Mínimo
def minimo(lista_promedio):
     menor = lista_promedio[0]
     for n in lista_promedio:
          if n < menor:
               menor = n
     return menor

# Máximo
def maximo(lista_promedio):
     mayor = lista_promedio[0]
     for n in lista_promedio:
          if n > mayor:
               mayor = n
     return mayor

df = lectura_csv("API_EN.ATM.CO2E.KT_DS2_es_csv_v2_1942967.csv")

df.rename(columns = {'ï»¿"Country Name"':'Country Name'}, inplace = True) 
#print(df.head())

chile = df.loc[df["Country Name"] == "Chile"]
#print(chile.columns)
years = list()
for i in range(4,len(chile.columns)-1):
    years +=list(chile[chile.columns[i]])

# se calcula el promedio para reemplazarlo en los años NaN
prom = promedio(years[:len(years)-4])

for i in range(len(years)-4,len(years)):
    years[i] = prom

# Se hacen las operaciones requeridas para Chile
# Se obtiene el promedio
prom = promedio(years)
print("El promedio de emición de CO2 desde 1960 hasta la actualidad es: ", prom)

# Se obtiene el máximo
maximo_valor = maximo(years)
print("El valor máximo de emición de CO2 registrado desde 1960 hasta la actualidad es: ", maximo_valor)

# Se obtiene el mínimo
minimo_valor = minimo(list(years))
print("El valor mínimo de emición de CO2 registrado desde 1960 hasta la actualidad es: ", minimo_valor)

name_years = [str(i) for i in range(1960,2021)]

df_grafico ={"Year":name_years, "Ema":years}
data_frame = pd.DataFrame(df_grafico)
data_frame.plot(kind ="bar", x= "Year" , y="Ema",color="red", title="Emanación vs Año", rot = -90)
plt.show()