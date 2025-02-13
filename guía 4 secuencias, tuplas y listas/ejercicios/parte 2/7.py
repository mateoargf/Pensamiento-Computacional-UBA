# 7. Manuel y su pareja armaron una lista numerada con las actividades de mantenimiento de la casa.
# Decidieron dividirse las tareas, a Manuel le tocó hacer todas las actividades con número par, por eso necesitamos hacer una función que reciba una lista de enteros, y devuelva otra lista que solamente contenga números pares, que vienen a ser las tareas de Manuel.

# Recibe un parámetro e imprime los pares de la lista
def imprimir_par(lista):
     print('Lista de Manuel:')
     for i in lista:
          if i[0] % 2 == 0:
               print(i)
          else: 
               continue

lista_casa = [(1,'barrer'), (2, 'cocinar'), (3, 'fregar'), (4,'ordenar'), (5, 'guardar ropa'), (6, 'lavar ropa')]

imprimir_par(lista_casa)