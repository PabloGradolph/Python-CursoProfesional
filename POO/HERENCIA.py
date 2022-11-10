'''
La herencia consiste en crear una nueva clase a partir de una o más clases ya existentes.
'''

'''
Herencia:
class NombreSubClase(NombreClaseSuperior):
class ClaseBase:
    Cuerpo de la clase base
class DerivadoClase(ClaseBase):
    Cuerpo de clase derivada
'''

class Pokemon:
    pass

    # Constructor
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

    # Método
    def descripcion(self):
        return "{} es un pokemon de tipo: {}".format(self.nombre, self.tipo)

# Clases hijas
class pikachu(Pokemon):

    def ataque(self, tipo_ataque):
        return "{} tipo de ataque: {}".format(self.nombre, tipo_ataque)

class charmander(Pokemon):

    def ataque(self, tipo_ataque):
        return "{} tipo de ataque: {}".format(self.nombre, tipo_ataque)

# Ejecutamos de la siguiente manera
nuevo_pokemon = pikachu("Boby", "eléctrico")
print(nuevo_pokemon.descripcion())
print(nuevo_pokemon.ataque("Impacto trueno"))

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Herencia ejemplo práctico
class Calculadora:

    def __init__(self, numero):
        self.n = numero
        self.datos = [0 for i in range(numero)]

    def ingresardato(self):
        self.datos = [int(input("Ingresar datos: " + str(i+1) + " = ")) for i in range(self.n)]

class op_basicas(Calculadora):

    def __init__(self):
        # Llamamos a la clase padre de esta forma
        Calculadora.__init__(self, 2)

    def suma(self):
        a,b, = self.datos
        s = a + b
        print(f"El resultado es: {s}")

    def resta(self):
        a,b, = self.datos
        r = a - b
        print(f"El resultado es: {r}")

class raiz(Calculadora):

    def __init__(self):
        Calculadora.__init__(self, 1)

    def cuadrada(self):
        from math import sqrt
        a, = self.datos
        print("El resultado es: ", sqrt(a))

# Ejecutamos el código
ejemplo = op_basicas()
print(ejemplo.ingresardato())
print(ejemplo.suma())

ejemplo = raiz()
print(ejemplo.ingresardato())
print(ejemplo.cuadrada())

# FUNCIONES DE PRUEBAS EN HERENCIA
objeto = op_basicas()
# Lo que hace la siguiente función es verificar si el objeto pertenece a la clase
print(isinstance(objeto, op_basicas))
print(isinstance(objeto, raiz))
print(isinstance(objeto, Calculadora)) # También pertenece a la clase padre

# Lo que hace la siguiente función es comprobar si es subclase o no. Primero la subclase
print(issubclass(Calculadora, op_basicas))
print(issubclass(op_basicas, Calculadora))