# 2. Crear una función, utilizando el punto anterior, que le pida al usuario un número entero. Utilizarla para calcular el producto entre dos números enteros ingresados
x = input('Ingresá un número entero: ')
y = input('Ingresá un número entero: ')

      
def validar_entero(z):
   while not z.isnumeric():
      try:
         z = input('Ingresá un número entero: ')
         return int(z)
      except ValueError:
         print(f'{z}: es un dato inválido.')
         
x = validar_entero(x)
y = validar_entero(y)

z = x*y
print(f'El producto entre {x} X {y} = {z}')