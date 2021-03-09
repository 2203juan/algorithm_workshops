import matplotlib.pyplot as plt
test = [1,5,7,13,18,29,45,60,72]

def graficar(datos, color,textura, titulo):
    x = []

    for i in range(1,len(datos)+1):
        x.append(i)
    plt.title(titulo)
    plt.xlabel("X")
    plt.ylabel("Tiempo de ejecución")
    plt.plot(x, datos,color = color,  label = "Tiempo de ejecución",linestyle = textura)
    plt.legend(loc = 4)
    plt.show()

#recursivo
graficar(test, color = "limegreen",textura = "-.", titulo = "Tiempo Algoritmo Recursivo")

#iterativo
graficar(test, color = "royalblue",textura = "-", titulo = "Tiempo Algoritmo Iterativo")