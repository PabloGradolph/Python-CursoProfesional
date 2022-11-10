# Curso profesional de Python (AEPI): 6_Ejercicios
# Autor: Pablo Gradolph Oliva
# 05/07/2022



# 1 - Sin modificar directamente el texto, utilizando todo lo que sabes sobre cadenas, listas, sus métodos internos...
# Transforma este texto:

'''
un día que el viento soplaba con fuerza#mira como se mueve aquella bandolera -dijo un monje#lo que se mueve es el viento
-respondió otro monje#ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro.
'''

# En este otro:

'''
Un día que el viento soplaba con fuerza...
--Mira como se mueve aquella banderola -dijo un monje.
--Lo que se mueve es el viento -respondió otro monje.
--Ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro.
'''

# CÓDIGO:
primer_texto = "un día que el viento soplaba con fuerza#mira como se mueve aquella bandolera -dijo un monje#lo que se "\
               "mueve es el viento -respondió otro monje#ni las banderolas ni el viento, " \
               "lo que se mueve son vuestras mentes -dijo el maestro"

print(f"Transformando el texto: \n{primer_texto}")

lista_en_lineas = primer_texto.split("#")

lineas_en_mayúsculas = []
for i in lista_en_lineas:
    lineas_en_mayúsculas.append(i.capitalize())

lineas_en_mayúsculas_con_puntos = []
for i in lineas_en_mayúsculas:
    if i == lineas_en_mayúsculas[0]:
        lineas_en_mayúsculas_con_puntos.append(i + "...")
    else:
        lineas_en_mayúsculas_con_puntos.append(i + ".")

lineas_en_mayúsculas_con_puntos_y_guiones = []
for i in lineas_en_mayúsculas_con_puntos:
    if i != lineas_en_mayúsculas_con_puntos[0]:
        lineas_en_mayúsculas_con_puntos_y_guiones.append("-- " + i)
    else:
        lineas_en_mayúsculas_con_puntos_y_guiones.append(i)

texto_final = "\n".join(lineas_en_mayúsculas_con_puntos_y_guiones)
print()
print("En:")
print(texto_final)
