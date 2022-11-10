# CLASE DEL DÍA 21/07/2022

# FICHEROS
import os
print(os.getcwd()) # Te dice la ubicación en la que estás trabajando

directorio_actual = os.getcwd()
directorio = os.path.dirname(os.path.abspath(__file__)) # Son formas equivalentes
print(f"Directorio con __file__: {directorio}")
nombre_objetivo = "hola.txt" # Hemos creado este archivo para que lo encuentre posteriormente

for raiz, dirs, archivos in os.walk(directorio_actual): # Recorremos todo el directorio actual
    print("-------------------------------------------------------")
    print(f"Raíz: {raiz}")
    print(f"Directorios: {dirs}")
    print(f"Archivos: {archivos}")
    print("-------------------------------------------------------")

    if nombre_objetivo in archivos:
        print("Está aquí:")
        print(raiz)
        loquebuscaba = raiz

ruta_completa = os.path.join(loquebuscaba, nombre_objetivo)
print(ruta_completa) # Unimos la raíz con el nombre del archivo para la ruta completa de esta forma

# CREAR FICHERO Y ESCRIBIR TEXTO
texto = "Una línea con texto\nOtra línea con texto"
fichero = open(ruta_completa, "a") # fichero.txt ruta donde lo crearemos
fichero.write(texto)
fichero.close

fichero2 = open(ruta_completa, "w") # Escribimos el texto borrando lo anterior
fichero2.write(texto)
fichero2.close

# LECTURA DE UN FICHERO DE TEXTO
fichero = open(ruta_completa, "r") # Modo lectura
texto = fichero.read()
fichero.close()
print(texto)
print(texto.encode("utf8").decode("latin1"))

fichero = open(ruta_completa, "r")
texto_como_lineas = fichero.readlines() # Leer creando una lista de líneas
fichero.close()
print(texto_como_lineas)
print(texto_como_lineas[-1]) # Última línea

# Extensión de un fichero de texto
fichero = open(ruta_completa, "a")
fichero.write("\nUna línea adicional")
fichero.close()

# Lectura de un fichero no existente, nos genera la excepción de tipo FileNotFoundError
fichero = open("fichero_inventado.txt", "r")

# Se crea un archivo si no existe
fichero = open("fichero_inventado.txt", "a+")
fichero.close()

# Lectura línea a línea secuencial
with open(ruta_completa, "r") as fichero: # Cuando terminas con este tipo de trabajo se cierra automáticamente
    for linea in fichero:
        print(linea)

# Manejando el puntero
fichero = open(ruta_completa, "r")
fichero.seek(0) # Puntero al principio
print(fichero.read(10)) # Leemos 10 caracteres
print(fichero.read(10)) # leemos 10 caracteres más, a partir del 10 donde está el puntero
fichero.seek(0)
print(fichero.seek(len(fichero.readline()))) # Leemos la primera línea y situamos el puntero al principio de la segunda
fichero.close()

# Lectura y escritura a la vez
fichero2 = open("fichero2.txt", "w")
texto = "Línea 1\nLínea 2 \nLínea 3"
fichero2.write(texto)
fichero2.close()
fichero2 = open("fichero2.txt", "a+")
fichero2.write("\nasdfgh")
fichero2.close()

# Modificar una línea específica
fichero2 = open("fichero2.txt", "r+") # Modo lectura con escritura
texto = fichero2.readlines()
texto[1] = "Esta es la línea 3 modificada"
fichero2.writelines(texto)
fichero2.close()

# Mejor forma de hacerlo
fichero_trabajo = open("fichero2.txt", "r")
with fichero_trabajo as f:
    texto = f.readlines()
    texto[2] = " ---- Línea modificada ----"

fichero_trabajo = open("fichero2.txt", "w")
with fichero_trabajo as f:
    f.writelines(texto)

# Extra lectura escritura simultánea:
fichero2 = open("fichero2.txt", "w")
texto = "Línea 1\nLínea 2 \nLínea 3\nTexto"
fichero2.write(texto)
fichero2.close()
with open("fichero2.txt", "r") as l, open("hola.txt", "w") as e:
    linea = l.readlines()
    while linea != "":
        linea = l.readline()
        if "Texto" in linea:
            res = linea[0:3]
            e.write(res + "\n")

# OTROS TIPOS DE FICHEROS

# El módulo pickle
# Guardar estructura o colecciones en ficheros binarios
import pickle

lista = [1, 2, 3, 4, 5]
# Podemos guardar lo que queramos
fichero = open("lista.pckl", "wb")
# Escritura en modo binario, vacía el fichero si existe
pickle.dump(lista, fichero)
fichero.close()

# Recuperar estructura de fichero binario
fichero = open("lista.pckl", "rb") # Lectura en modo binario
lista_fichero = pickle.load(fichero)
print(lista_fichero)

# Lógica para trabajar con objetos
#1º Crear una colección
#2º Introducir los objetos en la colección
#3º Guardar la colección haciendo un dump
#4º Recuperar la colección haciendo un load
#5º Seguir trabajando con nuestros objetos

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return self.nombre


nombres = ["Héctor", "Mario", "Marta"]
personas = []

'''
Te faltan cosas por poner en el 
código mira a ver 
si puedes completarlo 
'''

import pickle

f = open("Personas.pckl", "wb")
pickle.dump(personas, f)
f.close()

f = open("Personas.pckl", "rb")
personas = pickle.load(f)
f.close()
for p in personas:
    print(p)

f = open("Personas.pckl", "rb")
lista_fichero = pickle.load(fichero)
print(lista_fichero)

# TERMINA CON EL MATERIAL DEL PROFESOR