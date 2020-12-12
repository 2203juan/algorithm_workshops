from abc import ABC, abstractmethod

class Carro(ABC):
    @abstractmethod
    def conducir(self):
        pass

class Sport(Carro):
    def conducir(self):
        print("Sport mode")

class Fly(Carro):
	def conducir(self):
		print("Fly mode")

def main():
	strategy = Sport()
	strategy.conducir()

	strategy = Fly()
	strategy.conducir()
main()