# 6. Hacer una lista con 5 nombres, y realizar las siguientes actividades con la misma:
# a. Cambiar el último elemento de la lista y cambiar el último nombre por “Juan”. Olvidándonos de
# que sabemos que tiene 5 elementos, ¿Cómo podría saber cuál es el último elemento si no sé la
# longitud?
# b. Devolver el nombre que esté a dos posiciones del final. ¿Cómo hacemos para que nos funcione
# para cualquier lista y no solo para la que tenga 5 elementos?
# c. Recorrer la lista e imprimir cada nombre por pantalla.
# d. Imprimir por pantalla la lista con 3 repeticiones, usar el operador repetición (*).

# Recibe un parámetro y retorna el ultimo valor de la lista

nombres= ['Martin', 'Mateo', 'Jose', 'Julian', 'Manuel']

# Recibe un parámetro y elimina el último de la lista para sustituirlo por otro nombre
def cambiar_ultimo(nombres):
     ultimo= len(nombres) -1
     nombres.pop(ultimo)
     nombres.append(input('Agregar nuevo nombre: '))
     return nombres

print(f'La lista anterior: {nombres}')
         
nueva_lista= cambiar_ultimo(nombres)


print(f'La lista actual: {nueva_lista}')