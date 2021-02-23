
def tiempo_transferencia(tamano: float, ancho_banda: int) -> str:

    segundos_totales = (8192*tamano)/ancho_banda

    hor = str(segundos_totales // 3600)
    min = str((segundos_totales % 3600) // 60)
    seg = str(round((segundos_totales % 3600) % 60, 2))

    ans = "El archivo tardará "+str(hor)+" horas, "+str(min)+" minutos y "+str(seg)+" segundos en transferirse"
    return ans


def costo_procesamiento_compromiso(dedicados: int, compartidas: int, costo: float) -> float:
    dedicados = (costo * dedicados)**(9/10)
    costo = costo - (costo*0.1)
    compartidas = ((costo * compartidas)**(17/20))
    hra = compartidas + dedicados
    return hra*720


def costo_procesamiento_libre(dedicados: int, compartidas: int, costo: float) -> float:
    dedicados = costo*dedicados
    costo = costo - (costo*0.1)
    compartidas = costo*compartidas

    hra = compartidas + dedicados
    return hra*720


def costo_almacenamiento(lectura: int, escritura: int, almacenamiento: float) -> float:
    lectura_ent = lectura // 1000
    costo_lectura = lectura_ent*0.0004 + ((lectura_ent - lectura_ent/1000)*(0.0004))/1000

    escritura_ent = escritura // 1000
    costo_escritura = escritura_ent*0.005 + ((lectura_ent - lectura_ent/1000)*(0.005))/1000

    almacenamiento = almacenamiento*0.023

    return costo_lectura + costo_escritura + almacenamiento


def costo_transferencia(datos: float, porcentaje_aws: float) -> float:
    datos_aws = round(datos*porcentaje_aws)
    datos_normales = datos - datos_aws - 1

    costo = datos_normales*0.09 + datos_aws*0.02

    return costo


def costo_total(servidores_compromiso: int, porcentaje_compartidas_compromiso: float, servidores_libres: int, porcentaje_compartidas_libres: float, costo_dedicado: float, solicitudes_totales: int, almacenamiento: float, datos: float, porcentaje_aws: float) -> str:

    compartidas_1 = round(servidores_compromiso *
                        porcentaje_compartidas_compromiso)
    dedicados_1 = servidores_compromiso - compartidas_1

    costo_procesamiento_comp = costo_procesamiento_compromiso(
        dedicados_1, compartidas_1, costo_dedicado)

    compartidas_2 = round(servidores_libres*porcentaje_compartidas_libres)
    dedicados_2 = servidores_libres - compartidas_2

    costo_procesamiento_lib = costo_procesamiento_libre(
        dedicados_2, compartidas_2, costo_dedicado)

    escritura = round((1/3)*solicitudes_totales)
    lectura = solicitudes_totales - escritura
    costo_almac = costo_almacenamiento(lectura, escritura, almacenamiento)
    costo_transf = costo_transferencia(datos, porcentaje_aws)

    costo_total = costo_procesamiento_comp + \
        costo_procesamiento_lib + costo_almac + costo_transf

    return str(round(costo_total,2))
