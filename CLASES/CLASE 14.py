# CLASE DEL DÍA 04/08/2022

import threading
import time


# Ejemplo de hilos
def contar(leg):

    '''Contar hasta 25'''

    contador = 0
    while contador < 25:
        start_counting = time.time()
        contador += 1
        time.sleep(leg)
        stop_counting = time.time()
        tiempo_proceso = stop_counting - start_counting

        # El método getName nos retorna el nombre del hilo que se está ejecutando.
        # Si esta tachado, es que esta bajo aviso de "deprecation"
        # Cambiará en la siguiente versión del módulo.
        # Podemos usar: threading.current_thread().name mejor (el tachado es que no estará en la siguiente versión)
        print(threading.current_thread().getName(),
              'con identificador:', threading.current_thread().ident,
              'Contador:', contador, '\nHemos contado en ', tiempo_proceso)

    nombre_hilo = threading.current_thread().name # Forma correcta.
    print(f"******Hilo {nombre_hilo} ha finalizado!******")


# target nos permite indicarle que función se va a ejecutar en el hilo.
hilo1 = threading.Thread(target=contar, args=[0.3])
hilo1.name = "Proceso Rápido"

hilo2 = threading.Thread(target=contar, args=[0.6])
hilo2.name = "Proceso Lento"

hilo1.start()
hilo2.start()


for i in range(15):
    print(f"Hola número {i} - Parando 0.5 segundos")
    time.sleep(0.5)


if hilo1.is_alive():
    print("El hilo 1 está vivo\n")

# Ejemplo de hilos

# Digamos que con el time.sleep se va ejecutando lo que viene después.


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

'''
import threading
import time

# Ejemplo cambiado
def contar(lag):
    """Contar hasta 25"""
    contador = 0
    while contador < 25:
        start_counting = time.time()
        contador += 1
        if lag == "input":
            _ = input("Inserta un número rápido: ")
        else:
            time.sleep(lag)
        stop_counting = time.time()
        tiempo_proceso = stop_counting - start_counting

        # El método getName nos retorna el nombre del hilo que se está ejecutando.
        # Si esta tachado, es que esta bajo aviso de "deprecation"
        # Cambiará en la siguiente versión del módulo.
        # Podemos usar: threading.current_thread().name mejor (el tachado es que no estará en la siguiente versión)
        print(threading.current_thread().getName(),
              'con identificador:', threading.current_thread().ident,
              'Contador:', contador, '\nHemos contado en ', tiempo_proceso)

    nombre_hilo = threading.current_thread().name # Forma correcta.
    print(f"******Hilo {nombre_hilo} ha finalizado!******")


# target nos permite indicarle que función se va a ejecutar en el hilo.
hilo1 = threading.Thread(target=contar, args=[3])
hilo1.name = "Proceso Rápido"

hilo2 = threading.Thread(target=contar, args=["input"])
hilo2.name = "Proceso Lento"

hilo1.start()
hilo2.start()

for i in range(15):
    print(f"Hola número {i} - Parando 0.5 segundos")
    time.sleep(0.5)

if hilo1.is_alive():
    print("El hilo 1 está vivo")
'''

import threading
import time

class MiHilo(threading.Thread):
    # Función inicio del hilo
    def __init__(self):
        threading.Thread.__init__(self)
        self.stoprequest = threading.Event()
        # podemos asignar un nombre personalizado al hilo
        self.name = "******* Hilo 1 *******"

    def run(self):
        for i in range(0, 10):
            time.sleep(1.26)
            print(f"Hilo: {self.name} contando por {i}")
            # dormimos el hilo para dar oportunidad a los demás hilos.
            # tiempo en segundos
            # quitamos esta línea después para ver que no van en paralelo

class Hilo2(threading.Thread):
    # Funcióninicio del hilo
    def __init__(self):
        threading.Thread.__init__(self)
        self.stoprequest = threading.Event()
        # podemos asignar un nombre personalizado al hilo
        self.name = "******* Hilo 2 *******"

    def run(self):
        for i in range(0, 10):
            time.sleep(2)
            print(f"Hilo: {self.name} contando por {i}")
            # dormimos el hilo para dar oportunidad a los demás hilos.
            # tiempo en segundos
            # quitamos esta línea después para ver que no van en paralelo

hilo1 = MiHilo()
hilo2 = Hilo2()
hilo1.start()
hilo1.join()
hilo2.start()

# podemos asignar prioridades a los hilos mediante join

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

import tkinter as tk

window = tk.Tk()
# Podemos ir moviendo el inicio -> window.mainloop()
window.title("Bienvenidos a la App.")
window.geometry('700x400')

fonts = ['Comic Sans MS', 'Arial']

etiqueta1 = tk.Label(window, text="Hola otra vez 1,1", font=(fonts[0], 50))
etiqueta1.grid(column=0, row=1)

etiqueta2 = tk.Label(window, text="Hola en el 0,0", font=(fonts[1], 25))
etiqueta2.grid(column=0, row=0)

fichero = open('texto.txt', 'r')

def clicked1():
    texto = fichero.readline()
    etiqueta1.configure(text=texto, font=(fonts[-1], 40))

boton1 = tk.Button(window, text="Click Aqui", command=clicked1)
boton1.grid(column=1, row=0)

entrada = tk.Entry(window, width=10)
entrada.grid(column=1, row=3)

def resetear_archivo():
    fichero.seek(0)

btn2 = tk.Button(window, text="Leer Texto", command=resetear_archivo)
btn2.grid(column=2, row=3)

window.mainloop()

'''
Para crear un ejecutable portable:
En la terminal:
pip install pyinstaller
pyinstaller --onefile tkinter_example.py
# el ejecutable estará en el directorio /dist'''