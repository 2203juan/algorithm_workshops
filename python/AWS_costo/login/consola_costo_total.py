import calculadora_aws as calc

def main()->None:

    print("Calcular costo total")
    
    servidores_compromiso = int(input("Ingrese el número total de máquinas virtuales con compromiso de permanencia: "))
    porcentaje_compartidas_compromiso =  float(input("Ingrese el porcentaje de instancias que serán compartidas, con compromiso de permanencia: "))
    servidores_libres =  int(input("Ingrese número total de máquinas virtuales libres: "))
    porcentaje_compartidas_libres =  float(input("Ingrese el porcentaje de instancias que serán compartidas, libres: "))
    costo_dedicado = float(input("Ingrese el costo por hora de un servidor dedicado: "))
    solicitudes_totales =  int(input("Ingrese el número de solicitudes totales de lectura y escritura: "))
    almacenamiento = float(input("Ingrese el espacio de almacenamiento en GB: "))
    datos = float(input("Ingrese la cantidad de datos en GB que se transfieren: "))
    porcentaje_aws =  float(input("Ingrese el porcentaje de tráfico que se dirige a otros servicios de AWS: "))

    costo = calc.costo_total(servidores_compromiso, porcentaje_compartidas_compromiso, servidores_libres, porcentaje_compartidas_libres, costo_dedicado, solicitudes_totales, almacenamiento, datos, porcentaje_aws)

    print("El costo total mensual de mantener la infraestructura en AWS es $", costo," USD")

main()