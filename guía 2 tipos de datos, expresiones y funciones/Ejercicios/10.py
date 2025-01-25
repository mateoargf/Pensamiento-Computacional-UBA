# 10. Obtener una palabra e imprimir la cantidad de letras.

# Recibe un parámetro string y devuelve la cantiad de letras
def devolver_length(x):
     return len(x)


palabra = input('Ingrese su palabra: ')
total_letras = devolver_length(palabra)

print(f'su total de letras es: {total_letras}')