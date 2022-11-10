# CLASE DEL DÍA 27/06/2022

# ESTRUCTURAS DE DATOS

# Listas
# En una lista podemos mezclar tipos de datos
lista = ["hola", 1, 2.2, True]
print(lista)
print(type(lista)) # Objeto list

# Creando lista vacía
lista = list()
lista = []

# Agregando datos a la lista ya creada
lista = ["hola", 1, 2.2, True]
lista += ["adiós", False]
print(lista)

lista.append(56)
lista.append("Pedro") # append solo permite añadir 1 elemento
print(lista)

# Agregando varios datos a la vez
lista.extend(["Marta", 100])
print(lista)

# Eliminando datos de la lista
lista = ["hola", 1, 2.2, 1, True]
lista.remove(1) #Quita el primer 1 que encuentre
print(lista)

# Creando listas mediante el método list()
lista_nombre = list("Esto es un texto largo")
print(lista_nombre)

# Método split para crear una lista a partir de una frase
frase = "Hola como estás"
print(frase.split())

# Separamos mediante un delimitador dentro de split
frase = "Pizza, hamburguesa, ensalada"
print(frase.split(","))

# Método join para crear cadenas a partir de una lista
bebidas = ["agua", "vino", "cerveza", "refresco"]
nueva_frase = ", ".join(bebidas)
print("Mis bebidas favoritas son:", nueva_frase)

# Devolviendo la posición mediante un valor
frase = "Hola como estas".split()
print(frase)
print(frase.index("como"))

# Devolviendo un valor mediante su posición
print(frase[2])

# Repitiendo los valores de la lista
print(frase * 3)

# Buscando valores con in
vocales = ["a", "e", "i", "o", "u"]
resultado = "a" in vocales
print("¿Está a en la lista?:", resultado)
print("¿Está z en la lista?:", "z" in vocales)
if "o" in vocales:
    vocales.remove("o")
    print(vocales)

# RECORRIENDO LISTAS
# 1ª forma de recorrer la lista
vocales = ["a", "e", "i", "o", "u"]
for vocal in vocales:
    print("En la posición: ", vocales.index(vocal), "esta el valor: ", vocal) # Problema si añades otra "a".

# 2ª forma de recorrer la lista
vocales = ["a", "e", "i", "o", "u", "a"]
índice = 0
for vocal in vocales:
    print("En la posición:", índice, " está el valor: ", vocal)
    índice += 1

# 3ª forma de recorrer la lista
vocales = ["a", "e", "i", "o", "u", "a"]
enumeración = enumerate(vocales)
enumeración_como_lista = list(enumeración)
print(enumeración_como_lista) #El primer valor es el índice y el segundo el valor
print(enumeración_como_lista[3]) #Imprime el elemento 3
print(enumeración_como_lista[3][1]) #Dentro del elemento 3 te da la posición 1

vocales = ["a", "e", "i", "o", "u", "a"]
for indice, valor in enumerate(vocales):
    print(f"Índice: {indice}")
    print(f"valor: {valor}")
    print(f"Valor de la lista: {vocales[indice]}")

# Empieza por el final
vocales = ["a", "e", "i", "o", "u", "a"]
print(vocales[-1])
print(vocales[-3])

# Imprimimos slizes (rangos) en la lista
print(vocales[1:4])
print(vocales[2:-1])
print(vocales[1:]) # Llega hasta el final
print(vocales[:]) # La coge entera

# TUPLAS
# Creando tuplas
tupla_1 = (1, 2, 3, 4)
tupla_2 = 1, 2, 3, 4, "Hector", False
print(type(tupla_2))
print(tupla_2)
print(tupla_1[-1])

# Usamos tuplas si no tenemos que modificar los elementos de dentro ya que ocupan la mitad de memoria

# Modificamos listas dentro de las listas
tupla_3 = (1, "Pedro", [0, 1, 2])
print(tupla_3[2])
print(tupla_3[2][0])
tupla_3[2][0] = "Hola"
print(tupla_3[2])
print(tupla_3[1][1])

# Ya no puedo cambiar el elemento de la posición 2
tupla_3 = (1, "Pedro", (0, 1, 2))

# Recorremos la tupla
tupla_1 = 1, 2, 3, 4
for indice, valor in enumerate(tupla_1):
    print(indice, valor)

# DICCIONARIOS
futbolistas = dict()

futbolistas = {1: "Casillas",
               15: "Ramos",
               3: "Pique",
               5: "Puyol",
               11: "Capdevila",
               14: "Xabi Alonso",
               16: "Busquets",
               8: "Xavi Hernandez",
               'Uno': "Pedrito",
               'Otro': "Iniesta",
               7: "Villa"
               }

print(futbolistas['Uno'])
print(futbolistas[14])

# Recorrer un diccionario, imprimiendo su clave-valor.
for key, value in futbolistas.items():
    print(f"{key} -> {value}")

# Vemos cuantos elementos tiene nuestro diccionario
numero_elementos = len(futbolistas)
print("\nNúmero de elementos del diccionario len(futbolistas) = %i" %numero_elementos)
print(f"Número de elementos del diccionario len(futbolistas) = {numero_elementos}")

# Imprimimos una lista con las claves del diccionario
keys = futbolistas.keys()# Esto todavía no es una lista
print(f"Claves del diccionario: {keys}")
key_list = list(futbolistas.keys()) # Esto ya si que es una lista
print(key_list)

# Imprimimos una lista con los valores del diccionario
values = futbolistas.values()
print(values)
values_list = list(futbolistas.values())
print(values_list)

# Obtenemos el valor de un elemento dada su clave
elemento = futbolistas.get(6)
print(f"Obtenemos el valor cuya clave es '6' futbolistas.get(6): {elemento}") # Obtenemos un None porque no está
elemento = futbolistas.get(14)
print(f"Obtenemos el valor cuya clave es '14' futbolistas.get(14): {elemento}") # Obtenemos el valor correspondiente

# Añadimos un nuevo elemento al diccionario
futbolistas = {1: "Casillas",
               15: "Ramos",
               3: "Pique",
               5: "Puyol",
               11: "Capdevila",
               14: "Xabi Alonso",
               16: "Busquets",
               8: "Xavi Hernandez",
               'Uno': "Pedrito",
               'Otro': "Iniesta",
               7: "Villa"
}

futbolistas[22] = "Navas"
print(futbolistas)

# Eliminamos un elemento del diccionario dada su clave
print(f"Pop me devuelve: {futbolistas.pop(22)}")
futbolistas.pop(22)
print(f"\nDiccionario tras eliminar un elemento: futbolistas.pop(22) \n{futbolistas}")

# Hacemos una copia del diccionario
futbolistas = {1: "Casillas",
               15: "Ramos",
               3: "Pique",
               5: "Puyol",
               11: "Capdevila",
               14: "Xabi Alonso",
               16: "Busquets",
               8: "Xavi Hernandez",
               'Uno': "Pedrito",
               'Otro': "Iniesta",
               7: "Villa"
               }
futbolistas_copy = futbolistas.copy()
futbolista2 = futbolistas
print(futbolistas)
print("\nRealizamos una copia: \n%s" %futbolistas_copy)
futbolistas[11] = "Cap"
print("\nRealizamos una copia: \n%s" %futbolistas)
print("\nRealizamos una copia: \n%s" %futbolistas_copy)
print("\nRealizamos una copia: \n%s" %futbolista2)

# Eliminamos los elementos de un diccionario
futbolistas_copy.clear()
print("\nEliminamos los elementos de un diccionario futbolistas_copy.clear(): %s" %futbolistas_copy)

# Creamos un diccionario a partir de una lista con las claves
claves = ["nombre", "apellidos", "edad"]

dict_lista = dict.fromkeys(claves, "nada") # No es necesario meter el valor "nada"
print(f"Creamos un diccionario a partir de una lista: {dict_lista}")

# Comprobamos si existe o no una clave con el valor 2
futbolistas = {1: "Casillas",
               15: "Ramos",
               3: "Pique",
               5: "Puyol",
               11: "Capdevila",
               14: "Xabi Alonso",
               16: "Busquets",
               8: "Xavi Hernandez",
               'Uno': "Pedrito",
               'Otro': "Iniesta",
               7: "Villa"
               }

if 2 in futbolistas:
    print("Si existe la clave", 2)
else:
    print("No existe la clave", 2)

if 8 in futbolistas:
    print("Si existe la clave", 8)
else:
    print("No existe la clave", 8)

# Comprobamos si existe o no una clave con el valor "Puyol"
valores = futbolistas.values()
print(valores)

if "Puyol" in valores:
    print("Si existe Puyol")
else:
    print("No existe Puyol")

# Devolvemos los elementos del diccionario en tuplas
tuplas = futbolistas.items()
print(f"Pasamos el diccionario a tuplas con clave-valor: tuplas = futbolistas.items()\n{tuplas}")

# Unimos dos diccionarios
suplentes = {
    4: 'Marchena', 9: 'Torres', 12: 'Valdes',
    13: 'Mata', 17: 'Arbeloa', 19: 'Llorente',
    20: 'Javi Martinez', 21: 'Silva', 23: 'Reina'
}

futbolistas.update(suplentes) # Es una actualización: Si la clave 15 ya está te pone la nueva
print(f"Añadimos los elementos de un diccionario: {futbolistas}")

