f2 = open("libros_consolidados.txt","w")

def leer_archivo(nombre):
    f = open(nombre+".txt", "r")
    ans = list()
    i = 0
    for line in f:
        if i > 0:
            ans.append(line.strip().split(";"))
        i+=1
    f.close()
    return ans



def solve():
    libros = leer_archivo("info_libros")
    libros_cnt = list()
    max_id = -1
    for lib in libros:
        if int(lib[0]) > max_id:
            max_id = int(lib[0])
        #print("lib: ", lib)
        i = 0
        while i < len(libros_cnt) and libros_cnt[i][0]!= lib[0]:
            i+=1
        if i == len(libros_cnt):
            libros_cnt.append([lib[0],0,0,0,0])
        if lib[1] == "Vendido":
            libros_cnt[i][1] +=1
        elif lib[1] == "Arrendado":
            libros_cnt[i][2] +=1

        elif lib[1]=="Disponible":
            libros_cnt[i][3] +=1
        elif lib[1]=="Dañado":
            libros_cnt[i][4] +=1    
    
    #print(libros_cnt)
    max_id +=1


    i = 0
    line = "ID;Vendidos;Arrendados;Disponibles;Dañados\n"

    #print("El archivo se creó exitosamente")
    #print("Se acaban de ordenar exitosamente las lineas del archivo libros_consolidados.txt")
    #print("Lineas en el archivo:")
    #print()
    #print(line)
    #print()

    f2.write(line)
    while i < len(libros_cnt):
        idx = -1
        max_id2 = max_id
        j = 0
        while j < len(libros_cnt):
            if int(libros_cnt[j][0]) < max_id2:
                idx = j
                max_id2 = int(libros_cnt[j][0])
            j+=1

        
        line = str(libros_cnt[idx][0])+";"+str(libros_cnt[idx][1])+";"+str(libros_cnt[idx][2])+";"+str(libros_cnt[idx][3])+";"+str(libros_cnt[idx][4])+"\n"
        #print(line)
        #print()
        f2.write(line)
        libros_cnt[idx][0] = max_id+1
        i+=1
    f2.close()


solve()