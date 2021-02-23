import matplotlib.pyplot as plt

def eliminar_salto_linea(lista):
    i = 0
    while i < len(lista):
        lista[i] = lista[i].strip()
        i+=1
    return lista

def cargar_correos():
    correos = list()
    
    f = open("correo1.txt", "r")
    correos.append(eliminar_salto_linea(f.readlines()))
    f.close()

    f = open("correo2.txt", "r")
    correos.append(eliminar_salto_linea(f.readlines()))
    f.close()

    f = open("correo3.txt", "r")
    correos.append(eliminar_salto_linea(f.readlines()))
    f.close()

    f = open("correo4.txt", "r")
    correos.append(eliminar_salto_linea(f.readlines()))
    f.close()

    f = open("correo5.txt", "r")
    correos.append(eliminar_salto_linea(f.readlines()))
    f.close()

    f = open("correo6.txt", "r")
    correos.append(eliminar_salto_linea(f.readlines()))
    f.close()

    f = open("correo7.txt", "r")
    correos.append(eliminar_salto_linea(f.readlines()))
    f.close()

    f = open("correo8.txt", "r")
    correos.append(eliminar_salto_linea(f.readlines()))
    f.close()

    f = open("correo9.txt", "r")
    correos.append(eliminar_salto_linea(f.readlines()))
    f.close()

    f = open("correo10.txt", "r")
    correos.append(eliminar_salto_linea(f.readlines()))
    f.close()

    return correos

def cargar_palabras():
    f = open("PalabrasMalas.txt","r")
    palabras = f.readline().split(":")
    return palabras

def obtener_correo_para(mail):
    mail = mail.replace("Para:","")
    return mail.strip()


def obtener_correo_de(mail):
    mail = mail.replace("De:","")
    return mail.strip()

def grafico_a(correos):
    destinatarios = list()
    
    for correo in correos:
        dest = obtener_correo_para(correo[1])
        if dest not in destinatarios:
            destinatarios.append(dest)

    cuenta_destinatarios = [ 0 for i in range(len(destinatarios))]

    for i in range(len(destinatarios)):
        for correo in correos:
            if obtener_correo_para(correo[1]) == destinatarios[i]:
                cuenta_destinatarios[i] +=1

    lista_5_dest = list()

    for i in range(len(destinatarios)):
        lista_5_dest.append((destinatarios[i], cuenta_destinatarios[i]))
    
    lista_5_dest.sort(key = lambda x: -x[1])

    lista_5_dest = lista_5_dest[:5]

    x = list()
    y = list()

    for a,b in lista_5_dest:
        x.append(a)
        y.append(b)
    
    plt.figure(figsize=(20,15))
    plt.bar(x, y)
    plt.xticks(rotation = 10)
    plt.show()

def grafico_b(correos, palabras):
    conteo_palabras = [0 for i in range(len(palabras))]

    for i in range(len(palabras)):
        for j in range(len(correos)):
            for k in range(len(correos[j])):
                if palabras[i] in correos[j][k]:
                    conteo_palabras[i] +=1
            
    lista_10_pal = list()

    for i in range(len(palabras)):
        lista_10_pal.append((palabras[i], conteo_palabras[i]))
    
    lista_10_pal.sort(key = lambda x: -x[1])

    lista_10_pal = lista_10_pal[:10]

    x = list()
    y = list()

    for a,b in lista_10_pal:
        x.append(a)
        y.append(b)
    
    plt.figure(figsize=(20,15))
    plt.bar(x, y)
    plt.xticks(rotation = 10)
    plt.show()

def grafico_c(correos, palabras):
    normales = 0
    anormales = 0
    peligrosos = 0

    for i in range(len(correos)):
        tmp_corr = 0
        for j in range(len(correos[i])):
            for k in range(len(palabras)):
                if palabras[k] in correos[i][j]:
                    tmp_corr +=1
        
        if tmp_corr == 0:
            normales +=1
        
        elif tmp_corr >=1 and tmp_corr <= 10:
            anormales +=1
        elif tmp_corr >= 11:
            peligrosos +=1

    plt.figure(figsize=(20,15))
    plt.bar("Normales",normales)
    plt.bar("Anormales",anormales)
    plt.bar("Peligrosos",peligrosos)
    plt.show()


def obtener_empresa_correo(mail):
    i = len(mail) - 1

    while i > 0 and mail[i]!=".":
        i-=1
    
    ans = list()

    while i > 0 and mail[i]!="@":
        ans.append(mail[i])
        i-=1
    
    res = ""

    i = len(ans) - 1

    while i > 0:
        res+=ans[i]
        i-=1

    return res

def correos_mas_usados(correos):
    lista_correos = list()
    for correo in correos:
        if obtener_correo_de(correo[0]) not in lista_correos:
            lista_correos.append(obtener_correo_de(correo[0]))
        
        if obtener_correo_para(correo[1]) not in lista_correos:
            lista_correos.append(obtener_correo_para(correo[1]))
    
    correos_existentes = list()
    
    for correo in lista_correos:
        if obtener_empresa_correo(correo) not in correos_existentes:
            correos_existentes.append(obtener_empresa_correo(correo))
    
    cuenta_correos = [ 0 for i in range(len(correos_existentes))]

    for i in range(len(correos_existentes)):
        for j in range(len(lista_correos)):
            if correos_existentes[i] == obtener_empresa_correo(lista_correos[j]):
                cuenta_correos[i] +=1

    
    lista_mas_usados = list()

    for i in range(len(correos_existentes)):
        lista_mas_usados.append((correos_existentes[i], cuenta_correos[i]))
    
    lista_mas_usados.sort(key = lambda x: -x[1])
    ans = list()

    # se devuelven los 3 correos mas usados
    for a,b in lista_mas_usados:
        ans.append(a)
    
    return ans[:3]


def obtener_dominio_correo(mail):
    i = len(mail) - 1
    ans = list()

    while i > 0 and mail[i]!=".":
        ans.append(mail[i])
        i-=1
    i = len(ans) - 1

    res = ""
    while i >= 0:
        res+=ans[i]
        i-=1

    return res

def dominios_mas_usados(correos):
    lista_correos = list()
    for correo in correos:
        if obtener_correo_de(correo[0]) not in lista_correos:
            lista_correos.append(obtener_correo_de(correo[0]))
        
        if obtener_correo_para(correo[1]) not in lista_correos:
            lista_correos.append(obtener_correo_para(correo[1]))
    
    correos_existentes = list()
    
    for correo in lista_correos:
        if obtener_dominio_correo(correo) not in correos_existentes:
            correos_existentes.append(obtener_dominio_correo(correo))
    
    cuenta_correos = [ 0 for i in range(len(correos_existentes))]

    for i in range(len(correos_existentes)):
        for j in range(len(lista_correos)):
            if correos_existentes[i] == obtener_dominio_correo(lista_correos[j]):
                cuenta_correos[i] +=1

    
    lista_mas_usados = list()

    for i in range(len(correos_existentes)):
        lista_mas_usados.append((correos_existentes[i], cuenta_correos[i]))
    
    lista_mas_usados.sort(key = lambda x: -x[1])
    ans = list()

    # se devuelven los 3 correos mas usados
    for a,b in lista_mas_usados:
        ans.append(a)
    
    return ans[:3]


def generar_resumen(correos, palabras):
    lineas = "Las 3 empresas de correo más utilizadas son: "
    mas_usados = correos_mas_usados(correos)
    mas_usados_dom = dominios_mas_usados(correos)

    for i in range(len(mas_usados)):
        if i+1 == len(mas_usados):
            lineas += (mas_usados[i]+"\n\n")
        else:
            lineas += (mas_usados[i]+",")
    
    lineas += "Los 3 dominios más utilizados son: "
    for i in range(len(mas_usados_dom)):
        if i+1 == len(mas_usados_dom):
            lineas += (mas_usados_dom[i]+"\n\n")
        else:
            lineas += (mas_usados_dom[i]+",")

    for i in range(len(correos)):
        lineas += "Correo "+str(i+1)+"\n"
        tmp_corr = 0
        tmp_pal = list()
        for j in range(len(correos[i])):
            for k in range(len(palabras)):
                if palabras[k] in correos[i][j]:
                    tmp_pal.append(palabras[k])
                    tmp_corr +=1
        
        lineas += correos[i][0]+"\n"
        lineas += correos[i][1]+"\n"

        lineas += "Palabras peligrosas encontradas: "

        if len(tmp_pal) == 0:
            lineas += "0\n"
        else:
            for m in range(len(tmp_pal)):
                if m+1 == len(tmp_pal):
                    lineas += tmp_pal[m]+"\n"
                else:
                    lineas += tmp_pal[m]+","

        if tmp_corr == 0:
            lineas += "Este correo es: Normal\n\n"
        
        elif tmp_corr >=1 and tmp_corr <= 10:
            lineas += "Este correo es: Anormal\n\n"
            
        elif tmp_corr >= 11:
            lineas += "Este correo es: Peligroso\n\n"

    f = open("resumen.txt","w")
    f.write(lineas)
    f.close()
def main():
    op = 1
    correos = cargar_correos()
    palabras_peligrosas = cargar_palabras()
    
    while op !=0:
        print("Seleccione una opcion")
        print("0) Salir")
        print("1) Grafico 5 correos mas citados como destino")
        print("2) Grafico 10 palabras maliciosas mas utilizadas")
        print("3) Gráfico cantidad de correos ”Normales”, correos ”Anormales”,y correos ”Peligrosos.")
        print("4) Generar Resumen")
        op = int(input())

        while op < 0 and op > 4:
            print("opcion no valida!!")
            print("Seleccione una opcion")
            print("0) Salir")
            print("1) Grafico 5 correos mas citados como destino")
            print("2) Grafico 10 palabras maliciosas mas utilizadas")
            print("3) Gráfico cantidad de correos ”Normales”, correos ”Anormales”,y correos ”Peligrosos.")
            print("4) Generar Resumen")

            op = int(input())
        
        if op == 1:
            grafico_a(correos)
        
        elif op == 2:
            grafico_b(correos, palabras_peligrosas)
        
        elif op == 3:
            grafico_c(correos, palabras_peligrosas)
        
        elif op == 4:
            generar_resumen(correos, palabras_peligrosas)    
main()