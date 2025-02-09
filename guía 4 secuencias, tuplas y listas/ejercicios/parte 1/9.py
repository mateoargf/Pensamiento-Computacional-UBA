# 9. Una librería tiene un sistema que guarda los nombres de todos los libros que tienen en una lista de la siguiente forma: [“El principito”, “It”, “Sherlock Holmes”...]. Se quiere saber cuántos libros repetidos tienen. Hacer código que imprima para cada título, cuántos ejemplares hay.
# Aclaración: No se sabe la cantidad de elementos que tiene la lista, la lista nombrada es solo un ejemplo.

# Recibe un parámetro y verifica e informa si se repiten libros y los imprima con nombre y cuantos son
def ver_stock(libreria):
     lista = []
     for i in libreria:
          contador = libreria.count(i)
          if contador == 1:
               lista.append(i)
               print(f'Nombre: {i} - Cantidad: {contador}')
          elif contador > 1:
               valido = True
               for j in lista:
                    if j == i:
                         valido = False
               if valido == True: 
                    lista. append(i)
                    print(f'Nombre: {i} - Cantidad: {contador}')
                         
                      
          
  
libros = ["Cien años de soledad", "Drácula", "Don Quijote de la Mancha", "Moby-Dick", "1984", "Orgullo y prejuicio", "Crimen y castigo", "El retrato de Dorian Gray", "Los miserables", "Fahrenheit 451", "Don Quijote de la Mancha", "Moby-Dick", "1984", "Moby-Dick", "1984", ]

ver_stock(libros)