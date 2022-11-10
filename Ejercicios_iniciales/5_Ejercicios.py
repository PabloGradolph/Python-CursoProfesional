# Curso profesional de Python (AEPI): 5_Ejercicios
# Autor: Pablo Gradolph Oliva
# 28/06/2022

# 1 - Pedir los coeficientes de una ecuación de 2º grado, y mostrar sus soluciones reales. Si no existen, debe indicarlo
from math import sqrt
print("SOLUCIONES DE UNA ECUACIÓN DE 2º GRADO (ax^2+bx+c=0) A PARTIR DE SUS COEFICIENTES:")
A = float(input("Introduzca el valor del coeficiente a: "))
B = float(input("Introduzca el valor del coeficiente b: "))
C = float(input("Introduzca el valor del coeficiente c: "))
if A == 0 and B == 0 and C == 0:
    print()
    print(f"La ecuación a resolver es: {A}x^2 + {B}x + {C} = 0")
    print("X puede tomar cualquier valor real")
if A == 0 and B == 0 and C != 0:
    print()
    print(f"La ecuación a resolver es: {A}x^2 + {B}x + {C} = 0")
    print("Esta ecuación no tiene soluciones reales")
if A == 0 and B != 0 and C == 0:
    print()
    print(f"La ecuación a resolver es: {A}x^2 + {B}x + {C} = 0")
    print("La solución de la ecuación es x = 0")
if A == 0 and B != 0 and C != 0:
    print()
    print(f"La ecuación a resolver es: {A}x^2 + {B}x + {C} = 0")
    x = (-C)/B
    print(f"La solución de la ecuación es x = {x}")
if A != 0 and B == 0 and C == 0:
    print()
    print(f"La ecuación a resolver es: {A}x^2 + {B}x + {C} = 0")
    print("La solución de la ecuación es doble y es x = 0")
if A != 0 and B == 0 and C != 0:
    print()
    print(f"La ecuación a resolver es: {A}x^2 + {B}x + {C} = 0")
    if (-C)/A < 0:
        print("Esta ecuación no tiene soluciones reales")
    else:
        x_1 = ((-C)/A)**(1/2)
        x_2 = -((-C)/A)**(1/2)
        print("Las soluciones de la ecuación son:")
        print(f"x = {x_1}")
        print(f"x = {x_2}")
if A != 0 and B != 0 and C == 0:
    print()
    print(f"La ecuaicón a resolver es: {A}x^2 + {B}x + {C} = 0")
    x_1 = 0
    x_2 = (-B)/A
    print("Las soluciones de la ecuación son:")
    print(f"x = {x_1}")
    print(f"x = {x_2}")
if A != 0 and B != 0 and C != 0:
    print()
    print(f"La ecuaicón a resolver es: {A}x^2 + {B}x + {C} = 0")
    if (B**2 - 4 * A * C) < 0:
        print("La ecuación no tiene soluciones reales")
    elif (B**2 - 4 * A * C) == 0:
        x = (-B)/(2*A)
        print(f"La solución de la ecuación es doble y es: x = {x}")
    else:
        x_1 = ((-B) + sqrt(B**2 - 4 * A * C)) / (2*A)
        x_2 = ((-B) - sqrt(B**2 - 4 * A * C)) / (2*A)
        print(f"Las soluciones de la ecuación son:")
        print(f"x = {x_1}")
        print(f"x = {x_2}")
print()
print("FIN DEL PROGRAMA")

# 2 - Pedir el radio de un círculo y calcular su área. A = PI*r^2
import math
PI = math.pi
print("CALCULANDO EL ÁREA DE UN CÍRCULO A PARTIR DE SU RADIO:")
r = float(input("Introduzca el valor del radio en metros: "))
área = PI * (r**2)
print()
print(f"Dado el radio = {r} metros, el área del círculo es: {área} m^2")
print()
print("FIN DEL PROGRAMA")

# 3 - Pedir el radio de una circunferencia y calcular su longitud
import math
PI = math.pi
print("CALCULANDO LA LONGITUD DE UNA CIRCUNFERENCIA A PARTIR DE SU RADIO:")
r = float(input("Introduzca el valor del radio en metros: "))
print()
l = 2*PI*r
print(f"Dado el radio = {r} metros, la longitud de la circunferencia es: {l} metros")
print()
print("FIN DEL PROGRAMA")

# 4 - Pedir dos números y decir si son iguales o no
print("COMPARACIÓN DE NÚMEROS:")
numero_1 = float(input("Introduzca el primer número: "))
numero_2 = float(input("Introduzca el segundo número: "))
print()
if numero_2 == numero_1:
    print("Los números introducidos son iguales")
else:
    print("Los números introducidos son diferentes")
print()
print("FIN DEL PROGRAMA")

# 5 - Pedir un número e indicar si es positivo o negativo
print("NÚMERO POSITIVO O NEGATIVO:")
numero = float(input("Introduzca un número: "))
print()
if numero < 0:
    print("El número introducido es negativo")
elif numero == 0:
    print("El número introducido es 0")
else:
    print("El número introducido es positivo")
print()
print("FIN DEL PROGRAMA")

# 6 - Pedir dos números y decir si uno es múltiplo del otro
print("¿SON MÚLTIPLOS EL UNO DEL OTRO?")
numero_1 = float(input("Introduzca el primer número: "))
numero_2 = float(input("Introduzca el segundo número: "))
print()
if numero_2 % numero_1 == 0:
    print(f"{numero_2} es múltiplo de {numero_1}")
elif numero_1 % numero_2 == 0:
    print(f"{numero_1} es múltiplo de {numero_2}")
else:
    print("Los números introducidos no son múltiplos entre sí")
print()
print("FIN DEL PROGRAMA")

# 7 - Pedir dos números y decir cual es el mayor
# 8 - Pedir dos números y decir cual es el mayor o si son iguales
print("¿QUÉ NÚMERO ES MAYOR?")
numero_1 = float(input("Introduzca el primer número: "))
numero_2 = float(input("Introduzca el segundo número: "))
print()
if numero_2 == numero_1:
    print("Los números introducidos tienen el mismo valor")
elif numero_1 < numero_2:
    print(f"{numero_2} es mayor que {numero_1}")
else:
    print(f"{numero_1} es mayor que {numero_2}")
print()
print("FIN DEL PROGRAMA")

# 9 - Pedir dos números y mostrarlos ordenados de mayor a menor
print("ORDEN DE NÚMEROS:")
numero_1 = float(input("Introduzca el primer número: "))
numero_2 = float(input("Introduzca el segundo número: "))
print()
if numero_2 == numero_1:
    print(f"{numero_2} = {numero_1}")
elif numero_1 < numero_2:
    print(f"{numero_2} > {numero_1}")
else:
    print(f"{numero_1} > {numero_2}")
print()
print("FIN DEL PROGRAMA")

# 10 - Pedir tres números y mostrarlos ordenados de mayor a menor
print("ORDEN DE NÚMEROS:")
numero_1 = float(input("Introduzca el primer número: "))
numero_2 = float(input("Introduzca el segundo número: "))
numero_3 = float(input("Introduzca el tercer número: "))
print()
if numero_3 == numero_2 == numero_1: # Todos iguales
    print(f"{numero_3} = {numero_2} = {numero_1}")
elif numero_1 == numero_2 < numero_3: # Primero y segundo iguales. Tercero mayor.
    print(f"{numero_3} > {numero_1} = {numero_2} ")
elif numero_1 == numero_3 < numero_2: # Primero y tercero iguales. Segundo mayor.
    print(f"{numero_2} > {numero_1} = {numero_3} ")
elif numero_2 == numero_3 < numero_1: # Segundo y tercero iguales. Primero mayor.
    print(f"{numero_1} > {numero_3} = {numero_2} ")
elif numero_1 == numero_2 > numero_3: # Primero y segundo iguales. Tercero menor.
    print(f"{numero_1} = {numero_2} > {numero_3}")
elif numero_1 == numero_3 > numero_2: # Primero y tercero iguales. Segundo menor.
    print(f"{numero_1} = {numero_3} > {numero_2}")
elif numero_2 == numero_3 > numero_1: # Segundo y tercero iguales. Primero menor.
    print(f"{numero_3} = {numero_2} > {numero_1}")
elif numero_1 < numero_2 < numero_3: # Primero menor que segundo menor que tercero.
    print(f"{numero_3} > {numero_2} > {numero_1}")
elif numero_1 < numero_3 < numero_2: # Primero menor que tercero menor que segundo.
    print(f"{numero_2} > {numero_3} > {numero_1}")
elif numero_2 < numero_1 < numero_3: # Segundo menor que primero menor que tercero.
    print(f"{numero_3} > {numero_1} > {numero_2}")
elif numero_2 < numero_3 < numero_1:  # Segundo menor que tercero menor que primero.
    print(f"{numero_1} > {numero_3} > {numero_2}")
elif numero_3 < numero_2 < numero_1: # Tercero menor que segundo menor que primero.
    print(f"{numero_1} > {numero_2} > {numero_3}")
else: # Tercero menor que primero menor que segundo.
    print(f"{numero_2} > {numero_1} > {numero_3}")
print()
print("FIN DEL PROGRAMA")

# 11 - Pedir un número entre 0 y 9.999 y decir cuantas cifras tiene
print("CANTIDAD DE CIFRAS DE UN NÚMERO:")
numero = float(input("Introduzca un número entre 0 y 10: "))
print()
cadena = str(numero)
if 0 < numero < 10:
    contador = 0
    for i in cadena: # Con esta estructura se podría hacer para cualquier número
        if i != ".":
            contador += 1
    print(f"El número {numero} tiene {contador} cifras")
else:
    print(f"{numero} no está entre 0 y 10")
print()
print("FIN DEL PROGRAMA")