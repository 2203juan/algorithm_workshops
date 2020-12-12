

def extraerPalabras(texto):
    """
    Esta función toma todas las palabras del texto dado obviando los espacios 
    entre estas y las devuelve en una lista
    """
    # res es una lista que va a tener todas las palabras que se encuentren
    # tmp sirve para ir armando en el ciclo cada palabra
    res,i,tmp = [],0,""
    while i < len(texto):
        while(i < len(texto) and texto[i] != "" and texto[i] != " " and texto[i] != "\n"):# cico para tomar todas las letras
            tmp += texto[i] # si se llega a un espacio se rompe el ciclo
            i += 1
        if(len(tmp) > 0): # si hay al menos una letra en el string temporal lo agrego a la lista de respuesta
            res.append(tmp)
            tmp = ""
        i += 1
    return res


def contarSilabas(palabra):
    """
    Esta función cuenta todas las silabas de una palabra dada 
    """
    # res es la variable que sirve para contar la cantidad de silabas
    res = 0
    vocales = ["a","e","i","o","u","A","E","I","O","U"]
    if palabra[0] in vocales:# si empieza en unca vocal ya es una silaba
        res += 1
    for i in range(1, len(palabra)):# ciclo para recorrer la palabra en busca de silabas
        if palabra[i] in vocales and palabra[i-1] not in vocales:# si la letra actual es una vocal y la amterior es consonante se cuenta una nueva silaba
            res += 1
    if palabra[-1] == "e" or palabra[-1] == "E":# si la ultima letra es una e , se resta una silaba
        res -= 1
    if res == 0:# al menos hay una silaba
        res = 1
    return res

def silabasPorPalabra(palabras):
    """
    Esta funcion recibe una lista de palabras y cuenta cuantas silabas tiene cada una de ellas
    """
    # res es la variable que sirve para contar la cantidad de silabas por palabra
    res = 0
    for i in range(len(palabras)):#ciclo para recorrer la lista de palabras
        res += contarSilabas(palabras[i])
    return res

def graficarFrecSilabas(palabras):
    """
    Esta funcion sirve para graficar con * la frecuencia de cada tipo de silaba (monosilaba,bisilaba,etc..) 
    """
    # la palabra mas larga en español tiene a lo sumo 9 silabas
    contSilabas = [0 for i in range(9)] #la 0 representa si es monosilaba, la 1 si es bisilaba, etc
    for i in range(len(palabras)):# ciclo para recorrer la lista de palabras
        contSilabas[contarSilabas(palabras[i])-1] += 1 # actualiza la frecuencia de la cantidad de silabas

    for i in range(len(contSilabas)):# ciclo para imprimir la frecuencia
        print(i+1,end = " ")
        for j in range(contSilabas[i]):
            print("*",end="")
        print()
    

def graficarFrecPalabras(palabras):
    """
    Esta funcion sirve para graficar con * la frecuencia de cada palabra de la lista de palabras
    """
    palabrasVistas = [False for i in range(len(palabras))]
    contPalabra = [0 for i in range(len(palabras))]
    i = 0
    #El algoritmo consiste en pararme en la i-esima palabra y revisar de la i+1 en adelante cuantas veces aparece
    #dicha palabra, se tiene en cuenta que no se haya contado antes con el arreglo de palabras visitadas, si contPalabra
    #tiene  en alguna posicion un 0 significa que esa palabra ya la conté anteriormente
    while i < len(palabras):
        cont = 1
        j = i+1
        band = False
        if(palabrasVistas[i] == True):
            band = True
        palabrasVistas[i] = True
        while j < len(palabras) and not band:
            if(palabrasVistas[j] == False and palabras[i] == palabras[j]):
                palabrasVistas[j] = True
                cont += 1
            j += 1
        if(band):
            contPalabra[i] = 0
        else:
            contPalabra[i] = cont
        i += 1 
    
    for i in range(len(palabras)):# ciclo para graficar con * la frecuencia
        if contPalabra[i] > 0:
            print(palabras[i],end = " ")
        for j in range(contPalabra[i]):
            print("*",end = "")
        print()
    
#graficarFrecPalabras("hola hola hola mundo hola mundo la el lo lo".split())


def palabrasInfinitivo(palabras):
    """
    Esta funcion sirve para extraer los verbos en infinito que se encuentren en la lista de palabras    
    """
    palabrasInf = [] # esta lista sirve para guardar palabras que pueden significar el infinitivo de un verbo
    for i in range(len(palabras)):#ciclo para recorrer la lista de palabras
        final = ""
        j = len(palabras[i])-2 # en j se guarda el indice anterior a las ultimas dos letras de la palabra
        if(j >= 0):
            while j < len(palabras[i]):# ciclo para unir las dos ultimas letras
                final += palabras[i][j]
                j += 1
        if(final == "ar" or final == "er" or final == "ir"):# se revisa si terminan en ar,er o ir
            palabrasInf.append(palabras[i])
    return palabrasInf

#palabrasInfinitivo("palabra hola amar odiar fingir tejer".split())

def sustantivosPlurales(palabras):
    """
    La funcion recibe la lista de palabras y revisa los posibles sustantivos plurales,
    se tomand dos casos en cuenta: el primero es que hay un articulo plurar y lo siguiente
    a este es una palabra que termina en "s" y el otro caso es que la palabra termine en "s"
    """
    articulosPlurales = ["los","las","unos","unas"] # esta lista contiene los articulos que preceden a posibles plurales
    sustPlurales = []
    i = 0
    while i < len(palabras):
        if(palabras[i] in articulosPlurales and i+1 < len(palabras) and palabras[i+1][-1] == "s" and palabras[i+1] not in articulosPlurales):
            sustPlurales.append(palabras[i+1])
            i += 2
        elif(palabras[i][-1] == "s" and palabras[i] not in articulosPlurales):
            sustPlurales.append(palabras[i])
            i += 1
        else:
            i+=1
    return sustPlurales



def palabrasPreposiciones(palabras):
    """
    Esta funcion recibe la lista de palabras y se busca cada una de ellas en el arreglo que contiene
    todas las preposiciones
    """
    preposiciones = [ "a", "ante", "bajo", "cabe", "con", 
    "contra", "de", "desde", "durante", "en", "entre", "hacia", "hasta", "mediante", "para", "por", 
    "segun", "sin", "so", "sobre", "tras", "versus", "via"] # esta lista contiene todas las preposiciones existentes en español
    palabrasPrep = [] # esta lista sirve para guardar las preposiciones presentes en el texto
    for i in range(len(palabras)):
        if(palabras[i] in preposiciones):
            palabrasPrep.append(palabras[i])
    return palabrasPrep


def inicianVocal(palabras):
    """
    Esta funcion revisa la primera letra de cada palabra de la lista de palabras
    y se agrega a la lista palabrasIni en caso de que esta sea una vocal
    """
    palabrasIni = [] # esta lista sirve para guardar las palabras que empiezan en vocal
    vocales = ["a","e","i","o","u","A","E","I","O","U"]
    for i in range(len(palabras)):
        if(palabras[i][0] in vocales):
            palabrasIni.append(palabras[i])
    return palabrasIni
    

def finalizanVocal(palabras):
    """
    Esta funcion revisa la ultima letra de cada palabra de la lista de palabras
    y se agrega a la lista palabrasFin en caso de que esta sea una vocal
    """
    palabrasFin = [] # esta lista sirve para guardar las palabras que finalizan en vocal
    vocales = ["a","e","i","o","u","A","E","I","O","U"]
    for i in range(len(palabras)):
        if(palabras[i][-1] in vocales):
            palabrasFin.append(palabras[i])
    return palabrasFin
    
def inicianConsonante(palabras):
    """
    Esta funcion revisa la primera letra de cada palabra de la lista de palabras
    y se agrega a la lista palabrasIni en caso de que esta sea una consonante
    """
    palabrasIni = [] # esta lista sirve para guardar las palabras que empiezan en consonante
    vocales = ["a","e","i","o","u","A","E","I","O","U"]
    for i in range(len(palabras)):
        if(palabras[i][0] not in vocales):
            palabrasIni.append(palabras[i])
    return palabrasIni

def finalizanConsonante(palabras):
    """
    Esta funcion revisa la ultima letra de cada palabra de la lista de palabras
    y se agrega a la lista palabrasFin en caso de que esta sea una consonante
    """
    palabrasFin = [] # esta lista sirve para guardar las palabras que finalizan en consonante
    vocales = ["a","e","i","o","u","A","E","I","O","U"]
    for i in range(len(palabras)):
        if(palabras[i][-1] not in vocales):
            palabrasFin.append(palabras[i])
    return palabrasFin



def buscarPatron(p,t):
     """
     Esta funcion busca si el string p esta dentro del string t
     """    
     res = False # esta bandera sirve para identificar cuando se encuentra un patron p en una palabra t
     i = 0
     while i < len(t) and not res:
         j = 0
         k = i
         while j < len(p) and k < len(t) and p[j] == t[k]:# mientras sean iguales lo caracteres de ambos strings sigo iterando sobre ellos teniendo en cuenta el tamaño de ambos
             j += 1
             k += 1
         if(j == len(p)):# si j = tamaño del patron es porque todos los caracteres son iguales respceto al segmento de texto que se esta revisando
            res = True # ya se encontro el patron
         i += 1
     return res


"""
claro -> aclarar, claridad, claramente, clarificar
"""
def buscarFamilia(palabra,palabras):
    """
    Esta funcion busca si las palabras de la lista de palabras contienen la palabra que se recibe por parametro
    """
    familia = [] # esta liste sirve para guardar la familia de palabras que tengan la raiz dada en palabra
    for i in range(len(palabras)):
        if(buscarPatron(palabra,palabras[i])):
            familia.append(palabras[i])
    return familia

