# 1. Escribir la expresión para saber si un número es más grande que otro. Guardarla en una variable de tipo
# bool e imprimirla por pantalla para ver su valor.

def validar_mayor(a,b):
     if a >= b:
          return a
     return b

print('Ingrese dos valores enteros')
valor_a = int(input('Ingrese el primer entero: '))
valor_b = int(input('Ingrese el segundo entero: '))

el_mayor = validar_mayor(valor_a,valor_b)

print(f'El mayor valor es: {el_mayor}')