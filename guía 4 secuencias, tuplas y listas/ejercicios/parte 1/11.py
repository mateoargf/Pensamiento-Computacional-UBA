# 11. Se tiene la siguiente lista de palabras: [“entender”, “pueden”, “humanos”, “los”, “que”, “código”,
# “escriben”, ”programadores”, “buenos”, “Los”, “entiende.”, “computadora”, “una”, “que”, “código”,
# “escribe”, “tonto”, “Cualquier”]. Hacer una función que reciba una lista, y devuelva un string uniendo
# las palabras desde el final de la lista hasta el principio con un “ ” (espacio) entre cada una, para formar la frase. (ver funciones de listas y strings).

# Recibe un parámetro y devuelve la lista con espacio entre elementos
def unir_oracion(lista):
     lista.reverse()
     oracion = ""
     for n in lista:
          oracion += n + " "
     return oracion

palabras = ['entender', 'pueden', 'humanos', 'los', 'que', 'código', 'escriben', 'programadores', 'buenos', 'Los', 'entiende.', 'computadora', 'una', 'que', 'código', 'escribe', 'tonto', 'Cualquier']

frase = unir_oracion(palabras)

print(frase)