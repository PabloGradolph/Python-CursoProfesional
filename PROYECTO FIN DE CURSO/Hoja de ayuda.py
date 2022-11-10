
def ra():
    INVALIDOS = {"00000000T", "00000001R", "99999999R"}
    while True:
        numero = input("Introduzca únicamente los números de su DNI ")
        if len(numero) == 8:
            intnumero = int(numero)
            diccionario = {0:"T",1:"R",2:"W",3:"A",4:"G",5:"M",6:"Y",7:"F",8:"P",9:"D",10:"X",
                       11:"B",12:"N",13:"J",14:"Z",15:"S",16:"Q",17:"V",18:"H",19:"L",
                       20:"C",21:"K",22:"E"}
            resto = intnumero%23
            letra = diccionario[resto]
            DNI = numero + letra
            if DNI in INVALIDOS:
                print("Número de DNI incorrecto, por favor, vuelva a intentarlo.")
            else:
                break
        else:
            print("Número de DNI incorrecto, debe tener 8 caracteres. Por favor, vuelva a intentarlo.")
    return DNI

print(ra())

import phonenumbers
def comprobar_telefono():
    while True:
        try:
            telefono = input("Inserte el teléfono del paciente: ")
            clave_pais = "+34"
            telefono_completo = clave_pais + telefono
            phone = phonenumbers.parse(telefono_completo, "ES")
            if phonenumbers.is_valid_number(phone) == False:
                print("Número de teléfono no válido. Por favor, inténtelo de nuevo.")
                continue
            return telefono_completo
        except:
            print("Número de teléfono no válido. Por favor, inténtelo de nuevo.")


telefono = comprobar_telefono()
print(telefono)


import datetime
from Clase_pacientes import pacientes, Pacientes


paciente = pacientes.select().where(pacientes.id == max(pacientes.id))
if paciente.exists():
    paciente = pacientes.get(pacientes.id == max(pacientes.id))
    with open("aciertos.txt", "a+", encoding="utf-8") as f:
        texto = f"El registro con nombre: {paciente.nombre} y DNI: {paciente.DNI} se ha insertado correctamente el" \
                f"día {str(datetime.now())}"
        total_lines = sum(1 for line in f)
        if total_lines < 25:
            f.write(texto)
        else:
            lines = f.readlines()
            lines.pop(0)
            for line in lines:
                f.write(line)
            f.write(texto)
else:
    print("Se ha producido algún tipo de error, por favor, inténtelo más tarde.")

import pytz
def insertar_texto_errores():
    tz = pytz.timezone('Europe/Madrid')
    with open("errores.txt", "a+", encoding="utf-8") as f:



        total_lines = sum(1 for line in f)
        if total_lines < 25:
            f.write(texto)
        else:
            lines = f.readlines()
            lines.pop(0)
            for line in lines:
                f.write(line)
            f.write(texto)


with open("aciertos.txt", "a+", encoding="utf-8") as fichero:

    lineas = []
    lines = fichero.readline()

    for linea in lines:
        lineas.append(linea.strip("\n"))
    print(lineas)
    '''
    if len(lineas) < 3:
        f.write(f"{texto}\n")
    else:
        lineas.pop(0)
        for line in lineas:
            f.write(f"{line}\n")
        f.write(f"{texto}\n")'''





from tkinter import filedialog

archivo = filedialog.openfile(title="Abrir archivo")