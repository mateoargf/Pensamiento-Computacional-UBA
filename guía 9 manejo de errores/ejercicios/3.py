# 3. Se quiere hacer un programa que le solicite al usuario un número divisor y un dividendo, y calcule el
# cociente entre ellos.
# AYUDA: Considerar que el usuario podría brindar un valor no numérico o un divisor nulo.
      
def validar_entero():
   z = input('Ingresá un número entero: ')
   while not z.isnumeric():
      try:
         z = input('Ingresá un número entero: ')
         return int(z)
      except ValueError:
         print('Es un dato inválido.')
      except ZeroDivisionError:
         print('No se puede dividir por cero.')
         
divisor = validar_entero()
dividendo = validar_entero()

z = divisor/dividendo
print(f'La división entre {divisor} / {dividendo} = {z}')