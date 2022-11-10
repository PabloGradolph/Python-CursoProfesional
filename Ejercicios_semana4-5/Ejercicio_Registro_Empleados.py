# Curso profesional de Python (AEPI): 13_Ejercicios_Herencia
# Autor: Pablo Gradolph Oliva
# 31/07/2022
# Ejercicios sobre herencia de clases

'''
1 - Vamos a crear un programa para llevar un pequeño registro de empleados de una
empresa de desarrollo de software. Para ello vamos a tener dos clases siguiendo la
siguiente estructura:

1) Clase Empleado

Atributos:
- edad : int (Rango entre 18 y 45 años)
- casado: boolean

Métodos:
- Métodos getter y setter.

Si edad es menor o igual a 21: categoria = “Junior”

Si edad es >=22 y <=35: categoria =  “Senior”

Si edad es >35: categoria “Jefe de proyecto”

- Un método llamado calculaMejoraSalario que permita aumentar el salario en un
porcentaje que sería pasado como parámetro al método.

2) Clase Programador
Clase que hereda de Empleado todos los atributos y métodos. Además esta clase
tendrá lo siguiente:

Atributos:
- lineasDeCodigoPorHora : tipo entero
- lenguajePreferido: tipo cadena

Métodos:
- Métodos getter y setter.
- Método llamado muestraDatos, que imprima por consola los siguientes datos:
nombre, apellidos, lenguaje preferido, departamento
'''


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# CLASES
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Creamos la clase Empleado.
class Empleado:
    # Constructor
    def __init__(self, nombre, edad, casado, salario, categoria):
        self.nombre = nombre
        self.edad = edad
        self.casado = casado
        self.salario = salario
        self.categoria = categoria

    # Getters
    def getNombre(self):
        return self.nombre
    def getEdad(self):
        return self.edad
    def getCasado(self):
        return self.casado
    def getSalario(self):
        return self.salario

    # Setters
    def setNombre(self, nombre):
        self.nombre == nombre
        print("Nombre modificado con éxito")
    def setEdad(self, edad):
        self.edad = edad
        print("Edad modificada con éxito")
    def setCasado(self, casado):
        self.casado = casado
        print("Estado civil modificado con éxito")
    def setSalario(self, salario):
        self.salario = salario
        print("Salario modificado con éxito")
    def setCategoria(self, categoria):
        self.categotia = categoria
        print("Categoría modificada con éxito")

    # Método para calcular la mejora salarial
    def calcular_mejora_salario(self, porcentaje):
        self.salario = (self.salario * porcentaje) + self.salario

# Creamos la clase hija 'Programador'
class Programador(Empleado):
    # Constructor
    def __init__(self, nombre, edad, casado, salario, categoria, lineas_de_codigo_por_hora, lenguaje_preferido):
        super().__init__(nombre, edad, casado, salario, categoria)
        self.lineas_de_codigo_por_hora = lineas_de_codigo_por_hora
        self.lenguaje_preferido = lenguaje_preferido

    # Getters
    def getLineas_de_codigo_por_hora(self):
        return self.lineas_de_codigo_por_hora
    def getLenguaje_preferido(self):
        return self.lenguaje_preferido

    # Setters
    def setLineas_de_codigo_por_hora(self, lineas_de_codigo_por_hora):
        self.lineas_de_codigo_por_hora = lineas_de_codigo_por_hora
    def setLenguaje_preferido(self, lenguaje_preferido):
        self.lenguaje_preferido = lenguaje_preferido

    # Método para imprimir por pantalla posteriormente
    def __str__(self):
        return f"Nombre: {self.nombre} - Edad: {self.edad} - Casado: {self.casado} - Salario: {self.salario}" \
               f" - Categoría: {self.categoria} - Líneas de código por hora: {self.lineas_de_codigo_por_hora}" \
               f" - Lenguaje preferido: {self.lenguaje_preferido}"


# Creamos la clase 'ListaEmpleados' que usaremos para imprimir por pantalla
class ListaEmpleados(Programador):
    # Constructor
    def __init__(self, lista_empleados=[]):
        self.lista_empleados = lista_empleados

    # Método para agregar los empleados a este objeto 'lista'
    def agregar(self, empleado):
        self.lista_empleados.append(empleado)

    # Método para limpiar la lista cada vez que se hace una modificación en los atributos de los empleados.
    def limpiar(self):
        self.lista_empleados.clear()

    # Método para mostrar por pantalla todos los empleados que haya en esta lista.
    def mostrar(self):
        print()
        print("---LISTA DE EMPLEADOS---")
        for p in self.lista_empleados:
            print(p)
        print("---FIN DE LA LISTA---")
        print()

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# FUNCIONES
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Función que define la categoría del empleado, recibe por parámetro la edad de dicho empleado
def definir_categoria(edad):

        if edad <= 21:
            categoria = "Junior"
            return categoria
        elif 21 < edad <= 35:
            categoria = "Senior"
            return categoria
        else:
            categoria = "Jefe de Proyecto"
            return categoria

# Función que utilizaremos para agregar empleados a la lista de empleados
def agregar_empleado():
    print("---AGREGAR LOS DATOS DE UN EMPLEADO---")

    # Gestión de errores
    try:

        # Pedimos los datos del nuevo empleado
        nombre = input("Introduzca el nombre del empleado: ")
        edad = int(input("Introduzca la edad del empleado: "))
        casado = (input("¿El empleado está casado? True/False: "))
        salario = float(input("Introduzca el salario del empleado: "))
        lineas_de_código_hora = int(input("Introduzca las líneas de código por hora que realiza el empleado: "))
        lenguaje_preferido = input("Introduzca el lenguaje de programación preferido del empleado: ")

        # Gestionamos el Boolean de casado
        if casado == "True" or casado == "true":
            casado = True
        elif casado == "False" or casado == "false":
            casado = False
        else:
            print("Respuesta incorrecta. Inténtelo de nuevo.")
            agregar_empleado()

        # Creamos el objeto con los datos ingresados
        empleado = Programador(nombre, edad, casado, salario, definir_categoria(edad), lineas_de_código_hora, lenguaje_preferido)
        lista_objetos.append(empleado) # Añadimos el objeto a la lista con todos los objetos.
        nombres_empleados.append(nombre) # Añadimos el nombre del empleado a la lista con los nombres.
        print("Empleado agregado con éxito")

    except ValueError as error:
        print(f"Se está produciendo el siguiente error: \n{error} \nPor favor, vuelva a intentarlo.")
        agregar_empleado()

# Función que utilizaremos para eliminar empleados de la lista de empleados
def eliminar_empleado():
    print("---ELIMINAR LOS DATOS DE UN EMPLEADO---")

    # Primero gestionamos si existen empleados en nuestra lista para poder eliminar a alguno.
    if len(nombres_empleados) == 0:
        print("No hay empleados en la lista de empleados.")

    else:

        # Gestión de errores
        try:

            # Pedimos el nombre del empleado que queremos eliminar
            nombre = input("Introduzca el nombre del empleado que desea eliminar: ")

            # Gestionamos que esté en nuestra "Base de datos" o en nuestro caso lista.
            if nombre not in nombres_empleados:
                print("El empleado no se encuentra en la lista de empleados. Vuelva a intentarlo.")
                eliminar_empleado()

            else:

                # Contamos el número de veces que está ese nombre en nuestra lista
                veces = nombres_empleados.count(nombre)

                # Si solo está una vez, será más fácil y lo eliminamos directamente
                if veces == 1:
                    print(f"Existe un único empleado con ese nombre.")
                    posicion = nombres_empleados.index(nombre)
                    del(lista_objetos[posicion])
                    nombres_empleados.remove(nombre)
                    print("Empleado eliminado con éxito.")

                else:
                    # Si está más veces, damos la opción de eliminar a todos los empleados con ese nombre, o no.
                    opcion = input("¿Desea eliminar todos los empleados con ese nombre? Si/No: ")

                    # Si la opción es "Si", se eliminan todos.
                    if opcion == "SI" or opcion == "Si" or opcion == "si":
                        for i in range(veces):
                            posicion = nombres_empleados.index(nombre)
                            del(lista_objetos[posicion])
                            nombres_empleados.remove(nombre)
                        print("Empleados eliminados con éxito.")

                    # Si la opción es "No", mostramos a todos los empleados con ese nombre
                    # Y hacemos elegir cual quiere eliminar.
                    elif opcion == "NO" or opcion == "No" or opcion == "no":
                        print("MOSTRANDO TODOS LOS EMPLEADOS CON ESE NOMBRE:")
                        lista_empleados.limpiar()
                        nombres_empleados_copia = nombres_empleados.copy()
                        for i in range(veces):
                            posicion = nombres_empleados_copia.index(nombre)
                            lista_empleados.agregar(lista_objetos[posicion])
                            nombres_empleados_copia[posicion] = ""
                        lista_empleados.mostrar()
                        print()

                        # Le hacemos elegir a través de la línea en la que está dicho empleado una vez mostrados.
                        linea = int(input("Seleccione por el número de línea el empleado que quiere borrar: "))

                        # Gestionamos la eliminación trabajando con una copia de la lista de nombres.
                        # De esta manera obtenemos la posición del empleado que queremos eliminar de la lista.
                        nombres_empleados_copia = nombres_empleados.copy()
                        for i in range(linea):
                            posicion = nombres_empleados_copia.index(nombre)
                            nombres_empleados_copia[posicion] = ""
                        del(lista_objetos[posicion])
                        del(nombres_empleados[posicion])
                        print("Empleado eliminado con éxito")

        except ValueError as error:
            print(f"Se está produciendo el siguiente error: \n{error} \nPor favor, vuelva a intentarlo.")
            eliminar_empleado()

# Función que utilizaremos para calcular la mejora de salario de uno de los empleados.
def mejorar_salario():

    print("---MEJORAR SALARIO A ALGUNO DE LOS EMPLEADOS---")

    # Primero gestionamos si existen empleados en nuestra lista para poder mejorar el salario de alguno.
    if len(nombres_empleados) == 0:
        print("No hay empleados en la lista de empleados.")

    else:

        # Gestión de errores.
        try:

            # Pedimos el nombre del empleado al que queremos mejorar el salario.
            nombre = input("Introduzca el nombre del empleado al que desea subir el salario: ")

            # Gestionamos que ese nombre esté o no en nuestra lista.
            if nombre not in nombres_empleados:
                print("El empleado no se encuentra en la lista de empleados. Vuelva a intentarlo.")
                mejorar_salario()

            else:
                # Contamos el número de veces que aparece ese nombre en la lista.
                veces = nombres_empleados.count(nombre)

                # Si solo está una vez en la lista, mejoramos su salario directamente
                if veces == 1:
                    porcentaje = float(input(f"Introduzca el porcentaje del salario que quiere incrementar a {nombre}: "))
                    porcentaje = porcentaje / 100
                    posicion = nombres_empleados.index(nombre)
                    lista_objetos[posicion].calcular_mejora_salario(porcentaje)

                # Si no, mostramos todos los empleados con ese nombre y hacemos elegir al usuario.
                else:

                    # Se muestran los empleados con ese nombre.
                    print("MOSTRANDO TODOS LOS EMPLEADOS CON ESE NOMBRE:")
                    lista_empleados.limpiar()
                    nombres_empleados_copia = nombres_empleados.copy()
                    for i in range(veces):
                        posicion = nombres_empleados_copia.index(nombre)
                        lista_empleados.agregar(lista_objetos[posicion])
                        nombres_empleados_copia[posicion] = ""
                    lista_empleados.mostrar()
                    print()

                    # Se le hace elegir por el número de línea en el que aparece el empleado que desea seleccionar.
                    linea = int(input("Seleccione por el número de línea el empleado al que quiere mejorar el salario: "))

                    # Se gestiona la mejora de salario del empleado seleccionado de una forma similar a la de la función
                    # Anterior. Haciendo una copia de la lista de nombres de los empleados y trabajando sobre ella.
                    nombres_empleados_copia = nombres_empleados.copy()
                    for i in range(linea):
                        posicion = nombres_empleados_copia.index(nombre)
                        nombres_empleados_copia[posicion] = ""
                    porcentaje = float(
                            input(f"Introduzca el porcentaje del salario que quiere incrementar a {nombre}: "))
                    porcentaje = porcentaje / 100
                    lista_objetos[posicion].calcular_mejora_salario(porcentaje)

        except ValueError as error:
            print(f"Se está produciendo el siguiente error: \n{error} \nPor favor, vuelva a intentarlo.")
            eliminar_empleado()

# Función que utilizaremos para mostrar el/los atributos de alguno de los empleados
def mostrar_atributo():

    print("---MOSTRAR ATRIBUTO DE ALGUNO DE LOS EMPLEADOS---")

    # Primero gestionamos si existen empleados en nuestra lista para poder mostrar sus atributos.
    if len(nombres_empleados) == 0:
        print("No hay empleados en la lista de empleados.")

    else:

        # Gestión de errores
        try:

            # Pedimos el nombre del empleado
            nombre = input("Introduzca el nombre del empleado al que quiere ver algún atributo: ")

            # Gestionamos que esté o no en nuestra lista de empleados.
            if nombre not in nombres_empleados:
                print("El empleado no se encuentra en la lista de empleados. Vuelva a intentarlo.")
                mostrar_atributo()

            else:
                # Contamos cuantas veces aparece en nuestra lista.
                veces = nombres_empleados.count(nombre)

                # Si sólo aparece una vez, pedimos al usuario que escoja el atributo que desea visualizar.
                if veces == 1:

                    print("---ATRIBUTOS---")
                    print("1 - Nombre")
                    print("2 - Edad")
                    print("3 - Categoría")
                    print("4 - Casado")
                    print("5 - Salario")
                    print("6 - Líneas de código por hora")
                    print("7 - Lenguaje preferido")

                    atributo = int(input("Seleccione el NÚMERO de atributo que desea visualizar: "))
                    posicion = nombres_empleados.index(nombre)
                    if atributo == 1:
                        print(f"Nombre: {lista_objetos[posicion].getNombre()}")
                    elif atributo == 2:
                        print(f"Edad: {lista_objetos[posicion].getEdad()}")
                    elif atributo == 3:
                        print(f"Categoría: {definir_categoria(lista_objetos[posicion].getEdad())}")
                    elif atributo == 4:
                        print(f"Casado: {lista_objetos[posicion].getCasado()}")
                    elif atributo == 5:
                        print(f"Salario: {lista_objetos[posicion].getSalario()}")
                    elif atributo == 6:
                        print(f"Líneas de código por hora: {lista_objetos[posicion].getLineas_de_codigo_por_hora()}")
                    elif atributo == 7:
                        print(f"Lenguaje preferido: {lista_objetos[posicion].getLenguaje_preferido()}")
                    else:
                        print("Error en la selección de atributo. Inténtelo de nuevo.")
                        mostrar_atributo()

                # Si existe más de un empleado con ese nombre, se imprimen por pantalla todos los atributos de cada
                # uno de ellos.
                else:
                    print("EXISTE MÁS DE UN EMPLEADO CON ESE NOMBRE. IMPRIMIENDO POR PANTALLA TODOS LOS RESULTADOS:")
                    lista_empleados.limpiar()
                    nombres_empleados_copia = nombres_empleados.copy()
                    for i in range(veces):
                        posicion = nombres_empleados_copia.index(nombre)
                        lista_empleados.agregar(lista_objetos[posicion])
                        nombres_empleados_copia[posicion] = ""
                    lista_empleados.mostrar()
                    print()

        except ValueError as error:
            print(f"Se está produciendo el siguiente error: \n{error} \nPor favor, vuelva a intentarlo.")
            mostrar_atributo()

# Función que utilizaremos para modificar algún atributo de alguno de los empleados.
def modificar_atributo():

    print("---MODIFICAR ATRIBUTO DE ALGUNO DE LOS EMPLEADOS---")

    # Primero gestionamos si existen empleados en nuestra lista para poder mostrar sus atributos.
    if len(nombres_empleados) == 0:
        print("No hay empleados en la lista de empleados.")

    else:

        # Gestión de errores
        try:

            # Pedimos el nombre del empleado al que queremos modificar algún atributo.
            nombre = input("Introduzca el nombre del empleado al que quiere modificar algún atributo: ")

            # Gestionamos que esté en nuestra lista de nombres.
            if nombre not in nombres_empleados:
                print("El empleado no se encuentra en la lista de empleados. Vuelva a intentarlo.")
                modificar_atributo()

            else:
                # Contamos el número de veces que aparece ese nombre en nuestra lista.
                veces = nombres_empleados.count(nombre)

                # Imprimimos todos los que haya por pantalla
                print("MOSTRANDO TODOS LOS EMPLEADOS CON ESE NOMBRE:")
                lista_empleados.limpiar()
                nombres_empleados_copia = nombres_empleados.copy()
                for i in range(veces):
                    posicion = nombres_empleados_copia.index(nombre)
                    lista_empleados.agregar(lista_objetos[posicion])
                    nombres_empleados_copia[posicion] = ""
                lista_empleados.mostrar()
                print()

                # Le decimos al usuario que elija el empleado al que desea modificar un atributo.
                linea = int(input("Seleccione por el número de línea el empleado al que quiere modificar: "))

                # Obtenemos la posición del empleado en nuestra lista.
                nombres_empleados_copia = nombres_empleados.copy()
                for i in range(linea):
                    posicion = nombres_empleados_copia.index(nombre)
                    nombres_empleados_copia[posicion] = ""

                # Le pedimos que elija el atributo que desea modificar del empleado.
                print("---ATRIBUTOS---")
                print("1 - Nombre")
                print("2 - Edad")
                print("3 - Casado")
                print("4 - Salario")
                print("5 - Líneas de código por hora")
                print("6 - Lenguaje preferido")

                atributo = int(input("Seleccione el NÚMERO de atributo que desea modificar: "))

                if atributo == 1: # Se cambia el nombre
                    nuevo_nombre = input("Introduzca el nuevo nombre del empleado: ")
                    lista_objetos[posicion].setNombre(nuevo_nombre)

                elif atributo == 2: # Se cambia la edad, y con ello la categoría
                    print("Con la edad, también cambiará la categoría del empleado")
                    print()
                    nueva_edad = int(input(f"Introduzca la nueva edad de {nombre}: "))
                    lista_objetos[posicion].setEdad(nueva_edad)
                    categoria = definir_categoria(nueva_edad)
                    lista_objetos[posicion].setCategoria(categoria)

                elif atributo == 3: # Se cambia el estado civil del empleado.
                    casado = (input(f"¿{nombre} está casado? True/False: "))
                    # Gestionamos el Boolean de casado
                    if casado == "True" or casado == "true":
                        casado = True
                    elif casado == "False" or casado == "false":
                        casado = False
                    else:
                        print("Respuesta incorrecta. Inténtelo de nuevo.")
                        modificar_atributo()

                    lista_objetos[posicion].setCasado(casado)

                elif atributo == 4: # Se cambia el salario
                    nuevo_salario = float(input(f"Introduzca el nuevo salario de {nombre}: "))
                    lista_objetos[posicion].setSalario(nuevo_salario)

                elif atributo == 5: # Se cambian las líneas de código que hace el empleado por hora.
                    lineas = int(input(f"Introduzca las líneas de código por hora que hace {nombre}: "))
                    lista_objetos[posicion].setLineas_de_codigo_por_hora(lineas)

                elif atributo == 6: # Se cambia el lenguaje de programación preferido del empleado.
                    lenguaje = input(f"Introduce el nuevo lenguaje de programación preferido de {nombre}: ")
                    lista_objetos[posicion].setLenguaje_preferido(lenguaje)

                else:
                    print("Atributo escogido incorrectamente. Inténtelo de nuevo")
                    modificar_atributo()

        except ValueError as error:
            print(f"Se está produciendo el siguiente error: \n{error} \nPor favor, vuelva a intentarlo.")
            mostrar_atributo()

# Función principal del programa que gestiona su funcionamiento
def funcionamiento():
    # Con este bucle podemos realizar muchas acciones antes de finalizar el programa.
    while True:
        print("---MENÚ DE OPCIONES---")
        print("1 - Mostrar lista de empleados con sus atributos")
        print("2 - Agregar empleado a la lista de empleados")
        print("3 - Eliminar un empleado de la lista de empleados")
        print("4 - Mejorar salario a alguno de los empleados")
        print("5 - Obtener algún atributo de los empleados")
        print("6 - Modificar algún atributo de algún empleado")
        print("7 - Finalizar el programa")
        print()

        # Le pedimos al usuario la opción que desea realizar.
        opcion = (input("Inserte la opción que desea realizar: "))
        print()

        if opcion == "1": # Mostramos la lista de empleados con sus atributos

            # Borramos el contenido que hubiese previamente
            lista_empleados.limpiar()

            # Agregamos los empleados a la lista para imprimirla
            for i in lista_objetos:
                posicion = lista_objetos.index(i)
                lista_empleados.agregar(lista_objetos[posicion])

            # Mostramos la lista
            lista_empleados.mostrar()

        elif opcion == "2":
            # Llamamos a la función que sirve para agregar empleados.
            agregar_empleado()
            print()

        elif opcion == "3":
            # Llamamos a la función que sirve para eliminar empleados.
            eliminar_empleado()
            print()

        elif opcion == "4":
            # Llamamos a la función que sirve para mejorar el salario de algún empleado.
            mejorar_salario()
            print()

        elif opcion == "5":
            # Llamamos a la función que sirve para mostrar los atributos de los empleados.
            mostrar_atributo()
            print()

        elif opcion == "6":
            # Llamamos a la función que sirve para modificar los atributos de los empleados.
            modificar_atributo()
            print()

        elif opcion == "7":
            # Finalizamos el programa
            print()
            print("FIN DEL PROGRAMA")
            break

        else:
            print("Opción no válida, por favor, vuelva a intentarlo.")
            funcionamiento()

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# EJECUCIÓN
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Estos son los 3 objetos que hemos estado mencionando con los que trabajamos:
# "lista_empleados" que es un objeto de la clase "ListaEmpleados" servirá para guardar e imprimir su información.
# "lista_objetos" es la lista en la que guardamos todos los objetos=empleados creados/eliminados etc.
# "nombres_empleados" guarda los nombres de los empleados para gestionar si están los objetos con estos nombres...
lista_empleados = ListaEmpleados()
lista_objetos = []
nombres_empleados = []

print("--------REGISTRO DE EMPLEADOS--------")
print()
# Llamamos a la función principal para ejecutar.
funcionamiento()

