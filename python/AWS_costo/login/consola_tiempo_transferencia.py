import calculadora_aws as calc

def main()->None:

    print("Calcular tiempo transferencia")
    
    tamano = float(input("Ingrese el tamaño total en GB de los archivos a transferir: "))
    ancho_banda =  int(input("Ingrese el ancho de banda en Mbps contratados: "))

    ans = calc.tiempo_transferencia(tamano, ancho_banda)
    print(ans)
main()