# 5. Un profesor guarda las notas del primer parcial de sus alumnos en una lista de diccionarios que guarda
# la siguiente información:
# ● Nombre
# ● Apellido
# ● Intento
# ● Nota
# Donde ”intento” es la instancia que está rindiendo, 1 si es la primera vez que rinde el parcial, 2 si es el
# primer recuperatorio y 3 si es el segundo recuperatorio.
# Se pide hacer una función que, dado esta lista de diccionarios, devuelva el promedio de las notas en la
# primera oportunidad que rindieron los alumnos.
# ¿Cómo harían para generalizar la función y que el intento sea parametrizable? Es decir, que no
# solamente sirve para el intento 1, sino que también pueda servir para los demás.

def promedio(listado):
   cant_notas = 0
   total = 0
   for alumno in listado:
      if alumno['instancia'] == 1:
         cant_notas = cant_notas + 1
         total = total + alumno['nota']
   return total / cant_notas
   
         
         

notas = [
    {
       "nombre": "Mateo",
       "apellido": "Gomez",
       "instancia": 1,
       "nota": 10
       },
    {
       "nombre": "Mateo",
       "apellido": "Sujatovich",
       "instancia": 2,
       "nota": 8
       },
    {
       "nombre": "Mateo",
       "apellido": "Gonzalez",
       "instancia": 3,
       "nota": 9
       },
    {
       "nombre": "Ana",
       "apellido": "Lopez",
       "instancia": 1,
       "nota": 6
       },
    {
       "nombre": "Ana",
       "apellido": "Saenz",
       "instancia": 2,
       "nota": 7
       },
    {
       "nombre": "Ana",
       "apellido": "Beltran",
       "instancia": 3,
       "nota": 8
       },
    {
       "nombre": "Juan",
       "apellido": "Perez",
       "instancia": 1,
       "nota": 5
       },
    {
       "nombre": "Juan",
       "apellido": "Sasaki",
       "instancia": 2,
       "nota": 6
       },
    {
       "nombre": "Juan",
       "apellido": "Pedel",
       "instancia": 3,
       "nota": 7
       },
    {
       "nombre": "Sofia",
       "apellido": "Martinez",
       "instancia": 1,
       "nota": 9
       },
    {
       "nombre": "Sofia",
       "apellido": "De Elia",
       "instancia": 2,
       "nota": 8
       },
    {
       "nombre": "Sofia",
       "apellido": "Matarazzo",
       "instancia": 3,
       "nota": 10
       },
]

print(promedio(notas))
