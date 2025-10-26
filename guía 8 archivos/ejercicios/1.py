# 1. Se tiene un archivo con la pregunta “¿Cómo estás hoy?” llamado pregunta.txt. Se pide leerlo y mostrar
# la pregunta por pantalla para luego pedirle al usuario que ingrese una respuesta. Después, guardar la respuesta
# dada por el usuario en el archivo.
# Por ejemplo, se tiene el archivo pregunta.txt que originalmente tiene:
# ¿Cómo estás hoy?
# Y el usuario da la respuesta: “¡Bien, porque me comí una hamburguesa!”
# Entonces el archivo debería quedar de la forma:
# ¿Cómo estás hoy?
# ¡Bien, porque me comí una hamburguesa!

pregunta = open('\\Users\\mgfleytas\\Pensamiento-Computacional-UBA\\guía 8 archivos\\ejercicios\\pregunta.txt', encoding='utf-8')

line = pregunta.readline()
print(line)

rta = input('')

pregunta = open('\\Users\\mgfleytas\\Pensamiento-Computacional-UBA\\guía 8 archivos\\ejercicios\\pregunta.txt', 'a', encoding='utf-8')

pregunta.writelines(f'\n {rta}')

pregunta.close()