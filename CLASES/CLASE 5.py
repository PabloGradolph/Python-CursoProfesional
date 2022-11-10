# CLASE DEL DÍA 04/07/2022

# TRATAMIENTO DE CADENAS DE CARACTERES EN PYTHON

# Incluyendo comillas simples y dobles dentro de una cadena
print("Esta \"palabra\" se encuentra escrita entre comillas dobles")
# La antibarra dice que el siguiente caracter no se interprete como código de python sino como es el símbolo.

# Incluyendo comillas simples y dobles dentro de una cadena
print("Esta 'palabra' se encuentra escrita entre comillas simples")
print("Esta \"palabra\" se encuentra escrita entre comillas dobles")

# carácteres especiales como las tabulaciones /t o los saltos de línea /n
print("Un texto\tuna tabulación")
print("Un texto\t\t\t\tuna tabulación")
print("Un texto\nuna nueva línea")

# Podemos utilizar """ (triple comillas) para cadenas multilínea
print("""Una línea
otra línea
otra línea\tuna tabulación""")

# Dando formato a los datos que mostramos por consola
texto = "cualquiera"
numero = 20
cadena = "Un texto {} y un numero {}".format(texto, numero)
print(cadena)
cadenaInvertida = "Un texto '{1}' y un numero '{0}'".format(texto, numero)
print(cadenaInvertida)

# Alineando el texto a la derecha 30 caracteres
print("{:>30}".format("palabra"))

# Alineando el texto a la izquierda 30 caracteres
print("{:30}".format("palabra"))

# Alineando al centro 30 caracteres
print("{:^30}".format("palabra"))

# Para evitar los caracteres especiales, debemos indicar que una cadena es cruda (raw)
print(r"C:\nombre\directorio")

# Concatenando cadenas
print("Un divertido "+"programa "+"de "+ "radio")

# Multiplicar una cadena por un número
print(3 * "programas ")

# averiguar la longitud de una cadena
len("programas ")

# recorrer todos los caracteres de una cadena
for x in "programas ":
    print (x)

# Acceder a una posición de la cadena
nombre = "Veronica"
print(nombre[1])

# Obteniendo Segmentos de cadenas
print(nombre[3:7])

# f-strings: formatted strings o cadenas formateadas:
a = 5
cadena_con_formato = f"Este es un numero entero {a}."
print(cadena_con_formato)

b = 199.9876543123456123456
cadena_con_formato = f"Este es un numero de punto flotante dificil de leer {b}."
print(cadena_con_formato)
cadena_con_formato = f"Este es un numero de punto flotante facil de leer {b:.5f}." # Redondea
print(cadena_con_formato)

# Inmutabilidad
# Una propiedad de las cadenas es que no se pueden modificar.
# Si intentamos reasignar un carácter, no nos dejará
# nombre[0] = "A" # -> Error



# FUNCIONES SIN ARGUMENTOS

# Definición de la función
def pedir_pizza():
    print("Has pedido pizza")

# Llamada a la función
pedir_pizza()

# FUNCIONES CON ARGUMENTOS
def pedir_pizza_personalizada(ingrediente, extra_queso):
    if extra_queso == True:
        print(f"Has pedido una pizza con {ingrediente} y con extra de queso")
    else:
        print(f"Has pedido una pizza con {ingrediente} y sin extra de queso")

pedir_pizza_personalizada("cebollas", False) # Son necesarios los dos argumentos


def saludo_mal(nombre):
    return "Hola " + nombre

print(saludo_mal("Hector "))


def saludo(nombre: str) -> str: # Es para el lector, hacen lo mismo ambas funciones
    nombre = str(nombre)
    return "Hola " + nombre

print(saludo("3"))

# FUNCIONES QUE RETORNAN DATOS
def sumar(numero_1, numero_2):
    return numero_1 + numero_2

suma = sumar(10, 2)
print(f"La suma es {suma}")

# Retornando distintos valores
def test():
    return "una cadena", 20, [1, 2, 3]
print(test())
cadena, numero, lista = test()
print(cadena, numero, lista)

# PASANDO DATOS A LAS FUNCIONES

# Pasando datos indeterminados a la función, estos datos se transforman en una tupla
def datos_indeterminados(*args):
    if True in args:
        print("Está True!")
    for arg in args:
        print(f"argumento {arg}")
        print(f"del tipo {type(arg)}")

datos_indeterminados(5, "hola", [1, 2, 3], 5.6, True, True)

def pedir_pizza_personalizada(ingrediente, extra_queso = True):
    if extra_queso == True:
        print(f"Has pedido una pizza con {ingrediente} y con extra de queso")
    else:
        print(f"Has pedido una pizza con {ingrediente} y sin extra de queso")

pedir_pizza_personalizada("Piña") # Ahora puedo pasar solo un argumento. Pk extra_queso siempre = True

# Pasando datos indeterminados a la función, en modo diccionario
def datos_indeterminados(**kwargs):
    for kwarg in kwargs:
        print(kwarg, " - ", kwargs[kwarg])

datos_indeterminados(n=5, c="hola", l=[1, 2, 3])

