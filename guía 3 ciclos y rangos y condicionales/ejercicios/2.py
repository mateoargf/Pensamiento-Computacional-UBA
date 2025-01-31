# 2. Repetir el punto anterior pero con la expresión que determina que una letra NO es vocal.

# recibe un parámetro y devuevle si una letra no es vocal
def devolver_antivocal(letra):
     if (letra == 'a') or (letra == 'e') or (letra == 'i') or (letra == 'o') or (letra == 'u'):
          return(f'{letra}: es una vocal')
     return(f'{letra}: no es vocal')

print('Ingrese una letra: ')

letra = input('Ingrese su vocal: ')

respuesta = devolver_antivocal(letra)

print(respuesta)