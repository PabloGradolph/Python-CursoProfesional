# Grado en ciencias (UC3M): Técnicas informáticas y bases de datos: Ejercicio POO1
# Autor: Pablo Gradolph Oliva
# V 1.0 13/05/2021 primera versión.
# (c) Código abierto
# Programación orientada a objetos, creamos una calse fracción para representar números racionales como 1/2 y -3/8, se almacenarán en forma reducida, se utilizarán métodos como la suma y la multiplicación y se definen operadores: + * == <.
print("FRACCIONES")
print ()
class Fracción: # Para poder crear objetos (fracciones), definimos la clase fracción
    def __init__(self,numerador,denominador): #Creador de objetos
        self.numerador=numerador
        self.denominador=denominador

    def Representación (self, numerador, denominador): # Esto representa la fracción que hemos introducido
        print (f"{numerador}/{denominador}")

    def MCD (self, numerador, denominador): # Esto lo utilizaremos para reducir la fracción
        global mcd
        import math
        mcd = math.gcd(numerador,denominador) # Aquí calculamos el máximo común divisor
        numerador = int(numerador/mcd)
        denominador = int(denominador/mcd) # Dividiendo entre el máximo común divisor en el numerador y en el denominador obtenemos la fracción reducida.
        # Utilizo int para que no salga x.00
        print (f"{numerador}/{denominador}")

    def suma (self, numerador_2, denominador_2): # Esto nos servirá para sumar dos fracciones
        global denominador
        global numerador
        if denominador == denominador_2: # Si los denominadores de ambas fracciones son iguales simplemente sumamos numeradores
            numerador += numerador_2
            print (f"{numerador}/{denominador}")
        else: # Sino, calculamos le mínimo común múltiplo con la fórmula de abajo.
            import math
            MCD = math.gcd(denominador,denominador_2)
            mcm = (denominador * denominador_2)/MCD
            denominador_anterior = denominador # Guardamos el denominador de la primera fracción
            denominador_anterior_2 = denominador_2 # Y el de la segunda
            denominador = mcm # Ahora ambos denominadores se convierten en el mínimo común múltiplo
            denominador_2 = mcm
            numerador = numerador*(denominador/denominador_anterior) # Y el numerador se múltiplica por el número al que hemos multiplicado el denominador anterior para llegar al mínimo común múltiplo
            numerador_2 = numerador_2*(denominador/denominador_anterior_2)
            nuevo_numerador = int(numerador+numerador_2)
            denominador = int (denominador) # Utilizo int para que no salgan .00
            print (f"{nuevo_numerador}/{denominador}")

    def multiplicación (self, numerador_2, denominador_2): # En el caso de querer multiplicar dos fracciones se multiplican numeradores y se multiplican denominadores entre sí
        global denominador
        global numerador
        numerador = numerador * numerador_2
        denominador = denominador * denominador_2
        print (f"{numerador}/{denominador}")

def datos_fracción(): # Con esta función se piden los datos de la primera función
    global numerador
    global denominador
    try:
        numerador = int (input ("Introduzca el valor del numerador de la fracción que desea construir: "))
        denominador = int (input ("Introduzca el valor del denominador de la fracción que desea construir: "))
    except:
        print ("Se ha introducido de forma errónea alguno de los datos de entrada, por favor inténtelo de nuevo")
        datos_fracción()

def suma_y_multiplicación (): # Con esta función calcularemos la suma o la multiplicación, según lo que elija el usuario
    global numerador
    global denominador
    global numerador_2
    global denominador_2
    global opción
    try:
        while opción!=1 and opción!=2 and opción!=3: # Esto ocurre en caso de que las opciones no sean correctas
            print ("La opción deseada no se encuentra disponible, por favor introduzca una opción válida")
            opción = int (input ("Introduzca de nuevo la opción deseada: "))
        if opción == 1: # Si la opción es 1 se suman, se piden los datos de la segunda fracción y se llama al método suma para que se sumen ambas fracciones
            print ()
            print("A decidido sumarle otra fracción")
            numerador_2 = int (input ("Introduzca el valor del numerador de la fracción que va a sumar: "))
            denominador_2 = int (input ("Introduzca el valor del denominador de la fracción que va a sumar: "))
            print ("El resultado obtenido al sumar las dos fracciones es:")
            fracción.suma(numerador_2,denominador_2) # Se imprime el resultado
            print()
            print ("FIN DE LA PRIMERA PARTE DEL PROGRAMA") # Finalizaría esta parte del programa
        elif opción == 2: # Si la opción es 2 se multiplican, se piden los datos de la segunda fracción y se llama al método multiplicación para multiplicarlas
            print ()
            print ("A decididdo multiplicarle otra fracción")
            numerador_2 = int (input ("Introduzca el valor del numerador de la fracción que va a multiplicar: "))
            denominador_2 = int (input ("Introduzca el valor del denominador de la fracción que va a multiplicar: "))
            print ("El resultado obtenido al multiplicar las dos fracciones es:")
            fracción.multiplicación(numerador_2,denominador_2) # Si imprime el resultado
            print ()
            print ("FIN DE LA PRIMERA PARTE DEL PROGRAMA") # Finalizaría esta parte del programa
        elif opción == 3: # Si la opción es la 3 acaba esta parte del programa
            print ()
            print ("FIN DE LA PRIMERA PARTE DEL PROGRAMA")
    except:
        print ("Se ha producido un error en alguna de las entradas, por favor, inténtelo de nuevo")
        suma_y_multiplicación()

datos_fracción() # Se piden los datos de la fracción
fracción = Fracción(numerador,denominador) # Se convierten los datos en un objeto de la clase Fracción
print()
print ("El valor de la fracción que ha crado es:")
fracción.Representación(numerador,denominador) # Se imprime el valor de la fracción creada (aquí sin reducir)
print ()
print ("Su fracción reducida, con la que vamos a trabajar, es:")
fracción.MCD(numerador,denominador) # Se aplica el método que reduce la fracción y se imprime por pantalla
print()
print ("TRABAJEMOS CON ESTA FRACCIÓN") # Trabajaremos ahora con la fracción creada
print ()
print ("Escriba 1 si desea sumarle otra fracción a esta")
print ("Escriba 2 si desea multiplicarle otra fracción a esta")
print ("Escriba 3 si desea finalizar la primera parte del programa") # Se expecifican las opciones que puede elegir el usuario ahora
opción = int (input ("Introduzca la opción deseada: ")) # Se pide la opción
suma_y_multiplicación() # Y se ejecuta la función que suma, multiplica o finaliza en función de la opción elegida
print ()
print ("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -") # Segunda parte del programa
print ()
print ("VAMOS A COMPROBAR QUE FUNCIONAN LOS OPERADORES CREADOS +,*,== y <") # Realizaremos la sobrecarga de estos operadores
print ()
print ("Para ello he creado dos productos del mercado con sus respectivos precios, Manzana y Pera.") # Con el objetivo de comprobar que funcionan he creado ya dos objetos
print ("El objetivo es compararlos con la sobrecarga de los operadores para ver si funcionan.")
print ("Puedes ver los productos a continuación:")

class Producto: # Definimos la clase producto, de donde he creado los objetos manzana y pera
    def __init__(self,nombre, precio): #Creador de objetos
        self.nombre = nombre
        self.precio = precio

    def __str__(self): # Este método simplemente ayuda a imprimir por pantalla los objetos
        return "Producto "+self.nombre+" cuesta "+str(self.precio)+" euros "

    def __add__(self,other): # Este sobrecarga el +
        suma_nombres = self.nombre+" y "+other.nombre # La suma de los nombres (concatenación de éstos) se expresa de esta forma
        suma_precios = self.precio+other.precio # Y esta es la suma de los precios
        return Producto(suma_nombres,suma_precios) # Se retorna un objeto con la suma de los nombres y la de los precios

    def __mul__(self,other): # Este sobrecarga el *
        multiplicación_precios = self.precio*other.precio # En este caso solo hemos multiplicado los precios de los productos
        return multiplicación_precios # Retorna esta multiplicación

    def __eq__(self,other): # Sobrecarga el ==
        if self.precio==other.precio: # Si los prcios son iguales retorna True, sino lo son retorna False.
            return True
        else:
            return False
    
    def __gt__(self,other): # Sobrecara el >
        if self.precio>other.precio: # Si el precio del primer porducto es mayor, retorna True, sino lo es, retorna False
            return True
        else:
            return False

def comprobar_operadores():
    global option
    try:
        while option!=1 and option!=2 and option!=3 and option!=4 and option!=5: # En caso de que la opción elegida no sea correcta
            print ("La opción deseada no se encuentra disponible, por favor introduzca una opción válida")
            option = int (input ("Introduzca de nuevo la opción deseada: "))
        while option>0 and option<6:
            if option == 1: # Si la opción es 1, se comprueba el +
                print ()
                suma = manzana + pera # Se suman ambos objetos y se imprme el resultado  por pantalla
                print ("La suma de productos es:")
                print (suma)
                print ()
                print ("Escriba 1 para comprobar el +")
                print ("Escriba 2 para comprobar el *")
                print ("Escriba 3 para comprobar el ==")
                print ("Escriba 4 para comprobar el <")
                print ("Escriba 5 para finalizar el programa")
                option = int (input ("Introduzca la opción deseada: ")) # Volvemos a pedir opción
            elif option == 2: # Si la opción es 2, se multiplican los precios de los productos
                print ()
                multiplicación = manzana * pera # Se multiplican los objetos y se imprime el resultado por pantalla
                print ("La multiplicación de los precios de los productos es:")
                print (multiplicación)
                print ()
                print ("Escriba 1 para comprobar el +")
                print ("Escriba 2 para comprobar el *")
                print ("Escriba 3 para comprobar el ==")
                print ("Escriba 4 para comprobar el <")
                print ("Escriba 5 para finalizar el programa")
                option = int (input ("Introduzca la opción deseada: ")) # Volvemos a pedir opción
            elif option == 3: # Si la opción es 3, se comprueba si los precios son iguales
                print ()
                if manzana==pera: # En caso de ser iguales, se indicará por pantalla
                    print ("El precio de la manzana y de la pera es el mismo")
                else: # En caso contrario, también se indicará
                    print ("El precio de la manzana y de la pera es distinto")
                print()
                print ("Escriba 1 para comprobar el +")
                print ("Escriba 2 para comprobar el *")
                print ("Escriba 3 para comprobar el ==")
                print ("Escriba 4 para comprobar el <")
                print ("Escriba 5 para finalizar el programa")
                option = int (input ("Introduzca la opción deseada: ")) # Volvemos a pedir opción
            elif option == 4: #Si la opción es 4, se comparan los precios
                print ()
                if manzana>pera: # Si el precio de la manzana es mayor, se indicará por pantalla
                    print ("La manzana es más cara")
                else: # En caso contrario también se indicará
                    print ("La pera es más cara")
                print()
                print ("Escriba 1 para comprobar el +")
                print ("Escriba 2 para comprobar el *")
                print ("Escriba 3 para comprobar el ==")
                print ("Escriba 4 para comprobar el <")
                print ("Escriba 5 para finalizar el programa")
                option = int (input ("Introduzca la opción deseada: ")) # Volvemos a pedir opción
            elif option == 5: # Si la opción es la 5, finaliza el programa
                print ()
                print ("FIN DEL PROGRAMA")
                break
    except:
        print ("Se ha producido un error en alguna de las entradas, por favor, inténtelo de nuevo")
        comprobar_operadores()

print()
manzana = Producto("Manzana", 5.6)
pera = Producto("Pera", 4.5) # Estos son los productos creados
print (manzana)
print (pera) # Se imprimen por pantalla con el método str para que el usuario los vea
print ()
print ("Escriba 1 para comprobar el +")
print ("Escriba 2 para comprobar el *")
print ("Escriba 3 para comprobar el ==")
print ("Escriba 4 para comprobar el <")
print ("Escriba 5 para finalizar el programa")
option = int (input ("Introduzca la opción deseada: ")) # Se pide opción
comprobar_operadores() # Se ejecuta la función que comprueba el funcionamiento de los operadores
