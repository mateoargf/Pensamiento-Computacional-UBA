# 4. Escribir un programa que le pida a un usuario su año de nacimiento y otro año, y le diga qué edad tenía
# el usuario en el año ingresado.

# Recibe dos enteros y calcula cuantos años tiene el usuario en el año indicado
def calcular_anio(nacimiento, seleccionado):
     edad = seleccionado - nacimiento
     return edad

anio_nacimiento = int(input('ingrese su año de nacimiento: '))
anio_x = int(input('ingrese un año x y calculará cuantos años tendrá: '))

resultado = calcular_anio(anio_nacimiento, anio_x)

print(f'su edad es de {resultado} años')