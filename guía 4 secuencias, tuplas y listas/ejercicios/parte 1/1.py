# 1. Crear una lista con los números del 1 al 10. Acceder con el índice a la posición que contiene el número
# 5, e imprimirlo por pantalla. Recordar que el índice de las listas empiezan con 0

numeros = list(range(1,11))

posicion = numeros.index(5)
print(f'El número 5 se encunetra en la posición: {posicion}')