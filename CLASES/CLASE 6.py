# CLASE DEL DÍA 07/07/2022

# FUNCIONES RECURSIVAS
def cuenta_atras(numero):
    numero -= 1
    if numero > 0:
        print(numero)
        cuenta_atras(numero)
    else:
        print("Fin de la función recursiva")

cuenta_atras(5)

# GESTIÓN DE EXCEPCIONES O DE ERRORES
def dividir(numero1, numero2):
    return (numero1+numero2)/numero2

# Dividir por cero no está programado como infinito en python
# Utilizamos los try/ except para que siga ejecutando
try:
    valor = dividir(8, 0)
    print(valor)
except:
    print("Hay un error")

# Estos errores es preferible controlarlos de antemano con while o if
try:
    print("Dame un numero")
    numero1 = int(input())
    print("Dame otro numero")
    numero2 = int(input())
except ValueError: # Gestiona un error en concreto
    print("Numero incorrecto")
else: # Esto se ejecuta si todo ha ido bien
    print(numero1 + numero2)

# Uno mejor hecho
while True:
    try:
        n1 = float(input("Numero 1: "))
        n2 = float(input("Numero 2: "))
        resultado = n1/n2
    except ValueError as error:
        print("Estas metiendo algo que no es un numero.")
        print(error)
    except ZeroDivisionError as error:
        print("Estas dividiendo por cero.")
        print(error)
    else:
        print(f"Resultado: {resultado}")
        break

# TRABAJAR CON FECHAS Y HORAS
from datetime import *

# Obteniendo la fecha actual
now = datetime.now()
print(now)

# Sacar una en concreto
print("Día:", now.day)
print("Mes:", now.month)
print("Año:", now.year)
print("Hora:", now.hour)
print("Minuto:", now.minute)
print("Segundo:", now.second)
print("Microsegundo:", now.microsecond)

# Aumento de tiempos
print(now + timedelta(days=5))
print(now + timedelta(days=545))
print(now + timedelta(days=8, minutes=25, hours=15))

# Formateando fechas
print(now.strftime("%d-%m-%Y %H:%M:%S"))
print(now.strftime("%d---%m---%Y %H:-%M:-%S"))