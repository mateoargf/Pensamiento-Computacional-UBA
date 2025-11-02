# 7. Para jugar al truco con un único mazo de cartas españolas, el número de jugadores puede ser: dos,
# cuatro o seis. Crear una función que pida al usuario informar el número de jugadores, considerando
# que este puede ingresar:
# ● un valor no válido, por ejemplo, una palabra.
# ● un valor menor a 2, en en cuyo caso, mostrar el mensaje "Debe haber al menos 2 jugadores."
# ● un valor mayor a 6, en cuyo caso, mostrar el mensaje "Se puede jugar con un máximo de 6
# jugadores.".
# ● un valor impar, como 3 y 5, en cuyo caso, mostrar el mensaje "Debe haber un número par de
# jugadores.".
# ● un valor válido, en cuyo caso, mostrarlo.

def validar_cant_jugadores():
   numero= 0
   while numero not in [2,4,6] :
      try:
         numero = int(input('Ingrese la cantidad de jugadores: '))
         
         if numero < 2:
            print('Debe haber al menos 2 jugadores.')
         elif numero > 6:
            print('Se puede jugar con un máximo de 6 jugadores.')
         elif numero % 2 != 0:
            print('Debe haber un número par de jugadores.')
         else:
            print(f'El número de jugadores será: {numero}')
      except ValueError:
         print('Ingresó un dato inválido.')
         
validar_cant_jugadores()
