'''
Los métodos son funciones que están dentro de las clases.
Los métodos lo que hacen son determinar una acción o un comportamiento.
'''

class Ropa:

    # Esto es el "método" constructor de atributos
    def __init__(self):
        self.marca = "Adidas"
        self.talla = "M"
        self.color = "Blanco"

# Creamos un objeto
camisa = Ropa()
# Podemos llamar a los atributos del creador
print(camisa.talla)
print(camisa.marca)

class Calculadora:

    # Constructor con variables que vamos a utilizar
    def __init__(self, n1, n2):
        self.suma = n1 + n2
        self.resta = n1 - n2
        self.producto = n1 * n2
        self.division = n1 / n2

# Creamos objeto metiendo las variables que pide la clase que tienen que entrar
operacion = Calculadora(2, 3)
print(operacion.suma)
print(operacion.producto)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# AHORA VAMOS A USAR FUNCIONES CON ATRIBUTOS QUE PUEDEN SER DE INTERÉS
class Persona:

    # Atributos generales de la clase
    edad = 27
    nombre = "vitor"
    pais = "Brasil"

# Creamos objetos y llamamos al atributo general
doctor = Persona()
print(f"La edad es: {doctor.edad}")

# Con getattr obtenemos el valor del atributo de manera directa igual que antes
print("La edad es: ", getattr(doctor, "edad"))
# Con veremos si existe o no el atributo que queramos
print("¿El doctor tiene edad?", hasattr(doctor, "edad"))
print("¿El doctor tiene apellido?", hasattr(doctor, "apellido"))
# Con setattr podemos hacer cambios a los atributos
print("Antes se llamaba: ", doctor.nombre)
setattr(doctor, "nombre", "Héctor")
print("Ahora se llama: ", doctor.nombre)
# Con delattr borramos atributos de la clase
delattr(Persona, "pais")
print(doctor.nombre)
# print(doctor.pais) no funciona ya

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# CONSTRUCTORES
class Persona2:
    # Por el momento no hay atributos generales, pero podrá haberlos más adelante: usamos 'pass' para evitar errores
    pass

    # Constructor de atributos de forma que pasen valores distintos posteriormente en cada objeto
    def __init__(self, nombre, año):
        self.nombre = nombre
        self.año = año

    # Métodos aparte del constructor
    def descripcion(self):
        return "{} tiene {} años ".format(self.nombre, self.año)

    def comentario(self, frase):
        return f"{self.nombre} dice: {frase}"

profesor = Persona2("Pablo", 20)
print(profesor.nombre)
# Ahora llamamos al método
print(profesor.descripcion())
print(profesor.comentario("Hola, ¿como estás?"))

# Modificar un atributo
class Email:

    def __init__(self):
        self.enviado = False

    def enviar_correo(self):
        self.enviado = True

mi_correo = Email()
print(mi_correo.enviado)

# Ahora trabajamos el mismo atributo pero en otro tipo de método
mi_correo.enviar_correo()
print(mi_correo.enviado)