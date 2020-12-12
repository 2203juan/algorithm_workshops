import palabras as p
def main():
    #print("Ingrese texto")
    opcion = 0
    texto = ""
    palabra = ""
    palabras = []

    print("Ingrese texto")
    texto = input()
    palabras = p.extraerPalabras(texto)
    while opcion != 1:
        #print(contarSilabas(line))
        print("Ingrese 1 para salir")
        print("Ingrese 2 para contar la cantidad de palabras en el texto")
        print("Ingrese 3 para contar la cantidad de silabas en las palabras del texto")
        print("Ingrese 4 para mostrar graficamente la frecuencia de palabras monosilabas, bisilabas, trisilabas, etc")
        print("Ingrese 5 para mostrar graficamente la frecuencia de palabras en el texto")
        print("Ingrese 6 para mostrar las palabras y cantidad de palabras que pueden significar el plural de un sustantivo")
        print("Ingrese 7 para mostrar las palabras y cantidad de palabras que pueden significar el infinitivo de un verbo")
        print("Ingrese 8 para mostrar las palabras y la cantidad de palabras que son preposiciones")
        print("Ingrese 9 para mostrar las palabras y la cantidad de palabras que empiezan en vocal")
        print("Ingrese 10 para mostrar las palabras y la cantidad de palabras que terminan en vocal")
        print("Ingrese 11 para mostrar las palabras y la cantidad de palabras que inician en consonante")
        print("Ingrese 12 para mostrar las palabras y la cantidad de palabras que terminan en consonante")
        print("Ingrese 13 para buscar familia de palabras de una palabra dada")
        opcion = int(input())
        
        if opcion == 2:
            palabras = p.extraerPalabras(texto)
            print("La cantidad de palabras en el texto es de",len(palabras))
            print()
        elif (opcion == 3):
            print("La cantidad de silabas total es",p.silabasPorPalabra(palabras))
            print()
        elif (opcion == 4):
            p.graficarFrecSilabas(palabras)
            print()
        elif(opcion == 5):
            p.graficarFrecPalabras(palabras)
            print()
        elif(opcion == 6):
            sustPlurales = p.sustantivosPlurales(palabras)

            if(len(sustPlurales) > 0):
                print("Hay",len(sustPlurales)," sustantivos plurales y son")
                for i in range(len(sustPlurales)):
                    print(sustPlurales[i])
            else:
                print("No hay sustantivos plurales!")
            print()
        elif(opcion == 7):
            palabrasInf = p.palabrasInfinitivo(palabras)
            if(len(palabrasInf) > 0):
                print("Hay",len(palabrasInf)," palabras en infinitivo y son")
                for i in range(len(palabrasInf)):
                    print(palabrasInf[i])
            else:
                print("No hay verbos en infinitivo!")
            print()
        elif(opcion == 8):
            palabrasPrep = p.palabrasPreposiciones(palabras)
            if(len(palabrasPrep) > 0):
                print("Hay",len(palabrasPrep)," preposiciones")
                for i in range(len(palabrasPrep)):
                    print(palabrasPrep[i])
            else:
                print("No hay preposiciones!")
            print()
        elif(opcion == 9):
            palabrasIni = p.inicianVocal(palabras)
            if(len(palabrasIni) > 0):
                print("Hay",len(palabrasIni)," que empiezan en vocal")
                for i in range(len(palabrasIni)):
                    print(palabrasIni[i])
            else:
                print("No hay palabras que comiencen en vocal!")
            print()
        elif(opcion == 10):
            palabrasFin = p.finalizanVocal(palabras)

            if(len(palabrasFin) > 0):
                print("Hay",len(palabrasFin)," que terminan en vocal")
                for i in range(len(palabrasFin)):
                    print(palabrasFin[i])
            else:
                print("No hay palabras que terminen en vocal!")
            print()
        elif(opcion == 11):
            palabrasIni = p.inicianConsonante(palabras)
            if(len(palabrasIni) > 0):
                print("Hay",len(palabrasIni)," que empiezan en consonante")
                for i in range(len(palabrasIni)):
                    print(palabrasIni[i])
            else:
                print("No hay palabras que comiencen en consonante!")
            print()
        elif(opcion == 12):
            palabrasFin = p.finalizanConsonante(palabras)
            if(len(palabrasFin) > 0):
                print("Hay",len(palabrasFin)," que terminan en consonante")
                for i in range(len(palabrasFin)):
                    print(palabrasFin[i])
            else:
                print("No hay palabras que terminan en consonante!")
            print()
        elif(opcion == 13):
            print("Ingrese la palabra")
            palabra = input()
            familia = p.buscarFamilia(palabra,palabras)
            if(len(familia) > 0):
                print("Las palabras familia son")
                for i in range(len(familia)):
                    print(familia[i])
            else:
                print("No hay palabras en familia")
            print()
main()
