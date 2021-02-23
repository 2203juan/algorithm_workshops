
def num_digitos(num):
    return len(str(num))

def multiplicacion(n):
    n_ = str(n)
    ans = 1

    for c in n_:
        ans *= int(c)
    return ans

def persistencia(n, cont):
    if num_digitos(n) == 1:
        return cont
    else:
        cont +=1
        return persistencia(multiplicacion(n), cont)

def main():
    print(persistencia(39,0))
    print(persistencia(999,0))
    print(persistencia(4,0))
main()