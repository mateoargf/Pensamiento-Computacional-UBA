# 2. Crear un programa que le solicite al usuario dos números enteros y luego imprima por pantalla:
# ● la suma de ambos números
# ● la resta de ambos números
# ● la multiplicación de ambos números
# ● la división entera de ambos números
# ● el resto
# Más adelante podríamos crear nuestra propia calculadora :)

# Recibe dos enteros y ejecuta las operaciones matemáticas: +,-,*,/,//,%
def calcular(a,b):
     sum = a + b
     rest = a - b
     mult = a * b
     div_decimal = a / b
     div_entero = a // b
     resto = a % b
     return (f'la suma: {sum}, resta: {rest}, multiplicación: {mult}, división decimal: {div_decimal}, división entera: {div_entero}, resto: {resto}')

num1 = int(input('ingrese un entero: '))
num2 = int(input('ingrese otro entero: '))

resultados = calcular(num1, num2)

print(resultados)
