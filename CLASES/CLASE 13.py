# CLASE DEL DÍA 01/08/2022
# sqlite3 y ORM con peewee.

# Toda la documentación de sqlite3 en: https://docs.python.org/3/library/sqlite3.html#prepareprotocol-objects

import sqlite3

con = sqlite3.connect("ejemplo.db")
cur = con.cursor()

# Crear una tabla:
cur.execute('''CREATE TABLE acciones
            (fecha TEXT, trans TEXT, accion TEXT, cant REAL, precio REAL)
            ''')

# Insertar una fila de datos:
cur.execute('''INSERT INTO acciones
            VALUES ('2022-08-01', 'COMP', 'TSLA', 100, 2314)
            ''')

con.commit()
con.close()

con = sqlite3.connect("ejemplo.db")
cur = con.cursor()
res = cur.execute('SELECT count(rowid) FROM acciones')
print(res.fetchone())

res = cur.execute("SELECT * FROM 'acciones'")
print(res.fetchone())

# Ahora he consumido todos
print(res.fetchone())

print(type(res))

# En este caso fetchall sería lo mismo que fetchone porque solo tenemos una línea
# Lo mete en una lista
res = cur.execute("SELECT * FROM 'acciones'")
print(res.fetchall())

datos = [('2011-07-25', 'VENT', 'IBM', 1000, 45.0),
         ('2022-06-15', 'COMP', 'MSFT', 1000, 72.0),
         ('2022-07-31', 'VENT', 'IBM', 500, 53.0)
]
cur.executemany('INSERT INTO acciones VALUES  (?, ?, ?, ?, ?)', datos)
con.commit()

for fila in cur.execute('SELECT * FROM acciones'):
  print(fila)

for fila in cur.execute('SELECT * FROM acciones ORDER BY fecha'):
  print(fila)

for fila in cur.execute('SELECT * FROM acciones ORDER BY precio LIMIT 3'):
  print(fila)

accion = 'IBM'
res = cur.execute(f'SELECT * FROM acciones WHERE accion="{accion}"')
for fila in res:
  print(fila)

accion = 'IBM'
res = cur.execute(f'SELECT fecha FROM acciones WHERE accion="{accion}"')
for fila in res:
  print(fila)

accion = 'IBM'
res = cur.execute(f'SELECT accion, fecha FROM acciones WHERE accion="{accion}"')
for fila in res:
  print(fila)

con.close()


# Meter en memoria una base de datos
con = sqlite3.connect(":memory:")
cur = con.cursor()
cur.execute("create table len (nombre, fecha_aparicion)")

'''
[26/7 21:13] Hector Barrio
https://sqlitebrowser.org
DB Browser for SQLite

[26/7 21:15] Hector Barrio
https://sqlzoo.net/wiki/SQL_Tutorial
SQLZOO

DOCUMENTACIÓN DE SQL(lite)
'''

cur.execute("INSERT INTO len VALUES (?, ?)", ('c', 1972))

len_lista = [("Fortran", 1957),
             ("Python", 1991),
             ("Go", 2009),
             ("C++", 1991)]
cur.executemany("INSERT INTO len VALUES (?, ?)", len_lista)

cur.execute("SELECT * FROM len WHERE fecha_aparicion=:año", {"año": 1991})
print(cur.fetchall())

cur.execute("SELECT * FROM len WHERE fecha_aparicion=:año", {"año": 2009})
print(cur.fetchall())


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


# ULTIMA PARTE DE BASE DE DATOS: ORM PEEWEE

# Relacionar objetos de python con elementos que tienes en una base de datos.
# !pip install peewee. Si no lo tienes instalado.

# Toda la documentación del módulo peewee en: http://docs.peewee-orm.com/en/latest/

from peewee import Model, SqliteDatabase, CharField, DateField, ForeignKeyField, BooleanField

db = SqliteDatabase('personas.db')
db.close()


class Persona(Model):
  nombre = CharField()
  cumple = DateField()
  es_familiar = BooleanField()

  class Meta:
    database = db


class Mascota(Model):
  propietario = ForeignKeyField(Persona, backref='mascotas')
  nombre = CharField()
  tipo_animal = CharField()

  class Meta:
    database = db


db.connect()
db.create_tables([Persona, Mascota])
db.close()

from datetime import date
jose = Persona(nombre="Jose", cumple=date(1969, 7, 25), es_familiar=True)
vars(jose)

print(jose.nombre)
print(jose.cumple)

jose.save()

jacinta = Persona.create(nombre="Jacinta", cumple=date(1935, 3, 31), es_familiar=False)
print(jacinta)
print(jose)

daniel = Persona.create(nombre="Daniel", cumple=date(1980, 1, 31), es_familiar=False)
daniel

jacinta.nombre = "Maria Jacinta"
jacinta.save()

obj = Persona.get(Persona.id == 2)

obj.delete_instance()

del obj

mochi = Mascota.create(propietario=jose, nombre = 'Mochi', tipo_animal = 'Gato')
vermu = Mascota.create(propietario=jose, nombre = 'Vermu', tipo_animal = 'Gato')
thor = Mascota.create(propietario=daniel, nombre = 'Thor', tipo_animal = 'Perro')
zeus = Mascota.create(propietario=jose, nombre = 'Zeus', tipo_animal = 'Pajaro')

vermu.delete_instance()

vermu = Mascota.create(propietario=jose, nombre = 'Vermu', tipo_animal = 'Gato')
vermu.propietario = daniel
vermu.save()

res = Persona.select().where(Persona.nombre == "Daniel").get()
print(res)

res = Persona.get(Persona.nombre == "Daniel")
print(res)

for persona in Persona.select():
  print(persona.nombre, persona.cumple)

res = Mascota.select().where(Mascota.tipo_animal == 'Gato')
for mascota in res:
  print(mascota.nombre, mascota.propietario.nombre)

for mascota in Mascota.select().where(Mascota.propietario == 'José').order_by(Mascota.nombre):
  print(mascota.nombre)

for persona in Persona.select().order_by(Persona.cumple.desc()):
  print(persona.nombre, persona.cumple)
# desc or asc el orden

