# Archivo .py con la tarea asíncrona en la que se leerán los archivos txt.

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# IMPORTACIONES
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
import threading
import time
import webbrowser as wb

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# CLASES/HILOS
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Hilo que revela el contenido del archivo 'Registros Correctos'.
# Se abre directamente el archivo, no se imprime por consola, ya que entorpecería el funcionamiento del programa.
# Para esto utilizamos el módulo webbrowser.
# Hacemos que se muestre cada 30 segundos para que no moleste demasiado.
class LeerFicherosAciertos(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.stoprequest = threading.Event()
        # podemos asignar un nombre personalizado al hilo
        self.name = "******* IMPRIMIENDO ÚLTIMOS REGISTROS *******"

    def run(self):
        while True:
            time.sleep(30)
            wb.open(r"Registros Correctos.txt")

# Hilo que revela el contenido del archivo 'Registros Erróneos'.
# Se abre directamente el archivo, no se imprime por consola, ya que entorpecería el funcionamiento del programa.
# Para esto utilizamos el módulo webbrowser.
# Hacemos que se muestre cada 30 segundos para que no moleste demasiado.
class LeerFicherosErrores(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.stoprequest = threading.Event()
        # podemos asignar un nombre personalizado al hilo
        self.name = "******* IMPRIMIENDO ÚLTIMOS REGISTROS INCORRECTOS *******"

    def run(self):
        while True:
            time.sleep(30)
            wb.open(r"Registros Erróneos.txt")



