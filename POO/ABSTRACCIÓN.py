'''
CLASES ABSTRACTAS:
    - No las vamos a instanciar nunca directamente.
    - Contienen por lo menos un método abtracto.
    - Las vamos a usar de base para subclases más específicas.

MÉTODOS ABSTRACTOS:
    - Debemos sobreescribirlos en cada una de las subclases.
'''

from abc import ABC, abstractmethod

# De esta forma hacemos que nuestra clase personaje sea abstracta NombreClase(ABS):
class Personaje(ABC):
    @abstractmethod # Este es nuestro método abstracto
    def __init__(self, nombre):
        self.nombre = nombre
        self.nivel = 0
        self.inventario = []
        self.vida = 100

    @abstractmethod
    def atacar(self, objetivo):
        pass # Hacemos esto porque este método lo vamos a redifinir en las subclases de forma distinta

    @abstractmethod
    def getStatus(self):
        print(f"Nombre: {self.nombre}. Nivel: {self.nivel}")

    def subir_de_nivel(self):
        self.nivel += 1

    def ver_inventario(self):
        print(f"Inventario de {self.nombre}")
        for objeto in self.inventario:
            print(objeto)

class Mago(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.vida = 120
        self.inteligencia = 95
        self.inventario = ["Poción de maná", "Grimorio"]

    def getStatus(self):
        print("Clase Mago")
        super().getStatus()

    def atacar(self, objetivo):
        objetivo.vida -= self.inteligencia * 0.6
        print(f"La vida actual del objetivo es: {objetivo.vida}")

    def saludar(self):
        print("Hola qué tal sou un mago")

class Guerrero(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.vida = 200
        self.fuerza = 75
        self.inventario = ["Poción de vida", "Escudo", "Espada"]

    def getStatus(self):
        print("Clase Guerrero")
        super().getStatus()

    def atacar(self, objetivo):
        objetivo.vida -= self.fuerza*0.8
        print(f"El objetivo se ha quedado con {objetivo.vida} puntos de vida")

guerrero = Guerrero("Kaladin")
mago = Mago("Gandalf")

guerrero.getStatus()
mago.getStatus()

mago.ver_inventario()
guerrero.ver_inventario()

mago.atacar(guerrero)
guerrero.atacar(mago)

