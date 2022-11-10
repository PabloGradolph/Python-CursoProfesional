# CLASE DEL DÍA 23/06/2022

# CONDICIONALES
edad = int(input("Introduzca su edad: "))
try:
    if edad >= 18 and edad != 20 and edad < 50:
        print("Puedes entrar enseñando el carnet")
    elif edad == 20:
        print("Puedes entrar")
    elif edad >= 50:
        print("No puedes entrar, eres muy mayor")
    else:
        print("No puedes entrar")
except:
    print("La edad introducida no es válida")

# BUCLE FOR

# Ascendente
for vuelta in range(0, 10):
    print("Vuelta "+str(vuelta))

# Descendente
num = 50
for i in range(1, num + 1):
    print(num - i)

# De dos en dos
for vuelta in range (0, 10, 2):
    print("Vuelta "+str(vuelta))

# Para trabajar con cadenas
for letter in "JUNIOR":
    if letter == "I":
        print("i")
    else:
        print("letra", letter)

# BUCLE WHILE
manzanas = 10
while manzanas > 0:
    print("Me estoy comiendo la manzana", manzanas)
    manzanas -= 1 # Es lo mismo que poner manzanas = manzanas - 1
print("Me he quedado sin manzanas")
print(manzanas) # Se guarda el número de la variable tras el while

# SENTENCIAS BREAK Y CONTINUE
for i in range(0, 10):
    if i == 5:
        break
    print("El valor de i es", i) # Podemos poner el print por encima del if y se imprimiría el número 5 también.

for i in range(0, 10):
    if i == 5:
        continue # Continua con la siguiente iteración sin tener en cuenta el resto de código que hay en el bucle.
        # Se salta el número 5.
    print("El valor de i es", i)

manzanas = 10
while manzanas > 0:
    print("Me estoy comiendo la manzana", manzanas)
    if manzanas == 3:
        break
    manzanas -= 1 # Es lo mismo que poner manzanas = manzanas - 1
print("Me he quedado sin manzanas")
print(manzanas) # Se guarda el número de la variable tras el while

# EJERCICIOS VISTOS EN CLASE

# Ejercicio 13 (DE LOS PRIMEROS)
suma_final = 0
for i in range(1, 51):
    suma_final = i + suma_final
print(f"La suma de los primeros 50 números naturales es igual a {suma_final}")
print("FIN DEL PROGRAMA")

# Ejercicio 6 (DE LOS PRIMEROS)
print("H\no\nl\na\n\nm\nn\nd\no\n")
for i in "Hola mundo":
    print(i)

# Ejercicio 1 (DE LOS TERCEROS)
numero_uno = float(input("Introduce el primer número: "))
numero_dos = float(input("Introduce el segundo número: "))
if numero_uno == numero_dos:
    print("Los números son iguales.")
else:
    print(f"Los números {numero_uno} y {numero_dos} son distintos")

if numero_uno > numero_dos:
    print(f"{numero_uno} es mayor que {numero_dos}")
elif numero_uno < numero_dos:
    print(f"{numero_uno} es menor que {numero_dos}")