# Curso profesional de Python (AEPI): Ejercicios archivos json
# Autor: Pablo Gradolph Oliva
# 23/07/2022

'''
Para este ejercicio vamos a disponer de dos archivos json (datos.json y
datosactualizar.json), los cuales serán suministrados con este ejercicio (en el zip enviado con el correo), además tendremos
que crear una base de datos sqlite llamada personas, con una tabla llamada datos, la
cual contendrá dos campos, uno id de tipo integer y auto incremental y otro persona de
tipo texto.

Debemos crear una clase llamada BaseDatos, la cual contendrá los siguientes métodos:

• def insertar(self, persona): Cada vez que llamemos a este método debe insertar
en la base de datos el contenido del archivo datos.json

• def visualizarPersona(self, id): Debe mostrar por consola el registro de la base de
datos que coincida con el id pasado como argumento.

• def eliminar(self, id): Debe eliminar el registro de la base de datos que coincida
con el id pasado como argumento.

• def actualizar(self, id, persona): Debe actualizar el registro de la base de datos
que coincida con el id pasado como argumento junto con los datos del archivo
datosactualizar.json

Debemos crear además cuatro funciones fuera de la clase que implementen los
métodos de la clase:

• def guardarBD():

• def leerBD():

• def eliminarPersona():

• def actualizarPersona():
'''

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# IMPORTACIONES
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

import json
from peewee import *


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# CLASES
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Clase principal que trabaja sobre la base de datos.
class BaseDatos:
    # No tiene atributos específicos.
    pass

    # Método para limpiar los datos de la base de datos.
    def limpiar_base_datos(self):
        limpio = Datos.delete().where(Datos.id > 0)
        limpio.execute()

    # Método para insertar los datos de las personas en la base de datos.
    def insertar(self, persona, apellido, edad, DNI):
        objeto = Datos(persona=persona, apellido=apellido, edad=edad, DNI=DNI)
        objeto.save()

    # Método para ver los datos de una persona en función de su id.
    def visualizarPersona(self, id):
        res = Datos.select().where(Datos.id == id)
        if res.exists():
            obj = Datos.get(Datos.id == id)
            return obj
        else:
            return None

    # Método para eliminar los datos de una persona en función de su id.
    def eliminar(self, id):
        res = Datos.select().where(Datos.id == id)
        if res.exists():
            obj = Datos.get(Datos.id == id)
            obj.delete_instance()
            return 0
        else:
            return None

    # Método para actualizar el nombre de una persona en función de su id.
    def actualizar(self, id, nombre):
        res = Datos.select().where(Datos.id == id)
        if res.exists():
            obj = Datos.get(Datos.id == id)
            obj.persona = nombre
            obj.save()
            return 0
        else:
            return None

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# FUNCIONES
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Función para guardar los datos del archivo "datos.json" en la BDD.
def guardar_BD():

    # Limpiamos la base de datos para que no se sigan agregando los mismos datos
    limpiar = BaseDatos()
    limpiar.limpiar_base_datos()

    # Leemos y bajamos los datos del archivo json
    lista_datos = []
    with open("datos.json") as file:
        diccionario = json.load(file)
        for key, value in diccionario.items():
            for i in value.items():
                lista_datos.append(i[1])

    # Guardamos los datos de las tres personas
    persona1 = lista_datos[0]
    persona2 = lista_datos[1]
    persona3 = lista_datos[2]

    nombre1 = persona1[0]
    apellido1 = persona1[1]
    edad1 = persona1[2]
    DNI1 = persona1[3]

    nombre2 = persona2[0]
    apellido2 = persona2[1]
    edad2 = persona2[2]
    DNI2 = persona2[3]

    nombre3 = persona3[0]
    apellido3 = persona3[1]
    edad3 = persona3[2]
    DNI3 = persona3[3]

    # Insertamos los datos en la base de datos
    persona1 = BaseDatos()
    persona2 = BaseDatos()
    persona3 = BaseDatos()
    persona1.insertar(nombre1, apellido1, edad1, DNI1)
    persona2.insertar(nombre2, apellido2, edad2, DNI2)
    persona3.insertar(nombre3, apellido3, edad3, DNI3)

# Función para leer los datos de una persona de la BDD
def leer_BD(id):

    # Leemos los datos de la persona en función del id pasado.
    objeto = BaseDatos()
    persona_pedida = objeto.visualizarPersona(id)
    if persona_pedida is not None:
        print(f"Nombre: {persona_pedida.persona} "
                f"\nApellido: {persona_pedida.apellido} "
                f"\nEdad: {persona_pedida.edad} \nDNI: {persona_pedida.DNI}")
    else:
        print("El id introducido no existe en la base de datos, inténtelo de nuevo.")

# Función para eliminar una persona de la BDD.
def eliminar_persona(id):

    # Eliminamos a la persona en función del id pasado.
    objeto = BaseDatos()
    persona_eliminada = objeto.eliminar(id)
    if persona_eliminada is not None:
        print(f"Persona con id = {id}, eliminada de la base de datos.")
    else:
        print("El id introducido no existe en la base de datos, inténtelo de nuevo.")

# Función para actualizar una persona de la BDD.
def actualizar_persona(id):

    # Leemos y bajamos los datos del archivo json
    lista_datos = []
    with open("datosactualizar.json") as file:
        diccionario = json.load(file)
        for key, value in diccionario.items():
            for i in value.items():
                lista_datos.append(i[1])

    # En función del id pasado, guardamos persona como una lista con los datos que nos interesan.
    if id == 1:
        persona = lista_datos[0]
    elif id == 2:
        persona = lista_datos[1]
    else:
        persona = lista_datos[2]

    # Solo cambia el nombre de la persona, sino haríamos lo mismo con el apellido, la edad y el DNI.
    nombre = persona[0]

    # Actualizamos.
    objeto = BaseDatos()
    persona_actualizar = objeto.actualizar(id, nombre)
    if persona_actualizar is not None:
        print("Persona acutalizada con éxito.")
    else:
        print("El id introducido no existe en la base de datos, inténtelo de nuevo.")

# Función principal del programa.
def funcionamiento_programa():

    # Bucle while para poder hacer más de una cosa durante el programa.
    while True:
        print("---CONTROL BASE DE DATOS---")
        print("1 - Insertar los datos del archivo 'datos.json' en la base de datos.")
        print("2 - Visualizar los datos de una persona a través de su id.")
        print("3 - Eliminar los datos de una persona a través de su id.")
        print("4 - Actualizar los datos de una persona con los datos del archivo 'datosactualizar.json'")
        print("Presione cualquier otra tecla para finalizar el programa.")
        print()

        # Pedimos la opción.
        opcion = input("Introduzca la opción que desea realizar: ")

        # Gestión de errores.
        try:

            # Cargar los datos de "datos.json" en la base de datos.
            if opcion == "1":

                guardar_BD()
                print("Datos cargados correctamente en la base de datos.")
                print()

            # Leer los datos de una persona en función de su id.
            elif opcion == "2":

                id = int(input("Inserte el id de la persona: "))
                print()
                leer_BD(id)
                print()

            # Eliminar los datos de una persona en función de su id.
            elif opcion == "3":

                id = int(input("Inserte el id de la persona: "))
                print()
                eliminar_persona(id)
                print()

            # Actualizar el nombre de una persona en función de su id con la información de "datosactualizar.json".
            elif opcion == "4":

                id = int(input("Inserte el id de la persona: "))
                print()
                actualizar_persona(id)
                print()

            # Se finaliza el programa.
            else:

                print()
                print("FIN DEL PROGRAMA")
                break

        except ValueError as error:
            print(f"Se está produciendo el siguiente error:\n{error}\nVuelva a intentarlo.")

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# EJECUTAMOS
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Creamos la base de datos, nos conectamos y creamos la tabla que se nos pide.
db = SqliteDatabase('personas.db')


# Clase para crear la tabla "Datos".
class Datos(Model):
    id = AutoField()
    persona = CharField()
    apellido = CharField()
    edad = CharField()
    DNI = CharField()

    class Meta:
        database = db

# Conectamos con la base de datos y creamos la tabla "Datos".
db.connect()
db.create_tables([Datos])

# Función principal del programa.
funcionamiento_programa()




