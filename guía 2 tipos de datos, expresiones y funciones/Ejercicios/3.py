# 3. Crear un programa que le solicite al usuario un entero y determine si es par, mostrando por pantalla un
# mensaje que indique el resultado.
# Para determinar si un número es par o impar, se puede determinar con el uso del operador %, les
# dejamos a ustedes el cómo.

# recibe un entero y determina si es par
def validar_par(entero):
     if entero % 2 == 0: 
          return (f'el número: {entero} es par')
     else:
          return (f'el número: {entero} es impar')
     
numero = int(input('ingresar un entero y calculará si es par o impar: '))
resultado = validar_par(numero)

print(resultado)