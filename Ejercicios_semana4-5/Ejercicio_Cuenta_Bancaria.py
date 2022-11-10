# Curso profesional de Python (AEPI): 14_Ejercicios
# Autor: Pablo Gradolph Oliva
# 01/08/2022
# Ejercicios objetos en las clases

'''
3 - Escribe una clase Cuenta para representar una cuenta bancaria.
Los datos de
la cuenta son:
nombre del cliente (str),
número de cuenta (str),
tipo de
interés (float) y saldo (float).

La clase contendrá los siguientes métodos:

• Constructor con todos los argumentos.

• Métodos setters/getters para asignar y obtener los datos de la cuenta.

• Métodos ingreso y reintegro. Un ingreso consiste en aumentar el saldo
en la cantidad que se indique. Esa cantidad no puede ser negativa. Un
reintegro consiste en disminuir el saldo en una cantidad pero antes se
debe comprobar que hay saldo suficiente. La cantidad no puede ser
negativa. Los métodos ingreso y reintegro devuelven true si la
operación se ha podido realizar o false en caso contrario.

• Método transferencia que permita pasar dinero de una cuenta a otra
siempre que en la cuenta de origen haya dinero suficiente para poder
hacerla.

Ejemplo de uso del método transferencia:

cuentaOrigen.transferencia(cuentaDestino, importe);

Esto indica que queremos hacer una transferencia desde cuentaOrigen
a cuentaDestino del importe indicado.

Prueba el funcionamiento de la clase Cuenta
'''

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# COMIENZA EL CÓDIGO
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Definimos la clase Cuenta
class Cuenta:
    # Constructor
    def __init__(self, nombre, numero, interes, saldo):
        self.__nombre = nombre
        self.__numero = numero
        self.__interes = interes
        self.__saldo = saldo

    # Getters
    def getNombre(self):
        return f"El propietario de la cuenta es {self.__nombre}."
    def getNumero(self):
        return f"El número de la cuenta es {self.__numero}."
    def getInteres(self):
        return f"El interés de la cuenta es del {self.__interes}%."
    def getSaldo(self):
        return f"El saldo de la cuenta es de {self.__saldo} euros."

    # Setters
    def setNombre(self, nombre):
        self.__nombre = nombre
        print(f"El propietario de la cuenta ahora es {self.__nombre}.")
    def setNumero(self, numero):
        self.__numero = numero
        print(f"El número de cuenta ahora es {self.__numero}.")
    def setInteres(self, interes):
        self.__interes = interes
        print(f"El interés de la cuenta ahora es del {self.__interes}%.")
    def setSaldo(self, saldo):
        self.__saldo = saldo
        print(f"El saldo de la cuenta ahora es de {self.__saldo} euros.")

    # Método ingreso
    def ingreso(self, importe):
        if importe < 0:
            print("No se puede hacer un ingreso de una cantidad negativa.")
        else:
            self.__saldo += importe

    # Método reintego / retirada de dinero
    def reintegro(self, importe):
        if importe < 0:
            print("No se puede retirar una cantidad negativa de dinero.")
        else:
            if self.__saldo < importe:
                print("No hay saldo suficiente para realizar el reintegro.")
            else:
                self.__saldo -= importe
                print("El reintegro se ha realizado correctamente.")

    # Transferencia entre dos cuentas (objetos) de la clase
    def transferencia(self, objeto, importe):
        if self.__saldo < importe:
            print("No hay saldo suficiente para realizar la transferencia")
        else:
            self.__saldo -= importe
            objeto.ingreso(importe)

# Función para crear la primera cuenta, que utilizaremos más adelante
def crear_cuenta():
    global cuenta

    # Gestión de errores
    try:
        print("Usted va a crear su cuenta, para ello siga estos pasos: ")
        nombre = input("Introduzca el nombre del propietario de la cuenta: ")
        numero = input("Introduza el número de cuenta: ")
        interes = float(input("Introduzca el tipo de interés que tiene su cuenta: "))
        saldo = float(input("Introduzca el saldo de su cuenta: "))
        cuenta = Cuenta(nombre, numero, interes, saldo)
        print("Cuenta creada con éxito")
        print()

    except ValueError as error:
        print(f"Se está produciendo el siguiente error: \n{error}. \nInténtelo de nuevo:")
        crear_cuenta()

# Función para modificar los datos de nuestra cuenta, que utilizaremos más adelante
def modificar_datos_cuenta(cuenta):

    # Gestión de errores
    try:
        # Cambiamos el nombre
        nombre = input("¿Desea modificar el propietario de la cuenta? Si/No: ")
        if nombre == "Si" or nombre == "si" or nombre == "SI":
            nom = input("Introduzca el nombre del nuevo propietario: ")
            cuenta.setNombre(nom)
            print()
        elif nombre == "No" or nombre == "no" or nombre == "NO":
            pass
        else:
            print("No se ha reconocido su respuesta, vuelva a intentarlo")
            modificar_datos_cuenta(cuenta)

        # Cambiamos el número
        numero = input("¿Desea modificar el número de la cuenta? Si/No: ")
        if numero == "Si" or numero == "si" or numero == "SI":
            num = input("Introduzca el nuevo número de cuenta: ")
            cuenta.setNumero(num)
            print()
        elif numero == "No" or numero == "no" or numero == "NO":
            pass
        else:
            print("No se ha reconocido su respuesta, vuelva a intentarlo")
            modificar_datos_cuenta(cuenta)

        # Cambiamos el tipo de interés
        interes = input("¿Desea modificar el interes de la cuenta? Si/No: ")
        if interes == "Si" or interes == "si" or interes == "SI":
            inter = float(input("Introduzca el nuevo interes de la cuenta: "))
            cuenta.setInteres(inter)
            print()
        elif interes == "No" or interes == "no" or interes == "NO":
            pass
        else:
            print("No se ha reconocido su respuesta, vuelva a intentarlo")
            modificar_datos_cuenta(cuenta)

        # Cambiamos el saldo
        saldo = input("¿Desea modificar el saldo de la cuenta? Si/No: ")
        if saldo == "Si" or saldo == "si" or saldo == "SI":
            sal = float(input("Introduzca el nuevo saldo de la cuenta: "))
            cuenta.setSaldo(sal)
            print()
        elif saldo == "No" or saldo == "no" or saldo == "NO":
            pass
        else:
            print("No se ha reconocido su respuesta, vuelva a intentarlo")
            modificar_datos_cuenta(cuenta)

    except ValueError as Error:
        print(f"Está ocurriendo el siguiente error: \n{Error} \nInténtelo de nuevo")
        modificar_datos_cuenta(cuenta)

# Función que utilizaremos más adelante para realizar una transferencia entre cuentas
def datos_transferencia(cuenta):
    global cuenta_destino

    # Gestión de errores
    try:
        nombre = input("Introduzca el nombre del propietario de la cuenta: ")
        numero = input("Introduza el número de cuenta: ")
        interes = float(input("Introduzca el tipo de interés que tiene la cuenta: "))
        saldo = float(input("Introduzca el saldo de la cuenta: "))
        cuenta_destino = Cuenta(nombre, numero, interes, saldo)
        print()
        print("Datos introducidos correctamente.")
        importe = float(input("Introduzca el importe de la transferencia: "))
        cuenta.transferencia(cuenta_destino, importe)

    except ValueError as error:
        print(f"Se está produciendo el siguiente error: \n{error}. \nInténtelo de nuevo:")
        datos_transferencia(cuenta)

# Función principal del programa, gestiona el funcionamiento del mismo.
def funcionamiento_3():
    global lista_cuentas

    # Creamos 'lista_cuentas' para gestionar si el usuario tiene ya o no una cuenta creada.
    lista_cuentas = []
    # El bucle nos permite hacer muchas de las opciones del programa antes de finalizarlo.
    while True:
        print("---MENÚ DE OPCIONES---")
        print("1 - Crear/Modificar su cuenta")
        print("2 - Visualizar los datos de su cuenta")
        print("3 - Realizar un ingreso en su cuenta")
        print("4 - Realizar un reintegro en su cuenta")
        print("5 - Realizar una transferencia entre dos cuentas")
        print("6 - Finalizar el programa")
        print()

        # Gestión de errores
        try:
            opcion = int(input("Introduzca la opción deseada: "))

            if opcion == 1: # Si 'lista_cuentas' está vacía crearemos una cuenta, sino, modificaremos los datos.

                if len(lista_cuentas) == 0:
                    crear_cuenta() # Función para crear la cuenta
                    lista_cuentas.append(cuenta)

                elif len(lista_cuentas) == 1:
                    print(f"Usted va a modificar los datos de su cuenta, siga los pasos:")
                    modificar_datos_cuenta(cuenta) # Función para modificar los datos

            elif opcion == 2: # Visualizar los datos por pantalla

                if len(lista_cuentas) == 0:
                    print("No tiene ninguna cuenta para poder visualizar sus datos, por favor, cree una primero.")

                elif len(lista_cuentas) == 1:
                    print("---MOSTRANDO LOS DATOS DE SU CUENTA---")
                    # Llamamos a los getters
                    print(cuenta.getNombre())
                    print(cuenta.getNumero())
                    print(cuenta.getInteres())
                    print(cuenta.getSaldo())
                    print()

            elif opcion == 3: # Realizamos un ingreso en la cuenta

                if len(lista_cuentas) == 0:
                    print("No tiene ninguna cuenta para poder realizar un ingreso, por favor, cree una primero.")

                elif len(lista_cuentas) == 1:
                    print("Usted va a realizar un ingreso en su cuenta:")
                    importe = float(input("Introduzca el importe del ingreso que desea realizar: "))
                    cuenta.ingreso(importe)
                    if importe >= 0:
                        print("El ingreso se ha realizado correctamente.")

            elif opcion == 4: # Realizamos un reintegro / retirada de dinero en la cuenta

                if len(lista_cuentas) == 0:
                    print("No tiene ninguna cuenta para poder realizar un reintegro, por favor, cree una primero.")

                elif len(lista_cuentas) == 1:
                    print("Usted va a realizar un reintegro en su cuenta:")
                    importe = float(input("Introduzca el importe del ingreso que desea realizar: "))
                    cuenta.reintegro(importe)

            elif opcion == 5: # Realizamos una transferencia entre dos cuentas

                if len(lista_cuentas) == 0:
                    print("No tiene ninguna cuenta para poder realizar una transferencia, por favor, cree una primero.")

                elif len(lista_cuentas) == 1:
                    print("Para poder realizar una transferencia debe introducir los datos de la cuenta de destino:")
                    datos_transferencia(cuenta) # Función encargada de hacer la transferencia
                    print()
                    # Mostramos los datos de ambas cuentas por pantalla, para ver como quedan.
                    # Para ello llamamos a los getters de ambas cuentas.
                    print("---TRANSFERENCIA REALIZADA CON ÉXITO---.")
                    print("DATOS DE LA CUENTA DE ORIGEN:")
                    print(cuenta.getNombre())
                    print(cuenta.getNumero())
                    print(cuenta.getInteres())
                    print(cuenta.getSaldo())
                    print()
                    print("DATOS DE LA CUENTA DE DESTINO:")
                    print(cuenta_destino.getNombre())
                    print(cuenta_destino.getNumero())
                    print(cuenta_destino.getInteres())
                    print(cuenta_destino.getSaldo())
                    print()

            elif opcion == 6: # Con esta opción se finaliza el programa

                print("FIN DEL PROGRAMA")
                break

            else:

                print("No se ha reconocido su opción, vuelva a intentarlo.")

        except ValueError as error:
            print(f"Se está produciendo el siguiente error en la entrada: \n{error}. \nInténtelo de nuevo:")
            print()

# Ejecutamos
funcionamiento_3()