# 10. Crear una lista que contenga los números del 1 al 10, luego recorrerla y guardar en otra lista esos
# números elevados al cuadrado. 

def elevar_cuadrado(n):
     return n * n

numeros = [1,2,3,4,5,6,7,8,9,10]

cuadrados = list(map(elevar_cuadrado, numeros))

print(cuadrados)