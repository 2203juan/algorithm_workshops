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

import Jojojo as archivo

def eliminar_salto_linea(lista):
    i = 0
    while i < len(lista):
        lista[i] = lista[i].strip()
        i+=1
    return lista


def bondad_promedio(lista):
    i = 1
    suma = 0
    n = len(lista)
    while i < n:
        suma += float(lista[i])
        i+=1
    
    return suma / (n-1)

def partir_string_lista(lista):
    n = len(lista)
    i = 0
    ans = list()
    
    while i < n:
        ans.append(lista[i].split(","))
        i+=1

    return ans

def calcular_nro_regalos(bondad):
    i = 0
    n = len(bondad)
    nro_regalos = list()

    while i < n:
        bondad_prom = bondad_promedio(bondad[i])
        if bondad_prom >= 6.5 and bondad_prom <= 7:
            nro_regalos.append(5)

        elif bondad_prom >= 6 and bondad_prom <= 6.4:
            nro_regalos.append(4)

        elif bondad_prom >= 5.5 and bondad_prom <= 5.9:
            nro_regalos.append(3)
        
        elif bondad_prom >= 5 and bondad_prom <= 5.4:
            nro_regalos.append(2)
        
        elif bondad_prom >= 4 and bondad_prom <= 4.9:
            nro_regalos.append(1)
        
        elif bondad_prom >= 1 and bondad_prom <= 3.9:
            nro_regalos.append(0)

        i+=1
    
    return nro_regalos

def verificar(bondad, elemento):
    n = len(bondad)
    i = 0

    while i < n:
        if bondad[i][0] == elemento:
            return True
        i+=1
    return False

def buscar_sin_pedido(bondad, elemento, nro_regalos, pedidos):
    i = 0
    n = len(bondad)

    while i < n:
        if bondad[i][0] == elemento:
            j = 0

            while j < len(pedidos):
                if pedidos[j][0] == elemento:
                    return False
                j+=1
            return True
        i+=1


def asignar_regalos(pedidos, nro_regalos, bondad):
    i = 0
    n = len(pedidos)
    regalos = list()

    while i < n:
        ok = verificar(bondad, pedidos[i][0])

        if ok:
            n_pedidos = len(pedidos[i]) - 1 # se resta uno por el nombre
            asignados = nro_regalos[i]

            if n_pedidos <= asignados:
                if asignados == 0:
                    regalos.append(["carbon"])

                if asignados > 0 and n_pedidos > 0:
                    j = 1
                    tmp = list()
                    while j < len(pedidos[i]):
                        tmp.append(pedidos[i][j])
                        j+=1
                    regalos.append(tmp)

            else:
                if asignados == 0:
                    regalos.append(["carbon"])
                else:
                    j = 1
                    tmp = list()
                    while j <= (len(pedidos[i]) - asignados + 1):
                        tmp.append(pedidos[i][j])
                        j+=1
                    regalos.append(tmp)

        i+=1

    i = 0
    while i < len(bondad):
        sin_pedido = buscar_sin_pedido(bondad, bondad[i][0], nro_regalos, pedidos)
        
        if sin_pedido:
            if nro_regalos[i] > 0:
                regalos.append(["bicicleta"])
            else:
                regalos.append(["carbon"])
        i+=1
    return regalos

def guardar_regalos(bondad, regalos):
    lineas = ""
    i = 0
    while i < len(regalos):
        lineas += bondad[i][0] +","
        j = 0

        while j < len(regalos[i]):
            if j+1 != len(regalos[i]):
                lineas +=regalos[i][j]+","
            
            else:
                lineas +=regalos[i][j]+"\n"
            j+=1
        
        i+=1
    archivo.escribir_archivo("regalos.txt", lineas)

def main():
    bondad = partir_string_lista(eliminar_salto_linea(archivo.leer_archivo("bondad.txt")))
    pedidos = partir_string_lista(eliminar_salto_linea(archivo.leer_archivo("pedidos.txt")))
    nro_regalos = calcular_nro_regalos(bondad)
    regalos = asignar_regalos(pedidos, nro_regalos, bondad)
    guardar_regalos(bondad, regalos)
main()

