# Todas las funciones necesarias para el proyecto

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# IMPORTACIONES
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

from Clase_pacientes import Pacientes, pacientes
import phonenumbers
from datetime import *
from peewee import *
import pytz

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# FUNCIONES DE COMPROBACIÓN
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Función que comprueba que los números introducidos en el DNI son válidos y devuelve el DNI completo con la letra.
def comprobar_DNI(nombre, apellidos):

    INVALIDOS = {"00000000T", "00000001R", "99999999R"}

    while True:
        numero = input("Introduzca únicamente los números de su DNI: ")

        if len(numero) == 8:
            intnumero = int(numero)
            diccionario = {0:"T",1:"R",2:"W",3:"A",4:"G",5:"M",6:"Y",7:"F",8:"P",9:"D",10:"X",
                       11:"B",12:"N",13:"J",14:"Z",15:"S",16:"Q",17:"V",18:"H",19:"L",
                       20:"C",21:"K",22:"E"}
            resto = intnumero%23
            letra = diccionario[resto]
            DNI = numero + letra

            if DNI in INVALIDOS:
                tz = pytz.timezone('Europe/Madrid')
                print("Número de DNI incorrecto, por favor, vuelva a intentarlo.")
                texto = f"El registro con nombre: {nombre} {apellidos} no se ha insertado correctamente debido a " \
                        f"utilizar un DNI no válido: {DNI}." \
                        f"Ocurre el día {str(datetime.now(tz=tz).strftime('%Y-%m-%d %H:%M:%S'))}"
                # Insertamos texto en el archivo Registros Erróneos porque el DNI es uno de los no válidos.
                insertar_error(texto)

            else:
                break

        else:
            tz = pytz.timezone('Europe/Madrid')
            print("Número de DNI incorrecto, debe tener 8 caracteres. Por favor, vuelva a intentarlo.")
            texto = f"El registro con nombre: {nombre} {apellidos} no se ha insertado correctamente debido a insertar " \
                    f"más de 8 números en su DNI. Ocurre el día {str(datetime.now(tz=tz).strftime('%Y-%m-%d %H:%M:%S'))}"
            # Insertamos texto en el archivo Registros Erróneos porque se han introducido más de 8 caracteres al pedir
            # Los números del DNI.
            insertar_error(texto)

    return DNI

# Función que comprueba que los números introducidos en el teléfono son válidos y que se trata de un número español.
def comprobar_telefono(nombre, apellidos):

    while True:
        telefono = input("Inserte el teléfono del paciente: ")
        clave_pais = "+34"
        telefono_completo = clave_pais + telefono
        phone = phonenumbers.parse(telefono_completo, "ES")

        if phonenumbers.is_valid_number(phone) == False:
            tz = pytz.timezone('Europe/Madrid')
            print("Número de teléfono no válido. Por favor, inténtelo de nuevo.")
            texto = f"El registro con nombre: {nombre} {apellidos} no se ha insertado correctamente debido a utilizar " \
                    f"un teléfono no válido: {telefono}. " \
                    f"Ocurre el día {str(datetime.now(tz=tz).strftime('%Y-%m-%d %H:%M:%S'))}"
            # Insertamos texto en el archivo Registros Erróneos porque el número de teléfono no es válido.
            insertar_error(texto)
            continue

        return telefono_completo


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# FUNCIONES RELACIONADAS CON LOS ARCHIVOS TXT
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Función que inserta el texto en Registros Correctos.
def insertar_acierto():

    paciente = Pacientes()
    paciente.insertar_texto_aciertos()

# Función que inserta el texto en Registros Erróneos.
def insertar_error(texto):

    paciente = Pacientes()
    paciente.insertar_texto_errores(texto)

# Función que sirve para leer el archivo Registros Correctos.
def leer_aciertos():

    print("---IMPRIMIENDO POR PANTALLA EL CONTENIDO DEL ARCHIVO ACIERTOS---")
    with open("Registros Correctos.txt", "r", encoding="utf-8") as f:
        texto = f.read()
    print(texto)

# Función que sirve para leer el archivo Registros Erróneos.
def leer_errores():

    print("---IMPRIMIENDO POR PANTALLA EL CONTENIDO DEL ARCHIVO ERRORES---")
    with open("Registros Erróneos.txt", "r", encoding="utf-8") as f:
        texto = f.read()
    print(texto)


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# FUNCIONES RELACIONADAS CON EL FUNCIONAMIENTO DE LA BASE DE DATOS
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Función para insertar un paciente en la Base de Datos.
def insertar_paciente():

    print("---INSERTAR PACIENTE EN LA BASE DE DATOS---")

    # Gestión de errores.
    try:

        # Pedimos nombre y apellidos.
        nombre = input("Inserte el nombre del paciente: ")
        apellidos = input("Inserte los apellidos del paciente: ")

        # Pedimos DNI y gestionamos que sea correcto y si el DNI se encuentra o no en la Base de Datos.
        DNI = comprobar_DNI(nombre, apellidos)
        paciente = pacientes.select().where(pacientes.DNI == DNI)

        if paciente.exists():
            print("El DNI introducido coincide con un registro de la base de datos. Es probable que esté intentando "
                  "introducir por segunda vez a un paciente. Por favor, vuelva a intentarlo.")
            tz = pytz.timezone('Europe/Madrid')
            texto = f"El registro con nombre: {nombre} {apellidos} no se ha insertado correctamente debido a utilizar un DNI" \
                    f" ya existente en la BDD: {DNI}. Ocurre el día {str(datetime.now(tz=tz).strftime('%Y-%m-%d %H:%M:%S'))}"
            # Insertamos texto en el archivo Registros Erróneos porque el DNI ya está en la Base de Datos.
            insertar_error(texto)

        else:

            # Pedimos teléfono y gestionamos que sea correcto.
            telefono = comprobar_telefono(nombre, apellidos)

            # Pedimos la dirección del paciente. Gestionar si la dirección es correcta o no requiere del módulo
            # geocoder. Este módulo requiere pagar para ser utilizado con éxito. Por lo tanto, no comprobaremos si las
            # direcciones son correctas o no.
            direccion = input("Inserte la dirección del paciente: ")

            # Pedimos observaciones del paciente.
            while True:
                tener_observaciones = input("¿Desea introducir alguna observación al paciente? Si/No: ")
                if tener_observaciones == "SI" or tener_observaciones == "Si" or tener_observaciones == "si":
                    print("Introduzca las observaciones del paciente: ")
                    observaciones = input("--> ")
                    break
                elif tener_observaciones == "NO" or tener_observaciones == "No" or tener_observaciones == "no":
                    observaciones = "Sin observaciones"
                    break
                else:
                    print("Opción no válida, por favor, vuelva a intentarlo.")

            # Insertamos al paciente en la Base de Datos cuando sea correcto.
            paciente = Pacientes()
            paciente.insertar(nombre, apellidos, DNI, telefono, direccion, observaciones)
            # Insertamos texto en el archivo Registros Correctos.
            insertar_acierto()
            print("Paciente introducido con éxito en la Base de Datos.")

    except ValueError as error:
        print(f"Se está produciendo el siguiente error:\n{error}\nPor favor, vuelva a intentarlo.")

# Función para actualizar el teléfono de un paciente.
def actualizar_registro():

    print("---ACTUALIZAR EL TELÉFONO DEL PACIENTE PASADO POR ID---")

    # Gestión de errores.
    try:
        id = int(input("Inserte el id del paciente al que quiere actualizar el teléfono: "))
        paciente = Pacientes()
        subq = pacientes.select(fn.MAX(pacientes.id)).scalar()
        nombre = pacientes.get(pacientes.id == subq).nombre
        apellidos = pacientes.get(pacientes.id == subq).apellidos
        telefono_completo = comprobar_telefono(nombre, apellidos)
        paciente.actualizar_registro(id, telefono_completo)

    except ValueError as error:
        print(f"Se está produciendo el siguiente error:\n{error}\nPor favor, vuelva a intentarlo.")

# Función para eliminar el registro de un paciente.
def eliminar_registro():

    print("---ELIMINAR UN PACIENTE POR ID---")

    # Gestión de errores.
    try:
        id = int(input("Inserte el id del paciente que desea eliminar: "))
        paciente = Pacientes()
        paciente.eliminar_registro(id)

    except ValueError as error:
        print(f"Se está produciendo el siguiente error:\n{error}\nPor favor, vuelva a intentarlo.")

# Función para visualizar los datos de un paciente a través de un nombre pasado.
def visualizarNombre():

    print("---VISUALIZAR PACIENTES POR NOMBRE---")

    nombre = input("Introduzca el nombre del paciente: ")
    paciente = Pacientes()
    paciente.visualizar_por_nombre(nombre)

# Función para visualizar los datos de un paciente a través de un id pasado.
def visualizarID():

    print("---VISUALIZAR PACIENTE POR ID---")

    try:
        id = int(input("Inserte el id del paciente que desea visualizar: "))
        paciente = Pacientes()
        paciente = paciente.visualizar_por_ID(id)

        if paciente is not None:
            print(f"Nombre: {paciente.nombre} - Apellidos: {paciente.apellidos} - DNI: {paciente.DNI} - "
                  f"Teléfono: {paciente.telefono} - Dirección: {paciente.direccion} - "
                  f"Observaciones: {paciente.observaciones}")

        else:
            print("El id introducido no existe en la base de datos. Por favor, inténtelo de nuevo.")

    except ValueError as error:
        print(f"Se está produciendo el siguiente error:\n{error}\nPor favor, vuelva a intentarlo.")

# Función para ver los pacientes de la Base de Datos.
def ver_BDD():

    print("---IMPRIMIENDO LOS REGISTROS DE LA BASE DE DATOS---")
    paciente = pacientes.select()

    # Gestionamos si la BDD está vacía o no.
    if paciente.exists():
        # Recorremos toda la BDD imprimiendo los datos.
        for i in pacientes.select():
            print(f"Nombre: {i.nombre} - Apellidos: {i.apellidos} - DNI: {i.DNI} - Teléfono: {i.telefono} - Dirección: "
                  f"{i.direccion} - Observaciones: {i.observaciones}")
        print("---FIN DE LA LISTA---")

    # Esto ocurre si la BDD está vacía.
    else:
        print("La Base de Datos está vacía.")


