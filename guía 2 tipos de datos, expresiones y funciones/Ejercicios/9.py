# 9. Pedirle nombre y apellido por separado e imprimir “Apellido, Nombre”.
# Este proceso se llama concatenar cadenas.

# Recibe dos parámetros y los une en una cadena de texto
def retornar_nombre(a, b):
     return(f'{b}, {a}')

nombre = input('Ingrese su nombre: ')
apellido = input('Ingrese su apellido: ')

union = retornar_nombre(nombre, apellido)

print(union)
