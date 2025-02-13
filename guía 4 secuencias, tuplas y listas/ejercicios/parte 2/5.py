# 5. Agustina está jugando a las cartas con sus amigos. A ella le gusta tener las cartas de su mano bien ordenadas. Esto significa que cada vez que tiene que agarrar una nueva carta, la quiere agregar a su mano en el lugar indicado para no romper el orden.
# Si se tiene una lista de enteros ordenadas de mayor a menor. Hacer una función que según esta lista inserte un nuevo entero, manteniendo el orden.
# Podemos pensar la lista de cartas como números enteros.
# Ejemplo:
# cartas: [1, 4, 6, 8]
# carta nueva: 5
# La lista de cartas debería quedar: [1, 4, 5, 6, 8]
# Tratar de pensar una solución sin usar el método sort. (no es obligatorio).

# Recibe un mazo de parámetro y devuelve en orden descendente
def ingresar_carta(mazo):
     nueva = -1
     while nueva != 0:
          mazo_actual = ordenar(mazo)
          print(f'El mazo anterior: {mazo_actual}')
          nueva = int(input('Ingrese una carta, 0 si desea salir: '))
          if nueva in mazo_actual:
               print(f'Existe la carta {nueva}, pruebe un número nuevo')
               continue
          elif nueva == 0:
               print(mazo_actual)
               break
          elif not(nueva in mazo_actual) and (nueva != 0):
               mazo.append(nueva)
               mazo_actual = ordenar(mazo)
     return(print(f'El mazo actual: {mazo_actual}'))
# Recibe un mazo y devuelve en orden descendente              
def ordenar(mazo):
     mazo_nuevo = []
     pos = -1
     for i in mazo:
          pos += 1
          index_i = 0 
          mayor = -1
          for j in mazo:
               if (i >= j) and (i > mayor):
                    mayor = i
               elif (i < j) and (j > mayor):
                    index_i += 1
                    mayor = j
                 
          mazo_nuevo.insert(pos,mayor)
          
          if mayor != i:
               mazo_nuevo.insert(pos + index_i, i)
     return mazo_nuevo  

# Recibe un mazo de parámetro y devuelve en orden descendente
def devolver_mazo(mazo):
     nueva = -1
     mazo.sort(reverse=True)
     print(f'El mazo anterior: {mazo}')
     while nueva != 0:
          nueva = int(input('Ingrese una carta, 0 si desea salir: '))
          if nueva in mazo:
               print(f'Existe la carta {nueva}, pruebe un número nuevo')
               continue
          elif nueva == 0:
               print(mazo)
               break
          else:
               mazo.append(nueva)
               mazo.sort(reverse=True)
     return(print(f'El mazo actual: {mazo}'))  
     
cartas = [1, 4, 6, 8]

devolver_mazo(cartas)