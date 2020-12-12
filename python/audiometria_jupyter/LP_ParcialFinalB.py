#!/usr/bin/env python
# coding: utf-8

# # Parcial final

# ** Modo de entrega: **
# 
# - El parcial final debe entregarse como un archivo de Python con extensión .py.
# Puede utilizar el entorno de desarrollo (IDE) que prefiera (ej. Jupyter Notebook, Spyder, Pycharm, etc).
# Si decide utlizar el Jupyter Notebook, recuerde exportar el archivo con extensión .py. 
# Esto puede hacerlo desde el menú en la opción file/archivo, download as/descargar como, Python (.py).
# 
# - Una vez resuelto el parcial, por favor suba el archivo correspondiente al link de entrega del aula virtual.

# **Datos para el parcial:**

# En el archivo audiometria2.py encuentra los resultados de la audiometría de dos pacientes.
# Trabaje con los datos del paciente que le fue asignado al iniciar el parcial.
# Adicionalmente, en este Jupyter Notebook encuentra ya dichos resutados asignados en una variable de tipo arreglo (array) llamada datos_audiometría.
# Para resolver el parcial, utilice los datos ya organizados en la variable datos_audiometria. 

# In[1]:


#Estos son los datos
import numpy as np

datos_audiometria = audiometria = np.array([('Persona','Banda(Hz)', 'Canal', 'Nivel(dB)'), 
(1, 500, 'I', 57), 
(1, 1000, 'I', 60),
(1, 2000, 'I', 62), 
(1, 4000, 'I', 55), 
(1, 6000, 'I', 24), 
(1, 8000, 'I', 22),
(1, 10000, 'I', 50), 
(1, 500, 'D', 62), 
(1, 1000, 'D', 70), 
(1, 2000, 'D', 65), 
(1, 4000, 'D', 20),
(1, 6000, 'D', 24),
(1, 8000, 'D', 19),
(1, 10000, 'D', 48), 
(2, 500, 'I', 23),
(2, 1000, 'I', 15),
(2, 2000, 'I', 18),
(2, 4000, 'I', 38),
(2, 6000, 'I', 36),
(2, 8000, 'I', 37),
(2, 10000, 'I', 50),
(2, 500, 'D', 20),
(2, 1000, 'D', 24),
(2, 2000, 'D', 29),
(2, 4000, 'D', 28),
(2, 6000, 'D', 32),
(2, 8000, 'D', 37),
(2, 10000, 'D', 54),
(3, 500, 'I', 14),
(3, 1000, 'I', 18),
(3, 2000, 'I', 20),
(3, 4000, 'I', 58),
(3, 6000, 'I', 63),
(3, 8000, 'I', 43),
(3, 10000, 'I', 44),
(3, 500, 'D', 10),
(3, 1000, 'D', 15),
(3, 2000, 'D', 17),
(3, 4000, 'D', 60),
(3, 6000, 'D', 64),
(3, 8000, 'D', 28),
(3, 10000, 'D', 30)])


# Los niveles en dB obtenidos en cada banda de frecuencia indican lo siguiente:
# 
# -Normal: 0-25 dB, es decir, no hay daño auditivo.
# 
# -Daño leve: 26-40 dB, es decir, hay un daño auditivo leve.
# 
# -Daño moderado: 41-55 dB, es decir, hay un daño auditivo moderado.
# 
# -Daño severo: 56-70 dB, es decir, hay un daño auditivo severo.

# ## Instrucciones:

# ** Aclaración importante sobre la calificación: **
# 
# - Para obtener el punto completo en los ejercicios planteados, es importante resolverlos por medio de for/bucles y condicionales. 

# ### Primera parte:
# 
# ### Función: **leer_resultados_audiometria**

# **Primera parte: (valor 2.0)**
# 
# Cree una función llamada **leer_resultados_audiometria** que permita leer los datos del paciente correspondiente.
# 
# La entrada de esta función son los datos almacenados en la variable ** datos_audiometria** y el número del paciente que le correspondió (1, 2 o 3). 
# La salida de la función deben ser dos listas con los niveles obtenidos por el paciente que le fue asignado. La primera lista debe corresponder a los valores obtenidos en el oído izquierdo, y la segunda lista a los valores obtenidos en el oído derecho. Cada lista debe contener siete valores que corresponden a cada una de las bandas evaluadas.
# 
# * Ejemplo de uso de la función:
# 
# leer_resultados_audiometria(datos_audiometria, 1)
# 
# ** El número del paciente puede ingresarse como un entero 1, o como un string '1', cualquiera de las dos opciones está bien.

# In[2]:


def leer_resultados_audiometria(datos_audiometria, paciente):
    oido_izquierdo = list()
    oido_derecho = list()
    n = len(datos_audiometria)
    
    for i in range(1,n):
        if datos_audiometria[i][2] == "I" and int(datos_audiometria[i][0]) == paciente:
            oido_izquierdo.append(datos_audiometria[i][3])
        if datos_audiometria[i][2] == "D" and int(datos_audiometria[i][0]) == paciente:
            oido_derecho.append(datos_audiometria[i][3])
    
    return (oido_izquierdo, oido_derecho)

print(leer_resultados_audiometria(datos_audiometria, 3))


# **segunda parte: (valor 1.0)**
# 
# Modifique la función **leer_resultados_audiometria** del tal manera que la función genere dos listas adicionales en la salida. 
# Las listas adicionales deben indicar en cuál de las cuatro categorías presentadas (Normal, daño leve, daño moderado, daño severo) se clasifica el nivel (dB) obtenido. Nuevamente, una de las listas debe corresponder al oído izquierdo, y la otra al oído derecho.
# 
# *Ejemplo de una de las listas:* 
# 
# ['N','N','DL','DL','DM','N', 'N']

# In[3]:


"""
Los niveles en dB obtenidos en cada banda de frecuencia indican lo siguiente:

-Normal: 0-25 dB, es decir, no hay daño auditivo.

-Daño leve: 26-40 dB, es decir, hay un daño auditivo leve.

-Daño moderado: 41-55 dB, es decir, hay un daño auditivo moderado.

-Daño severo: 56-70 dB, es decir, hay un daño auditivo severo.

"""

def leer_resultados_audiometria(datos_audiometria, paciente):
    oido_izquierdo = list()
    oido_derecho = list()
    nivel_oido_izquierdo = list()
    nivel_oido_derecho = list()
    n = len(datos_audiometria)
    
    for i in range(1,n):
        if datos_audiometria[i][2] == "I" and int(datos_audiometria[i][0]) == paciente:
            oido_izquierdo.append(datos_audiometria[i][3])
            
            nivel = int(datos_audiometria[i][3])
            if 0 < nivel <= 25:
                nivel_oido_izquierdo.append("N")
            
            elif 25 < nivel <= 40:
                nivel_oido_izquierdo.append("DL")
            
            elif 40 < nivel <= 55:
                nivel_oido_izquierdo.append("DM")
            elif 55 < nivel <= 70:
                nivel_oido_izquierdo.append("DS")
                
                
            
        if datos_audiometria[i][2] == "D" and int(datos_audiometria[i][0]) == paciente:
            oido_derecho.append(datos_audiometria[i][3])
            
            nivel = int(datos_audiometria[i][3])
            if 0 < nivel <= 25:
                nivel_oido_derecho.append("N")
            
            elif 25 < nivel <= 40:
                nivel_oido_derecho.append("DL")
            
            elif 40 < nivel <= 55:
                nivel_oido_derecho.append("DM")
            elif 55 < nivel <= 70:
                nivel_oido_derecho.append("DS")
    
    return (oido_izquierdo, oido_derecho, nivel_oido_izquierdo, nivel_oido_derecho)

print(leer_resultados_audiometria(datos_audiometria, 3))


# ### Tercera parte: 
# 
# ### Función: plot_resultados_audiometria

# Cree una función llamada **plot_resultados_audiometria** con la cuál se puedan visualizar los datos obtenidos en las funciones anteriores. En el eje Y deben mostrarse los niveles medidos, y en el eje X deben mostrarse las bandas (Hz) en las cuales se hizo la medición. (valor 1.0)

# La función **plot_resultados_audiometria** debe tener cuatro argumentos de entrada, estos son:
# 
# - Niveles oído izquierdo
# - Niveles oído derecho
# - Clasificación de niveles oído izquierdo
# - Clasificación de niveles oído derecho
# 
# *Ejemplo de uso:*
# 
# plot_resultados_audiometria(listaA, listaB, listaC,listaD)

# In[4]:


import matplotlib.pyplot as plt
def plot_resultados_audiometria(oido_izquierdo, oido_derecho, cla_oido_izq, cla_oido_der):
    bandas = [500,1000,2000,4000,6000,8000,10000]
    #--------------------- oido izquierdo
    normales_izq = list()
    bandas_norm_izq = list()
    no_normales_izq = list()
    bandas_no_norm_izq = list()
    
    for i in range(len(oido_izquierdo)):
        if cla_oido_izq[i] == "N":
            normales_izq.append(oido_izquierdo[i])
            bandas_norm_izq.append(bandas[i])
        else:
            no_normales_izq.append(oido_izquierdo[i])
            bandas_no_norm_izq.append(bandas[i])
    #normales_izq.sort()
    #no_normales_izq.sort()
    
    izq_norm = {}
    izq_no_norm = {}
    
    for i in range(len(normales_izq)):
        izq_norm[normales_izq[i]] = bandas_norm_izq[i]
        
    for i in range(len(no_normales_izq)):
        izq_no_norm[no_normales_izq[i]] = bandas_no_norm_izq[i]
        
    x = list()
    y = list()
    for key in sorted(izq_norm):
        x.append(izq_norm[key])
        y.append(key)
    
    xp = list()
    yp = list()
    
    for key in sorted(izq_no_norm):
        xp.append(izq_no_norm[key])
        yp.append(key)
    #------------------------- oido derecho
    normales_der = list()
    bandas_norm_der = list()
    no_normales_der = list()
    bandas_no_norm_der = list()
    
    for i in range(len(oido_derecho)):
        if cla_oido_der[i] == "N":
            normales_der.append(oido_derecho[i])
            bandas_norm_der.append(bandas[i])
        else:
            no_normales_der.append(oido_derecho[i])
            bandas_no_norm_der.append(bandas[i])
    
    der_norm = {}
    der_no_norm = {}
    
    for i in range(len(normales_der)):
        der_norm[normales_der[i]] = bandas_norm_der[i]
        
    for i in range(len(no_normales_der)):
        der_no_norm[no_normales_der[i]] = bandas_no_norm_der[i]
        
    xd = list()
    yd = list()
    for key in sorted(der_norm):
        xd.append(der_norm[key])
        yd.append(key)
    
    xpd = list()
    ypd = list()
    
    for key in sorted(der_no_norm):
        xpd.append(der_no_norm[key])
        ypd.append(key)
            
            
    fig=plt.figure()
    ax = fig.add_axes([0,0,1,1])
    # oido izquiero rojo normales- azul otro
    ax.scatter(x, y , color='r')
    ax.scatter(xp, yp, color='b')
    # oido derecho verde normales - amarillo otros
    ax.scatter(xd, yd , color='g')
    ax.scatter(xpd, ypd, color='y')
    ax.set_xlabel('Banda(Hz)')
    ax.set_ylabel('Nivel medido')
    ax.set_title('Oido Izquierdo y Derecho paciente 3')
    plt.show()

listas = leer_resultados_audiometria(datos_audiometria, 3)
plot_resultados_audiometria(listas[0], listas[1], listas[2], listas[3])


# En el plot creado, los valores que corresponden a la categoría niveles normales deben tener un color, y los niveles que correspondan a las otras categorías deben tener otro color. (valor 1.0)
