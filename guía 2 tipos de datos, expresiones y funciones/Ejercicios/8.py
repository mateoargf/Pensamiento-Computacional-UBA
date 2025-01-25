# 8. Crear una función que reciba dos enteros y que retorne (devuelva) el resto y el cociente

# Recibe dos parámetros y retorna resto y cociente
def calcular_resto_cociente(a,b):
     resto = a % b
     cociente = a / b
     return(f'el resto es {resto} y el cociente {cociente}')

num1 = int(input('Ingrese un entero: '))
num2 = int(input('Ingrese un entero: '))

resultado = calcular_resto_cociente(num1, num2)

print(resultado)