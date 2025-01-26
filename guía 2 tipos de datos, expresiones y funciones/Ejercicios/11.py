# 11. Obtener una palabra e imprimir los primeros 5 caracteres (pista: slicear la palabra).

# Recibe un parámetro palabra y devuelve los primeros 5 caracteres
def devolver_caracteres(palabra):
     
     return palabra[:5:]

palabra = input('Ingrese una palabra: ')

cinco_caracteres = devolver_caracteres(palabra)

print(cinco_caracteres)