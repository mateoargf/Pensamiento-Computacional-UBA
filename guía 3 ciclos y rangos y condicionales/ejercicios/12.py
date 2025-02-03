# 12. Escribir código que recorra los números del 1 al 20 y determine para cada uno si es par o impar,
# imprimiendo un mensaje por pantalla en cada caso. Es decir, el output esperado sería:
# > El número 1 es impar.
# > El número 2 es par.
# …
# > El número 20 es par

# Recorre del 1 al 20 y retorna si es par o impar
def si_es_par():
     for i in range(1, 20 + 1):
          if(i % 2 == 0):
               paridad = 'par'
          else:     
               paridad = 'impar'
          print(f'El número {i} es {paridad}')
          
si_es_par()