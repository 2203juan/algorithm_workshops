import statistics as st
def p1():
    monto = int(input("Ingrese el monto: "))
    monto_final = 0

    while monto != 0:
        if monto > 0:
            monto_final += monto
        monto = int(input("Ingrese el monto: "))

    if monto_final > 1000:
        monto_final = monto_final*(1-0.1)# descuento del 10%
    
    if monto_final < 100:
        monto_final += 500 # recargo extra
    
    print("El total a pagar es: ", monto_final)


def p2():
    numero = int(input("Ingrese el numero: "))
    n = 0
    pares = 0
    impares = 0
    numeros = list()
    promedio =  0
    std = 0

    while numero > 0:
        n +=1
        numeros.append(numero)

        if numero % 2 == 0:
            pares +=1
        else:
            impares +=1

        numero = int(input("Ingrese el numero: "))
    
    print("Cantidad de numeros ingresados: ", n)
    print("Porcentaje de numeros pares ingresados", (pares/n)*100)
    print("Porcentaje de numeros impares ingresados", (impares/n)*100)
    print("Numero de mayor valor: ", max(numeros))
    print("NUmero de menor valor: ", min(numeros))
    print("Promedio = ", sum(numeros)/len(numeros))
    print("Desviacion estandar = ", st.pstdev(numeros))

def p3():
    titulo = input("Ingrese Libro: ")
    libros = ""
    num_lineas = 0
    while titulo !="*":
        if titulo == "/":
            num_lineas +=1
            cont = 0
            for c in libros:
                if c.isdigit():
                    cont +=1
            print("Cambio de linea. Aparecen {} dıgitos numericos".format(cont))
            libros = ""            
        else:
            libros+=titulo
        titulo = input("Ingrese Libro: ")
    print("Salida: se leyo {} linea".format(num_lineas))

def p4(dni):

    for c in dni:
        if not c.isdigit():
            return False
    if len(dni) < 8 or len(dni) > 10:
        return False
    return True


def p5(cadena):
    linea = cadena.strip()

    i = len(linea) - 1
    n = 0
    while i >= 0 and linea[i]!=" ":
        n+=1
        i-=1

    return n

def p6():
    print("Seleccione una opcion: ")
    print("1) Ingresar  Miembro")
    print("2) Salir")
    op = int(input())
    while op !=2:


        nombre = input("Ingrese el nombre: ")
        while len(nombre) < 5:
            print("El nombre debe tener al menos 5 caracteres")
            nombre = input("Ingrese el nombre: ")
        
        apellido = input("Ingrese el apellido: ")
        while len(apellido) < 3:
            print("El apellido debe tener al menos 3 caracteres")
            apellido = input("Ingrese el apellido: ")

        rut = input("Ingrese el rut: ")
        while len(rut) < 7:
            print("El rut debe tener al menos 7 caracteres")
            rut = input("Ingrese el rut: ")

        identificador = ""

        identificador += nombre[1:len(nombre)-2]
        identificador += apellido[:2]
        rut = rut.replace("-","")

        identificador+= rut[-4:]

        print("El identificador de este socio es: ", identificador)

        print("Seleccione una opcion: ")
        print("1) Ingresar  Miembro")
        print("2) Salir")
        op = int(input())

p1()
p2()
p3()
print(p4("12345678"))
print(p5("Hola Mundo"))
p6()