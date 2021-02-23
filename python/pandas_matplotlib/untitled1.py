#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 16:22:18 2020

@author: juan
"""

import csv
import pandas as pd
import matplotlib.pyplot as plt

def cargar_datos(nombre):
    
    datos = []
    
    with open(nombre, encoding = "utf-8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ",")
        
        for row in csv_reader:
            if len(row) > 0:
                datos.append([str(v) for v  in row])
                
    dataFrame = pd.DataFrame(data = datos[1:], columns = datos[0])

    dataFrame[["Cantidad","ValorMilesDolar","ValorMilesPesos"]] = dataFrame[["Cantidad","ValorMilesDolar","ValorMilesPesos"]].astype('float64') 
    dataFrame[["﻿Anio"]] = dataFrame[["﻿Anio"]].astype('int64')

    return dataFrame

def segundo_punto():
    df = cargar_datos("exportaciones.csv")
    por_banano = df.groupby('Producto').ValorMilesDolar.sum()
    por_banano.plot.pie(y = "bananos",figsize = (10,10))
    print(por_banano)

def tercer_punto():
    df = cargar_datos("exportaciones.csv")
    df = df[df["Producto"] !="Cavendish Valery"]
    por_banano = df.groupby('Producto').ValorMilesDolar.sum()
    por_banano.plot.pie(y = "bananos",figsize = (10,10))
    print(por_banano)

def cuarto_punto():
    df = cargar_datos("exportaciones.csv")
    name = df.columns[0]
    df = df[df["Producto"] !="Cavendish Valery"]
    df = df[df[name] == 2016]
    por_banano = df.groupby('Producto').ValorMilesDolar.sum()
    por_banano.plot.pie(y = "bananos",figsize = (10,10))
    #print(por_banano)
    

def quinto_punto():
    df = cargar_datos("exportaciones.csv")
    name = df.columns[0]
    df = df[df[name]%2 == 0]
    por_banano = df.groupby(name).ValorMilesDolar.sum()
    por_banano.plot(kind = 'bar', figsize=(10,5), colormap = "Paired")
    
def sexto_punto():
    df = cargar_datos("exportaciones.csv")
    #df = df.sort_values(["ValorMilesDolar"], ascending = False).groupby("PaisDestino").ValorMilesDolar.sum()
    df = df.groupby("PaisDestino").ValorMilesDolar.sum().reset_index()
    df = df.sort_values(by = ["ValorMilesDolar"], ascending = False)
    print(df.head(5))

sexto_punto()