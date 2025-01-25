# 6. Crear una función que reciba un número y muestre el anterior y el siguiente

# Recibe un número y muestra el anterior y el siguiente
def siguiente_anterior(x):
     anterior = x -1
     siguiente = x + 1
     return(f'El valor anterior es: {anterior} y el siguiente es: {siguiente}')

numero = int(input('Ingrese un entero: '))

resultados = siguiente_anterior(numero)

print(resultados)