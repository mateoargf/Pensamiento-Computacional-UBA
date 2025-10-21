# 2. En un vivero se guardan las plantas en una lista de diccionario con la siguiente información: especie, si
# necesita luz solar o no, y el precio. (OBSERVACIÓN: ¿Qué tipo de dato nos permitía guardar si algo es
# verdad o no?). Ahora se necesita un sistema que guarde las plantas a medida que van llegando. Se pide
# hacer una función que reciba la lista de diccionarios de plantas, y los datos de la planta nueva y agregue
# esa planta a la lista de diccionarios.

def guardar_plantas(listado, especie, necesita_luz, precio):
   planta = {
      'especie': especie,
      'usa_luz': necesita_luz,
      'valor': precio
   }
   listado.append(planta)

vivero = []

guardar_plantas(vivero, 'jazmines', True, 1240.55)
guardar_plantas(vivero, 'rosas', True, 1549.10)
guardar_plantas(vivero, 'monsteras', False, 17400.30)

print(vivero)
