# Curso profesional de Python (AEPI): 14_Ejercicios
# Autor: Pablo Gradolph Oliva
# 31/07/2022
# Ejercicios objetos en las clases

'''
1 - Crea una clase llamada Contador que contenga un único atributo entero llamado
cont.

Métodos getter y setter.

La clase contendrá los métodos:

• incrementar: incrementa el contador en una unidad.

• decrementar: decrementa el contador en una unidad.

El contador nunca podrá tener un valor negativo. Si al decrementar se alcanza un
valor negativo el contador toma el valor cero.
'''

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# COMIENZA EL CÓDIGO
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Definimos la clase Contador
class Contador:
    # Constructor
    def __init__(self):
        self.__cont = 0

    # Getters
    def getContador(self):
        return f"Contador: {self.__cont}"

    # Setters
    def setContador(self, nuevo_contador):
        if nuevo_contador < 0:
            print("Error, el contador no puede ser menor que 0, se restablecerá su valor a cero")
            self.__cont = 0
        else:
            self.__cont = nuevo_contador

    # Método incrementar contador
    def incrementar(self):
        self.__cont += 1

    # Método decrementar contador
    def decrementar(self):
        self.__cont -= 1
        if self.__cont < 0:
            print("Error, el contador no puede ser negativo, se mantendrá en cero")
            self.__cont = 0

# Función principal del programa que gestiona el funcionamiento del mismo
def funcionamiento1():
    # Bucle para permitir hacer muchas acciones antes de finalizar el programa
    while True:
        print("----------MENÚ DE OPCIONES----------")
        print("1 - Ver contador.")
        print("2 - Cambiar el valor del contador.")
        print("3 - Incrementar contador.")
        print("4 - Decrementar contador. ")
        print("5 - Finalizar el programa.")
        print()

        # Gestión de errores
        try:
            opcion = input("Introduzca la opción que desea realizar: ")

            if opcion == "1": # Vemos el contador
                visualizacion = contador.getContador()
                print(visualizacion)

            elif opcion == "2": # Cambiamos el valor del contador
                nuevo_contador = int(input("Introduzca un nuevo valor del contador: "))
                contador.setContador(nuevo_contador)

            elif opcion == "3": # Incrementamos el valor del contador
                contador.incrementar()

            elif opcion == "4": # Decrementamos el valor del contador
                contador.decrementar()

            elif opcion == "5": # Finalizamos el programa
                print()
                print("FIN DEL PROGRAMA")
                break

            else:
                print("Opción no reconocida")

        except ValueError as error:
            print(f"Ha ocurrido el siguiente error: {error}")

# Ejecutamos
print("---MANEJO DE UN CONTADOR---")
print("Su contador empieza en 0")
print()
contador = Contador()
funcionamiento1()