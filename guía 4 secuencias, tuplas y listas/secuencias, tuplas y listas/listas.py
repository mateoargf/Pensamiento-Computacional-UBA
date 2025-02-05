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

