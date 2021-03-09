# Se importa datetime del módulo datetime
from datetime import datetime
import matplotlib.pyplot as plt

def calcular_tiempo_transcurrido(inicio, termino):
    return (termino - inicio).total_seconds()*1000000

# Se guarda el momento exacto de inicio de la ejecución a evaluar

# Se obtiene el tiempo total transcurrido

def recursiva(a,b,c,d,ac,comp): #d es la cantidad de dias que lleva hasta ahora, ac cuanto ha recorrido hasta el momento 
    #y comp es para saber si ya avance los 3 dias o no, solo toma valor 0 o 1 (0 si no se baro un dia, 1 si puede avanzar los 3)
    if(ac >= c):
        return d
    elif(b >= a or ac < 0):
        return -1
    elif(comp == 1):
        return recursiva(a,b,c,d+1,ac-b,1-comp)
    else:
        return recursiva(a,b,c,d+3,ac+a,1-comp)

def iterativa(a,b,c):
    d = 0
    ac = 0
    comp = 0
    if(b >= a):
        return -1
    while(ac < c and ac >= 0):
        if(comp == 1):
            d += 1
            ac -= b
        else:
            d += 3
            ac += a
        comp = 1-comp
    if(ac < 0):
        return -1
    
    return d

def ordenar_por_iterativo(lista):
    N = len(lista)
    for i in range(N-1):
        for j in range(0,N-i-1):
            if(lista[j][4]> lista[j+1][4]):
                lista[j],lista[j+1] = lista[j+1],lista[j]
    #return lista


def ordenar_por_recursivo(lista):
    N = len(lista)
    for i in range(N-1):
        for j in range(0,N-i-1):
            if(lista[j][5]> lista[j+1][5]):
                lista[j],lista[j+1] = lista[j+1],lista[j]
    #return lista





def escribir_salida(lista):
    archivo = open("salida.txt","w")
    for linea in lista:
        archivo.write(str(linea[0])+ " "+str(linea[1])+ " "+ str(linea[2])+ " "+ str(linea[3])+" "+str(linea[4])+ " " +str(linea[5])+"\n")
    archivo.close()

def obtener_tiempo(lista, pos):
    #pos = 4 iterativo
    #pos = 5 recursivo
    ans = list()
    for i in lista:
        ans.append(i[pos])
    return ans

def graficar_recursivo(lista):
    n = len(lista)
    x = [i for i in range(1,n+1)]
    y = lista
    plt.plot(x, y,color = "r", linestyle = "dotted", lw = 2, label = "Tiempo de ejecución")
    plt.title("Gráfico de Tiempo - Recursivo")
    plt.xlabel("Muestras de tiempo")
    plt.ylabel("Tiempo de ejecución")
    plt.legend()
    plt.show()

def graficar_iterativo(lista):
    n = len(lista)
    x = [i for i in range(1,n+1)]
    y = lista
    plt.plot(x, y,color = "b", linestyle = "dashed", lw = 2, label = "Tiempo de ejecución")
    plt.title("Gráfico de Tiempo - Iterativo")
    plt.xlabel("Muestras de tiempo")
    plt.ylabel("Tiempo de ejecución")
    plt.legend()
    plt.show()

def leer_entrada():
    archivo = open("entrada.txt","r")
    todos_los_resultados = []
    for linea in archivo:
        valores = linea.strip().split()
        for i in range(len(valores)):
            valores[i] = int(valores[i])
        resultado = [valores[0],valores[1],valores[2]] 
        inicio = datetime.now()
        res = iterativa(valores[0],valores[1],valores[2])
        termino = datetime.now()
        resultado.append(res)
        print("Resultado iterativa",res)
        resultado.append(calcular_tiempo_transcurrido(inicio,termino))
        inicio = datetime.now()
        res = recursiva(valores[0],valores[1],valores[2],0,0,0)
        termino = datetime.now()
        print("Resultado recursiva",res)
        resultado.append(calcular_tiempo_transcurrido(inicio,termino))
        todos_los_resultados.append(resultado.copy())
    escribir_salida(todos_los_resultados)
    ordenar_por_iterativo(todos_los_resultados)
    print(todos_los_resultados)
    iterativo = obtener_tiempo(todos_los_resultados, pos = 4)
    recursivo = obtener_tiempo(todos_los_resultados, pos = 5)
    print(iterativo)
    print(recursivo)
    graficar_recursivo(recursivo)
    graficar_iterativo(iterativo)
    archivo.close()

leer_entrada()


        
