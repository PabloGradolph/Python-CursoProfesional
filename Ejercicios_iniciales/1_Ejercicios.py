# Curso profesional de Python (AEPI): 1_Ejercicios
# Autor: Pablo Gradolph Oliva
# 25/06/2022

doskey python = python3

# 1 - Mostrar el precio del IVA (21%) de un producto con un valor de 100 y su precio final
print("IVA Y PRECIO FINAL DE UN PRODUCTO CON UN VALOR DE 100")
valor_producto = 100
IVA = 0.21
IVA_producto = valor_producto * IVA
precio_final = valor_producto + IVA_producto

print(f"El precio del IVA (21%) de un producto con un valor de 100 es de {IVA_producto}")
print(f"El precio final del producto es de {precio_final}")
print("FIN DEL PROGRAMA")

# 2 - Crea una variable numérica y si está entre 0 y 10 muestra un mensaje indicándolo.
print("CREA UNA VARIABLE NUMÉRICA E INDICA SI ESTÁ ENTRE 0 y 10")
una_variable = 9
if 0 < una_variable < 10:
    print(f"La variable creada tiene un valor entre 0 Y 10. Este valor es: {una_variable}")
print("FIN DEL PROGRAMA")

# 3 - Añadir al anterior ejercicio, que si está entre 11 y 20, muestre otro mensaje diferente y si está entre 21 y 30
# otro mensaje.
print("CREA UNA VARIABLE NUMÉRICA E INDICA SI ESTÁ ENTRE 0 Y 10, 11 Y 20 O 21 Y 30")
una_variable = float(input("Por favor, introduzca el valor de la variable: "))
if 0 < una_variable < 10:
    print(f"La variable creada tiene un valor entre 0 y 10. Este valor es: {una_variable}")
elif 11 < una_variable < 20:
    print(f"la variable creada tiene un valor entre 11 y 20. Este valor es: {una_variable}")
elif 21 < una_variable < 30:
    print(f"La variable creada tiene un valor entre 21 y 30. Este valor es: {una_variable}")
print("FIN DEL PROGRAMA")

# 4 - Mostrar con un while los números del 1 al 100.
print("IMPRIMIENDO POR PANTALLA LOS NÚMEROS DEL 1 AL 100:")
valor_numero = 1
while 0 < valor_numero < 101:
    print(valor_numero)
    valor_numero += 1
print("FIN DEL PROGRAMA")

# 5 - Mostrar con un bucle for los números del 1 al 100.
print("IMPRIMIENDO POR PANTALLA LOS NÚMEROS DEL 1 AL 100:")
for i in range(1, 101):
    print(i)
print("FIN DEL PROGRAMA")

# 6 - Mostrar los caracteres de la cadena "Hola mundo" secuencialmente.
print("IMPRIMIENDO POR PANTALLA LOS CARACTERES DE LA CADENA 'Hola mundo' SECUENCIALMENTE:")
for i in "Hola mundo":
    print(i)
print("FIN DEL PROGRAMA")

# 7 - Mostrar los números pares entre el 1 y el 100.
print("IMPRIMIENDO POR PANTALLA LOS NÚMEROS PARES ENTRE EL 1 Y EL 100:")
for i in range(2, 101, 2):
    print(i)
print("FIN DEL PROGRAMA")

# 8 - Programa que imprima los 25 primeros números naturales.
print("IMPRIMIENDO POR PANTALLA LOS 25 PRIMEROS NÚMEROS NATURALES:")
for i in range(1, 26):
    print(i)
print("FIN DEL PROGRAMA")

# 10 - Imprimir los números impares desde el 1 hasta el 25, ambos inclusive.
print("IMPRIMIENDO POR PANTALLA LOS NÚMEROS IMPARES DESDE EL 1 HASTA EL 25:")
for i in range(1, 26, 2):
    print(i)
print("FIN DEL PROGRAMA")

# 11 - Imprimir los números pares desde el 40 hasta el 60, ambos inclusive.
print("IMPRIMIENDO POR PANTALLA LOS NÚMEROS PARES DESDE EL 40 HASTA EL 60:")
for i in range(40, 61, 2):
    print(i)
print("FIN DEL PROGRAMA")

# 12 - Imprimir los números 48, 52, 56, ..., 120.
print("IMPRIMIENDO POR PANTALLA LOS NÚMEROS 48, 52, 56, ..., 120:")
for i in range(48, 121, 4):
    print(i)
print("FIN DEL PROGRAMA")

# 13 - Calcular e imprimir la suma 1 + 2 + 3 + 4 + 5 + ... + 50.
print("CALCULANDO LA SUMA DE LOS PRIMEROS 50 NÚMEROS:")
suma = 0
for i in range(1, 51):
    suma += i
print(f"La suma es: {suma}")
print("FIN DEL PROGRAMA")

# 14 - Calcular e imprimir el producto 1x2x3x4x5x ... x20.
print("CALCULANDO EL PRODUCTO DE LOS PRIMEROS 20 NÚMEROS:")
producto = 1
for i in range(1, 21):
    producto = producto * i
print(f"El producto es: {producto}")
print("FIN DEL PROGRAMA")

# 15 - Calcular e imprimir la suma 50 + 48 + 46 + 44 +...+ 20.
print("CALCULANDO LA SUMA 50 + 48 + 46 + 44 +...+ 20:")
numero = 50
suma = 0
for i in range(0, 31, 2):
    suma += (numero - i)
print(f"La suma es: {suma}")
print("FIN DEL PROGRAMA")

# 16 - Programa que imprima los números impares desde el 100 hasta la unidad y calcule su suma.
print("IMPRIMIENDO LOS NÚMEROS IMPARES DESDE EL 100 HASTA LA UNIDAD:")
numero = 100
suma = 0
for i in range(1, 101, 2):
    print(numero - i)
    suma += (numero - i)
print(f"La suma de todos estos números es: {suma}")
print("FIN DEL PROGRAMA")

# 17 - Introducir un número por teclado y decir si es par o impar.
print("AL INTRODUCIR UN NÚMERO POR TECLADO TE AVISA SI ESTE ES PAR O IMPAR")
numero = int(input("Introduzca un número: "))
if numero % 2 == 0:
    print(f"El número introducido ({numero}) es par.")
else:
    print(f"El número introducido ({numero}) es impar.")
print("FIN DEL PROGRAMA")

# 18 - Imprimir los números del 1 al 100 y calcular la suma de todos los números pares por un lado y la de los impares
# por otro.
print("ESTOS SON LOS NÚMEROS DEL 1 AL 100:")
numero = 1
suma_pares = 0
suma_impares = 0
while 0 < numero < 101:
    if numero % 2 == 0:
        suma_pares += numero
    else:
        suma_impares += numero
        print(suma_impares)
    numero += 1
print(f"La suma de los números pares del 1 al 100 es: {suma_pares}")
print(f"La suma de los números impares del 1 al 100 es: {suma_impares}")
print("FIN DEL PROGRAMA")

# 19 - Introducir dos números por teclado. Imprimir los números que hay entre ellos comenzando por el más pequeño.
# Contar cuántos hay y cuántos de ellos son pares. Calcular la suma de los pares.
numero_uno = int(input("Introduzca el primer número: "))
numero_dos = int(input("Introduzca un segundo número más grande que el primero: "))
if numero_dos < numero_uno:
    print("Error en la entrada, el segundo número introducido es menor que el primero.")
else:
    print()
    diferencia = numero_dos - numero_uno - 1
    if diferencia == 0:
        print("Hay 0 números entre los dos que usted ha introducido.")
    else:
        pares = 0
        suma_pares = 0
        print(f"Hay {diferencia} números entre los dos que usted ha introducido. Estos son:")
        for i in range(numero_uno + 1, numero_dos):
            print(i)
            if i % 2 == 0:
                pares += 1
                suma_pares += i
        print()
        print(f"{pares} de los {diferencia} números que hay entre los que usted ha introducido son pares.")
        print(f"La suma de los números pares es: {suma_pares}")
print("FIN DEL PROGRAMA")

# 20 - Imprimir y contar los números múltiplos de 3 que hay entre 1 y 100
print("IMPRIMIENDO LOS NÚMEROS MÚLTIPLOS DE 3 QUE HAY ENTRE 1 Y 100:")
contador = 0
for i in range(1, 101):
    if i % 3 == 0:
        contador += 1
        print(i)
print(f"Hay {contador} múltiplos de 3 entre 1 y 100.")
print()
print("FIN DEL PROGRAMA")

# 21 - Imprimir, sumar y contra los números que son a la vez múltiplos de 2 y de 3, que hay entre la unidad y un
# determinado número introducido por el teclado.
numero_introducido = int(input("Introduzca un número: "))
print()
print(f"IMPRIMIENDO TODOS LOS NÚMEROS MÚLTIPLOS A LA VEZ DE 2 Y DE 3 QUE HAY ENTRE 1 Y {numero_introducido}")
suma = 0
contador = 0
for i in range(1, numero_introducido + 1):
    if i % 2 == 0 and i % 3 == 0:
        print(i)
        contador += 1
        suma += i
if contador == 1:
    print(f"Solo hay un número y su suma es {suma}")
else:
    print(f"Son {contador} números.")
    print(f"La suma de estos es: {suma}")
print()
print("FIN DEL PROGRAMA")

# 22 - Introducir dos valores A y B: Si A>=B, calcular e imprimir la suma 10+14+18+...+50. Si A/B<=30, calcular e
# imprimir el valor de (A^2+B^2).
A = float(input("Introduzca un valor numérico para A: "))
B = float(input("Introduzca otro valor numérico para B: "))
if A >= B:
    suma = 0
    for i in range(10, 51, 4):
        suma += i
    print(f"El valor de A: {A} es mayor o igual que el valor de B: {B}")
    print(f"La suma 10 + 14 + 18 + ... + 50 es igual a: {suma}")
if A/B <= 30:
    division = A/B
    calculo = A**2 + B**2
    print(f"A/B = {division} y es menor o igual a 30")
    print(f"(A^2 + B^2) = {calculo}")
print()
print("FIN DEL PROGRAMA")

# 23 - Introducir los valores A, B y C: Si A/B>30, calcular e imprimir A/C * B^3. Si A/B<=30, calcular e imprimir
# 2^2 + 4^2 + 6^2 + ... + 30^2.
A = float(input("Introduzca un valor numérico para A: "))
B = float(input("Introduzca un valor numérico para B: "))
C = float(input("Introduzca un valor numérico para C: "))
print()
if A/B > 30:
    calculo = A/C * B**3
    print(f"A/C * B^3 = {calculo}")
else:
    suma = 0
    for i in range(2, 31, 2):
        suma += (i**2)
    print(f"La suma 2^2 + 4^2 + 6^2 + ... + 30^2 es: {suma}")
print()
print("FIN DEL PROGRAMA")

# 24 - Pedir una nota de 0 a 10, como número entero, y mostrarla de la forma: insuficiente, por debajo de 5, suficiente
# entre 5 y 6, bien entre 6 y 7, Notable entre 8 y 9 y Sobresaliente entre 9 y 10.
print("CALCULA EL VALOR DE SU NOTA:")
nota = float(input("Introduzca una nota del 1 al 10: "))
if nota < 0 or nota > 10:
    print ("Error en la entrada, no se ha introducido una nota entre 0 y 10.")
else:
    if 0 <= nota < 5:
        print(f"Su calificación ({nota}) es de Insuficiente.")
    elif 5 <= nota < 6:
        print(f"Su calificación ({nota}) es de Suficiente.")
    elif 6 <= nota < 7:
        print(f"Su calificación ({nota}) es de Bien.")
    elif 7 <= nota < 9:
        print(f"Su calificación ({nota}) es de Notable.")
    elif 9 <= nota < 10:
        print(f"Su calificación ({nota}) es de Sobresaliente.")
print()
print("FIN DEL PROGRAMA")

# 25 - Pedir el día, mes y año de una fecha e indicar si la fecha es correcta. Suponiendo todos los meses de 30 días.
print("CALCULA SI UNA FECHA ES VÁLIDA O NO:")
dia = int(input("Introduzca un día: "))
mes = int(input("Introduzca un mes del año (con números): "))
año = int(input("Introduzca un año: "))
if dia < 0 or dia > 30:
    print("Error en la entrada, día no válido.")
if mes < 0 or mes > 12:
    print("Error en la entrada, mes no válido.")
if año > 2022:
    print("Error en la entrada, aún no hemos alcanzado ese año.")
if 1 <= dia <= 30 and 1 <= mes <= 12 and 0 <= año <= 2022:
    print(f"La fecha es correcta: Día {dia} del mes {mes} del año {año} después de Cristo.")
if 1 <= dia <= 30 and 1 <= mes <= 12 and año < 0:
    año = año * -1
    print(f"La fecha es correcta: Día {dia} del mes {mes} del año {año} antes de Cristo.")
print()
print("FIN DEL PROGRAMA")