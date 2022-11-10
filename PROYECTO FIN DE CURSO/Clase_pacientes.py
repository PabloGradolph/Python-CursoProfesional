# Archivo .py con la clase Pacientes.

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# IMPORTACIONES
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

from peewee import *
from datetime import *
import pytz


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# BASE DE DATOS
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Creamos la base de datos 'clínica', nos conectamos y creamos la tabla 'pacientes'.
db = SqliteDatabase('clínica.db')

class pacientes(Model):
    id = AutoField()
    nombre = CharField()
    apellidos = CharField()
    DNI = CharField()
    telefono = CharField()
    direccion = CharField()
    observaciones = CharField()

    class Meta:
        database = db

# Clase principal que trabaja sobre la base de datos.
class Pacientes:
    # No tiene atributos específicos.
    pass

    # Método para conectar con la Base de Datos.
    def conectar(self, db):
        db.connect()

    # Método para crear las tablas de la Base de Datos.
    def crear_tabla(self, db):
        db.create_tables([pacientes])

    # Método para insertar un paciente en la Base de Datos.
    def insertar(self, nombre, apellidos, DNI, telefono, direccion, observaciones):
        paciente = pacientes(nombre=nombre, apellidos=apellidos, DNI=DNI, telefono=telefono, direccion=direccion,
                             observaciones=observaciones)
        paciente.save()

    # Método para visualizar el contenido de la Base de Datos.
    # Está vacío puesto que esto lo he trabajado a través de una función.
    def visualizar_todo(self):
        pass

    # Método para visualizar los datos de un paciente a través de un id pasado como argumento.
    def visualizar_por_ID(self, id):
        obj = pacientes.select().where(pacientes.id == id)
        if obj.exists():
            paciente = pacientes.get(pacientes.id == id)
            return paciente
        else:
            return None

    # Método para visualizar los datos de un paciente a través de un nombre pasado como argumento.
    def visualizar_por_nombre(self, nombre):
        obj = pacientes.select().where(pacientes.nombre == nombre)
        if obj.exists():
            for i in pacientes.select().where(pacientes.nombre == nombre):
                print(f"Nombre: {i.nombre} - Apellidos: {i.apellidos} - DNI: {i.DNI} - Teléfono: {i.telefono} - "
                      f"Dirección: {i.direccion} - Observaciones: {i.observaciones}")
        else:
            print("El nombre del paciente no se encuentra en la Base de Datos.")

    # Método para eliminar el registro de uno de los pacientes a través de su id.
    def eliminar_registro(self, id):
        obj = pacientes.select().where(pacientes.id == id)
        if obj.exists():
            paciente = pacientes.get(pacientes.id == id)
            paciente.delete_instance()
            print(f"Paciente con id: {id}, eliminado de la Base de Datos.")
        else:
            print(f"No existe paciente en la Base de Datos con id: {id}.")

    # Método para actualizar el teléfono de un paciente a través de su id.
    def actualizar_registro(self, id, telefono):
        obj = pacientes.select().where(pacientes.id == id)
        if obj.exists():
            paciente = pacientes.get(pacientes.id == id)
            paciente.telefono = telefono
            paciente.save()
            print(f"Teléfono de {paciente.nombre}, con id: {id}, actualizado con éxito.")
        else:
            print(f"No existe paciente en la Base de Datos con id: {id}.")

    # Método para cerrar la conexión con la Base de Datos.
    def cerrar_conexion(self, db):
        db.close()

    # Método para insertar el texto correspondiente en el archivo txt de Registros Correctos.
    # Cuando el archivo llega a 10 líneas se borra la primera línea y se escribe en la última.
    # Por lo tanto, son los 10 últimos registros correctos los que imprime.
    def insertar_texto_aciertos(self):
        subq = pacientes.select(fn.MAX(pacientes.id)).scalar()
        nombre = pacientes.get(pacientes.id == subq).nombre
        apellidos = pacientes.get(pacientes.id == subq).apellidos
        DNI = pacientes.get(pacientes.id == subq).DNI
        tz = pytz.timezone('Europe/Madrid')
        lineas = []

        with open("Registros Correctos.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()

        texto = f"El registro con nombre: {nombre} {apellidos} y DNI: {DNI} se ha insertado correctamente el" \
                f" día {str(datetime.now(tz=tz).strftime('%Y-%m-%d %H:%M:%S'))}"

        for linea in lines:
            lineas.append(linea.strip("\n"))

        if len(lineas) < 10:
            with open("Registros correctos.txt", "a", encoding="utf-8") as f:
                f.write(f"{texto}\n")
        else:
            lineas.pop(0)
            f = open("Registros correctos.txt", "w", encoding="utf-8")
            f.close()

            with open("Registros Correctos.txt", "a", encoding="utf-8") as f:
                for line in lineas:
                    f.write(f"{line}\n")
                f.write(f"{texto}\n")

    # Método para insertar el texto correspondiente en archivo txt de Registros Erróneos.
    # Cuando el archivo llega a 10 líneas se borra la primera línea y se escribe en la última.
    # Por lo tanto, son los 10 últimos registros correctos los que imprime.
    def insertar_texto_errores(self, texto):
        lineas = []

        with open("Registros Erróneos.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()

        for linea in lines:
            lineas.append(linea.strip("\n"))

        if len(lineas) < 10:
            with open("Registros Erróneos.txt", "a", encoding="utf-8") as f:
                f.write(f"{texto}\n")
        else:
            lineas.pop(0)
            f = open("Registros Erróneos.txt", "w", encoding="utf-8")
            f.close()

            with open("Registros Erróneos.txt", "a", encoding="utf-8") as f:
                for line in lineas:
                    f.write(f"{line}\n")
                f.write(f"{texto}\n")


