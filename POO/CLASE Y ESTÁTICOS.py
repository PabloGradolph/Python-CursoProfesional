'''
Existen 3 tipos de métodos:
    Métodos estáticos
    Métodos de clase
    Métodos de instancia
'''

'''
Método de clase: 
Para indicar a python que es un método de clase se debe anteponer la palabra reservada @classmethod.
Este método puede ser llamado sin crear una instancia de la clase. No necesitamos el __init__.
'''

# Ejemplo
class Pastel:

    def __init__(self, ingredientes):
        self.ingredientes = ingredientes

    # repr trabaja con listas y demás: diferentes valores que se van a depositar en un solo atributo (ingredientes)
    # !r hace que se ejecute siguiendo este método
    def __repr__(self):
        return f"pastel({self.ingredientes !r})"

    # Ahora trabajamos con el método de clase.
    # Con classmethod trabajamos con cls como palabra reservada
    @classmethod
    def Pastel_chocolate(cls):
        return cls(["harina", "leche", "chocolate"])

    @classmethod
    def Pastel_vainilla(cls):
        return cls(["harina", "leche", "vainilla"])

print(Pastel.Pastel_chocolate())

'''
Método estático: 
Para indicarle a Python que es un método estático usamos @staticmethod.
Pueden ser llamados sin tener una instancia de la clase, además este tipo de métodos no tienen acceso al exterior.
Por esta razón, no pueden acceder a ningún otro atributo o llamar a ninguna otra función dentro de la clase.
'''
from math import pi

class Pastel:
    def __init__(self, ingredientes, tamaño):
        self.ingredientes = ingredientes
        self.tamaño = tamaño

    def __repr__(self):
        return (f"Pastel({self.ingredientes}, "f"{self.tamaño})")

    def area(self):
        return self.tamaño_area(self.tamaño)

    @staticmethod
    def tamaño_area(area):
        return area ** 2 * pi

nuevo_pastel = Pastel(["Harina", "Azúcar", "Leche", "Crema"], 4)
print(nuevo_pastel.ingredientes)
print(nuevo_pastel.tamaño)
# No tienes por qué meter el 4 ya que el método estático trabaja de manera independiente
print(nuevo_pastel.tamaño_area(12))