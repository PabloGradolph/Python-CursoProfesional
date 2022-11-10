# Curso profesional de Python (AEPI): 10_Ejercicios
# Autor: Pablo Gradolph Oliva
# 23/07/2022

'''
1 - Localiza el error en el siguiente bloque de código. Crea una excepción para evitar que el programa se bloquee y
además explica en un mensaje al usuario la causa y/o solución:

Existen al menos dos posibles errores que hay que gestionar.
'''

def realizarOperacion(operacion, numero1, numero2):
    if operacion == 1:
        return numero1 + numero2
    elif operacion == 2:
        return numero1 - numero2
    elif operacion == 3:
        return numero1 * numero2
    else:
        return numero1 / numero2

def funcionamiento():
    while True:
        try:
            print("Escoge una opcion:")
            print("1. Sumar")
            print("2. Restar")
            print("3. Multiplicar")
            print("4. Dividir")

            operacion = int(input("Introduce el numero de la operacion: "))
            numero1 = float(input("Introduce el primer numero: "))
            numero2 = float(input("Introduce el segundo numero: "))

            if operacion < 1 or operacion > 4:
                print("Opcion no valida")
                continue

            resultado = realizarOperacion(operacion, numero1, numero2)
            print("Resultado: ", resultado)

            continuar = input("¿Desea continuar? si/no ")
            print()
            if continuar == "si" or continuar == "Si":
                continue
            elif continuar == "no" or continuar == "No":
                break
            else:
                print("No se ha reconocido si desea continuar o no, vuelva a intentarlo")
                continue

        except ValueError as error:
            print(f"Se ha producido un error en la entrada: \n{error}")
            print()

        except ZeroDivisionError:
            print("Se ha producido un error, estás intentando dividir por cero.")
            print()

funcionamiento()
print("FIN DEL PROGRAMA")

'''
2 - Realiza una función llamada agregar_una_vez() que reciba una lista y un
elemento. La función debe añadir el elemento al final de la lista con la
condición de no repetir ningún elemento. Además si este elemento ya se
encuentra en la lista se debe invocar un error de tipo ValueError que debes
capturar y mostrar este mensaje en su lugar:

Error: Imposible añadir elementos duplicados => [elemento].

Prueba de agregar los elementos 10, -2, "Hola" a la lista de elementos con la función
una vez la has creado y luego muestra su contenido.

Nota: Puedes utilizar la sintaxis: elemento in lista
'''

def agregar_una_vez(lista, elemento):

    if elemento not in lista:
        lista.append(elemento)

    else:
        print(f"Error: Imposible añadir elementos duplicados => {elemento}")

    print(f"La lista ha quedado como: \n{lista}")

lista = []
elemento = input("Introduzca el primer elemento en la lista: ")
agregar_una_vez(lista, elemento)

while True:
    continuar = input("¿Desea continuar añadiendo elementos? Si/No")
    if continuar == "si" or continuar == "Si":
        elemento = input("Introduzca otro elemento en la lista: ")
        agregar_una_vez(lista, elemento)
        continue
    elif continuar == "no" or continuar == "No":
        break
    else:
        print("No se ha reconocido si desea continuar o no, vuelva a intentarlo")
        continue

print()
print("FIN DEL PROGRAMA")