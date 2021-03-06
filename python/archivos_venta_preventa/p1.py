def cargar_info(nombre_archivo):
    f = open(nombre_archivo+".txt","r")
    info = list()

    for line in f:
        info.append(line.strip().split(";"))

    f.close()
    return info

def agregar_venta(nombre_archivo, datos):
    data = cargar_info(nombre_archivo)

    if datos in data:
        return False
    else:
        f = open(nombre_archivo+".txt","a")
        line = datos[0]+";"+datos[1]+"\n"
        f.write(line)
        f.close()
        return True


def preventa_a_venta(archivo_venta, archivo_preventa, titulo):
    preventas = cargar_info(archivo_preventa)

    band = False
    for i in range(len(preventas)):
        if preventas[i][0] == titulo:
            band = True
            break

    if band:
        f = open("nueva"+archivo_preventa+".txt","w")
        for i in range(len(preventas)):
            if preventas[i][0] != titulo:
                line = preventas[i][0]+";"+preventas[i][1]+"\n"
                f.write(line)
            else:
                f2 = open(archivo_venta+".txt","a")
                line = preventas[i][0]+";"+preventas[i][1]+"\n"
                f2.write(line)
        
        return True

    else:
        return False 


def buscar_juegos(archivo_venta, archivo_preventa, empresa):
    ventas = cargar_info(archivo_venta)
    preventas = cargar_info(archivo_preventa)

    ans = list()

    for juego,empresa_ in ventas:
        if empresa_ == empresa:
            ans.append((juego,archivo_venta))
    
    for juego,empresa_ in preventas:
        if empresa_ == empresa:
            ans.append((juego,archivo_preventa))
    
    return ans

def main():
    archivo_venta = "ventas"
    archivo_preventa = "preventa"
    print(agregar_venta(archivo_venta, ["MarioRun","Nintendo"]))
    print(preventa_a_venta(archivo_venta, archivo_preventa, "fifa21"))
    print(buscar_juegos(archivo_venta, archivo_preventa, "FIFA"))

main()