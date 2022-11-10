# Curso profesional de Python (AEPI): Ejercicios_serialización
# Autor: Pablo Gradolph Oliva
# 23/07/2022

'''
1 - En este ejercicio vamos a trabajar en parejas. Envia al estudiante de tu derecha una
instacia del objeto programador del ejercicio 13 sin enviar la estructura de la clase.
El estudiante receptor tiene que cargar el objeto y comprobar sus métodos. ¿Sois capaces de abrirlos?

Daniel -> Arantxa -> Pablo -> Esther -> Sergio -> Daniel
'''

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# IMPORTACIONES
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

from Ejercicio_Registro_Empleados import Programador
import pickle

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# CÓDIGO
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Creamos el objeto de ejemplo con los atributos: nombre, edad, casado, salario, categoría, líneas de código por hora y
# lenguaje de programación preferido.

programador = Programador("Pablo", 21, True, 1200, "Junior", 300, "Python")

# Creamos el archivo binario y cargamos en él el objeto creado anteriormente.
# Este es el archivo que enviaré a Esther. Puede que ella tenga algún problema por la cantidad de atributos...
fichero_binario = open("Archivo_Objeto", "wb")
pickle.dump(programador, fichero_binario)
fichero_binario.close()

# Comprobamos que se puede leer nuestro propio fichero.
# Este es el código que utilizaré para cargar el archivo recibido de Arantxa, cambiando el nombre del archivo
# por el que ella me pase.
fichero_binario_2 = open("Archivo_Objeto", "rb")
objeto = pickle.load(fichero_binario_2)
print(objeto)
fichero_binario_2.close()

