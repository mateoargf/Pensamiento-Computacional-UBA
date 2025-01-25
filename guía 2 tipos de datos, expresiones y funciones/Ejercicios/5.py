# 5. Crear un programa que le solicite al usuario 5 enteros y muestre por pantalla el promedio de ellos.
# Es muy común usar variables para acumular valores

# Recibe 5 enteros y hace el promedio
def calcular_promedio(a, b, c, d, e):
     promedio = (a + b + c + d + e)/5
     return promedio
     
num1 = int(input('Ingrese un entero: '))
num2 = int(input('Ingrese un entero: '))
num3 = int(input('Ingrese un entero: '))
num4 = int(input('Ingrese un entero: '))
num5 = int(input('Ingrese un entero: '))

resultado = calcular_promedio(num1, num2, num3, num4, num5)

print(f'El promedio es: {resultado}')