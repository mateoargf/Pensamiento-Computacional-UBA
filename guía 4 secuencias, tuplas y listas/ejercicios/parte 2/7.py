# 7. Manuel y su pareja armaron una lista numerada con las actividades de mantenimiento de la casa.
# Decidieron dividirse las tareas, a Manuel le tocó hacer todas las actividades con número par, por eso necesitamos hacer una función que reciba una lista de enteros, y devuelva otra lista que solamente contenga números pares, que vienen a ser las tareas de Manuel.

# Recibe un parámetro e imprime los pares de la lista
def filtrar_por_pares_a(lista):
     print('Lista de Manuel:')
     lista_par = []
     
     for n in lista:
          if es_par_a(n[0]) and not(n in lista_par):
               lista_par.append(n)
          else: 
               continue
     return lista_par

def filtrar_por_pares_b(lista):
     lista_par = list(filter(es_par_b,lista))
     return lista_par

def es_par_a(num):
     if num % 2 == 0: return True
     else: return False

def es_par_b(num):
     if num[0] % 2 == 0:              
          return True  
     else: return False   

lista_deberes = [(1,'barrer'), (2, 'cocinar'), (3, 'fregar'), (4,'ordenar'), (5, 'guardar ropa'), (6, 'lavar ropa'), (1,'barrer'), (2, 'cocinar')]

lista_pares = filtrar_por_pares_b(lista_deberes)

print(lista_pares)