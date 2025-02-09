# 9. Una librería tiene un sistema que guarda los nombres de todos los libros que tienen en una lista de la siguiente forma: [“El principito”, “It”, “Sherlock Holmes”...]. Se quiere saber cuántos libros repetidos tienen. Hacer código que imprima para cada título, cuántos ejemplares hay.
# Aclaración: No se sabe la cantidad de elementos que tiene la lista, la lista nombrada es solo un ejemplo.

# Recibe un parámetro y verifica e informa si se repiten libros y los imprima con nombre y cuantos son
def ver_stock(libreria):
     for i in libreria:
          cont = 0
          for j in libreria:
               if i == j:
                    cont +=1
          return cont

def validar_repetido(libreria):
     for i in libreria:
          if i != ver_stock(libreria):
               return True
          else:
               return False
          
          
          
libros = ["Cien años de soledad", "Drácula", "Don Quijote de la Mancha", "Moby-Dick", "1984", "Orgullo y prejuicio", "Crimen y castigo", "El retrato de Dorian Gray", "Los miserables", "Fahrenheit 451", "Don Quijote de la Mancha", "Moby-Dick", "1984", "Moby-Dick", "1984", ]

info = validar_repetido(libros)
