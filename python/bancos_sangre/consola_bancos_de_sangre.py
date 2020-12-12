"""
Ejercicio nivel 2: Bancos de Sangre.
Modulo de interaccion por consola.

Temas:
* Variables.
* Tipos de datos.
* Expresiones aritmeticas.
* Instrucciones basicas y consola.
* Dividir y conquistar: funciones y paso de parametros.
* Especificacion y documentacion.
* Instrucciones condicionales.
* Diccionarios.
"""

import bancos_de_sangre as mod

def mostrar_banco(banco: dict)-> None:
    """ Muestra en pantalla la informacion de un banco
    Parametros:
        banco (dict): El banco de sangre del que se van a mostrar los detalles.
    """
    nombre = banco["nombre"]
    localidad = banco["localidad"]
    donantes = banco["donantes"]
    a_positivo = banco["A+"]
    a_negativo = banco["A-"]
    b_positivo = banco["B+"]
    b_negativo = banco["B-"]
    ab_positivo = banco["AB+"]
    ab_negativo = banco["AB-"]
    o_positivo = banco["O+"]
    o_negativo = banco["O-"]

    cantidades1 = "A+:  {:3d}\t\tA-:  {:3d}\t\tB+: {:3d}\t\tB-: {:3d}"
    cantidades2 = "AB+: {:3d}\t\tAB-: {:3d}\t\tO+: {:3d}\t\tO-: {:3d}"

    print("Nombre: " + nombre + " - Localidad: " + localidad + " - Donantes: " + str(donantes) )
    print("Bolsas Disponibles:")
    print(cantidades1.format(a_positivo, a_negativo, b_positivo, b_negativo))
    print(cantidades2.format(ab_positivo, ab_negativo, o_positivo, o_negativo))



def ejecutar_recibir_donacion(b1: dict, b2: dict, b3: dict, b4: dict)->None:
    """Ejecuta la opcion de recibir una donacion para uno de los bancos de sangre.
    Parametros:
        b1 (dict): Diccionario con la informacion del banco 1.
        b2 (dict): Diccionario con la informacion del banco 2.
        b3 (dict): Diccionario con la informacion del banco 3.
        b4 (dict): Diccionario con la informacion del banco 4.
    """
    nombre_banco = input("Ingrese el nombre del banco de sangre que recibira al donante: \n")

    banco_donante = mod.buscar_banco(nombre_banco, b1, b2, b3, b4)
    if banco_donante is None:
        print("No se encontro el banco " + nombre_banco + " en los registros.")
    
    else:
        genero = input("Ingrese su genero (M o F): \n")
        peso = int(input("Ingrese su peso (en kilogramos - numero entero):\n"))
        edad = int(input("Ingrese su edad (en años - numero entero)\n"))
        tipo_Sangre = input("Ingrese su tipo de sangre: A+, A-, AB+, AB-, B+, B-, O+, O-\n")
        validacion_donante = mod.recibir_donacion(genero, edad,peso, tipo_Sangre,banco_donante)

        if validacion_donante == 0:
            print("Lo sentimos, no eres apto para donar sangre\n")
        else:
            print("La cantidad de bolsas que fueron donadas al banco fueron:  ",validacion_donante)


def ejecutar_suministrar_bolsas(b1: dict, b2: dict, b3: dict, b4: dict)->None:
    """Ejecuta la opcion de suministrar bolsas desde un banco de sangre.
    Parametros:
        b1 (dict): Diccionario con la informacion del banco 1.
        b2 (dict): Diccionario con la informacion del banco 2.
        b3 (dict): Diccionario con la informacion del banco 3.
        b4 (dict): Diccionario con la informacion del banco 4.
    """

    nombre_banco = input("Ingrese el nombre del banco de sangre que suministrara las bolsas: ")

    banco_suministro = mod.buscar_banco(nombre_banco, b1, b2, b3, b4)
    if banco_suministro is None:
        print("No se encontro el banco " + nombre_banco + " en los registros.")
    else:
        cantidadBolsas = int(input("Ingrese la cantidad de bolsas de sangre que se desean suministrar:\n"))
        tipoSangre = input("Ingrese el tipo de sangre que necesita: A+, A-, AB+, AB-, B+, B-, O+, O-\n")
        suministro_realizado = mod.suministrar_bolsas(tipoSangre,cantidadBolsas,banco_suministro)
        if suministro_realizado == True:
            print("Suministro realizado exitosamente!!")
        else:
            print("Lo sentimos, no esta disponible el suministro porque hay al menos un tipo de sangre en riesgo.")
            

def ejecutar_transferir_bolsas(b1: dict, b2: dict, b3: dict, b4: dict)->None:
    """Ejecuta la opcion de transferir bolsas entre dos bancos de sangre.
    Parametros:
        b1 (dict): Diccionario con la informacion del banco 1.
        b2 (dict): Diccionario con la informacion del banco 2.
        b3 (dict): Diccionario con la informacion del banco 3.
        b4 (dict): Diccionario con la informacion del banco 4.
    """
    nombre_banco1 = input("Ingrese el nombre del banco de sangre origen: ")
    nombre_banco2 = input("Ingrese el nombre del banco de sangre destino: ")

    banco1 = mod.buscar_banco(nombre_banco1, b1, b2, b3, b4)
    banco2 = mod.buscar_banco(nombre_banco2, b1, b2, b3, b4)
    if banco1 is None:
        print("No se encontro el banco origen " + nombre_banco1 + " en los registros.")
    elif banco2 is None:
        print("No se encontro el banco destino " + nombre_banco2 + " en los registros.")
    else:
        cantidad_a_transferir = int(input("Ingrese la cantidad de bolsas de sangre que se desean transferir\n"))
        tipoSangre = input("Ingrese el tipo de sangre que se va a transferir: A+, A-, AB+, AB-, B+, B-, O+, O-\n")
        ans = mod.transferir_bolsas(tipoSangre,cantidad_a_transferir,banco1,banco2)
        print("Cantidad de bolsas transferidas exitosamente: ",ans)
def ejecutar_buscar_por_localidad(b1: dict, b2: dict, b3: dict, b4: dict)->None:
    """ Ejecuta la opcion de buscar por localidad.
    Parametros:
        b1 (dict): Diccionario con la informacion del banco 1.
        b2 (dict): Diccionario con la informacion del banco 2.
        b3 (dict): Diccionario con la informacion del banco 3.
        b4 (dict): Diccionario con la informacion del banco 4.
    """
    print("Buscando por localidad")
    cadena = input("Por favor indique la cadena para buscar por localidad: ")
    bancos = mod.buscar_por_localidad(b1,b2,b3,b4,cadena)
    if len(bancos)!=0:
        print("Los bancos de sangre que tienen esa cadena en el nombre de su localidad: ",bancos)
    else:
        print("Ningun bancos de sangre tiene esa cadena en el nombre de su localidad")

def ejecutar_banco_con_mas_bolsas_de_un_tipo(b1: dict, b2: dict, b3: dict, b4: dict)->None:
    """Ejecuta la opcion de encontrar el banco con mas bolsas de un tipo de sangre
       en especifico.
    Parametros:
        b1 (dict): Diccionario con la informacion del banco 1.
        b2 (dict): Diccionario con la informacion del banco 2.
        b3 (dict): Diccionario con la informacion del banco 3.
        b4 (dict): Diccionario con la informacion del banco 4.
    """

    tipo = input("Ingrese el tipo de sangre a consultar (A+, A-, B+, B-, AB+, AB-, O+, O-): ")
    dic_bancos = mod.banco_con_mas_bolsas_de_un_tipo(b1,b2,b3,b4,tipo)
    keys = list(dic_bancos)
    print("El banco que tiene la mayor cantidad de bolsas de dicho tipo es:",dic_bancos[keys[0]])


def ejecutar_disponibilidad_por_tipo(b1: dict, b2: dict, b3: dict, b4: dict)->None:
    """Ejecuta la opcion de consultar la disponibilidad de bolsas de un tipo
       de sangre en especifico.
    Parametros:
        b1 (dict): Diccionario con la informacion del banco 1.
        b2 (dict): Diccionario con la informacion del banco 2.
        b3 (dict): Diccionario con la informacion del banco 3.
        b4 (dict): Diccionario con la informacion del banco 4.
    """

    tipo = input("Ingrese el tipo de sangre a consultar (A+, A-, B+, B-, AB+, AB-, O+, O-): ")
    print("la cantidad de bolsas disponibles de dicho tipo de sangre: ",mod.disponibilidad_por_tipo(b1,b2,b3,b4,tipo))


def ejecutar_tipo_mas_escaso(b1: dict, b2: dict, b3: dict, b4: dict)->None:
    """Ejecuta la opcion de encontrar el tipo de sangere mas escaso sumando
       todos los bancos.
    Parametros:
        b1 (dict): Diccionario con la informacion del banco 1.
        b2 (dict): Diccionario con la informacion del banco 2.
        b3 (dict): Diccionario con la informacion del banco 3.
        b4 (dict): Diccionario con la informacion del banco 4.
    """

    print("El tipo de sangre mas escaso es: ",mod.tipo_mas_escaso(b1,b2,b3,b4))


def ejecutar_hay_tipo_en_riesgo(b1: dict, b2: dict, b3: dict, b4: dict)->None:
    """ Ejecuta la opcion de encontrar si hay algun tipo de sangre en riesgo.
    Parametros:
        b1 (dict): Diccionario con la informacion del banco 1.
        b2 (dict): Diccionario con la informacion del banco 2.
        b3 (dict): Diccionario con la informacion del banco 3.
        b4 (dict): Diccionario con la informacion del banco 4
    """

    riesgo = int(input("Ingrese el valor minimo para que un tipo sea considerado en riesgo: "))
    band = mod.hay_tipo_en_riesgo(b1,b2,b3,b4,riesgo)

    if band == True:
        print("existe un tipo de sangre cuya cantidad total de bolsas (teniendo en cuenta los 4 bancos) es inferior a un número ingreado")
    else:
        print("No existe un tipo de sangre cuya cantidad total de bolsas (teniendo en cuenta los 4 bancos) es inferior a un número ingreado")

def ejecutar_promedio_donantes(b1: dict, b2: dict, b3: dict, b4: dict)->None:
    """Ejecuta la opcion de consultar la cantidad promedio de donantes por
       banco de sangre.
    Parametros:
        b1 (dict): Diccionario con la informacion del banco 1.
        b2 (dict): Diccionario con la informacion del banco 2.
        b3 (dict): Diccionario con la informacion del banco 3.
        b4 (dict): Diccionario con la informacion del banco 4
    """
    prom = mod.promedio_donantes(b1,b2,b3,b4)
    print("La cantidad promedio de donantes por banco de sangre es:",prom)


def iniciar_aplicacion():
    """Inicia la ejecucion de la aplicacion por consola.
    Esta funcion primero crea los cuatro bancos de sangre.
    Luego la funcion le muestra el menu al usuario y espera a que seleccione una opcion.
    Esta operacion se repite hasta que el usuario seleccione la opcion de salir.
    """
    banco1 = mod.crear_banco("Techo", "Kennedy", 0, 48, 42, 36, 13, 31, 50, 43, 42)
    banco2 = mod.crear_banco("Shaio", "Suba", 0, 20, 23, 21, 28, 32, 7, 36, 5)
    banco3 = mod.crear_banco("Bachue", "Engativa", 0, 23, 42, 45, 15, 50, 34, 20, 26)
    banco4 = mod.crear_banco("Cardioinfantil", "Usaquen",  0, 7, 20, 16, 37, 7, 43, 25, 10)

    ejecutando = True
    while ejecutando:
        print("\n\nEstado de los bancos" + ("-"*50))
        print("Banco de Sangre 1")
        mostrar_banco(banco1)
        print("-"*50)

        print("Banco de Sangre 2")
        mostrar_banco(banco2)
        print("-"*50)

        print("Banco de Sangre 3")
        mostrar_banco(banco3)
        print("-"*50)

        print("Banco de Sangre 4")
        mostrar_banco(banco4)
        print("-"*50)

        ejecutando = mostrar_menu_aplicacion(banco1, banco2, banco3, banco4)

        if ejecutando:
            input("Presione cualquier tecla para continuar ... ")


def mostrar_menu_aplicacion(b1: dict, b2: dict, b3: dict, b4:dict) -> bool:
    """Le muestra al usuario las opciones de ejecucion disponibles.
    Parametros:
        b1 (dict): Diccionario que contiene la informacion del banco 1.
        b2 (dict): Diccionario que contiene la informacion del banco 2.
        b3 (dict): Diccionario que contiene la informacion del banco 3.
        b4 (dict): Diccionario que contiene la informacion del banco 4.
    Retorno:
        Esta funcion retorna True si el usuario selecciono una opcion diferente
        a la opcion que le permite salir de la aplicacion.
        Esta funcion retorna False si el usuario selecciono la opcion para salir
        de la aplicacion.

    """
    print("Menu de opciones")
    print(" 1 - Recibir donacion")
    print(" 2 - Suministrar bolsas")
    print(" 3 - Transferir bolsas")
    print(" 4 - Buscar por localidad")
    print(" 5 - Consultar banco con mas bolsas de un tipo")
    print(" 6 - Consultar disponibilidad por tipo")
    print(" 7 - Consultar tipo de sangre mas escaso")
    print(" 8 - Consultar tipo de sangre en riesgo")
    print(" 9 - Consultar promedio de donantes")
    print(" 10 - Salir de la aplicacion.")

    opcion_elegida = input("Ingrese la opcion que desea ejecutar: ").strip()

    continuar_ejecutando = True

    if opcion_elegida == "1":
        ejecutar_recibir_donacion(b1, b2, b3, b4)
    elif opcion_elegida == "2":
        ejecutar_suministrar_bolsas(b1, b2, b3, b4)
    elif opcion_elegida == "3":
        ejecutar_transferir_bolsas(b1, b2, b3, b4)
    elif opcion_elegida == "4":
        ejecutar_buscar_por_localidad(b1, b2, b3, b4)
    elif opcion_elegida == "5":
        ejecutar_banco_con_mas_bolsas_de_un_tipo(b1, b2, b3, b4)
    elif opcion_elegida == "6":
        ejecutar_disponibilidad_por_tipo(b1, b2, b3, b4)
    elif opcion_elegida == "7":
        ejecutar_tipo_mas_escaso(b1, b2, b3, b4)
    elif opcion_elegida == "8":
        ejecutar_hay_tipo_en_riesgo(b1, b2, b3, b4)
    elif opcion_elegida == "9":
        ejecutar_promedio_donantes(b1, b2, b3, b4)
    elif opcion_elegida == "10":
        continuar_ejecutando = False
    else:
        print("La opcion " + opcion_elegida + " no es una opcion valida.")
    return continuar_ejecutando


iniciar_aplicacion()
