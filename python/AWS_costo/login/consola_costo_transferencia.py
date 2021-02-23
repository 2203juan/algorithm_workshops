import calculadora_aws as calc

def main()->None:
    print("Calcular costo de transferencia")

    datos =  float(input("Ingrese la cantidad total de datos que se transfirieron en GB: "))
    porcentaje_aws = float(input("Ingrese el porcentaje de los datos que se fueron hacia instancias de AWS en otra región: "))

    costo_total = round(calc.costo_transferencia(datos, porcentaje_aws),2)

    print("El costo total mensual de la transferencia de datos realizada es $",costo_total," USD.")

main()