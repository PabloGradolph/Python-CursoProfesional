# Curso profesional de Python (AEPI): 9_Ejercicios
# Autor: Pablo Gradolph Oliva
# 06/07/2022

# 1 - Crea una función modificar() que a partir de una lista de números realice las siguientes tareas sin modificar la
# original:

'''
· Borrar los elementos duplicados
· Ordenar la lista de mayor a menor
· Eliminar todos los números impares
· Realizar una suma de todos los números que quedan
· Añadir como primer elemento de la lista la suma realizada
· Devolver la lista modificada
'''

# Finalmente, después de ejecutar la función, comprueba que la suma de todos los números a partir del segundo, concuerda
# con el primer número de la lista, tal que así:
# nueva_lista = modificar(lista) print(nueva_lista[0] == sum(nueva_lista[1:]))

def modificar():
    global nueva_lista
    nueva_lista = []

    for i in lista_numeros:
        if i not in nueva_lista:
            nueva_lista.append(i)

    nueva_lista = sorted(nueva_lista, reverse=True)

    for i in nueva_lista:
        if i % 2 != 0:
            nueva_lista.remove(i)
    suma = sum(nueva_lista)
    nueva_lista.insert(0, suma)

print("MODIFICANDO LISTA DE NÚMEROS DE LA SIGUIENTE FORMA:")
print('''
· Borrar los elementos duplicados
· Ordenar la lista de mayor a menor
· Eliminar todos los números impares
· Realizar una suma de todos los números que quedan
· Añadir como primer elemento de la lista la suma realizada
· Devolver la lista modificada
''')
lista_numeros = [9, 8, 7, 9, 8, 5, 5, 6, 3, 4, 1, 1, 2, 10]
modificar()
print(f"De la lista: \n{lista_numeros} \n\nHemos pasado a la lista: \n{nueva_lista}")
print()
print("Realizando comprobación...")
if nueva_lista[0] == sum(nueva_lista[1:]):
    print()
    print(f"Programa realizado con éxito: {nueva_lista[0]} = {sum(nueva_lista[1:])}")
print()
print("FIN DEL PROGRAMA")