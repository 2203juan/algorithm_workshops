import calculadora_aws as calc

def main()->None:

    print("Calcular costo de almacenamiento")

    lectura =  int(input("Ingrese el número de solicitudes de lectura: "))
    escritura = int(input("Ingrese el número de solicitudes de escritura: "))
    almacenamiento = float(input("Ingrese el tamaño de la información almacenada en GB: "))

    costo_total = round(calc.costo_almacenamiento(lectura, escritura, almacenamiento),2)
    print("El costo total mensual del bucket es : $",costo_total," USD.")

main()