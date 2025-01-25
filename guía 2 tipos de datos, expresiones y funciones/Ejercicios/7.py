# 7. Crear una función que una un string y un entero, ambos dentro de un string.

# Recibe dos parámetros (str, int) y devuelve ambos en un str
def convertir_en_string(str, int):
      return (f'uniendo {str} y {int}')

valor1 = str(input('Ingrese un string: '))
valor2 = int(input('Ingrese un entero: '))    

nueva_frase = convertir_en_string(valor1, valor2)

print(nueva_frase)
