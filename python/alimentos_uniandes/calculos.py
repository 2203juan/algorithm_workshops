def calcular_cantidad_comida(numero_gatos: int, n_dias:int)->str:
    a1 = calcular_cant_bolsas(numero_gatos,n_dias)
    ans = bolsas(numero_gatos,n_dias, a1)
    return ans


def calcular_cant_bolsas(numero_gatos: int, n_dias:int)->str:
    consumo_gato = 300 #gramos
    bolsa = 7000 #gramos

    total_gramos = 300*numero_gatos*n_dias

    n_bolsas = total_gramos//bolsa

    gramos_restantes = total_gramos - (n_bolsas*bolsa)
    ans = str(n_bolsas)+" bolsas y "+str(gramos_restantes)+" gramos adicionales."
    return ans

def bolsas(numero_gatos: int, n_dias:int, a1:str)->str:
    ans = "Para alimentar "+str(numero_gatos)+"gatos por "+str(n_dias)+" dias se requieren" + a1
    return ans