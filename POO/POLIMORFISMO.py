'''
El polimorfismo es la capacidad que tienen los objetos en diferentes clases para usar un comportamiento o atributo
del mismo nombre pero con diferente valor.
'''

'''
El polimorfismo nos sirve para hacer nuestro código y trabajo más óptimo y entendible
'''

# Ejemplo
class Auto:
    rueda = 4

    def desplazamiento(self):
        print("El auto se está desplazando sobre 4 ruedas")

class Moto:
    rueda = 2

    def desplazamiento(self):
        print("La moto se está desplazando sobre 2 ruedas")

# Tengo dos clases con dos objetos de mismo nombre, lo mismo pasa con su método

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

class Animales:
    def __init__(self, nombre):
        self.nombre = nombre

    def tipo_animal(self):
        pass

class Leon(Animales):

    def tipo_animal(self):
        print("Animal salvaje")

class Perro(Animales):

    def tipo_animal(self):
        print("Animal doméstico")

nuevo_animal = Leon("Simba")
nuevo_animal.tipo_animal()
nuevo_animal2 = Perro("Arlo")
nuevo_animal2.tipo_animal()

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# POLIMORFISMO POR FUNCIÓN
class Tomate:

    def tipo(self):
        print("Vegetal")

    def color(self):
        print("Rojo")

class Manzana:

    def tipo(self):
        print("Fruta")

    def color(self):
        print("Verde")

def funcion(objeto):
    objeto.tipo()
    objeto.color()

nuevo_tomate = Tomate()
funcion(nuevo_tomate)
nueva_manzana = Manzana()
funcion(nueva_manzana)

# POLIMORFISMO CON MÉTODOS
class Colombia:

    def capital(self):
        print("Bogotá")

    def idioma(self):
        print("Castellano")

class Francia:

    def capital(self):
        print("París")

    def idioma(self):
        print("Francés")

colombiano = Colombia()
frances = Francia()
# Necesitamos trabajar mínimo con dos objetos. Recorre las dos clases que tienen los mismos atributos
for pais in (colombiano, frances):
    pais.capital()
    pais.idioma()

# POLIMORFISMO CON HERENCIA
class Aves:

    def volar(self):
        print("La mayoría de las aves pueden volar, pero algunas no.")

class Aguila(Aves):

    def volar(self):
        print("Las águilas pueden volar")

class Gallina(Aves):

    def volar(self):
        print("La gallina no puede volar")

obj_ave = Aves()
obj_aguila = Aguila()
obj_gallina = Gallina()
obj_ave.volar()
obj_aguila.volar()
obj_gallina.volar()