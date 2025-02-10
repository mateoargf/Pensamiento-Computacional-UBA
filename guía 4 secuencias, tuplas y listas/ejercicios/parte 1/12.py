# 12. Se quiere hacer un sistema en la facultad para que un alumno pueda ir guardando las materias que va haciendo. Para eso, crear una función que le pregunte al usuario la materia que quiere almacenar, e ir guardando la información en una lista hasta que ingrese una ‘X’. ¿Qué funciones de listas no permiten insertar en una lista?

# Recibe un parámetro lista de materias y almacena las que cursa el usuario en una nueva lista
def elegir_materia(materias):
     lista = []
     for i in materias:
          valor = input(f'Ingrese "S"(si), "N"(no) y "X"(salir) si cursa {i}: ')
          if valor == 'S':
               lista.append(i)
          elif valor == 'N':
               print(f'no cursará: {i}')
          elif valor == 'X':
               print('Cortar proceso')
               return lista
          else:
               while (valor != 'S') and (valor != 'N') and (valor != 'X'):
                    valor = input(f'Ingrese "S"(si), "N"(no) y "X"(salir) si cursa {i}: ') 
                    if valor == 'S':
                         lista.append(i)
                    elif valor == 'N':
                         print(f'no cursará: {i}')
                    elif valor == 'X':
                         print('Cortar proceso')  
                         return lista
     return lista
         
lista_materias = ['matemática', 'álgebra', 'introducción a la programación', 'física', 'Sociedad y Estado']

materias_alumno = elegir_materia(lista_materias)

print(f'Usted cursa: {materias_alumno}')