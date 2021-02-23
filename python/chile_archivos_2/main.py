# FUNDAMENTOS DE PROGRAMACIÓN PARA INGENIERÍA
# SECCIÓN DEL CURSO: 2-L-1
# PROFESOR DE TEORÍA: FELIPE MORENO
# PROFESOR DE LABORATORIO: JUAN PADILLA
#
# AUTOR
# NOMBRE: Juan Carlos Perez Gonzalez
# RUT: 20.345.432-2
# CARRERA: Ingeniería Civil Mecánica
# DESCRIPCIÓN DEL PROGRAMA ...<CONTINÚE CON EL PROGRAMA A PARTIR DE AQUÍ> 

import Jojojo

def leer_bondad():
    bondad = Jojojo.leer_archivo("bondad.txt")
    
    i = 0

    while i < len(bondad):
        bondad[i] = bondad[i].strip()
        i+=1
    
    i = 0

    while i < len(bondad):
        bondad[i] = bondad[i].split(",")
        j  = 1

        while j < len(bondad[i]):
            bondad[i][j] = float(bondad[i][j])
            j+=1
        i+=1
    
    return bondad

def leer_pedidos():
    pedidos = Jojojo.leer_archivo("pedidos.txt")
    i = 0

    while i < len(pedidos):
        pedidos[i] = pedidos[i].strip()
        i+=1

    i  = 0

    while i < len(pedidos):
        pedidos[i] = pedidos[i].split(",")
        i+=1
    
    return pedidos

def calcular_cantidad_regalos(bondad):
    i = 1
    n = 0
    num = 0

    prom = 0
    while i < len(bondad):
        num += bondad[i]
        n+=1
        i+=1
    prom = num / n

    regalos = 0

    if prom >= 6.5 and prom <= 7:
        regalos = 5
    elif prom >= 6 and prom <= 6.4:
        regalos = 4

    elif prom >= 5.5 and prom <= 5.9:
        regalos = 3
    
    elif prom >= 5 and prom <= 5.4:
        regalos = 2
    
    elif prom >= 4 and prom <= 4.9:
        regalos = 1
    elif prom >= 1 and prom <= 3.9:
        regalos = 0

    return regalos


def revisar_sin_pedido(pedidos, bondad, ans):
    i = 0

    while i < len(bondad):
        j = 0

        band = False
        while j < len(pedidos) and not band:
            if bondad[i][0] == pedidos[j][0]:
                band = True
            j+=1
        if not band:
            regalos  = calcular_cantidad_regalos(bondad[i])
            if regalos > 0:
                ans.append(bondad[i][0]+",bicicleta\n")
            
            if regalos == 0:
                ans.append(bondad[i][0]+",carbon\n")

        i+=1

    return ans


def asignar_regalos(pedidos, bondad):
    n = len(pedidos)
    i = 0

    ans = list()
    while i < n:
        j = 0

        regalos = -1
        while j < len(bondad) and regalos == -1:
            if pedidos[i][0] == bondad[j][0]:
                regalos = calcular_cantidad_regalos(bondad[j])
                cant_pedidos = len(pedidos[i]) - 1

                tmp = pedidos[i][0]+","
                
                if regalos == 0:
                    tmp+="carbon\n"
                
                elif cant_pedidos < regalos:
                    k = 1

                    while k < cant_pedidos + 1:
                        if k+1 != cant_pedidos + 1:
                            tmp +=pedidos[i][k] + ","
                        else:
                            tmp +=pedidos[i][k] + "\n"
                        k+=1
                
                else:
                    k = 1

                    while k-1 < regalos:
                        if k != regalos:
                            tmp +=pedidos[i][k] + ","
                        else:
                            tmp +=pedidos[i][k] + "\n"
                        k+=1

                ans.append(tmp)
                
                    

            j+=1

        i+=1
    
    ans = revisar_sin_pedido(pedidos, bondad, ans)

    return ans

bondad = leer_bondad()
pedidos =  leer_pedidos()
ans = asignar_regalos(pedidos, bondad)
Jojojo.escribir_archivo("regalos.txt",ans)

