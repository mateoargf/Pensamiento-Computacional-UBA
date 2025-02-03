# 10. Crear una función que simule un cumpleaños: que dado un entero imprima “Que los cumplas feliz” esa
# cantidad de veces.

# Recibe un parámetro y le canta cumpleaños feliz la cantidad de veces respectivamente
def cantar_cumple(anios):
     for i in range(1, anios + 1):
          print(f'Que los complas feliz')

print('Ingrese su edad de cumpleaños')

usuario = int(input('Ingrese el entero de edad: '))

cantar_cumple(usuario)