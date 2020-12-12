"""
Ejercicio nivel 2: Bancos de Sangre.
Modulo de calculos.

Temas:
* Variables.
* Tipos de datos.
* Expresiones aritmeticas.
* Instrucciones basicas y consola.
* Dividir y conquistar: funciones y paso de parametros.
* Especificacion y documentacion.
* Instrucciones condicionales.
* Diccionarios.


NOTA IMPORTANTE PARA TENER EN CUENTA EN TODAS LAS FUNCIONES DE ESTE MoDULO:
        Los diccionarios de los bancos de sangre tienen las siguientes parejas de llave-valor:
            -   nombre (str): Nombre del banco.
            -   localidad (str): Nombre de la localidad donde se encuentra el banco.
            -   donantes (int): Numero de donantes que ha tenido el banco.
            -   A+ (int): Cantidad de bolsas disponibles de tipo A positivo.
            -   A- (int): Cantidad de bolsas disponibles de tipo A negativo.
            -   B+ (int): Cantidad de bolsas disponibles de tipo B positivo.
            -   B- (int): Cantidad de bolsas disponibles de tipo B negativo.
            -   AB+ (int): Cantidad de bolsas disponibles de tipo AB positivo.
            -   AB- (int): Cantidad de bolsas disponibles de tipo AB negativo.
            -   O+ (int): Cantidad de bolsas disponibles de tipo O positivo.
            -   O- (int): Cantidad de bolsas disponibles de tipo O negativo.
"""

def crear_banco(nombre:str, loc:str, cant_donantes:int, a_positivo:int, a_negativo:int,
                b_positivo:int, b_negativo:int, ab_positivo:int, ab_negativo:int,
                o_positivo:int, o_negativo:int)->dict:

    """Crea un diccionario que representa un nuevo banco con todos sus atributos
       inicializados.
    Parametros:
        nombre (str): Nombre del banco.
        loc (str): Nombre de la localidad donde se encuentra el banco.
        cant_donantes (int): Numero de donantes que ha tenido el banco.
        a_positivo (int): Cantidad de bolsas disponibles de tipo A positivo.
        a_negativo (int): Cantidad de bolsas disponibles de tipo A negativo.
        b_positivo (int): Cantidad de bolsas disponibles de tipo B positivo.
        b_negativo (int): Cantidad de bolsas disponibles de tipo B negativo.
        ab_positivo (int): Cantidad de bolsas disponibles de tipo AB positivo.
        ab_negativo (int): Cantidad de bolsas disponibles de tipo AB negativo.
        o_positivo (int): Cantidad de bolsas disponibles de tipo O positivo.
        o_negativo (int): Cantidad de bolsas disponibles de tipo O negativo.
     Retorna:
        dict: Diccionario con los datos del banco.
    """

   
    return {"nombre":nombre, "localidad":loc,"donantes":cant_donantes, "A+":a_positivo,
    "A-":a_negativo,"B+":b_positivo,"B-":b_negativo,"AB+":ab_positivo,
    "AB-":ab_negativo,"O+":o_positivo,"O-":o_negativo}


def buscar_banco(nombre_banco:str, b1:dict, b2:dict, b3:dict, b4:dict)->dict:
    """Busca en cual de los 4 diccionarios que se pasan por parametro esta
       el banco de sangre cuyo nombre es dado por parametro.
       Si no se encuentra el banco se debe retornar None.
    Parametros:
        nombre_banco (str): El nombre del banco que se desea buscar.
        b1 (dict): Diccionario con la informacion del banco 1.
        b2 (dict): Diccionario con la informacion del banco 2.
        b3 (dict): Diccionario con la informacion del banco 3.
        b4 (dict): Diccionario con la informacion del banco 4.
    Retorna:
        dict: Diccionario del banco cuyo nombre fue dado por parametro.
        None si no se encuentra.
    """
    
    if(b1["nombre"] == nombre_banco):
        return b1
    elif(b2["nombre"] == nombre_banco):
        return b2
    elif(b3["nombre"] == nombre_banco):
        return b3
    elif(b4["nombre"] == nombre_banco):
        return b4
    return None


def validar_donante(genero:str, edad:int, peso:int)->int:
    """Valida los datos del donante y calcula la cantidad de bolsas que este
       debe donar segun sus datos personales.
    Parametros:
        genero (str): Genero del donante, puede ser "M" o "F".
        edad (int): Edad del donante en años.
        peso (int): Peso del donante en kilogramos, como un número entero.
    Retorna:
        int: El numero de bolsas que el donante debe donar. Si la persona no
        es apta para donar por incumplir alguna de las reglas, se retorna 0.
    """
    bolsas = 0
    if(edad >= 18 and edad <= 65 and peso >= 50):
        if(genero == "M"): #masculino
            if(peso < 80):
                bolsas = 1
            elif(peso >= 80 and peso < 120):
                bolsas=2
            else:
                bolsas = 3
        else: #femenino
            if(peso < 75):
                bolsas =  1
            else:
                bolsas = 2
    return bolsas


def recibir_donacion(genero:str, edad:int, peso:int, tipo:str, banco:dict)->int:
    """Registra una donacion de bolsas de sangre segun las reglas descritas en
       el enunciado.
    Parametros:
        genero (str): Genero del donante, puede ser "M" o "F".
        edad (int): Edad del donante en años.
        peso (int): Peso del donante en kilogramos.
        tipo (str): Tipo de sangre del donante. Corresponde a uno de los tipos válidos
                    A+, A-, AB+, AB-, B+, B-, O+, O-
        banco (banco): Banco de sangre receptor.
    Retorna:
        int: El numero de bolsas que se donaron.
    """
    donaciones = validar_donante(genero,edad,peso)
    if(donaciones > 0):
        if(tipo == "O+" or tipo == "A+"):
            donaciones=1
        banco[tipo] += donaciones
        banco["donantes"] += 1
    return donaciones


def suministrar_bolsas(tipo:str,cantidad:int,banco:dict)->bool:
    """Registra un suministro de bolsas de sangre a un hospital segun las reglas
       descritas en el enunciado. Esta funcion es responsable de verificar previamente
       que el suministro sea viable.
    Parametros:
        tipo (str): Tipo de sangre que se necesita. Corresponde a uno de los tipos válidos
                    A+, A-, AB+, AB-, B+, B-, O+, O-
        cantidad (int): Cantidad de bolsas que se desean suministrar.
        banco (banco): Banco de sangre que suministrara las bolsas.
    Retorna:
        bool: True si el suministro pudo ser realizado. False de lo contrario.
    """
    realizado=None
    if(banco[tipo]-cantidad >= 5):
        realizado = True
    else:
        realizado = False
    
    return realizado


def transferir_bolsas(tipo:str,cantidad:int,banco1:dict,banco2:dict)->int:
    """Registra una transferencia de bolsas de sangre entre bancos segun las reglas
       descritas en el enunciado. Esta funcion es responsable de verificar previamente
       que la transferencia sea viable.
    Parametros:
        tipo (str): Tipo de sangre que se necesita. Corresponde a uno de los tipos válidos
                    A+, A-, AB+, AB-, B+, B-, O+, O-
        cantidad (int): Cantidad de bolsas que se desean transferir.
        banco1 (banco): Banco de sangre origen.
        banco2 (banco): Banco de sangre destino.
    Retorna:
        int: Numero de bolsas efectivamente transferidas. 0 en caso de que no se haya
        podido realizar la transferencia.
    """
    bolsas = 0
    if(suministrar_bolsas(tipo,cantidad,banco1) == True):
        banco2[tipo]+=cantidad
        banco1[tipo]-=cantidad
        bolsas=cantidad
    else:
        if(banco1[tipo]-5 > 0):
            bolsas=banco1[tipo]-5
            banco2[tipo]+=bolsas
            banco1[tipo]-=bolsas

    return bolsas

def buscar_por_localidad(b1:dict, b2:dict, b3:dict, b4:dict, cadena: str)->str:
    """Busca entre los bancos de sangre cuales tienen en su localidad la cadena recibida
       por parametro. La busqueda no tiene en cuenta mayusculas o minusculas.
    Parametros:
        b1 (dict): Diccionario con la informacion del banco 1.
        b2 (dict): Diccionario con la informacion del banco 2.
        b3 (dict): Diccionario con la informacion del banco 3.
        b4 (dict): Diccionario con la informacion del banco 4.
        cadena (str): La cadena usada para la busqueda.
    Retorna:
        str: Una cadena con el nombre del banco que contiene la cadena parámetro
        en su localidad. Si hay mas de un banco, entonces se retornan los
        nombres de todos los bancos relevantes separados por comas. Si ningún banco
        tiene la cadena entonces retorna una cadena vacía.
    """

    nombre = ""
    cadena = cadena.lower()
    if(b1["localidad"].lower() == cadena):
        nombre = b1["nombre"]
    if(b2["localidad"].lower() == cadena):
        if(nombre != ""):
            nombre = nombre+", "+b2["nombre"]
        else:
            nombre = b2["nombre"]
    if(b3["localidad"].lower() == cadena):
        if(nombre != ""):
            nombre = nombre+", "+b3["nombre"]
        else:
            nombre = b3["nombre"]
    if(b4["localidad"].lower() == cadena):
        if(nombre != ""):
            nombre = nombre+", "+b4["nombre"]
        else:
            nombre = b4["nombre"]

    return nombre


def banco_con_mas_bolsas_de_un_tipo(b1:dict, b2:dict, b3:dict, b4:dict,tipo:str)->dict:
    """Busca el banco de sangre que tiene la mayor cantidad de bolsas del tipo recibido
       por parametro.
    Parametros:
        b1 (dict): Diccionario con la informacion del banco 1.
        b2 (dict): Diccionario con la informacion del banco 2.
        b3 (dict): Diccionario con la informacion del banco 3.
        b4 (dict): Diccionario con la informacion del banco 4.
        tipo (str): Tipo de sangre a buscar. Corresponde a uno de los tipos válidos
                    A+, A-, AB+, AB-, B+, B-, O+, O-
    Retorna:
        dict: El diccionario del banco con mayor disponibilidad de bolsas del tipo
        recibido por parametro.
    """
    banco = None
    if(b1[tipo] >= b2[tipo] and b1[tipo] >= b3[tipo] and b1[tipo] >= b4[tipo]):
        banco = b1
    elif(b2[tipo] >= b1[tipo] and b2[tipo] >= b3[tipo] and b2[tipo] >= b4[tipo]):
        banco = b2
    elif(b3[tipo] >= b1[tipo] and b3[tipo] >= b2[tipo] and b3[tipo] >= b4[tipo]):
        banco = b3
    else:
        banco = b4
    return banco


def disponibilidad_por_tipo(b1:dict, b2:dict, b3:dict, b4:dict, tipo:str)->int:
    """Calcula la cantidad de bolsas de sangre disponibles en todos los bancos
       de un tipo de sangre en especifico.
    Parametros:
        b1 (dict): Diccionario con la informacion del banco 1.
        b2 (dict): Diccionario con la informacion del banco 2.
        b3 (dict): Diccionario con la informacion del banco 3.
        b4 (dict): Diccionario con la informacion del banco 4.
        tipo (str): Tipo de sangre a consultar. Corresponde a uno de los tipos válidos
                    A+, A-, AB+, AB-, B+, B-, O+, O-
    Retorna:
        int: La suma de todas las bolsas disponibles en todos los bancos del
        tipo de sangre a consultar.
    """

    return b1[tipo]+b2[tipo]+b3[tipo]+b4[tipo]


def tipo_mas_escaso_banco(banco:dict)->str:
    """Busca el tipo de sangre que tiene la menor cantidad de bolsas disponibles
       en un solo banco.
    Parametros:
        banco(dict): diccionario con la informacion del banco
    Retorna:
        str: Cadena de caracteres con el tipo de sangre menos disponible del banco.
    """
    tipo = ""
    if(banco["A+"] <= banco["A-"] and banco["A+"] <= banco["B+"] and banco["A+"] <= banco["B-"] and banco["A+"] <= banco["AB+"] and banco["A+"] <= banco["AB-"] and banco["A+"] <= banco["O+"] and banco["A+"] <= banco["O-"]):
        tipo = "A+"
    elif(banco["A-"] <= banco["A+"] and banco["A-"] <= banco["B+"] and banco["A-"] <= banco["B-"] and banco["A-"] <= banco["AB+"] and banco["A-"] <= banco["AB-"] and banco["A-"] <= banco["O+"] and banco["A-"] <= banco["O-"]):
        tipo ="A-"
    elif(banco["B+"] <= banco["A+"] and banco["B+"] <= banco["A-"] and banco["B+"] <= banco["B-"] and banco["B+"] <= banco["AB+"] and banco["B+"] <= banco["AB-"] and banco["B+"] <= banco["O+"] and banco["B+"] <= banco["O-"]):
        tipo = "B+"
    elif(banco["B-"] <= banco["A+"] and banco["B-"] <= banco["A-"] and banco["B-"] <= banco["B+"] and banco["B-"] <= banco["AB+"] and banco["B-"] <= banco["AB-"] and banco["B-"] <= banco["O+"] and banco["B-"] <= banco["O-"]):
        tipo = "B-"
    elif(banco["AB+"] <= banco["A+"] and banco["AB+"] <= banco["A-"] and banco["AB+"] <= banco["B+"] and banco["AB+"] <= banco["B-"] and banco["AB+"] <= banco["AB-"] and banco["AB+"] <= banco["O+"] and banco["AB+"] <= banco["O-"]):
        tipo = "AB+"
    elif(banco["AB-"] <= banco["A+"] and banco["AB-"] <= banco["A-"] and banco["AB-"] <= banco["B+"] and banco["AB-"] <= banco["B-"] and banco["AB-"] <= banco["AB+"] and banco["AB-"] <= banco["O+"] and banco["AB-"] <= banco["O-"]):
        tipo = "AB-"
    elif(banco["O+"] <= banco["A+"] and banco["O+"] <= banco["A-"] and banco["O+"] <= banco["B+"] and banco["O+"] <= banco["B-"] and banco["O+"] <= banco["AB+"] and banco["O+"] <= banco["AB-"] and banco["O+"] <= banco["O-"]):
        tipo = "O+"
    else:
        tipo = "O-"
    return tipo


def tipo_mas_escaso(b1:dict, b2:dict, b3:dict, b4:dict)->str:
    """Busca el tipo de sangre que tiene la menor cantidad de bolsas disponibles
       teniendo en cuenta todos los bancos.
    Parametros:
        b1 (dict): Diccionario con la informacion del banco 1.
        b2 (dict): Diccionario con la informacion del banco 2.
        b3 (dict): Diccionario con la informacion del banco 3.
        b4 (dict): Diccionario con la informacion del banco 4.
    Retorna:
        str: Cadena de caracteres con el tipo de sangre menos disponible.
    """
    tipo = ""
    menorb1 = tipo_mas_escaso_banco(b1)
    menorb2 = tipo_mas_escaso_banco(b2)
    menorb3= tipo_mas_escaso_banco(b3)
    menorb4=tipo_mas_escaso_banco(b4)
    if(b1[menorb1] <= b2[menorb2] and b1[menorb1] <= b3[menorb3] and b1[menorb1] <=b4[menorb4]):
        tipo = menorb1
    elif(b2[menorb2] <= b1[menorb1] and b2[menorb2] <= b3[menorb3] and b2[menorb2] <=b4[menorb4]):
        tipo = menorb2
    elif(b3[menorb3] <= b1[menorb1] and b3[menorb3] <= b2[menorb2] and b3[menorb3] <=b4[menorb4]):
        tipo = menorb3
    else:
        tipo = menorb4

    return tipo


def hay_tipo_en_riesgo(b1:dict, b2:dict, b3:dict, b4:dict, riesgo:int)->bool:
    """Determina si existe un tipo de sangre cuya cantidad total de bolsas (teniendo
       en cuenta los 4 bancos) es inferior al numero recibido por parametro.
    Parametros:
        b1 (dict): Diccionario con la informacion del banco 1.
        b2 (dict): Diccionario con la informacion del banco 2.
        b3 (dict): Diccionario con la informacion del banco 3.
        b4 (dict): Diccionario con la informacion del banco 4.
        riesgo (int): Numero minimo para considerar un tipo de sangre como en riesgo.
    Retorna:
        bool: True si hay algun tipo en riesgo, False de lo contrario.
    """

    tipoR = False
    if(b1["A+"] < riesgo or b1["A-"] < riesgo or b1["B+"] < riesgo or b1["B-"] < riesgo or b1["AB+"] < riesgo or b1["AB-"] < riesgo or b1["O+"] < riesgo or b1["O-"]< riesgo):
        tipoR = True
    if(b2["A+"] < riesgo or b2["A-"] < riesgo or b2["B+"] < riesgo or b2["B-"] < riesgo or b2["AB+"] < riesgo or b2["AB-"] < riesgo or b2["O+"] < riesgo or b2["O-"]< riesgo):
        tipoR = True
    if(b3["A+"] < riesgo or b3["A-"] < riesgo or b3["B+"] < riesgo or b3["B-"] < riesgo or b3["AB+"] < riesgo or b3["AB-"] < riesgo or b3["O+"] < riesgo or b3["O-"]< riesgo):
        tipoR = True
    if(b4["A+"] < riesgo or b4["A-"] < riesgo or b4["B+"] < riesgo or b4["B-"] < riesgo or b4["AB+"] < riesgo or b4["AB-"] < riesgo or b4["O+"] < riesgo or b4["O-"]< riesgo):
        tipoR = True    

    return tipoR


def promedio_donantes(b1:dict, b2:dict, b3:dict, b4:dict)->float:
    """Calcula la cantidad promedio de donantes por banco de sangre.
    Parametros:
        b1 (dict): Diccionario con la informacion del banco 1.
        b2 (dict): Diccionario con la informacion del banco 2.
        b3 (dict): Diccionario con la informacion del banco 3.
        b4 (dict): Diccionario con la informacion del banco 4.
    Retorna:
        float: Promedio de donantes entre los 4 bancos, redondeado a 2
        decimales.
    """

    return round((b1["donantes"]+b2["donantes"]+b3["donantes"]+b4["donantes"])/4,2)
