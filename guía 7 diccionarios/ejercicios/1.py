# 1. En una escuela se quiere tener un sistema para guardar la información de sus estudiantes para tener
# mejor organizado sus datos.
# a. Crear un diccionario que sirve para representar a una persona en este contexto, pensar en las
# características que se consideren más relevantes para identificar a una persona (su nombre,
# DNI, edad, etc).
# b. Agregar al diccionario creado, un campo que sea otro diccionario y sirva para guardar el curso
# del estudiante y sus características (año, división, orientación, etc).
# c. Teniendo una lista de diccionarios de estudiantes, buscar en la lista la persona con mayor edad
# e imprimirla por pantalla.

def guardar_alumnos(listado, dni, edad, nombre_completo, curso, division, orientacion):
   datos_escolares = {
      "curso": curso,
      "división": division,
      "orientación": orientacion
   } 
   alumno_nuevo = {
      "identidad": dni,
      "edad": edad,
      "nombre": nombre_completo,
      "info académica": datos_escolares
   } 
   alumnos.append(alumno_nuevo)
   
def buscar_mayor(listado):
      mayor_edad = -1
      alumno_mayor = None
      
      for alumno in listado:
         if alumno['edad'] > mayor_edad:
            alumno_mayor = alumno
            mayor_edad = alumno['edad']
      print(f'El alumno de mayor edad es: {alumno_mayor}')      
      return alumno_mayor
            
   
   
alumnos = []
print(alumnos)
guardar_alumnos(alumnos, 5439920, 12, "josé carranza", 7, "c", "exactas")
guardar_alumnos(alumnos, 2343242, 11, "jorge lorenzo", 7, "c", "exactas")
guardar_alumnos(alumnos, 32425532, 17, "saul momo", 7, "c", "exactas")
guardar_alumnos(alumnos, 453232, 16, "josé carranza", 7, "c", "exactas")
guardar_alumnos(alumnos, 232355, 13, "josé carranza", 7, "c", "exactas")
print(alumnos)
buscar_mayor(alumnos)