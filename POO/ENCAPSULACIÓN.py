'''
La encapsulación es uno de los pilares de la POO.
Permite regular el acceso a los métodos y atributos de una clase.
En cierta manera, enmascara la complejidad de una clase.
'''

'''
Queremos esto para regular el acceso a los métodos y los atributos
'''

'''
Modificadores de acceso en métodos y atributos: Existen 3 tipos.
Públicos:
    Son los que hemos visto hasta ahora. Son accesibles por:
        Cualquier punto del código
        Dentro/Fuera de la clase, subclase, etc.
Protegidos:
    Son accesibles por:
        La misma clase.
        Las subclases.
        Clases dentro del mismo paquete (otros ficheros).
Privados.
    Son como un nivel superior a los protegidos. Son accesibles por:
        Únicamente dentro de la misma clase.
'''

'''
_atributo = "atributoProtegido"
__atributo = "atributoPrivado"
La misma sintaxis para los métodos
'''

# Ejemplo ilustrativo
import math

class Circulo:
    def __init__(self, radio, pi):
        self.__radio = radio
        self.__pi = math.pi

    def calcular_perimetro(self):
        return 2*self.__pi*self.__radio

    def calcular_area(self):
        return self.__pi * (self.__radio ** 2)

    # Método público para acceder a un atributo privado
    def getPi(self):
        return self.__pi

    # Este método público sirve para modificar un atributo privado
    def setRadio(self, nuevo_valor):
        if type(nuevo_valor) == int or type(nuevo_valor) == float:
            if nuevo_valor > 0:
                self.__radio = nuevo_valor
                print(f"El radio se ha modificado correctamente: {self.__radio}")
            else:
                print("Oye el radio no puede ser negativo")
        else:
            print("El radio tiene que ser un número positivo")

# Ocurre un error al ser "privado"
c1 = Circulo(2, 5)
'''print(c1.calcular_area())
print(c1.calcular_perimetro())
print(c1.pi)''' # Comento para que no se produzca el error

# atributo: __radio -> _Circulo__radio. En general: _NombreDeLaClase__NombreDelAtributo

print(f"La constante PI es {c1._Circulo__pi}") # De esta forma podemos acceder al atributo en este caso.
print(f"La constante PI es {c1.getPi()}") # Esta es la forma mejor de acceder con el método

c1.setRadio(34)
c1.setRadio(-23)
c1.setRadio("Hola que tal")

# Todo esto es igual para los métodos

