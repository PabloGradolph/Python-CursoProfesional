# Curso profesional de Python (AEPI): 14_Ejercicios
# Autor: Pablo Gradolph Oliva
# 01/08/2022
# Ejercicios objetos en las clases

'''
2 - Crea una clase llamada Libro que guarde la información de cada uno de los libros de una biblioteca.
La clase debe guardar el título del libro, autor, número de ejemplares del libro y número de ejemplares prestados.
La clase contendrá los siguientes métodos:

Escribe un programa para probar el funcionamiento de la clase Libro.

La clase tendrá lo siguiente:

 - Método préstamo que incremente el atributo correspondiente cada vez que se realice un préstamo del libro.
No se podrán prestar libros de los que no queden ejemplares disponibles para prestar.
Devuelve true si se ha podido realizar la operación y false en caso contrario.

 - Método devolución que decremente el atributo correspondiente cuando se produzca la devolución de un libro.
No se podrán devolver libros que no se hayan prestado.
Devuelve true si se ha podido realizar la operación y false en caso contrario.

 - Método para mostrar los datos de los libros mediante un comando print.

Una vez creada la clase, escribe la lógica necesaria para probar la clase.

Libros:
    La chica del tren / Paula Hawkins / 3 / 1
    Historia de un canalla / Julia Navarro / 1 / 0
    La templanza / María Dueñas / 6 / 3
    Hombres desnudos / Alicia Giménez Bartlett / 6 / 4
    Los besos en el pan / Almudena Grandes / 5 / 2
    Todo esto te daré / Dolores Redondo / 10 / 4
    El amante japonés / Isabel Allende / 3 / 3
    La isla de Alice / Alicia Giménez Bartlett / 4 / 3
    Legado en los huesos / Dolores Redondo / 7 / 5
    Vestido de novia / Pierre Lemaitre / 3 / 1
'''

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# COMIENZA EL CÓDIGO
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Creamos la clase principal Libro
class Libro:
    # Constructor
    def __init__(self, nombre, autor, ejemplares, prestados):
        self.nombre = nombre
        self.autor = autor
        self.ejemplares = ejemplares
        self.prestados = prestados

    # Método para imprimir los datos de los libros posteriormente
    def __str__(self):
        return f"Título: {self.nombre} - Autor: {self.autor} - Ejemplares: {self.ejemplares} - Prestados: {self.prestados}"

    # Método para prestar un libro. Aumenta en 1 el atributo prestados de ese libro
    def prestar(self):
        if self.prestados < self.ejemplares:
            self.prestados += 1
            print("Se ha prestado el libro correctamente")
        else:
            print("No hay ejemplares suficientes para prestar este libro")

    # Método para devolver un libro. Disminuye en 1 el atributo prestados de ese libro.
    def devolver(self):
        if self.prestados > 0:
            self.prestados -= 1
            print("Libro devuelto correctamente")
        else:
            print("No se puede devolver un libro que no ha sido prestado con anterioridad")


# Clase hija que usaremos para imprimir por pantalla los libros cada vez que el usuario pida esta opción
class ListaLibro(Libro):
    # Constructor
    def __init__(self, lista_libros=[]):
        self.lista_libros = lista_libros

    # Método para agregar los libros a este objeto 'lista'
    def agregar(self, libro):
        self.lista_libros.append(libro)

    # Método para limpiar la lista cada vez que se hace una modificación en los libros.
    def limpiar(self):
        self.lista_libros.clear()

    # Método para mostrar por pantalla todos los libros que haya en esta lista.
    def mostrar(self):
        print()
        print("---LISTA DE LIBROS---")
        for p in self.lista_libros:
            print(p)
        print("---FIN DE LA LISTA---")
        print()


# Contenido de la biblioteca al principio
libro1 = Libro("La chica del tren", "Paula Hawkins", 3, 1)
libro2 = Libro("Historia de un canalla", "Julia Navarro", 1, 0)
libro3 = Libro("La tamplanza", "María Dueñas", 6, 3)
libro4 = Libro("Hombres desnudos", "Alicia Giménez Bartlett", 6, 4)
libro5 = Libro("Los besos en el pan", "Almudena Grandes", 5, 2)
libro6 = Libro("Todo esto te daré", "Dolores Redondo", 10, 4)
libro7 = Libro("El amante japonés", "Isabel Allende", 3, 3)
libro8 = Libro("La isla de Alice", "Alicia Giménez Bartlett", 4, 3)
libro9 = Libro("Legado en los huesos", "Dolores Redondo", 7, 5)
libro10 = Libro("Vestido de novia", "Pierre Lemaitre", 3, 1)

# Lista con todos los libros, se añadirán más posteriormente si el usuario así lo desea.
lista_objetos = [libro1, libro2, libro3, libro4, libro5, libro6, libro7, libro8, libro9, libro10]

# Lista con los nombres de los libros que hay en la biblioteca, nos será útil para saber si se pueden prestar los libros
# Si se pueden devolver, o si se puede añadir otro que no esté ya en esta lista
lista_nombres_libros = ["La chica del tren", "Historia de un canalla", "La templanza", "Hombres desnudos",
                        "Los besos en el pan", "Todo esto te daré", "El amante japonés", "La isla de Alice",
                        "Legado en los huesos", "Vestido de novia"]


# Esta función sirve para agregar libros a la biblioteca
def agregar_libro_biblioteca():
    print("AGREGAR UN LIBRO A LA BIBLIOTECA:")

    # Gestión de errores
    try:
        # Pedimos el nombre del libro
        nombre = input("Introduzca el nombre del libro: ")

        # Comprobamos que el libro no esté ya en la biblioteca
        if nombre in lista_nombres_libros:
            print("Ese libro ya está en la biblioteca")

        # Si no está seguimos pidiendo los datos del libro
        else:
            autor = input("Introduzca el autor del libro: ")
            ejemplares = int(input("Introduzca el número de ejemplares que quiere agregar: "))
            prestados = 0  # Al añadirlo el atributo prestados será cero

            # Creamos el objeto nuevo_libro que pasará a pertenecer a la biblioteca
            nuevo_libro = Libro(nombre, autor, ejemplares, prestados)
            print("Libro agregado con éxito")
            lista_nombres_libros.append(nombre)  # Se añade el nombre a la lista de nombres.
            lista_objetos.append(nuevo_libro)  # Se añade el libro a la lista con los libros.

    except ValueError as error:
        print(f"Se está produciendo el siguiente error: \n{error}. \nInténtelo de nuevo")
        agregar_libro_biblioteca()


# Función principal del programa que gestiona su funcionamiento
def funcionamiento2():
    # Bucle while para permitir hacer muchas opciones antes de finalizar el programa
    while True:
        print("---MENÚ DE OPCIONES---")
        print("1 - Mostrar los libros de la biblioteca")
        print("2 - Prestar un libro de la biblioteca")
        print("3 - Devolver un libro a la biblioteca")
        print("4 - Agregar un libro a la biblioteca")
        print("5 - Finalizar el programa")
        print()

        # Gestión de errores
        try:
            opcion = int(input("Introduzca la opción deseada: "))

            if opcion == 1:  # Mostramos los libros de la biblioteca

                lista_libros = ListaLibro()  # Objeto lista_libros de la clase hija para mostrar los libros.
                # Limpiamos el contenido del objeto, por si ya lo hemos ejecutado con anterioridad,
                # que no sigan añadiéndose y estén duplicados
                lista_libros.limpiar()

                # Agregamos los libros
                for i in lista_objetos:
                    posicion = lista_objetos.index(i)
                    lista_libros.agregar(lista_objetos[posicion])

                # Los mostramos por pantalla
                lista_libros.mostrar()

            elif opcion == 2:  # Prestamos un libro de la biblioteca

                nombre = input("Introduzca el nombre del libro que desea prestar: ")

                # Comprobamos que esté o no en la biblioteca
                if nombre not in lista_nombres_libros:
                    print("El libro no está en la biblioteca")

                else:
                    # Prestamos el libro pedido
                    for i in lista_nombres_libros:
                        if i == nombre:
                            posicion = lista_nombres_libros.index(i)
                            lista_objetos[posicion].prestar()

            elif opcion == 3:  # Devolvemos un libro a la biblioteca

                nombre = input("Introduzca el nombre del libro que desea devolver: ")

                # Comprobamos que esté o no en la biblioteca
                if nombre not in lista_nombres_libros:
                    print("Este libro no es de la biblioteca")

                else:
                    # Devolvemos el libro pedido
                    for i in lista_nombres_libros:
                        if i == nombre:
                            posicion = lista_nombres_libros.index(i)
                            lista_objetos[posicion].devolver()

            elif opcion == 4:  # Agregamos un libro a la biblioteca llamando a la función que ejecuta esta acción

                agregar_libro_biblioteca()

            elif opcion == 5:  # Finalizamos el programa

                print("FIN DEL PROGRAMA")
                break

            else:

                print("Opción no válida")
                print()

        except ValueError as error:
            print(f"Se está produciendo un error:\n{error}.\nInténtelo de nuevo.")


# Ejecutamos
funcionamiento2()