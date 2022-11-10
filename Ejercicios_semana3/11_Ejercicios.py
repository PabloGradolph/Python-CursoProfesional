# Curso profesional de Python (AEPI): 11_Ejercicios
# Autor: Pablo Gradolph Oliva
# 24/07/2022

'''
1 - Realiza una función llamada area_rectangulo() que devuelva el área del
rectángulo a partir de una base y una altura. Calcula el área de un rectángulo de 15
de base y 10 de altura.

Nota: El área de un rectángulo se obtiene al multiplicar la base por la altura.
'''

def area_rectangulo(base, altura):

    return base * altura

base = 15
altura = 10
area = area_rectangulo(base, altura)
print(f"El área del triángulo con base 15 y altura 10 es: \n{area}")
print()
print("FIN DEL PROGRAMA")

'''
2 - Realiza una función llamada area_circulo() que devuelva el área de un círculo
a partir de un radio. Calcula el área de un círculo de 5 de radio:

Nota: El área de un círculo se obtiene al elevar el radio a dos y multiplicando el
resultado por el número pi. Puedes utilizar el valor 3.14159 como pi o importarlo
del módulo math:

import math

print(math.pi)
> 3.1415...
'''
from math import pi

def area_circulo(radio):

    return radio**2 * pi

radio = 5
area = area_circulo(radio)
print(f"El área del círculo con radio 5 es: \n{area}")
print()
print("FIN DEL PROGRAMA")

'''
3 - Realiza una función llamada relacion() que a partir de dos números cumpla lo
siguiente:

• Si el primer número es mayor que el segundo, debe devolver 1.

• Si el primer número es menor que el segundo, debe devolver -1.

• Si ambos números son iguales, debe devolver un 0.

• Comprueba la relación entre los números: '5 y 10', '10 y 5' y '5 y 5'
'''

def relacion(numero_1, numero_2):

    if numero_1 > numero_2:
        return 1
    elif numero_1 < numero_2:
        return -1
    else:
        return 0

print("Relación entre 5 y 10:")
numero_1 = 5
numero_2 = 10
relacion_1 = relacion(numero_1, numero_2)
print(relacion_1)

print("Relación entre 10 y 5:")
numero_1 = 10
numero_2 = 5
relacion_2 = relacion(numero_1, numero_2)
print(relacion_2)

print("Relación entre 5 y 5:")
numero_1 = 5
numero_2 = 5
relacion_3 = relacion(numero_1, numero_2)
print(relacion_3)

print()
print("FIN DEL PROGRAMA")

'''
4 - Realiza una función llamada intermedio() que a partir de dos números,
devuelva su punto intermedio:

Nota: El número intermedio de dos números corresponde a la suma de los dos
números dividida entre 2.

Comprueba el punto intermedio entre -12 y 24
'''

def intermedio(numero_1, numero_2):

    return (numero_1 + numero_2)/2

numero_1 = -12
numero_2 = 24
punto = intermedio(numero_1, numero_2)
print(f"El punto intermedio entre {numero_1} y {numero_2} es: \n{punto}")
print()
print("FIN DEL PROGRAMA")

'''
5 - Realiza una función llamada recortar() que reciba tres parámetros. El primero
es el número a recortar, el segundo es el límite inferior y el tercero el límite
superior. La función tendrá que cumplir lo siguiente:

• Devolver el límite inferior si el número es menor que éste.

• Devolver el límite superior si el número es mayor que éste.

• Devolver el número sin cambios si no se supera ningún límite.

• Comprueba el resultado de recortar 15 entre los límites 0 y 10.
'''

def recortar(numero, limite_inferior, limite_superior):

    if numero < limite_inferior:
        return limite_inferior
    elif numero > limite_superior:
        return limite_superior
    else:
        return numero

numero = 15
limite_inferior = 0
limite_superior = 10
recorte = recortar(numero, limite_inferior, limite_superior)
print(f"El resultado tras recortar {numero} entre los límites {limite_inferior} y {limite_superior} es:")
print(recorte)

print()
print("FIN DEL PROGRAMA")

'''
6 - Realiza una función separar() que tome una lista de números enteros y
devuelva dos listas ordenadas. La primera con los números pares, y la
segunda con los números impares:

Por ejemplo:

pares, impares = separar([6,5,2,1,7])

print(pares) # valdría [2, 6]

print(impares) # valdría [1, 5, 7]

Nota: Para ordenar una lista automáticamente puedes usar el método .sort().

In [20]:
numeros = [-12, 84, 13, 20, -33, 101, 9]
'''

def separar(numeros, pares, impares):

    for i in numeros:
        if i % 2 == 0:
            pares.append(i)
        else:
            impares.append(i)

    pares = sorted(pares)
    impares = sorted(impares)

    print(f"Dada la lista de números: \n{numeros}")
    print()
    print(f"La separamos en:")
    print(f"Números pares --> {pares}")
    print(f"Números impares --> {impares}")

numeros = [-12, 84, 13, 20, -33, 101, 9]
pares = []
impares = []
separar(numeros, pares, impares)
print()
print("FIN DEL PROGRAMA")