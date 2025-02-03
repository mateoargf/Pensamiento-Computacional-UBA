# 8. Se quiere hacer un programa para enseñar a unos niños a contar. Crear una función que reciba un
# número entero e imprima por pantalla los números del 1 hasta ese número con la estructura de control
# iterativa for.

# Recibe un parámetro y devuelve el conteo desde el 1 hasta el valor correspondiente
def devolver_conteo(fin):
     for i in range(1, fin + 1):
          print(i)

print('Contaremos hasta donde puedas')

usuario = int(input('Ingrese un entero: '))   

devolver_conteo(usuario)