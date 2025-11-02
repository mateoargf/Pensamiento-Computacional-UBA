# numero = None
# while type(numero) is not int:
#    try:
#       numero = input('Ingresá un número entero: ')
#       numero = int(numero)
#       print('Tu número entero es ', int(numero))
#    except ValueError:
#       print('El valor ingresado no es válido.')
      
# def probar_finally():
#    try:
#       return 2
#    finally:
#       print("Código del bloque finally")
# probar_finally()

# x = 10
# if x > 5:
#    raise Exception(f'No debe exceder 5. El valor es: {x}')

def calcular_division(x, y):
   print(f'\nDividiendo {x} sobre {y}')
   try:
      cociente = x / y
   except ZeroDivisionError:
      print('No se puede dividir por cero.')
   else:
      print(f'El cociente es: {cociente}')
   finally:
      print('El bloque finally siempre se ejecuta.')

calcular_division(15,0)
calcular_division(15,5)