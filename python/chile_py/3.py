import math

# punto 3
h1 = float(input("Alto del rec 1: "))
h2 = float(input("Alto del rec 2: "))
d1 = float(input("diametro del rec 1: "))
d2 = float(input("diametro del rec 1: "))

r1 = d1/2
r2 = d2/2

v1 = math.pi*((r1)**(2))*h1
v2 = math.pi*((r2)**(2))*h2

sup1 = 2*math.pi*r1*(r1+h1)
sup2 = 2*math.pi*r2*(r2+h2)

print()

print("Volumen del rec 1: ", v1)
print("Superficie del rec 1: ", sup1)

print("Volumen del rec 2: ", v2)
print("Superficie del rec 2: ", sup2)
print()