# Una profesora tiene una lista de diccionarios para guardar las notas que sacaron sus alumnos en el
# último parcial que tomó. Cada uno de esos diccionarios tiene el nombre del alumno, su apellido, su dni
# y la nota que sacó.
# a. Hacer una función que reciba este diccionario, y guarde las notas en un archivo csv, llamados
# notas.csv
# b. Tiempo después de guardar las notas, la profesora quiso saber la cantidad de alumnos que
# aprobaron. Hacer una función que lea el archivo creado en el ejercicio anterior, y devolver la
# cantidad de alumnos aprobados (su nota es mayor a 4).

notas_alumnos = [
   {'nombre': 'Mateo', 'apellido': 'Gomez', 'dni': '12345678', 'nota': 8.5},
   {'nombre': 'Lucia', 'apellido': 'Perez', 'dni': '23456789', 'nota': 9.0},
   {'nombre': 'Javier', 'apellido': 'Ramirez', 'dni': '34567890', 'nota': 7.5},
   {'nombre': 'Sofia', 'apellido': 'Lopez', 'dni': '45678901', 'nota': 10},
   {'nombre': 'Martin', 'apellido': 'Fernandez', 'dni': '56789012', 'nota': 6.5},
   {'nombre': 'Juana', 'apellido': 'Gonzalez', 'dni': '67890123', 'nota': 3.5}
]

def guardar_notas(lista_alumnos, notas_csv='guía 8 archivos\\ejercicios\\notas.csv'):
   archivo = open(notas_csv,'a', encoding='utf')

   for alumno in lista_alumnos:
      linea = f'{alumno['nombre']};{alumno['apellido']};{alumno['dni']};{alumno['nota']}\n'
      archivo.write(linea)
   
   archivo.close()
   
def calcular_aprobados(notas_csv='guía 8 archivos\\ejercicios\\notas.csv'):
   cont = 0
   archivo = open(notas_csv, encoding='utf-8')
   for linea in archivo:
      campos = linea.strip('\n').split(';')
      nota = float(campos[3])
      if nota > 4:
         cont +=1
   archivo.close()
   print(f'El total de alumnos aprobados es: {cont}')
   return cont

guardar_notas(notas_alumnos)

calcular_aprobados()