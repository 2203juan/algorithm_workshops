import calculadora_aws as calc

def main()->None:

    print("Calcular costo procesamiento libre")

    dedicados = int(input("Ingrese el número de servidores dedicados libres que se utilizarán: "))
    compartidas = int(input("Ingrese el número de instancias compartidas libres que se utilizarán: "))
    costo = float(input("Ingrese el costo de un servidor dedicado reservado por una hora: "))

    costo_total = round(calc.costo_procesamiento_libre(dedicados, compartidas, costo),2)
    print("El costo total a pagar por el mes de procesamiento libre: $",costo_total," USD")

main()