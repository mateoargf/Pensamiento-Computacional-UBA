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
     mazo_actual = ordenar(mazo)
     print(f'El mazo anterior: {mazo_actual}')
     nueva = -1
     while nueva != 0:
          nueva = abs(int(input('Ingrese una carta, 0 si desea salir: ')))
          if nueva in mazo_actual:
               print(f'Existe la carta {nueva}, pruebe un número nuevo')
               continue
          elif nueva == 0:
               print(mazo_actual)
               break
          else:
               mazo.append(nueva)
               mazo_actual = ordenar(mazo)
          return(print(f'El mazo actual: {mazo_actual}'))
# Recibe un mazo y devuelve en orden descendente              
def ordenar(mazo):
     mazo_nuevo = []
     pos = -1
     for i in mazo:
          pos += 1
          mayor = 0
          for j in mazo:
               if i >= j:
                    mayor = i
               else:
                    mayor = j
          
          mazo_nuevo.insert(pos,mayor)
          if mayor > i:
               mazo_nuevo.append(i)
          mazo.remove(mayor)
     return mazo_nuevo             
     
cartas = [1, 4, 6, 8]

ingresar_carta(cartas)