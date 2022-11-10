# CLASE DEL DÍA 26/07/2022

# SEGUIMOS CON ARCHIVOS
import pandas as pd
import matplotlib.pyplot as plt

archivo = r"C:\Users\Pablo\PycharmProjects\CLASES\ejemplo_pandas.xlsx"

dataframe = pd.read_excel(archivo)
print(dataframe)
dataframe.plot()
plt.show()

# TE FALTAN LOS ARCHIVOS CVS O NSQ


# ARCHIVOS JSON

# Leyendo un fichero JSON
import json
fichero = open("datos.json")
with fichero as file:
    linea = fichero.readline()

    datos = json.loads(linea)
    print(f"El tipo del objeto json es {type(datos)}")
    print(datos["albums"]["titulos"])
    print(datos["albums"]["genero"])

# Escribiendo nuevos datos en el ficher JSON
fichero = open("datos.json", "r")
nuevo_fichero = open("datos.json", "a")
with fichero as src, nuevo_fichero as dest:
    linea = src.readline()
    datos = json.loads(linea)
    for i in range(50):
        datos["albums"]["titulos"].append(f"cancion Apendizada {i}")
    cadena = json.dumps(datos)
    dest.writelines(cadena)

# Creando un nuevo fichero json a partir del anterior
datos["albums"]["titulos"].append("cancion Nueva")
cadena = json.dumps(datos)
print(cadena)
nuevo_fichero = open("nuevo_archivo.json")
nuevo_fichero.close()

# Termina esto pk....


# BASES DE DATOS

# Trabajamos con sql
import sqlite3

conexion = sqlite3.connect("ejemplo.db")

with conexion as conn:
    cursor = conn.cursor()

    # Borrar una tabla si ya existe:
    cursor.execute("DROP TABLE IF EXISTS EMPLEADOS")

    # Crear una tabla:
    sql = '''CREATE TABLE EMPLEADOS(
        NOMBRE CHAR(20) NOT NULL, 
        APELLIDO CHAR(20),
        EDAD INT,
        SALARIO FLOAT)'''

    cursor.execute(sql)
    # Commit cambios
    conn.commit()
    print("--- Tabla creada con éxito ---")
    # Cerrar la conexión
    conn.close()

conn = sqlite3.connect("ejemplo.db")
cursor = conn.cursor()
sentencia_1 = '''INSERT INTO EMPLEADOS(NOMBRE, APELLIDO, EDAD, SALARIO)
                VALUES ("Hector", "Barrio", 41, 0)'''
cursor.execute(sentencia_1)
sentencia_2 = '''INSERT INTO EMPLEADOS(NOMBRE, APELLIDO, EDAD, SALARIO)
                VALUES ("Luis", "Gomez", 33, 110)'''
cursor.execute(sentencia_2)

conn.commit()
conn.close()

# Nuestro porpio gestor de contextos:
conexion = sqlite3.connect("ejemplo.db")

class SQLite():
    def __init__(self, file = "sqlite.db"):
        self.file=file

    def __enter__(self):
        self.conn = sqlite3.connect(self.file)
        self.conn.row_factory = sqlite3.Row
        return self.conn.cursor()

    def __exit__(self, type, value, traceback):
        self.conn.commit()
        self.conn.close()

with SQLite("ejemplo.db") as cur:
    print(f"Version: {cur.execute('SELECT SQLITE_VERSION();').fetchall()[0][0]}")





