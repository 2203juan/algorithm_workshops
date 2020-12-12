from abc import ABC, abstractmethod

class Sujeto(object):

	__observador = None
	__estado = None

	def __init__(self):
		""" Constructor. """
		self.__observador = list()
		self.__estado = 0

	def getEstado(self):
		return self.__estado

	def setEstado(self,estado):
		self.__estado = estado
		self.notifyAllObservers()
	def attach(self,observer):
		self.__observador.append(observer)

	def notifyAllObservers(self):
		for observer in self.__observador:
			observer.update()

class Observador(ABC):

	_sujeto = None
	
	def __init__(self):
		""" Constructor. """
		self._sujeto = Sujeto()


	@abstractmethod
	def update(self):
		pass

class BinaryObserver(Observador):

	def __init__(self,subject):
		""" Constructor. """
		self._sujeto = subject
		self._sujeto.attach(self)

	def update(self):
		print("Binary String: {}".format(bin(self._sujeto.getEstado())[2:]))

class HexadecimalObserver(Observador):

	def __init__(self,subject):
		""" Constructor. """
		self._sujeto = subject
		self._sujeto.attach(self)

	def update(self):
		print("Hexadecimal String: {}".format(hex(self._sujeto.getEstado())[2:]))

def main():
	sujeto = Sujeto()
	bina = BinaryObserver(sujeto)
	hexa = HexadecimalObserver(sujeto)
	
	cambio1 = 15
	print("Primer cambio: {} \n".format(cambio1))
	sujeto.setEstado(cambio1)

	cambio2 = 200
	print("\nSegundo cambio: {} \n".format(cambio2))
	sujeto.setEstado(cambio2)
main()