import matplotlib.pyplot as plt

test = [1,5,7,13,18,29,45,60,72]
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

graficar_recursivo(test)
graficar_iterativo(test)
