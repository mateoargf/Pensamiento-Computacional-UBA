# 5. Crear una función cuyos parámetros sean una lista y un índice de posición para mostrar el valor de la lista en esa ubicación.
# a. ¿Qué ocurre si ingreso un índice que se encuentra fuera del rango?
# b. Si el valor del índice ingresado se encuentra dentro del rango, mostrar el valor. En caso
# contrario, mostrar un mensaje apropiado para dicho error.
lista = [10, "rojo", 20, "verde", 30, "azul", 40, "amarillo", 50, "violeta"]

def mostrar_valor_lista(lista, indice):
   try:
      print(f'El valor en el índice: {indice} es: {lista[indice]}')
   except IndexError:
      print('El índice está fuera del rango de la lista.')
      
mostrar_valor_lista(lista, 3)  
mostrar_valor_lista(lista, 15) 
