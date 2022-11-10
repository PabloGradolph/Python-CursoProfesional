# Curso profesional de Python (AEPI): Ejercicios de ficheros de texto
# Autor: Pablo Gradolph Oliva
# 23/07/2022

'''
1 - Escribe un programa de Python para leer un archivo de texto completo usando una función.
'''


def leer_archivo_texto():

    # Utilizo el encoding para poder leer acentos y ñ
    with open("Archivo_lectura.txt", "r", encoding="utf-8") as f:
        texto = f.read()
        print(texto)

leer_archivo_texto()


'''
2 - Escribe un programa de Python para leer las primeras líneas de un archivo. Para
hacer este ejercicio debemos importar la librería islice “from itertools import islice” he
investigar su funcionamiento.
'''

from itertools import islice

def leer_dos_primeras_lineas_archivo():

    with open("Archivo_lectura.txt", "r", encoding="utf-8") as f:
        for linea in islice(f, 2):
            print(linea)

leer_dos_primeras_lineas_archivo()

'''
3 - Escribe un programa de Python para agregar texto a un archivo y mostrar el
contenido.
'''

def escribir_en_archivo():

    with open("Archivo_escritura.txt", "a", encoding="utf-8") as f:
        texto = input("Introduza lo que desea escribir en el archivo: ")
        f.write(f"{texto}\n")

    print()
    print("Se ha escrito correctamente su información en el archivo.")

def leer_archivo_texto_2():

    print("Imprimiendo por pantalla la información contenida en el archivo:")

    with open("Archivo_escritura.txt", "r", encoding="utf-8") as f:
        texto = f.read()
        print(texto)

escribir_en_archivo()
leer_archivo_texto_2()


'''4 - Escribe un programa Python para leer un archivo línea a línea y guárdalo en una lista.'''

def leer_archivo_y_guardar_en_lista():

    lineas = []
    with open("Archivo_lectura.txt", "r", encoding="utf-8") as f:
        texto = f.readlines()

    # Eliminamos el carácter \n de cada línea
    for linea in texto:
        lineas.append(linea.strip("\n"))
    print(lineas)

leer_archivo_y_guardar_en_lista()

'''
5 - Escribe un programa de Python para contar el número de líneas en un archivo de
texto.
'''

def contar_lineas_archivo():

    contador = 0
    with open("Archivo_lectura.txt", "r", encoding="utf-8") as f:
        texto = f.readlines()

    for i in texto:
        contador += 1

    print(f"El número de líneas del archivo es: {contador}")

contar_lineas_archivo()

'''
6 - Escribe un programa de Python para obtener el tamaño del archivo de texto.
'''

import os

directorio_actual = os.getcwd()
nombre_objetivo = "Archivo_lectura.txt" # Hemos creado este archivo para que lo encuentre posteriormente

for raiz, dirs, archivos in os.walk(directorio_actual):

    if nombre_objetivo in archivos:
        buscado = raiz

ruta_completa = os.path.join(buscado, nombre_objetivo)

file_size = os.path.getsize(ruta_completa)
print(f"El tamaño del archivo '{nombre_objetivo}' es: {file_size} bytes")

'''
7 - Escribe un programa de Python para escribir la siguiente lista en un archivo de texto:
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
'''

def escribir_lista_en_archivo():

    color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
    color_texto = str(color)
    # También podríamos hacer un bucle y escribir el contenido de la lista por líneas

    with open("Archivo_escritura.txt", "w", encoding="utf-8") as f:
        f.write(color_texto)

escribir_lista_en_archivo()
leer_archivo_texto_2() # Esta función es la del ejercicio 2

'''
8 - Escribe un programa de Python para copiar el contenido de un archivo a otro archivo.
Para ello tendremos que importar from shutil import copyfile e investigar su
funcionamiento.
'''

from shutil import copyfile

def copiar_archivo():

    # Este directorio solo funciona en mi ordenador, habría que cambiar la ruta en otro
    path = "C:\\Users\\Pablo\\PycharmProjects\\Ejercicios_Archivos"
    print("Directorio antes de copiar el archivo:")
    print(os.listdir(path))

    # Este source lo usaremos para crear "destination" solamente
    source_no_válido = path + "\\Archivo_lectura"

    # Copiando el archivo
    source = path + "\\Archivo_lectura.txt"
    destination = source_no_válido + "(copia)" + ".txt"
    dest = copyfile(source, destination)

    print("Directorio después de copiar el archivo:")
    print(os.listdir(path))

    print("Archivo copiado con éxito")

copiar_archivo()

'''
9- Escribe un programa de Python para evaluar si un archivo está cerrado o no.
'''

def archivo_abierto_cerrado():
    global archivo

    if archivo.closed == True:
        print("El archivo está cerrado")
    else:
        print("El archivo está abierto")

nombre_archivo = input("Introduzca el nombre del archivo sin la extensión: ")
nombre_archivo_completo = nombre_archivo + ".txt"

# Esta es la comprobación en los dos casos (abierto y cerrado)
archivo = open(nombre_archivo_completo, "r", encoding="utf-8")
archivo_abierto_cerrado()
archivo.close()
archivo_abierto_cerrado()

'''
10 - Escribe un programa de Python para leer una línea aleatoria de un archivo.
'''

from random import choice

def leer_linea_aleatoria(archivo):

    try:
        with open(archivo, "r", encoding="utf-8") as f:
            lineas = f.read().splitlines()
            return choice(lineas)

    except FileNotFoundError:
        return None

print("LEYENDO LÍNEA ALEATORIA DEL ARCHIVO:")
nombre_archivo = "Archivo_lectura.txt"
resultado = leer_linea_aleatoria(nombre_archivo)
print(resultado)

'''
11 - Escribe un programa de Python para eliminar el carácter ‘\n’ de cada línea del
fichero test.txt.
'''

def quitar_barra_n():

    lineas = []
    with open("Archivo_lectura.txt", "r", encoding="utf-8") as f:
        texto = f.readlines()

    # Eliminamos el carácter \n de cada línea
    for linea in texto:
        lineas.append(linea.strip("\n"))

    # Escribimos sobre el archivo el contenido de la lista ahora sin "\n"
    with open("Archivo_lectura.txt", "w", encoding="utf-8") as f:
        for linea in lineas:
            f.write(linea)

quitar_barra_n()
leer_archivo_texto() # Función del ejercicio 1
