# 6. Para jugar al chinchón con un único mazo de cartas españolas, el número de jugadores puede ser: dos,
# tres o cuatro. Crear una función que pida al usuario informar el número de jugadores, considerando
# que este puede ingresar:
# ● un valor no válido, por ejemplo, una palabra.
# ● un valor menor a 2, en en cuyo caso, mostrar el mensaje "Debe haber al menos 2 jugadores."
# ● un valor mayor a 4, en cuyo caso, mostrar el mensaje "Se puede jugar con un máximo de 4
# jugadores."
# ● un valor válido, en cuyo caso, mostrarlo.

def validar_cant_jugadores():
   numero= 0
   while not ( 2 <= numero <= 4) :
      try:
         numero = int(input('Ingrese la cantidad de jugadores: '))
         
         if numero < 2:
            print('Debe haber al menos 2 jugadores.')
         elif numero > 4:
            print('Se puede jugar con un máximo de 4 jugadores')
         else:
            print(f'El número de jugadores será: {numero}')
      except ValueError:
         print('Ingresó un dato inválido.')
         
validar_cant_jugadores()
