# 9. Se quiere mejorar el programa para enseñar matemáticas pensado en el ejercicio anterior. Ahora se
# necesita una funcionalidad que permita a los niños aprender las tablas. Crear una función que reciba un
# número entero e imprima por pantalla la tabla de ese número del 1 al 10.

# Recibe un parámetro que devuelve las tablas del 1 al 10 del mismo
def devolver_tablas(valor):
     for i in range(1, 10):
          mult = valor * i
          print(f'{valor} x {i} = {mult}')

print('Aprendamos las tablas del 1 al 10')

usuario = int(input('Ingrese su entero: '))

devolver_tablas(usuario)