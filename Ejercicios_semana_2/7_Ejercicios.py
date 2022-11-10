# Curso profesional de Python (AEPI): 7_Ejercicios
# Autor: Pablo Gradolph Oliva
# 05/07/2022

# 1 - Mete los valores del 1 al 100 en una lista
print("METIENDO LOS VALORES DEL 1 AL 100 EN UNA LISTA:")
lista_numeros = []
for i in range(1, 101):
    lista_numeros.append(i)
print()
print(lista_numeros)
print()
print("FIN DEL PROGRAMA")

# 2 - Crea una tupla con los meses del año, pide núeros al usuario, si el número esta entre 1 y la longitud máxima de la
# tupla, muestra el contenido de esa posición sino muestra un mensaje de error. El programa termina cuando el usuario
# introduce un cero.
tupla_meses = ("enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre",
               "octubre", "noviembre", "diciembre")
print("Introduzca un número del 1 al 12 para mostrar el mes correspondiente o 0 para finalizar el programa:")
numero = int(input())
if 12 <= numero <= 0:
    print("Error en la entrada")
else:
    while numero != 0:
        print(f"El mes seleccionado es {tupla_meses[numero - 1]}")
        numero = int(input("Introduzca otro número del 0 al 12: "))
print()
print("FIN DEL PROGRAMA")

# 3 - Pide un número por teclado y guarda en una lista su tabla de multiplicar hasta el 10. Por ejemplo, si pide el 5,
# la lista tendrá. 5, 10, 15, 20, 25, 30, 35, 40, 45, 50
print("CREANDO LA TABLA DE MULTIPLICAR DE UN NÚMERO HASTA EL 10:")
print()
numero = float(input("Introduzca un número: "))
tabla_multiplicar = []
for i in range(1, 11):
    tabla_multiplicar.append(i * numero)
print(f"La tabla de multiplicar hasta el 10 del número {numero} es: \n{tabla_multiplicar}")
print()
print("FIN DEL PROGRAMA")

# 4 - Pide números y mételos en una lista, cuando el usuario meta un 0 ya dejaremos de insertar. Por último, muestra los
# números ordenados de menor a mayor.
print("INSERTE NÚMEROS PARA ORDENARLOS DE MENOR A MAYOR. CUANDO INTRODUZCA UN 0 FINALIZARÁ EL PROGRAMA:")
print()
lista_numeros = []
while True:
    numero = float(input("Introduzca un número: "))
    if numero == 0:
        break
    else:
        lista_numeros.append(numero)

lista_ordenada = sorted(lista_numeros)
print(f"Los números introducidos en orden de menor a mayor son: \n{lista_ordenada}")
print()
print("FIN DEL PROGRAMA")

# 5 - Lo mismo que el anterior pero ordenando de mayor a menor.
print("INSERTE NÚMEROS PARA ORDENARLOS DE MAYOR A MENOR. CUANDO INTRODUZCA UN 0 FINALIZARÁ EL PROGRAMA:")
print()
lista_numeros = []
while True:
    numero = float(input("Introduzca un número: "))
    if numero == 0:
        break
    else:
        lista_numeros.append(numero)

lista_ordenada = sorted(lista_numeros, reverse=True)
print(f"Los números introducidos en orden de mayor a menor son: \n{lista_ordenada}")
print()
print("FIN DEL PROGRAMA")

# 6 - Pide una cadena por teclado, mete los caracteres en una lista sin espacios.
print("METIENDO LOS CARACTERES DE UNA CADENA EN UNA LISTA SIN ESPACIOS:")
print()
cadena = input("Introduzca una cadena de texto: ")
lista_sin_espacios = []
for i in cadena:
    if i != " ":
        lista_sin_espacios.append(i)

print()
print(f"Los caracteres de la cadena sin espacios son: \n{lista_sin_espacios}")
print()
print("FIN DEL PROGRAMA")

# 7 - Pide una cadena por teclado, mete los caracteres en una lista sin repetir caracteres
print("METIENDO LOS CARACTERES DE UNA CADENA EN UNA LISTA SIN ESPACIOS Y SIN REPETIR CARACTERES:")
print()
cadena = input("Introduzca una cadena de texto: ")
lista_sin_repetición = []
for i in cadena:
    if i not in lista_sin_repetición and i != " ":
        lista_sin_repetición.append(i)

print()
print(f"Los caracteres de la cadena sin espacios y sin caracteres repetidos son: \n{lista_sin_repetición}")
print()
print("FIN DEL PROGRAMA")

# 8 - Crea una tupla con números, pide un número por teclado e indica cuantas veces se repite.
tupla_con_numeros = (1, 2, 3, 4, 5, 1, 1, 2, 3, 3, 3, 4, 5, 5, 5, 5, 6, 5, 4, 8, 9, 8, 9, 9, 9, 8, 7, 7, 7, 6, 7, 6, 5,
                     5, 5, 4, 4, 3, 4, 3, 2, 1, 2, 3, 2, 3, 4, 5, 4, 3, 6, 7, 8, 6, 5, 7, 8, 9, 9, 0, 0, 0, 0, 0, 0, 0)
numero = int(input("Introduzca un número y se indicará cuantas veces se repite en la tupla: "))
cantidad = tupla_con_numeros.count(numero)
print(f"El número {numero} se repite {cantidad} veces")
print()
print("FIN DEL PROGRAMA")

# 9 - Crea una tupla con números e indica el número con mayor valor y el que menor tenga
tupla_con_numeros = (1, 2, 3, 4, 5, 1, 1, 2, 3, 3, 3, 4, 5, 5, 5, 5, 6, 5, 4, 8, 9, 8, 9, 9, 9, 8, 7, 7, 7, 6, 7, 6, 5,
                     5, 5, 4, 4, 3, 4, 3, 2, 1, 2, 3, 2, 3, 4, 5, 4, 3, 6, 7, 8, 6, 5, 7, 8, 9, 9, 0, 0, 0, 0, 0, 0, 0)
print(f"El valor máximo de la tupla creada con números es: {max(tupla_con_numeros)}")
print(f"El valor mínimo de la tupla creada con números es. {min(tupla_con_numeros)}")
print()
print("FIN DEL PROGRAMA")

# 10 - Crea un diccionario donde la clave sea el nombre del usuario y el valor sea el teléfono (no es necesario validar)
# Tendrás que ir pidiendo contactos hasta que el usuario diga que no quiere insertar más. No se podrán meter nombres
# repetidos.
diccionario = {}

opción = 1
while opción == 1 or opción == 2:
    print("MENÚ:")
    print("1 - Agregar contacto al diccionario")
    print("2 - Terminar el programa")
    print()
    opción = int(input("Ingrese una opción: "))
    if opción == 2:
        break
    else:
        nombre = input("Introduzca el nombre del contacto: ")
        if nombre in diccionario:
            print("Error el nombre ya está en el diccionario")
            print("Terminando el programa")
            break
        else:
            teléfono = int(input("Introduzca su número de teléfono: "))
            diccionario[nombre] = teléfono
print()
print("El diccionario ha quedado guardado de la siguiente forma:")
print(diccionario)
print()
print("FIN DEL PROGRAMA")