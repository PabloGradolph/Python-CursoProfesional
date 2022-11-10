# Curso profesional de Python (AEPI): 2_Ejercicios
# Autor: Pablo Gradolph Oliva
# 27/06/2022

# 1 - Antes de ejecutar el código, identifica el tipo de dato de los siguientes valores literales:
'''
"Hola Mundo"
[1, 10, 100]
-25
1.167
["Hola", "Mundo"]
'''
print("VIENDO EL TIPO DE DIFERENTES VARIABLES:")
print()
variable_1 = "Hola Mundo" # Str
variable_2 = [1, 10, 100] # List
variable_3 = -25 # Int
variable_4 = 1.167 # Float
variable_5 = ["Hola", "Mundo"] # List

# Comprobamos

tipo_1 = type(variable_1)
tipo_2 = type(variable_2)
tipo_3 = type(variable_3)
tipo_4 = type(variable_4)
tipo_5 = type(variable_5)
print(f"'Hola Mundo' es de tipo {tipo_1}")
print(f"'[1, 10, 100]' es de tipo {tipo_2}")
print(f"'-25' es de tipo {tipo_3}")
print(f"'1.167' es de tipo {tipo_4}")
print(f"'['Hola', 'Mundo']' es de tipo {tipo_5}")
print()
print("FIN DEL PROGRAMA")

# 2 - Determina, antes de ejecutar el código, el resultado que aparecerá por pantalla a partir de estas variables:
'''
a = 10
b = -5
c = "Hola "
d = [1, 2, 3]
print(a * 5)
print(c + "Mundo")
print(c * 2)
print(c[-1])
print(c[1:])
print(d + d)
'''
print("DETERMINANDO EL RESULTADO QUE APARECERÁ POR PANTALLA A PARTIR DE CIERTAS VARIABLES:")
a = 10
b = -5
c = "Hola "
d = [1, 2, 3]
print(a * 5) # 50
print(c + "Mundo") # "Hola Mundo"
print(c * 2) # "Hola Hola"
print(c[-1]) # El espacio (último caracter de la cadena)
print(c[1:]) # 'ola' Devuelve desde la posición 1 (o) en adelante
print(d + d) # [1, 2, 3, 1, 2, 3]
print()
print("FIN DEL PROGRAMA")

# 3 - El siguiente código pretende realizar una media entre 3 números, pero no funciona correctamente. ¿Eres capaz de
# identificar el problema y solucionarlo?
print("CALCULANDO LA NOTA MEDIA DE 3 NOTAS:")
numero_1 = 9
numero_2 = 3
numero_3 = 6
media = numero_1 + numero_2 + numero_3 / 3
print()
print(f"La nota media es {media}") # Esta está mal calculada.

# Escribimos ahora el código corregido:
print("CALCULANDO LA NOTA MEDIA DE 3 NOTAS:")
numero_1 = 9
numero_2 = 3
numero_3 = 6
media = (numero_1 + numero_2 + numero_3) / 3
print()
print(f"La nota media es {media}") # Esta está bien calculada.
print()
print("FIN DEL PROGRAMA")

# 4 - A partir del ejercicio anterior, vamos a suponer que cada número es una nota, y lo que queremos es obtener la nota
# media. El problema es que cada nota tiene un valor porcentual:
'''
La primera nota vale 15% del total
La segunda nota vale un 35% del total
La tercera nota vale un 50% del total
'''
# Desarrolla un porgrama para calcular perfectamente la nota final:
'''
nota_1 = 10
nota_2 = 7
nota_3 = 4
'''
print("CALCULANDO LA NOTA MEDIA CON PORCENTAJES:")
nota_1 = 10
nota_2 = 7
nota_3 = 4
valor_nota_1 = 15/100
valor_nota_2 = 35/100
valor_nota_3 = 50/100
media = nota_1 * valor_nota_1 + nota_2 * valor_nota_2 + nota_3 * valor_nota_3
print()
print(f"La nota media es {media}")
print()
print("FIN DEL PROGRAMA")