# Listas: al ser secuencia tiene un ordem
# list = [] -> vacía
# a=[1,2,3]
# b=[1,2,3] -> Error: no son iguales, son variables completamente diferentes
# segundo caso:
# a = [1,2,3]
# b = a
# print(b) -> En este caso b es una referencia de la variables a. Si modificamos una de las dos, el cambio se ve reflejado en ambas variables

# a = [1,2,3]
# b = a.copy() -> el método copy() nos permite emplear una copia y almacenar un registro puro de la primer lista a

# a[2] = 4
# print(f'lista a: {a}')
# print(f'lista b: {b}')

# La operación: A diferencia de con las tuplas, es válida.

# lis = [1,2,'ya']
# lis[2] = 3

# print(lis)

# a lis podemos emplear métodos que agregan un cajoncito a la estructura y permiten colocar algo dentro (append(), insert(),extend()) o quitárselos también (pop(),remove(),clear())
# lis.append(4) -> En Python, todas las funciones y métodos que no devuelven nada (no hay return en su cuerpo) devuelven la constante nula None.
# print(lis)

# lis.remove(4)
# print(lis)

# Métodos Específicos de la clase list (Lista):
append(valor) # -> Agrega el elemento valor al final de la lista. -> miLista.append(5)
insert(posic,valor) # -> Inserta el elemento valor en la posición posic. -> miLista.insert(2, 10)
remove(valor) # -> Quita de la lista el elemento valor. -> miLista.remove(7)
pop([índice]) # -> Quita de la lista el elemento de la posición índice. -> valor = miLista.pop(3)
extend(otraLista) # -> Agrega los elementos de otraLista al final de la lista. -> miLista.extend([8, 9, 10])
sort() # -> Ordena la lista. -> miLista.sort()
sorted() # -> Devuelve una nueva lista ordenada (sin modificar la original). -> lista_ordenada = sorted(miLista)
reverse() # -> Invierte el orden de la lista. * puede que este método no esté habilitado para su uso en la herramienta replit. En ese caso, se recomienda este sustituto: miLista[::-1] -> miLista.reverse()
count(valor) # -> Cuenta la cantidad de apariciones de valor en la lista. Este método es válido para cualquier secuencia. -> cantidad = miLista.count(5)
index(valor) # -> Devuelve el índice de la primera aparición de valor. Este método es válido para cualquier secuencia. -> indice = miLista.index(8)
len() # -> Devuelve la longitud de la lista. Este método es válido para cualquier secuencia. -> longitud = len(miLista)
clear() # -> Elimina todos los elementos de la lista. Otra opción es pisar el valor de la lista con una lista vacía: miLista = [] -> miLista.clear()
copy() # -> Crea una copia superficial de la lista. -> copia = miLista.copy()
max() # -> Devuelve el valor máximo de la lista. -> maximo = max(miLista)
min() # -> Devuelve el valor mínimo de la lista. -> minimo = min(miLista)
sum() # -> Devuelve la suma de los elementos de la lista. -> suma = sum(miLista)

#Ej de carga e impresión de listas
nombres= []

nom = input('Ingrese un nombre, * para salir: ')
while nom != '*':
     nombres.append(nom)
     nom = input('Ingrese un nombre, * para salir: ')

print('Lista de nombres')
print(nombres)
print('Salida detallada')
for n in nombres:
     print(n)
     
#Ejemplo con Listas
# for con una parte de lista, imprime la primera parte y otro for la segunda
from random import randint
a= []
for i in range(20):
     a.append(randint(1,35))
print('Segunda mitad')
for n in a[10:]:
     print(n, end=' ')
print()
print('Primera mitad')
for n in a[:10]:
     print(n, end=' ')
print()
