# 10. Crear una lista que contenga los números del 1 al 10, luego recorrerla y guardar en otra lista esos
# números elevados al cuadrado. 

def elevar_cuadrado(n):
     return n * n

numeros = list(range(1,11))

cuadrados = list(map(elevar_cuadrado, numeros))

print(cuadrados)