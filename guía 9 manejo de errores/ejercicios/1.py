# 1. Se quiere hacer un programa para pedirle al usuario que ingrese un número entero, y en caso de que el
# valor ingresado no sea un número entero, mostrarle un mensaje apropiado.
# a. Realizarlo utilizando isnumeric(). ¿Qué limitaciones encuentra?
# b. Realizarlo utilizando try/ except.

numero = input('Ingresá un número entero: ')

while not numero.isnumeric():
   try:
      numero = input('Ingresá un número entero: ')
      print(f'Tu número entero es: {int(numero)}')
   except ValueError:
      print(f'{numero}: es un dato inválido.')
      