# Curso profesional de Python (AEPI): PROYECTO FIN DE CURSO
# Autor: Pablo Gradolph Oliva
# 16/08/2022

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# IMPORTACIONES
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

from peewee import *
from Tarea_asíncrona import LeerFicherosAciertos, LeerFicherosErrores
from Clase_pacientes import Pacientes
from Funciones_proyecto import *
import time
import os
import sys


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# FUNCIÓN PRINCIPAL
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def funcionamiento():

    # Llamando a este comando se borrará la pantalla. Si no funciona, puede ser por dos opciones:
    # 1 --> Su sistema operativo es distinto y habría que usar "clear" en vez de "cls".
    # 2 --> Si tiene Windows y no funciona vaya a "Run/Debug Configuration" y haga click en
    # "Emulate terminal in output console".
    cls = lambda: os.system("cls")

    # Creamos la base de datos 'clínica', nos conectamos y creamos la tabla 'pacientes'.
    db = SqliteDatabase('clínica.db')

    # La conexión y la creación de la tabla están gestionadas desde la clase 'Pacientes'.
    clinica = Pacientes()
    clinica.conectar(db)
    clinica.crear_tabla(db)

    # Creamos los hilos secundarios para ver el contenido de los archivos.
    Hilo_aciertos = LeerFicherosAciertos()
    Hilo_errores = LeerFicherosErrores()

    # Los asociamos a un subrpoceso de Daemon para poder cerrarlos al finalizar el programa.
    Hilo_aciertos.daemon = True
    Hilo_errores.daemon = True

    # Creamos/Abrimos los archivos que utilizaremos de antemano para que no se produzca ningún error del tipo:
    # No se encuentra el archivo buscado (Sobretodo en los hilos).
    f = open("Registros Correctos.txt", "a")
    f.close()
    f = open("Registros Erróneos.txt", "a")
    f.close()

    # Bucle while para poder realizar muchas tareas antes de cerrar el programa.
    while True:
        # Si no están funcionando, empezamos los hilos que mostrarán el contenido de los archivos.
        # Se solaparán, esto podría cambiarse inicializando uno de los hilos en otro momento. Pero en este caso no es un
        # Problema.
        if Hilo_errores.is_alive() == False:
            Hilo_errores.start()
        if Hilo_aciertos.is_alive() == False:
            Hilo_aciertos.start()

        # Imprimimos el menú principal
        time.sleep(0.5)
        cls() # Nos aseguramos de que la consola esté limpia.
        print("----MENÚ PRINCIPAL----")
        print("1 - Insertar un paciente.")
        print("2 - Actualizar teléfono de un paciente.")
        print("3 - Eliminar un paciente.")
        print("4 - Visualizar un paciente por nombre.")
        print("5 - Visualizar un paciente por id.")
        print("6 - Visualizar todos los pacientes.")
        print("7 - Visualizar log de aciertos.")
        print("8 - Visualizar log de errores.")
        print("9 - Finalizar el programa.")
        print()

        # Pedimos al usuario la acción que desea realizar.
        opcion = input("Introduzca la opción que desea realizar: ")

        # Se limpia de nuevo la consola, ya que así cada función se ejecutará con la consola limpia.
        cls()

        # Insertar un paciente
        if opcion == "1":

            insertar_paciente()
            print()
            input("Pulse cualquier tecla para continuar: ")

        # Actualizar teléfono de un paciente.
        elif opcion == "2":

            actualizar_registro()
            print()
            input("Pulse cualquier tecla para continuar: ")

        # Eliminar un paciente.
        elif opcion == "3":

            eliminar_registro()
            print()
            input("Pulse cualquier tecla para continuar: ")

        # Visualizar un paciente por nombre.
        elif opcion == "4":

            visualizarNombre()
            print()
            input("Pulse cualquier tecla para continuar: ")

        # Visualizar un paciente por id.
        elif opcion == "5":

            visualizarID()
            print()
            input("Pulse cualquier tecla para continuar: ")

        # Visualizar todos los pacientes.
        elif opcion == "6":

            ver_BDD()
            print()
            input("Pulse cualquier tecla para continuar: ")

        # Visualizar log de aciertos.
        elif opcion == "7":

            leer_aciertos()
            print()
            input("Pulse cualquier tecla para continuar: ")

        # Visualizar log de errores.
        elif opcion == "8":

            leer_errores()
            print()
            input("Pulse cualquier tecla para continuar: ")

        # Finalizar el programa
        elif opcion == "9":

            print("FIN DEL PROGRAMA")
            # Cerramos la conexión con la BDD y cerramos también los hilos.
            clinica.cerrar_conexion(db)
            sys.exit()
            break

        else:
            print("Opción no reconocida, por favor, inténtelo de nuevo.")


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# EJECUTAMOS LA FUNCIÓN PRINCIPAL
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

funcionamiento()


