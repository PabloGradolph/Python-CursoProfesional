# Curso profesional de Python (AEPI): 12_Ejercicios
# Autor: Pablo Gradolph Oliva
# 24/07/2022

'''
1 - En este ejercicio vamos a realizar un programa que nos calcule el índice de masa corporal
de una persona en base a unos datos que nos facilite el usuario por consola. Para ello
debemos solicitar al usuario de nuestro programa los siguientes datos: nombre, edad,
peso y altura.
Debemos crear una clase llamada CalcularIMC(), esta clase tendrá lo siguiente:
- Constructor con argumentos.

Para calcular el imc se utiliza la siguiente formula:
valor = peso / (altura * altura);

Los mensajes que mostraremos en nuestro programa una vez realizado el calculo serán
los siguientes:
Cuando el programa comience, instanciaremos la clase CalcularIMC() y haremos que el constructor pida las entradas por consola.

si < 16.00

"Hola " + nombre + " tienes delgadez extrema"

si <= 16.00 || valor <= 16.99

"Hola " + nombre + " tienes delgadez moderada"

si <= 17.00 || valor <= 18.49)

"Hola " + nombre + " tienes delgadez aceptable"

si <= 18.50 || valor <= 24.99

"Hola " + nombre + " estas en tu peso"

si <= 25.00 || valor <= 29.99

"Hola " + nombre + " tienes sobrepeso"

si <= 30.00 || valor <= 34.99

"Hola " + nombre + " tienes obesidad de tipo I"

si <= 35.00 || valor <= 40.00

"Hola " + nombre + " tienes obesidad de tipo III"

si no
"no existe clasificacion"
'''

# - - - - - - - - - - - - - - - - - -
# COMIENZO DEL CÓDIGO
# - - - - - - - - - - - - - - - - - -

# Función para pedir los datos
def pedir_datos():
    global nombre
    global peso
    global altura

    try:
        nombre = input("Introduzca su nombre: ")
        peso = float(input("Introduzca su peso en kg: "))
        altura = float(input("Introduzca su altura en metros: "))

    except ValueError as error:
        print(f"Se está produciendo el siguiente error en la entrada: \n{error}")
        pedir_datos()


# Función para mostrar los mensajes tras los cálculos
def mensajes(nombre, valor):
    if valor < 16:
        print(f"Hola {nombre}, tienes delgadez extrema.")

    elif 16 <= valor < 17:
        print(f"Hola {nombre}, tienes delgadez moderada.")

    elif 17 <= valor < 18.5:
        print(f"Hola {nombre}, tienes delgadez aceptable.")

    elif 18.5 <= valor < 25:
        print(f"Hola {nombre}, estás en tu peso.")

    elif 25 <= valor < 30:
        print(f"Hola {nombre}, tienes sobrepeso.")

    elif 30 <= valor < 35:
        print(f"Hola {nombre}, tienes obesidad de tipo I")

    elif 35 <= valor < 40:
        print(f"Hola {nombre}, tienes obesidad de tipo III")

    else:
        print("No existe clasificación")


# Creamos la clase CalcularIMC
class CalcularIMC:
    def __init__(self, peso, altura):
        self.peso = peso
        self.altura = altura

    def calculo(self, peso, altura):
        return peso / (altura * altura)

# Ejecutamos
pedir_datos()
persona = CalcularIMC(peso, altura)
valor = persona.calculo(peso, altura)
print()
mensajes(nombre, valor)
print()
print("FIN DEL PROGRAMA")


'''
2 - Implementar una clase Juego con las siguientes características:

Atributos
- Tiene como atributo público un entero que indica el número de vidas que
le quedan al jugador en la partida actual.

Métodos
- Tiene como método el constructor que acepta un parámetro de tipo entero
que indica el número de vidas iniciales con las que parte el jugador.

- Tiene un método MuestraVidasRestantes que visualiza por pantalla el
número de vidas que le quedan al jugador en la partida actual.

- Además esta clase tiene también el método main que debe realizar lo
siguiente:

- Crea una instancia de la clase Juego indicando que el número de
vidas es 5.

- Resta una vida al valor del atributo con las vidas y vuelve a llamar
a MuestraVidasRestantes.

Clase Juego

- Llama al método MuestraVidasRestantes del objeto creado.

La logica es la siguiente: tenemos que informar al usuario que
introduzca un numero, cada vez que introduzca uno y no acierte
debemos informarle con las palabras mayor o menor que el
numero que hemos guardado en una variable al comienzo del
script, si no acierta vamos restando vidas, en caso de llegar las
vidas a 0 y no hayamos acertado debemos informar al jugado de
que se ha quedado sin vidas
'''

# - - - - - - - - - - - - - - - - - -
# COMIENZO DEL CÓDIGO
# - - - - - - - - - - - - - - - - - -

# Creamos la función que ejecuta el funcionamiento del juego
def funcionamiento():
    global numero
    global numero_adivinar
    global vidas

    numero_adivinar = 8
    print("VAMOS A JUGAR A ADIVINAR UN NÚMERO, TIENES 5 VIDAS:")
    print()
    try:
        numero = int(input("Introduzca un número: "))

        while True:

            if numero == numero_adivinar:
                print()
                print (f"¡Has acertado! El número para adivinar era {numero_adivinar}")
                break

            elif numero < numero_adivinar:
                print()
                print("Has fallado, el número que quieres adivinar es MAYOR")
                vidas = personaje.__main__(vidas)
                personaje.muestra_vidas_restantes(vidas)
                if vidas == 0:
                    break
                print()
                numero = int(input("Introduzca un número: "))

            else:
                print()
                print("Has fallado, el número que quieres adivinar es MENOR")
                vidas = personaje.__main__(vidas)
                personaje.muestra_vidas_restantes(vidas)
                if vidas == 0:
                    break
                print()
                numero = int(input("Introduzca un número: "))

        print()
        print("FIN DEL PROGRAMA")

    except ValueError as error:
        print(f"Se está produciendo el sigueinte error en la entrada: {error}")
        print("- - - - - - - - - REINICIANDO PROGRAMA - - - - - - - - -")
        print()
        funcionamiento()

# Creamos la clase Juego
class Juego:

    def __init__(self, vidas):
        self.vidas = vidas

    def muestra_vidas_restantes(self, vidas):
        if vidas > 0:
            print(f"Te quedan {vidas} vidas")
        else:
            print("Te has quedado sin vidas")

    def __main__(self, vidas):
        vidas -= 1
        return vidas

# Ejecutamos
vidas = 5
personaje = Juego(vidas)
funcionamiento()