import math #necesario para poder usar euler y potencias en python

def integrar(f,a,b,n):
	"""
	Esta funcion implementa el metodo numerico 
	del trapecio utilizado para aproximar integrales

	Sus entradas son:

	f: funcion que se quiere integrar
	a: limite inferior de la integral
	b: limite superior de la integral
	n:	numero de particiones

	Sus salidas es:

	Un número ( el valor de la integral )
	"""
	deltha_x = (b-a)/n
	suma = 0

	for k in range(1,n):
		suma = suma + 2*f(a+k*deltha_x)

	suma = (suma + f(a) + f(b))*(deltha_x/2)

	return suma

def f(x):
	"""
	Aqui se define la funcion que se quiere integrar
	"""
	return math.pow(math.e,-x**2)

def main():
	"""
	Desde esta funcion se llama la funcion integrar con sus
	respectivos parámetros según sea el caso
	"""
	a = -1
	b = 1
	n = 100
	print(integrar(f,a,b,n))
main()
