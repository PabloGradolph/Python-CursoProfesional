# Curso profesional de Python (AEPI): 4_Ejercicios
# Autor: Pablo Gradolph Oliva
# 27/06/2022

# 1 - Realiza un programa que lea dos números por teclado y permita elegir entre 3 opciones en un menú:
'''
· Mostrar una suma de los dos números.
· Mostrar una resta de los dos números (el primero menos el segundo).
· Mostrar una multiplicación de los dos números.
· En caso de no introducir una opción válida, el programa informará de que no es correcta.
'''
numero_1 = float(input("Introduzca el primer número: "))
numero_2 = float(input("Introduzca el segundo número: "))
while True:
    print()
    print("MENÚ DE OPCIONES:")
    print("1. Muestra la suma de los números")
    print("2. Muestra la resta de los números (el primero menos el segundo)")
    print("3. Muestra la multiplicación de los números")
    print("4. Terminar el programa")
    print()
    opcion = int(input("Introduzca la opción que desee: "))
    while opcion < 1 or opcion > 4:
        print("La opción introducida no es válida.")
        opcion = int(input("Por favor, vuelva a introducir una opción: "))
    if opcion == 1:
        suma = numero_1 + numero_2
        print(f"La suma de los números es: {suma}")
    elif opcion == 2:
        resta = numero_1 - numero_2
        print(f"La resta del primer número menos el segundo es: {resta}")
    elif opcion == 3:
        multiplicación = numero_1 * numero_2
        print(f"La multiplicación de los números es: {multiplicación}")
    else:
        break
print()
print("FIN DEL PROGRAMA")

# 2 - Realiza un programa que lea un número por teclado. Si el usuario no introduce un número impar, debe repetirse el
# proceso hasta que lo introduzca correctamente.
print("PEDIR NÚMEROS HASTA QUE UNO SEA IMPAR:")
numero = 2
while numero % 2 == 0:
    numero = int(input("Introduzca un número: "))
print()
print(f"El último número introducido ({numero}) es impar.")
print()
print("FIN DEL PROGRAMA")

# 3 - Realiza un programa que sume todos los números pares desde el 0 hasta el 100.
print("SUMA DE TODOS LOS NÚMEROS PARES DESDE EL 0 HASTA EL 100:")
numeros = range(0, 101, 2)
suma = sum(numeros)
print()
print(f"La suma es: {suma}")
print()
print("FIN DEL PROGRAMA")

# 4 - Realiza un programa que pida al usuario cuantos números quiere introducir.
# Luego lee todos los números y realiza una media aritmética.
print("MEDIA ARITMÉTICA DE VARIOS NÚMEROS:")
print()
cantidad_numeros = int(input("Escriba la cantidad de números que desea introducir: "))
suma = 0
if cantidad_numeros < 0:
    print("Error en la entrada")
else:
    for i in range(0, cantidad_numeros):
        numero = float(input("Introduzca un número: "))
        suma += numero
    media = suma/cantidad_numeros
    print()
    print(f"La media es: {media}.")
print()
print("FIN DEL PROGRAMA")