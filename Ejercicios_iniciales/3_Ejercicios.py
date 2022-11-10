# Curso profesional de Python (AEPI): 3_Ejercicios
# Autor: Pablo Gradolph Oliva
# 27/06/2022

# 1 - Realiza un programa que lea 2 números por teclado y determine los siguientes aspectos:
'''
· Si los dos números son iguales
· Si los dos números son diferentes
· Si el primero es mayor que el segundo
· Si el segundo es mayor o igual que el primero
'''
print("COMPARANDO DOS NÚMEROS INTRODUCIDOS POR TECLADO:")
print()
numero_1 = float(input("Introduzca el primer número: "))
numero_2 = float(input("Introduzca el segundo número: "))
print()
if numero_2 == numero_1:
    print("Los números introducidos son iguales.")
    print()
else:
    print("Los números introducidos son diferentes.")
    print()
if numero_1 > numero_2:
    print(f"El primer número ({numero_1}) es mayor que el segundo ({numero_2}).")
if numero_2 >= numero_1:
    print(f"El segundo número ({numero_2}) es mayor o igual que el primero ({numero_1}).")
print()
print("FIN DEL PROGRAMA")

# 2 - Utilizando operadores lógicos, determina si una cadena de texto introducida por el usuario tiene una longitud
# mayor o igual que 3 y a su vez es menor que 10 (es suficiente con mostrar True o False).
print("LONGITUD DE UNA CADENA DE TEXTO (MAYOR O IGUAL QUE 3 Y MENOR QUE 10) INTRODUCIDA POR EL USUARIO:")
cadena = input("Introduzca una cadena de texto: ")
contador = 0
for i in cadena:
    contador += 1
if contador >= 3 and contador < 10:
    print(f"La cadena de texto introducida: '{cadena}', tiene una longitud mayor o igual a 3 y menor que 10.")
    # Con la función len() también se puede medir la longitud de una cadena.
print()
print("FIN DEL PROGRAMA")

# 3 - Realiza un programa que cumpla el siguiente algoritmo utilizando siempre que sea posible operadores de aisgnación:
'''
Guarda en una variable denominada numero_magico el valor 12345679 (sin el 8).
Lee por pantalla otro número y guárdalo en la variable denominada numero_usuario,
especifica que sea entre 1 y 9 (asegúrate que sea un número entero).

Multiplica el numero_usuario por 9 en sí mismo.
Multiplica el numero_magico por el numero_usuario en sí mismo.
Finalmente, muestra el valor final del numero_magico por pantalla. 
 '''
print("NÚMERO MÁGICO:")
numero_magico = 12345679
numero_usuario = int(input("Introduzca un número entero entre 1 y 9: "))
while numero_usuario < 1 or numero_usuario > 9:
    print()
    print("Error en la entrada.")
    numero_usuario = int(input("Por favor, introduzca de nuevo un número entero entre 1 y 9: "))
numero_usuario *= 9
numero_magico *= numero_usuario
print()
print(f"El valor del número mágico es: {numero_magico}.")
print()
print("FIN DEL PROGRAMA")