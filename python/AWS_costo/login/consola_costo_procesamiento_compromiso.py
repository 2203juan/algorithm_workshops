import calculadora_aws as calc

def main()->None:

    print("Calcular costo procesamiento compromiso")

    dedicados = int(input("Ingrese el número de servidores dedicados con compromiso que se utilizarán: "))
    compartidas = int(input("Ingrese el número de instancias compartidas con compromiso que se utilizarán: "))
    costo = float(input("Ingrese el costo de un servidor dedicado reservado por una hora: "))

    costo_total = round(calc.costo_procesamiento_compromiso(dedicados, compartidas, costo),2)
    print("El costo total que se tendrá que pagar por el mes de procesamiento con compromiso es : $",costo_total," USD")

main()