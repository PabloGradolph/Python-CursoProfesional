# CLASE DEL DÍA 28/07/2022

# En colab "BasesDatos"

import sqlite3


def comprobar_conexion(conexion_db):
    try:
        conexion_db.cursor()
        return True

    except:
        print("la base de datos está cerrada")
        return False

bd = "ejemplo.sqlite"

conexion = sqlite3.connect(bd)
conexion.cursor() # Con esto podemos comprobar si la base de datos está abierta
                  # Nos devuelve un objeto

comprobar_conexion(conexion) # Comprobamos la conexión a la base de datos
type(conexion)

conexion.close()
comprobar_conexion(conexion)

# Aquí está la chicha
conexion = sqlite3.connect(bd)
nombre_tabla = "usuarios"
campo_1 = "nombre"
campo_2 = "apellidos"
campo_3 = "edad"
campo_4 = "ID"

cursor = conexion.cursor()

sentencia_sql_creacion = f'''CREATE TABLE IF NOT EXISTS {nombre_tabla} 
                             ({campo_1} text, {campo_2} text, {campo_3} INT,
                             {campo_4} INTEGER PRIMARY KEY AUTOINCREMENT)'''
                             # Con if not exists gestionamos el error
                             # Podríamos gestionarlo también con try except

cursor.execute(sentencia_sql_creacion) # Estamos creando una tabla

conexion.commit()

sql = f'''INSERT INTO {nombre_tabla} 
          ({campo_1}, {campo_2}, {campo_3})
          VALUES ("Hector", "Barrio", 41)
          '''
          # Secuencia para insertar, ahora la insertamos

cursor.execute(sql)
conexion.commit()
# Para ver los datos que hemos introducido usamos sqlite wiewer

# Otra forma de meter los datos (Con variables)
nombre = "Daniel"
apellido = "García"
edad = 32

sql = f'''INSERT INTO {nombre_tabla} 
          ({campo_1}, {campo_2}, {campo_3})
          VALUES ("{nombre}", "{apellido}", {edad})
          '''

cursor.execute(sql)
conexion.commit()

# Te devuelve la información
conexion.row_factory = sqlite3.Row

cursor_lectura = conexion.cursor()
sql_consulta = f'''SELECT * FROM "{nombre_tabla}"
                '''

cursor_lectura.execute(sql_consulta)

resultados = cursor_lectura.fetchone() # Fechone coje uno solo Fechall coge todo
print(resultados)

resultados.keys()

for columna in resultados.keys():
  print(f"Columna: {columna} -- Valor: {resultados[columna]}")


resultados_2 = cursor_lectura.fetchone() # Si lo volvemos ha hacer coje el siguiente
                                        # Si acabas te devolverá None

for columna in resultados_2.keys():
  print(f"Columna: {columna} -- Valor: {resultados_2[columna]}")


# Recorriendo la base de datos
cursor_lectura.execute(sql_consulta)

while True:
  res = cursor_lectura.fetchone()
  if res is None:
    print("------------FIN DE RESULTADOS---------------")
    break
  for columna in res.keys():
    print(f"Columna: {columna} -- Valor: {res[columna]}")


# Seleccionamos lo que queremos nada más
sql_filtrada = '''SELECT ID, nombre
                FROM "usuarios"
                WHERE nombre = "Hector"
                AND ID = 3'''

cursor_filtrado = conexion.cursor()
cursor_filtrado.execute(sql_filtrada)

while True:
  res = cursor_filtrado.fetchone()
  if res is None:
    print("------------FIN DE RESULTADOS---------------")
    break
  for columna in res.keys():
    print(f"Columna: {columna} -- Valor: {res[columna]}")