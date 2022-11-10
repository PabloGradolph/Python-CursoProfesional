'''
Las clases son modelos generales de objetos que tienen los mismos atributos (características) y métodos (funciones).
Cada objeto de la clase puede variar en el valor de los atributos, por eso hacemos clases, para no repetir el código
numerosas veces.
'''

# Creamos la clase Auto
class Auto:

    # Atributos generales
    marca = ""
    modelo = 0
    placa = ""

# Creamos un objeto (taxi) perteneciente a la clase y que tiene los atributos de la misma
taxi = Auto()
# Imprimimos uno de sus atributos
print(taxi.modelo)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

class Jugadores_A:

    # También podemos poner "objetos" aquí
    j1 = "Messi"
    j2 = "C. Ronaldo"

class Jugadores_B:

    j3 = "Marcelo"
    j1 = "Falcao"

# Podemos imprimir los objetos de la clase
print(Jugadores_A.j2)
print(Jugadores_B.j1)

'''
Normalmente, los objetos los creamos fuera de la clase con una serie de atributos y lo que ponemos dentro de la clase
son estos atributos. Pero está bien conocer que pueden funcionar como objetos también, ya veremos que no lo usaremos
así de forma común.
'''

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

class Nombre:
    # Con el pass decimos que no tiene atributos generales y que la usaremos sin estos
    pass

# Creamos objetos de la clase, los creamos fuera de ésta
victor = Nombre()
maria = Nombre()

# Para crear atributos a cada objeto usamos 'objeto.atributo = valor'
# Estos atributos serán solo para un único objeto ya que no están dentro de la clase
victor.edad = 30
victor.sexo = "masculino"
victor.pais = "Bolivia"

maria.edad = 25
maria.sexo = "femenino"
maria.pais = "Colombia"

print(victor.edad)
print(maria.edad)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -