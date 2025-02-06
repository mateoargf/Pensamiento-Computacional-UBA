# Métodos de Listas:
# append(valor) # -> Agrega el elemento valor al final de la lista. -> lista = [2, 3, 5] lista.append(1)
# # la lista queda: [2, 3, 5, 1]
# insert(posición, valor) # -> Inserta el elemento valor en la posición posición. -> lista = ['h', 'l', 'a'] lista.insert(1, 'o')
# # la lista queda: ['h', 'o','l', 'a']
# remove(valor) # -> Quita de la lista el elemento valor. -> lista = [1, 3, 5] lista.remove(3)
# # la lista queda: [1, 5]
# pop([índice]) # -> Quita de la lista el elemento de la posición índice. Si no se usa este parámetro, se quita el último elemento. -> lista = ['d', 'i', 'a', 'a'] valor = lista.pop()
# # la lista queda: ['d', 'i','a'] y en la variable valor queda guardado el elemento que sacamos (en este caso 'a')
# extend(otra_lista) # ->  Agrega al final de la lista otra_lista -> lista = [1, 2, 2] otra_lista = [4, 7] lista.extend(otra_lista)
# # la lista queda: [1, 2, 2, 4,7]
# sort([reverse=True], [key=función]) # -> Ordena la lista. Si se emplea el parámetro reverse, en orden descendente, si se usa key, con criterio de ordenamiento función. -> lista = [1, 4, 3, 2] lista.sort()
# # la lista queda: [1, 2, 3, 4]
# reverse() # -> Invierte el orden de la lista (el primero pasa a ser último) -> lista = ['h', 'o', 'l', 'a'] lista.reverse()
# # la lista queda: ['a', 'l','o', 'h']
# count(valor) # -> Cuenta la cantidad de apariciones de valor en la lista. -> lista = [4, 1, 2, 5, 1] cantidad = lista.count(1)
# # la lista queda igual y cantidad vale 2 porque el 1 aparece dos veces
# index(valor) # -> Devuelve la posición de la primera aparición de valor en la lista. -> lista = [1, 4, 3, 2] lugar = lista.index(4)
# # la lista queda igual y lugar vale 1 porque el 4 está en la posición 1

# lista=['Juan','ana','sergio','ELEna','ELEONORA','anALía']
# print('Lista Inicial')
# for n in lista:
#  print (n)
# for n in range(len(lista)):
#      lista[n] = lista[n].lower()
# lista.sort()
# print ()

# print('Lista Ordenada')
# for n in lista:
#  print (n)

# lista=['Juan','ana','sergio','ELEna','ELEONORA','anALía']
# print('Lista Inicial')
# for n in lista:
#  print (n)
# lista.sort(key=str.lower)
# print()
# print('Lista Ordenada')
# for n in lista:
#  print (n)

lista=['Juan','ana','sergio','ELEna','ELEONORA','anALía']
print('Lista Inicial')
for n in lista:
 print (n)
lista.sort(key=len)
print()
print('Lista Ordenada')
for n in lista:
 print (n)
 
def cant_vocales(palabra):
     palabra = palabra.lower()
     cant = 0
     for v in ('a','e','i','o','u','á','é','í','ó','ú'):
          cant += palabra.count(v)
          return cant
lista = ['Juan','ana','sergio','ELEna','ELEONORA','anALía']

print('Lista Inicial')
for n in lista:
     print (n)
lista.sort(reverse=True, key=cant_vocales)
print()

print('Lista Ordenada')
for n in lista:
     print (n)
     
# Map(): -> map(función,secuencia) 

def cuadrado(num):
     return num * num
lista= [3,6,1,2]
print(f'Lista: {lista}')

new_list= list(map(cuadrado, lista))
print(f'Nueva lista: {new_list}')
nueva_lista = map(cuadrado, lista)

for n in new_list:
     print(n)

# Filter(): -> filter(función,secuencia)

def empieza_con_m(palabra):
     return palabra[0] == 'm'

lista = ["manzana", "balde", "molde", "marrón", "carro", "pera"]
print("Lista: ")

for i in lista:
     print(i)

print()

nueva_lista= list(filter(empieza_con_m,lista))
print('Nueva lista: ')
for n in nueva_lista:
     print(n)
   
# Obtenemos lista con los cuadrados y los num pares 
def cuadrado(x):
     return x ** 2

def par(x):
     if x%2==0:
          return True
     else:
          return False
     
lista=[1,2,3,4,5,6]

print('Lista Original')
print(lista)

lis = list(map(cuadrado,lista))
print('Lista de cuadrados')
print(lis)

filtro= list(filter(par,lista))
print('Lista de pares:')
print(filtro)