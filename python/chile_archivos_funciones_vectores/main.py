import matplotlib.pyplot as plt

def cargar_profesores(archivo):
    f = open(archivo + ".txt", "r")
    ans = list()

    for line in f:
        ans.append(line.strip().split(":"))
    
    return ans

def cargar_alumnos(archivo):
    f = open(archivo + ".txt", "r")
    ans = f.readline().split(":")
    return ans

def cargar_notas(archivo):
    f = open(archivo + ".txt", "r")
    ans = list()

    for line in f:
        ans.append(line.split(":"))
    
    for i in range(len(ans)):
        tmp = list()
        for j in range(len(ans[i])):
            tmp.append(int(ans[i][j]))
        ans[i] = tmp
    return ans

def autenticar(usuario, clave, profesores):
    for prof in profesores:
        if prof[0] == usuario and prof[1] == clave:
            return True
    return False


def modificar_profesor(profesores):
    usuario = input("Ingrese el usuario del profesor: ")
    clave = input("Ingrese la nueva clave: ")
    band = True
    for prof in profesores:
        if prof[0] == usuario:
            prof[1] = clave
            band = False
            break
    if band:
        print("Este profesor no está en el sistema")
    else:
        f = open("Profesores.txt", "w")

        for prof in profesores:
            f.write(prof[0]+":"+prof[1]+"\n")


            
def agregar_notas(notas, flag, alumnos):
    if flag == "v":
        f = open("NotasVibraciones.txt", "w")
        for n in range(len(notas)):
            tmp = int(input("Ingrese la calificacion de "+alumnos[n]+" :"))
            notas[n].append(tmp)

        for i in range(len(notas)):
            for j in range(len(notas[i])):
                if j+1 == len(notas[i]):
                    f.write(str(notas[i][j])+"\n")
                else:
                    f.write(str(notas[i][j])+":")

    else:
        f = open("NotasProgra.txt", "w")
        print(len(notas))
        for n in range(len(notas)):
            tmp = int(input("Ingrese la calificacion de "+alumnos[n]+" :"))
            notas[n].append(tmp)

        for i in range(len(notas)):
            for j in range(len(notas[i])):
                if j+1 == len(notas[i]):
                    f.write(str(notas[i][j])+"\n")
                else:
                    f.write(str(notas[i][j])+":")


def modificar_notas(notas, flag, alumnos):
    alumno = input("Ingrese el nombre del alumno: ")

    for i in range(len(alumnos)):
        if alumnos[i] == alumno:
            print("Seleccione la nota que desea modificar, entre 0 y ",len(notas[i])-1)
            print(notas[i])
            op = int(input())
            notas[i][op] = int(input("Ingrese la calificacion: "))
            break
    if flag == "v":
        f = open("NotasVibraciones.txt", "w")
    else:
        f = open("NotasProgra.txt", "w")

    for nota in notas:
        for i in range(len(nota)):
            if i+1 == len(nota):
                f.write(str(nota[i])+"\n")
            else:
                f.write(str(nota[i])+":")

def agregar_alumno(nombre):
    f = open("Alumnos.txt", "a")
    f.write(":"+nombre)

    f2 = open("NotasProgra.txt","r")
    size = len(f2.readline().strip().split(":"))

    f3 = open("NotasProgra.txt","a")
    for i in range(size):
        if i+1 == size:
            f3.write("0")
        else:
            if i != 0:
                f3.write("0:")
            else:
                f3.write("\n0:")

    f4 = open("NotasVibraciones.txt","r")
    size = len(f4.readline().strip().split(":"))

    f5 = open("NotasVibraciones.txt","a")
    for i in range(size):
        if i+1 == size:
            f5.write("0")
        else:
            if i != 0:
                f5.write("0:")
            else:
                f5.write("\n0:")


def modificar_alumno(nombre, alumnos):
    for i in range(len(alumnos)):
        if alumnos[i] == nombre:
            alumnos[i] = input("Ingrese el nuevo nombre: ")
            break
    f = open("Alumnos.txt","w")

    for i in range(len(alumnos)):
        if i+1 == len(alumnos):
            f.write(alumnos[i])
        else:
            f.write(alumnos[i]+":")

def grafica_reprobando():
    print("Seleccione la asignatura:\n 1) Programacion - 2) Vibraciones: ")
    op = int(input())
    notas_progra = cargar_notas("NotasProgra")
    notas_vibra = cargar_notas("NotasVibraciones")
    alumnos = cargar_alumnos("Alumnos")

    perdiendo_prog  = list()
    prom_prog = list()
    perdiendo_vib = list()
    prom_vib = list()

    for i in range(len(notas_progra)):
        prom = sum(notas_progra[i])/len(notas_progra[i])

        if prom < 55:
            perdiendo_prog.append(alumnos[i])
            prom_prog.append(prom)

    for i in range(len(notas_vibra)):
        prom = sum(notas_vibra[i])/len(notas_vibra[i])

        if prom < 55:
            perdiendo_vib.append(alumnos[i])
            prom_vib.append(prom)
    if op == 1:
        plt.plot(perdiendo_prog, prom_prog, marker = ".", color = "red")
        plt.xlabel("Alumnos que van perdiendo programacion")
        plt.ylabel("Promedio")
        plt.show()
    else:
        plt.plot(perdiendo_vib, prom_vib, marker = ".", color = "red")
        plt.xlabel("Alumnos que van perdiendo vibraciones")
        plt.ylabel("Promedio")
        plt.show()


def grafica_aprobando():
    print("Seleccione la asignatura:\n 1) Programacion - 2) Vibraciones: ")
    op = int(input())
    notas_progra = cargar_notas("NotasProgra")
    notas_vibra = cargar_notas("NotasVibraciones")
    alumnos = cargar_alumnos("Alumnos")

    ganando_prog  = list()
    prom_prog = list()
    ganando_vib = list()
    prom_vib = list()

    for i in range(len(notas_progra)):
        prom = sum(notas_progra[i])/len(notas_progra[i])

        if prom >= 55:
            ganando_prog.append(alumnos[i])
            prom_prog.append(prom)

    for i in range(len(notas_vibra)):
        prom = sum(notas_vibra[i])/len(notas_vibra[i])

        if prom >= 55:
            ganando_vib.append(alumnos[i])
            prom_vib.append(prom)
    if op == 1:
        plt.plot(ganando_prog, prom_prog, marker = ".", color = "green")
        plt.xlabel("Alumnos que van aprobando programacion")
        plt.ylabel("Promedio")
        plt.show()
    else:
        plt.plot(ganando_vib, prom_vib, marker = ".", color = "green")
        plt.xlabel("Alumnos que van aprobando vibraciones")
        plt.ylabel("Promedio")
        plt.show()

def dos_mejores():
    print("Seleccione la asignatura:\n 1) Programacion - 2) Vibraciones: ")
    op = int(input())
    notas_progra = cargar_notas("NotasProgra")
    notas_vibra = cargar_notas("NotasVibraciones")
    alumnos = cargar_alumnos("Alumnos")

    prom_prog = list()
    prom_vib = list()

    for i in range(len(notas_progra)):
        prom = sum(notas_progra[i])/len(notas_progra[i])
        prom_prog.append((alumnos[i], prom))

    for i in range(len(notas_vibra)):
        prom = sum(notas_vibra[i])/len(notas_vibra[i])
        prom_vib.append((alumnos[i], prom))
    

    if op == 1:
        prom_prog.sort(key = lambda x: -x[1])  
        x = list()
        y = list()

        for i in range(2):
            x.append(prom_prog[i][0])
            y.append(prom_prog[i][1])

        plt.plot(x, y, marker = "*", color = "green")
        plt.xlabel("Alumnos con los dos mejores promedios")
        plt.ylabel("Promedio")
        plt.show()
    else:
        prom_vib.sort(key = lambda x: -x[1])  
        x = list()
        y = list()

        for i in range(2):
            x.append(prom_vib[i][0])
            y.append(prom_vib[i][1])

        plt.plot(x, y, marker = "*", color = "green")
        plt.xlabel("Alumnos con los dos mejores promedios")
        plt.ylabel("Promedio")
        plt.show()

def dos_peores():
    print("Seleccione la asignatura:\n 1) Programacion - 2) Vibraciones: ")
    op = int(input())
    notas_progra = cargar_notas("NotasProgra")
    notas_vibra = cargar_notas("NotasVibraciones")
    alumnos = cargar_alumnos("Alumnos")

    prom_prog = list()
    prom_vib = list()

    for i in range(len(notas_progra)):
        prom = sum(notas_progra[i])/len(notas_progra[i])
        prom_prog.append((alumnos[i], prom))

    for i in range(len(notas_vibra)):
        prom = sum(notas_vibra[i])/len(notas_vibra[i])
        prom_vib.append((alumnos[i], prom))
    

    if op == 1:
        prom_prog.sort(key = lambda x: x[1])  
        x = list()
        y = list()

        for i in range(2):
            x.append(prom_prog[i][0])
            y.append(prom_prog[i][1])

        plt.plot(x, y, marker = "*", color = "green")
        plt.xlabel("Alumnos con los dos peores promedios")
        plt.ylabel("Promedio")
        plt.show()
    else:
        prom_vib.sort(key = lambda x: x[1])  
        x = list()
        y = list()

        for i in range(2):
            x.append(prom_vib[i][0])
            y.append(prom_vib[i][1])

        plt.plot(x, y, marker = "*", color = "green")
        plt.xlabel("Alumnos con los dos peores promedios")
        plt.ylabel("Promedio")
        plt.show()

def mostrar_menu():
    print("0) Salir")
    print("1) Modificar clave de profesor")
    print("2) Agregar Notas")
    print("3) Modificar Notas")
    print("4) Agregar Alumnos")
    print("5) Modificar Alumno")
    print("6) Gráfico de los alumnos que están reprobando el ramo")
    print("7) Gráfico de los alumnos que están aprobando el ramo")
    print("8) Gráfico de los alumnos con los dos mejores promedios")
    print("9) Gráfico de los alumnos con los dos peores promedios")

    op = int(input())

    while op < 0 or op > 9:
        print("opcion no valida")
        print("Ingrese un numero entre 0 y 8")
        op = int(input())
    return op

def main():
    profesores = cargar_profesores("Profesores")
    alumnos = cargar_alumnos("Alumnos")
    notas_progra = cargar_notas("NotasProgra")
    notas_vibra = cargar_notas("NotasVibraciones")

    print("Bienvenido al sistema")
    print("Por favor ingrese sus credenciales")
    usuario = input("Usuario: ")
    clave = input("Clave: ")

    ok = autenticar(usuario, clave, profesores)
    while not ok:
        print("Credenciales no validas!!")
        print("Por favor ingrese sus credenciales")
        usuario = input("Usuario: ")
        clave = input("Clave: ")
        ok = autenticar(usuario, clave, profesores)

    print("Felicidades, te autenticaste como profesor")
    print("Por favor selecciona una opción")

    op = mostrar_menu()
    while op != 0:
        if op == 1:
            modificar_profesor(profesores)
            profesores = cargar_profesores("Profesores")
        
        elif op == 2:
            print("Seleccione la asignatura")
            asignatura = int(input("1) Programacion - 2) Vibraciones : "))
            if asignatura == 1:
                agregar_notas(notas_progra,"p", alumnos)
                notas_progra = cargar_notas("NotasProgra")
            else:
                agregar_notas(notas_vibra, "v", alumnos)
                notas_vibra = cargar_notas("NotasVibraciones")

        
        elif op == 3:
            print("Seleccione la asignatura")
            asignatura = int(input("1) Programacion - 2) Vibraciones"))

            if asignatura == 1:
                modificar_notas(notas_progra,"p", alumnos)
                notas_progra = cargar_notas("NotasProgra")
            else:
                modificar_notas(notas_vibra, "v", alumnos)
                notas_vibra = cargar_notas("NotasVibraciones")
        
        elif op == 4:
            print("Ingrese el nombre del alumno")
            nombre = input()
            agregar_alumno(nombre)
            alumnos = cargar_alumnos("Alumnos")

        elif op == 5:
            print("Ingrese el nombre del alumno")
            nombre = input()
            modificar_alumno(nombre, alumnos)
            alumnos = cargar_alumnos("Alumnos")

        elif op == 6:
            grafica_reprobando()

        elif op == 7:
            grafica_aprobando()

        elif op == 8:
            dos_mejores()        
        
        elif op == 9:
            dos_peores()
        op  = mostrar_menu()


        print("6) Gráfico de los alumnos que están reprobando el ramo")
        print("7) Gráfico de los alumnos que están aprobando el ramo")
        print("8) Gráfico de los alumnos con los dos mejores promedios")
        print("8) Gráfico de los alumnos con los dos peores promedios")
        
        profesores = cargar_profesores("Profesores")
        alumnos = cargar_alumnos("Alumnos")
        notas_progra = cargar_notas("NotasProgra")
        notas_vibra = cargar_notas("NotasVibraciones")
main()