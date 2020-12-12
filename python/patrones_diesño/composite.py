class Empleado(object):
    __nombre = None
    __departamento = None
    __salario = None
    __personasCargo = None

    def __init__(self, nombre, departamento, salario):
        """ Constructor. """
        self.__personasCargo = list()
        self.__nombre = nombre
        self.__departamento = departamento
        self.__salario = salario

    def adicionar(self, e):
        self.__personasCargo.append(e)

    def remover(self, e):
        self.__personasCargo.pop(e)

    def getPersonasCargo(self):
        return self.__personasCargo

    def toString(self):
        return ("Empleado:[ Nombre: {}, Departamento: {}, Salario: {} ]".
                format(self.__nombre, self.__departamento, self.__salario))


def main():
    # Composite
    gerenteGeneral = Empleado("Juan David Lozano", "Presidencia", 5000000)

    gerenteComercial = Empleado("Maria Victoria Estrada", "Ventas", 4000000)

    gerenteMercadeo = Empleado("Samuel Quintero", "Marketing", 4000000)

    marketing1 = Empleado("Sara Behar", "Marketing", 3000000)

    marketing2 = Empleado("Viviana Mendoza", "Marketing", 3000000)

    ventas1 = Empleado("Sara Dominguez", "Ventas", 2000000)

    ventas2 = Empleado("David Suarez", "Ventas", 2000000)

    gerenteGeneral.adicionar(gerenteComercial)
    gerenteGeneral.adicionar(gerenteMercadeo)

    gerenteMercadeo.adicionar(marketing1)
    gerenteMercadeo.adicionar(marketing2)

    gerenteComercial.adicionar(ventas1)
    gerenteComercial.adicionar(ventas2)

    print(gerenteGeneral.toString())
    for gerente in gerenteGeneral.getPersonasCargo():
        print(gerente.toString())

        for empleado in gerente.getPersonasCargo():
            print(empleado.toString())


main()
