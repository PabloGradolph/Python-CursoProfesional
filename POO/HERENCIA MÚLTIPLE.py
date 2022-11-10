'''
La herencia múltiple se refiere a la posibilidad de crear una clase a partir de múltiples clases superiores.

Herencia múltiple:

    class Base_uno:
        pass
    class Base_dos:
        pass
    class DerivadoMultiple(Base_uno, Base_dos):
        pass
'''

'''
Herencia multinivel:
    
    class Base:
        pass
    class Derivado_uno(Base):
        pass
    class Derivado_dos(Derivado_uno):
        pass

En la herencia multinivel, las características de la clase base y la clase derivada 
se heredan en la nueva clase derivada.
'''

# Herencia múltiple
class Telefono:

    def __init__(self):
        pass

    def llamar(self):
        print("Llamando...")

    def ocupado(self):
        print("Ocupado...")

class Camara:

    def __init__(self):
        pass

    def fotografia(self):
        print("Tomando fotos...")

class Reproduccion:

    def __init__(self):
        pass

    def reproduccion_de_musica(self):
        print("Reproduciendo música...")

    def reproduccion_de_video(self):
        print("Reproduciendo vídeo...")

# Esta es la clase que puede trabajar como herencia de todas las anteriores
class smartphone(Telefono, Camara, Reproduccion):

    # Aquí no empezamos con el constructor. Usamos __del__ para limpiar los recursos
    def __del__(self):
        print("Teléfono apagado")

movil = smartphone()
# Directorio con las acciones que podemos hacer con este objeto
print(dir(movil))
# Ahora llamamos a los métodos de las distintas clases
print(movil.fotografia())
print(movil.llamar())

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# MÉTODO SUPER()
class Mamifero:

    def __init__(self, nombre):
        print(nombre, "es un animal de sangre caliente")

class Leon(Mamifero):

    def __init__(self):
        print("El león es un animal de cuatro patas")
        # Llamamos a la clase superior
        super().__init__("Simba")
        # Esta es otra forma de hacer algo similar, en este caso llamamos a toda la clase Mamífero
        Mamifero.__init__(self, "Simba")

nuevo_leon = Leon()

