def comprar_lista(supermercados, lista_productos):
    ans = list()
    band = True
    for super in supermercados:
        productos = super[1]
        i = 0
        band = True
        while i < len(lista_productos) and band:
            j = 0
            while j < len(productos) and productos[j][0] != lista_productos[i][0]:
                j+=1
            
            if not (j < len(productos) and productos[j][2] >= lista_productos[i][1]):
                band = False
            i+=1
        
        if band:
            ans.append(super[0])
    return ans