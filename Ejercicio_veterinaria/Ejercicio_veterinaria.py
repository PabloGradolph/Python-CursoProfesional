# Curso profesional de Python (AEPI): Ejercicio_veterianaria BDD
# Autor: Pablo Gradolph Oliva
# 11/08/2022

'''
EJERCICIO CONSULTA VETERINARIA

El programa debe contar con un menú de usuario con las siguientes opciones:
1. Dar de alta un animal
2. Actualizar un animal
3. Eliminar un animal
4. Visualizar animal por nombre
5. Visualizar todos los animales
6. Salir

Opción 1: Si el usuario elige dar de alta un animal, el programa debe solicitar
por consola los siguientes datos: nombre, tipo, sexo, peso, teléfono_dueño y
guardar la información en la base de datos.

Opción 2: Si el usuario elige actualizar un animal, el programa debe solicitar por
consola el teléfono del dueño y cambiar el peso.

Opción 3: Si el usuario elige eliminar un animal, el programa debe solicitar por
consola el teléfono del dueño y eliminar ese registro.

Opción 4: Si el usuario elige visualizar animal por nombre, el programa debe
solicitar el nombre del animal y se mostrarán por consola todos los animales que
coincidan con ese nombre.

Opción 5: Si el usuario elige visualizar todos los animales, se mostrarán todos
los animales de la base de datos.

Opción 6: Salimos del programa.
Para este ejercicio vamos a crear una agenda para una consulta veterinaria en
python con una base de datos. La base de datos se llamará clínica y la tabla
se llamará animales.
'''

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# IMPORTACIONES
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
from peewee import *


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# CREAMOS LA BDD
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Creamos la base de datos Sqlite
db = SqliteDatabase('clínica.db')

# Creamos la clase que servirá como tabla en nuestra base de datos.
class Animales(Model):
    # Atributos de los animales
    id = AutoField()
    nombre = CharField()
    tipo = CharField()
    sexo = CharField()
    pesoKg = IntegerField()
    telefono_dueño = IntegerField()

    class Meta:
        database = db

# Nos conectamos a la base de datos y creamos la tabla 'Animales'.
db.connect()
db.create_tables([Animales])

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# FUNCIONES
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Función para ingresar los datos de un animal en la BDD
def dar_de_alta_animal():

    print()
    print("---DAR DE ALTA UN ANIMAL---")

    # Gestión de errores
    try:

        # Pedimos los datos
        nombre = input("Ingrese el nombre del animal: ")
        tipo = input("Ingrese el tipo de animal que es: ")
        sexo = input("Ingrese su sexo, Male/Female: ")

        # Gestionamos que el sexo introducido sea correcto.
        if sexo == "Male" or sexo == "male" or sexo == "Female" or sexo == "female":

            peso = int(input("Ingrese el peso del animal en kg: "))
            telefono_dueño = int(input("Ingrese el número de teléfono del dueño: "))
            animal = Animales.select().where(Animales.telefono_dueño == telefono_dueño)

            # Si ya existe un animal asociado a el número de teléfono introducido, comprobamos que no coincida el nombre
            if animal.exists():
                esta = False
                for i in Animales.select().where(Animales.telefono_dueño == telefono_dueño):
                    if i.nombre == nombre:
                        esta = True
                        print("Lo sentimos. No puede ingresar en la Base de Datos dos animales asociados al mismo "
                              "número de teléfono con el mismo nombre.")

                # Si no coincide el nombre, podemos crear el objeto.
                if esta == False:
                    objeto = Animales(nombre=nombre, tipo=tipo, sexo=sexo, pesoKg=peso, telefono_dueño=telefono_dueño)
                    objeto.save()
                    print("Datos introducidos correctamente, el animal ha sido dado de alta en la base de datos.")
                    print()

            # Si no existe ningún animal asociado a ese número de teléfono también podemos crear el objeto.
            else:
                objeto = Animales(nombre=nombre, tipo=tipo, sexo=sexo, pesoKg=peso, telefono_dueño=telefono_dueño)
                objeto.save()
                print("Datos introducidos correctamente, el animal ha sido dado de alta en la base de datos.")
                print()

        else:
            print("Lo siento, no se ha reconocido su respuesta en cuanto al sexo del animal. Inténtelo de nuevo.")
            print()
            dar_de_alta_animal()

    except ValueError as error:
        print()
        print(f"Se está produciendo el siguiente error:\n{error}\nPor favor, inténtelo de nuevo.")

# Función para actualizar el peso de un animal en la BDD
def actualizar_animal():

    print()
    print("---ACTUALIZAR EL PESO DE UN ANIMAL---")

    # Gestión de errores
    try:

        # Pedimos el número de teléfono del dueño
        telefono_dueño = int(input("Ingrese el número de teléfono del dueño: "))
        print()
        animal = Animales.select().where(Animales.telefono_dueño == telefono_dueño)

        # Si existe algún animal asociado al número de teléfono, imprimimos todos los que haya
        if animal.exists():
            print("Estos son todos los animales asociados a ese número de teléfono:")
            for i in Animales.select().where(Animales.telefono_dueño == telefono_dueño):
                print(f"{i.nombre}")

            # Le hacemos escoger el animal al que desea cambiar el peso.
            print()
            nombre = input("Ingrese el nombre del animal al que quiere actualizar el peso: ")
            animal = Animales.select().where(Animales.nombre == nombre)

            # Si el nombre es válido pedimos el nuevo peso y lo cambiamos.
            if animal.exists():
                animal = Animales.get(Animales.telefono_dueño == telefono_dueño and Animales.nombre == nombre)
                print()
                print(f"El animal seleccionado es: {animal.nombre}.")
                print(f"Es un/a {animal.tipo} que actualmente pesa {animal.pesoKg} Kg.")

                nuevo_peso = int(input("Ingrese el nuevo peso del animal: "))
                animal.pesoKg = nuevo_peso
                animal.save()
                print("El peso del animal ha sido actualizado correctamente.")

            # Esto ocurre si el nombre introducido no es válido
            else:
                print("Nombre introducido incorrectamente. Inténtelo de nuevo.")

        # Esto ocurre si no se encuentra ningún animal asociado al número de teléfono introducido.
        else:
            print("No se encuentra ningún animal asociado a ese número de teléfono en la Base de Datos.")

    except ValueError as error:
        print()
        print(f"Se está produciendo el siguiente error:\n{error}\nPor favor, inténtelo de nuevo.")

# Función para eliminar animales de la BDD
def eliminar_animal():

    print()
    print("---ELIMINAR LOS DATOS DE UN ANIMAL---")

    # Gestión de errores
    try:

        # Pedimos el número de teléfono del dueño del animal.
        telefono_dueño = int(input("Ingrese el número de teléfono del dueño: "))
        print()
        animal = Animales.select().where(Animales.telefono_dueño == telefono_dueño)

        # Si existe algún animal cuyo dueño tenga ese número de teléfono, imprimimos todos los que haya por pantalla
        if animal.exists():
            print("Estos son todos los animales asociados a ese número de teléfono:")
            for i in Animales.select().where(Animales.telefono_dueño == telefono_dueño):
                print(f"{i.nombre}")

            # Le hacemos esoger al usuario entre borrar todos los animales asociados a dicho número de teléfono o no
            print()
            opcion = input("¿Desea eliminar todos los animales asociados a este número de teléfono? Si/No: ")

            # Si la opción es si, se borran todos.
            if opcion == "Si" or opcion == "SI" or opcion == "si":

                for i in Animales.select().where(Animales.telefono_dueño == telefono_dueño):
                    Animales.delete().where(Animales.telefono_dueño == telefono_dueño).execute()
                print("Animales eliminados de la Base de Datos.")

            # Si la opción es no, se le hace escoger cuál borrar.
            elif opcion == "No" or opcion == "NO" or opcion == "no":

                print()
                nombre = input("Ingrese el nombre del animal al que quiere eliminar: ")
                animal = Animales.select().where(Animales.nombre == nombre)

                # Si escoge uno válido se borra
                if animal.exists():
                    animal = Animales.get(Animales.telefono_dueño == telefono_dueño and Animales.nombre == nombre)
                    print(f"{animal.nombre} eliminado de la Base de Datos")
                    animal.delete_instance()

                # Sino se imprime esto por pantalla.
                else:
                    print("Nombre introducido incorrectamente. Inténtelo de nuevo.")

            # Esto ocurre si la opción no es ni si ni no.
            else:
                print("Opción introducida incorrectamente. Inténtelo de nuevo.")

        # Esto ocurre si no se encuentran animales en la BDD asociados al número de teléfono introducido.
        else:
            print("No se encuentra ningún animal asociado a ese número de teléfono en la Base de Datos.")

    except ValueError as error:
        print()
        print(f"Se está produciendo el siguiente error:\n{error}\nPor favor, inténtelo de nuevo.")

# Función para ver todos los animales que hay en la base de datos en función del nombre.
def ver_animal_por_nombre():

    print()
    print("---VER LOS DATOS DE UN ANIMAL---")

    # Se pide el nombre del animal
    nombre = input("Ingrese el nombre del animal que desea visualizar: ")
    print()
    animal = Animales.select().where(Animales.nombre == nombre)

    # Si existe alguno con ese nombre se imprimirán todos por pantalla.
    if animal.exists():
        print("Imprimiendo por pantalla todos los animales con ese nombre:")
        for i in Animales.select().where(Animales.nombre == nombre):
            print(f"Nombre: {i.nombre} - Tipo: {i.tipo} - Sexo: {i.sexo} - Peso: {i.pesoKg} Kg - Teléfono del dueño: "
                  f"{i.telefono_dueño}")

    # Si no, decimos que el nombre introducido no está en la BDD
    else:
        print(f"No existen animales llamados {nombre} en la Base de Datos.")

# Función para ver todo el contenido de la base de datos.
def ver_BDD():

    print()
    print("---IMPRIMIENDO LOS ANIMALES DE LA BASE DE DATOS---")
    animal = Animales.select()

    # Gestionamos si la BDD está vacía o no.
    if animal.exists():
        # Recorremos toda la BDD imprimiendo los datos.
        for i in Animales.select():
            print(f"Nombre: {i.nombre} - Tipo: {i.tipo} - Sexo: {i.sexo} - Peso: {i.pesoKg} Kg - Teléfono del dueño: "
                  f"{i.telefono_dueño}")
        print("---FIN DE LA LISTA---")

    # Esto ocurre si la BDD está vacía.
    else:
        print("La Base de Datos está vacía.")

def funcionamiento():

    # Bucle while para poder hacer más de una acción antes de finalizar el programa
    while True:
        print()
        print("---CLÍNICA VETERINARIA---")
        print("1 - Dar de alta un animal.")
        print("2 - Actualizar el peso de un animal.")
        print("3 - Eliminar los datos de un animal")
        print("4 - Ver los animales con un mismo nombre.")
        print("5 - Ver todos los animales de la Base de Datos.")
        print("6 - Finalizar el programa.")
        print()

        # Pedimos una de las opciones.
        opcion = input("Seleccione una de las opciones mostradas: ")

        # Dar de alta un animal.
        if opcion == "1":

            dar_de_alta_animal()

        # Actualizar el peso de un animal.
        elif opcion == "2":

            actualizar_animal()

        # Eliminar los datos de algún animal.
        elif opcion == "3":

            eliminar_animal()

        # Ver los animales con un cierto nombre.
        elif opcion == "4":

            ver_animal_por_nombre()

        # Ver todo el contenido de la Base de Datos.
        elif opcion == "5":

            ver_BDD()

        # Finalizar el programa.
        elif opcion == "6":

            print()
            print("FIN DEL PROGRAMA")
            break

        # Opción no válida.
        else:
            print("Opción no reconocida. Inténtelo de nuevo.")

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# EJECUTAMOS
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

funcionamiento()
