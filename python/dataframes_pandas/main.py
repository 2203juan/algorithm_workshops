import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#lectura csv
def lectura_csv(dataset):
     data= pd.read_csv(dataset,encoding="latin-1", sep  =",", header=0)
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

# SOLUCIÓN

# Lectura de datos

df = lectura_csv("factores_de_emision.csv")

# Se agrega una nueva columna llamada emicion_aumentada, la cual
# aumenta la emicionCO2 en un 20%

df["emicion_aumentada"] = df["emicionCO2"]*(1+0.2)

# Se obtiene la columna de emición de C02
emicionCO2 = df["emicionCO2"]
# Se obtiene el promedio
prom = promedio(list(emicionCO2))
print("El promedio de emición de CO2 es: ", prom)

# Se obtiene el máximo
maximo_valor = maximo(list(emicionCO2))
print("El valor máximo de emición de CO2 registrado es: ", maximo_valor)

# Se obtiene el mínimo
minimo_valor = minimo(list(emicionCO2))
print("El valor mínimo de emición de CO2 registrado es: ", minimo_valor)

# Grafica de la emición de C02 en el mes 1
meses = list()
emicion = list()
for i in range(1, 13):
     meses.append(i)
     mes = df[df["mes"] == i]
     emicion_mes = list(mes["emicionCO2"])
     emicion.append(promedio(emicion_mes))

df_grafico ={"Mes":meses,"co2":emicion}
data_frame = pd.DataFrame(df_grafico)
data_frame.plot(kind ="bar", x= "Mes" , y="co2",color="red", title="Promedio de Emicion de CO2 por mes", rot = 0)
plt.show()