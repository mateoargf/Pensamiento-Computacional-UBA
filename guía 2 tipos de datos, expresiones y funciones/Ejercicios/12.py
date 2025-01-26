# 12. Obtener una palabra, borrarle todas las ‘a’ e imprimirla por pantalla (pista: usar una función predefinida
# de Python).
# Recibe un parámetro e identifica las 'a'
def filtrar_caracter(mens):
     return mens.replace('a', '')

mensaje = input('Ingrese su palabra: ')

nuevo_mens = filtrar_caracter(mensaje)

print(nuevo_mens)
