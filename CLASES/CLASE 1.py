# CLASE DEL DÍA 20/06/2022

print("Hola mundo!")

""" Esto sirve para comentar.
Al usar este tipo de comillas puedo
comentar en varias líneas"""
''' Este tipo de comillas también sirven para "comentar" '''

# Esto también es un comentario.

# VARIABLES
# Las variables en Python no requieren declarar la variable antes de usarla.

# Enteros
número_entero = 12
otro_número_entero = 10
suma_entero = número_entero + otro_número_entero
print(suma_entero)
print(type(número_entero)) #Type sirve para identificar el tipo de variable.

# Decimales
número_decimal = 12.8
otro_número = 10
suma_decimal = número_decimal + otro_número
print(suma_decimal)
print(type(número_decimal))
print(type(otro_número))
print(type(suma_decimal)) #La combinación nos sale float

# Cadenas
nombre = "Pedro"
print(nombre)
print(type(nombre))
apellidos = " Gutierrez Álvarez"
print(nombre + apellidos)
print(nombre * 5)

# Caracteres especiales en las cadenas
frase = "El me dijo: '¡Hola!'"
print(frase)
comillas_dobles = "Ella me dijo: \"Hola\""
print(comillas_dobles)
frase_intro = "Ella me dijo: \n\"Hola\""
print(frase_intro)

# CONVERSIÓN DE TIPOS O CASTING
numero_decimal = 10.8
print(type(numero_decimal))
numero_entero = int(numero_decimal) # Esta es la parte entera del número decimal.
print(numero_entero)
print(type(numero_entero))

numero_decimal = 10.8
print(type(numero_decimal))
numero_entero = str(numero_decimal) # Pasamos de un número decimal a un texto.
print(numero_entero)
print(numero_entero + " Hola")
print(type(numero_entero))

# SOLICITAR DATOS POR CONSOLA
print ("Introduce tu nombre: ")
nombre = input()
print("Introduce tu edad: ")
edad = input()
print("Introduce tu peso: ")
peso = input()
print("Hola "+ nombre+ "tienes "+ edad+ " años y pesas"+ peso+ "kilos")

'''Si dejo esto así, al leer un dato por consola este se recibe como si fuera una cadena de texto.
Para solucionarlo habría que convertirlo'''

print("Introduce un número:")
numero1 = float(input())

'O directamente podemos...'

numero1 = float(input("Introduce un número: "))

# OPERADORES MATEMÁTICOS
'SUMA'
print("Suma:",2 + 2)

'RESTA'
print("Resta:", 2 - 2)

'MULTIPLICACIÓN'
print("Multiplicación:", 2 * 2)

'DIVISIÓN'
print("División:", 2 / 2)

'PARTE ENTERA DE UNA DIVISIÓN'
print("Parte entera de la división:", 19 // 2)

'MÓDULO O RESTO - DEVUELVE EL RESTO DE LA DIVISIÓN'
print ("Resto de la división:", 35 % 3)

'POTENCIA'
print (2 * 2 * 2 * 2 * 2)
print (2 ** 5)

# OPERADORES DE ASIGNACIÓN
# ==
# +=
# -=
# /=
# %=
# **=
# //=

'''número = 10
número = número + 2
print (número)'''

número = 10
número += 2
print(número)

# OPERADORES DE COMPARACIÓN
# < Menor que
# > Mayor que
# <= Menor o igual que
# >= Mayor o igual que
# == Igual a
# != Distinto de

valor1 = 2
valor2 = 9
operación1 = valor1 < 3
print(operación1)
operación2 = valor2 == 6
print(operación2)

# OPERADORES LÓGICOS
# and
# or
# not

valor3 = 2
valor4 = 9
operación3 = ((valor3 < 3) and (valor4 == 6))
print(operación3)
operación4 = ((valor3 < 3) or (valor4 ==6))
print(operación4)
operación5 = not ((valor3 < 3) | (valor4 == 6))
print(operación5)