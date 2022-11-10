# Curso profesional de Python (AEPI): 8_Ejercicios
# Autor: Pablo Gradolph Oliva
# 09/07/2022

# 1 - Realiza un programa que siga las siguientes instrucciones:

'''
· Crea una lita llamada usuarios con los usuarios Marta, David, Elvira, Juan y Marcos.
· Crea otra lista llamada administradores con los administradores Juan y Marta.
· Borra el administrador Juan de la lista de administradores.
· Añade a Marcos como un nuevo administrador, pero no lo borres de la lista de usuarios.
· Muestra todos los usuarios por pantalla de forma dinámica, además debes indicar si cada usuario es administrador o no.
'''

print("USUARIOS Y ADMINISTRADORES:")
print()
usuarios = ["Marta", "David", "Elvira", "Juan", "Marcos"]
administradores = ["Juan", "Marta"]
administradores.remove("Juan")
administradores.append("Marcos")

for usuario in usuarios:
    if usuario in administradores:
        print(f"{usuario} --> Administrador")
    else:
        print(f"{usuario}")
print()
print("FIN DEL PROGRAMA")

# 2 - Durante la planificación de un proyecto se han acordado una lista de tareas. Para cada una de estas tareas se ha
# asignado un orden de prioridad (cuanto menor es el número de orden, más prioridad)
# ¿Eres capaz de crear una estructura del tipo cola con todas las tareas ordenadas, pero sin los números de orden?
# Pista: Para ordenar automáticamente una lista es posible utilizar el método .sort()

from collections import deque
lista_tareas = ["Iniciar programa", "Crear una lista llamada usuarios", "Crear otra lista llamada administradores",
                "Borrar un administrador de la lista de administradores", "Añadir a un nuevo administrador",
                "Mostrar usuarios y administradores por pantalla", "Comprobación de que el programa es correcto",
                "Comprobación del tiempo de ejecución", "Finalizar programa"]
números_orden = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print("IMPRIMIENDO LAS TAREAS EN ORDEN ALFABÉTICO:")
lista_tareas_alfabética = sorted(lista_tareas)
for i in lista_tareas_alfabética:
    print(i)

print()
print("Ordenando las tareas por orden de prioridad: ")
cola_tareas = deque()
for i, j in zip(números_orden, lista_tareas):
    print(i, "-->", j)
    cola_tareas.append(j)

print()
print("Imprimiendo por pantalla la cola ordenada por orden de prioridad sin los números: ")
print(cola_tareas)
print()
print("FIN DEL PROGRAMA")

# 3 - Durante el desarrollo de un pequeño videojuego se te encarga configurar y balancear cada personaje. Partiendo que
# la estadística base es 2, debes cumplir las siguientes condiciones:

'''
· El caballero tiene el doble de vida y defensa que un guerrero.
· El guerrero tiene el doble de ataque y alcance que un caballero.
· El arquero tiene la misma vida y ataque que un guerrero, pero la mitad de su defensa y el doble de su alcance.
· Muestra cómo quedan las propiedades de los tres personajes.
'''

vida_base = 2
defensa_base = 2
ataque_base = 2
alcance_base = 2

# VIDA
vida_guerrero = vida_base
vida_arquero = vida_guerrero
vida_caballero = 2 * vida_guerrero

# DEFENSA
defensa_arquero = defensa_base
defensa_guerrero = 2 * defensa_arquero
defensa_caballero = 2 * defensa_guerrero

# ATAQUE
ataque_caballero = ataque_base
ataque_guerrero = 2 * ataque_caballero
ataque_arquero = ataque_guerrero

# ALCANCE
alcance_caballero = alcance_base
alcance_guerrero = 2 * alcance_caballero
alcance_arquero = 2 * alcance_guerrero

personajes = ("Caballero", "Guerrero", "Arquero")
estadísticas = ["Vida", "Defensa", "Ataque", "Alacance"]
estadísticas_caballero = [vida_caballero, defensa_caballero, ataque_caballero, alcance_caballero]
estadísticas_guerrero = [vida_guerrero, defensa_guerrero, ataque_guerrero, alcance_guerrero]
estadísticas_arquero = [vida_arquero, defensa_arquero, ataque_arquero, alcance_arquero]

diccionario_caballero = {}
for key, value in zip(estadísticas, estadísticas_caballero):
    diccionario_caballero[key] = value

diccionario_guerrero = {}
for key, value in zip(estadísticas, estadísticas_guerrero):
    diccionario_guerrero[key] = value

diccionario_arquero = {}
for key, value in zip(estadísticas, estadísticas_arquero):
    diccionario_arquero[key] = value

lista_diccionarios = [diccionario_caballero, diccionario_guerrero, diccionario_arquero]
diccionario_propiedades = {}
for key, value in zip(personajes, lista_diccionarios):
    diccionario_propiedades[key] = value

key_list = list(diccionario_propiedades.keys())
values_list = list(diccionario_propiedades.values())

print("IMPRIMIENDO LAS ESTADÍSTICAS FINALES DE LOS PERSONAJES:")
for key, value in zip(key_list, values_list):
    print(key, "-->", value)

print()
print("FIN DEL PROGRAMA")