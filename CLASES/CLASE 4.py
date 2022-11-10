# CLASE DEL DÍA 30/06/2022

# Mirar la versión de Python
import sys; print("Python %s on %s" %(sys.version, sys.platform))

# PILAS Y COLAS EN PYTHON
from collections import deque

# CREANDO UNA PILA A TRAVÉS DE UNA LISTA, YA QUE EN PYTHON NO EXISTEN LAS PILAS COMO ESTRUCTURA DE DATOS

pila = [1, 2, 3, 4, 5, 6]

# Agragando datos a la pila
pila.append(7)
print(pila)

# Obteniendo el último elemento de la pila, mediante el método pop
# Este método obtiene el valor y después lo elimina
ultimo_valor_pila = pila.pop()
print(ultimo_valor_pila)
print(pila)

# Recorriendo la pila y mostrando los valores
for elemento in pila:
    print(elemento)

# Recorriendo la pila y eliminando sus valores
print("--- Recorriendo la pila y eliminando sus valores ---")
while True:
    if len(pila) == 0:
        print("Pila vacía")
        break
    print(pila)
    print(pila.pop())

# Comprobamos que la pila está vacía
print("--- Comprobamos que la pila está vacía ---")
print(pila)

# CREANDO COLAS EN PYTHON A TRAVÉS DE LA CLASE DEQUE
cola = deque(["Pedro", "Juan", "Miguel"])
print(cola)

# Agregando datos a la cola
cola.append("Ana")
cola.append("Marta")
print(cola)

# Obteniendo el primer elemento de la cola, mediante el método popleft
ultimo_valor_cola = cola.popleft()
print(ultimo_valor_cola)
print(cola)

# Recorriendo la cola y mostrando sus valores
print("--- Recorriendo la cola y eliminando sus valores ---")
while True:
    try:
        print(cola.popleft())
    except IndexError:
        print("Esto sería un error, pero sigo, porque soy así")
        break

print("Seguimos")



