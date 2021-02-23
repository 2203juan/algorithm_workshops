import random

#punto a
def generarToneladas():
    toneladas = list()

    for i in range(12):
        toneladas.append(random.randint(30,220))
    return toneladas

# punto b
def total_(toneladas):
    n = len(toneladas)
    sum = 0

    for i in range(n):
        sum += toneladas[i]
    return sum

# punto c
def ProdSup(toneladas):
    n = len(toneladas)
    promedio = total_(toneladas)
    promedio /= n
    ans = 0

    for i in range(n):
        if toneladas[i] > promedio:
            ans +=1
    print("La cantidad de meses con producción superior al promedio anual es: ", ans)


# punto d

def ProdMay(toneladas):
    n = len(toneladas)
    maximo = toneladas[0]
    idx = 0

    for i in range(1,n):
        if toneladas[i] > maximo:
            maximo = toneladas[i]
            idx = i

    print("La mayor produccion de toneladas se dio en el mes ", idx + 1, " y fue de:", maximo)

# punto e

def dosMesesCons(toneladas):
    n = len(toneladas)
    diff = abs(toneladas[1] - toneladas[0])
    mes1 = 0
    mes2 = 1

    for i in range(1,n):
        if abs(toneladas[i] -  toneladas[i-1]) > diff:
            diff = abs(toneladas[i] -  toneladas[i-1])
            mes2 = i
            mes1 = i-1
    print("Los dos meses consecutivos  en que la diferencia de producción  fue la mas significativas fueron: ", mes1+1," y", mes2+1)

def mostrarVector(toneladas):
    n = len(toneladas)

    for i in range(n):
        print("Produccion del mes ", i+1, " =", toneladas[i])

op = 1
toneladas = list()
while op != 0:
    print("Seleccione una opción")
    print("0) Salir")
    print("1) Generar vector de toneladas anuales aleatoriamente")
    print("2) Obtener total de toneladas anuales")
    print("3) Obtener cantidad de meses con producción superior al promedio anual")
    print("4) Obtener mes y cantidad de mayor producción")
    print("5) Obtener los dos meses consecutivos  en que la diferencia de producción  fue la mas significativas.")
    print("6) Mostrar producción anual de toneladas")
    op = int(input())

    if op == 1:
        toneladas = generarToneladas()
    elif len(toneladas) == 0 and op != 0:
        print("Debe primero generar el vector para usar las otras opciones")
    elif op == 2:
        total = total_(toneladas)
        print("Total de toneladas anuales: ", total)
    elif op == 3:
        ProdSup(toneladas)
    elif op == 4:
        ProdMay(toneladas)
    elif op == 5:
        dosMesesCons(toneladas)
    elif op == 6:
        mostrarVector(toneladas)






