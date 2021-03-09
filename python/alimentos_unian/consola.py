import calculos as gatos

def main()->None:
    n_gatos = int(input("Ingrese la cantidad de gatos en el refugio: "))
    n_dias = int(input("Ingrese el número de días que los necesita alimentar: "))

    print(gatos.calcular_cantidad_comida(n_gatos, n_dias))

main()