# 2. Hacer una función que reciba un string y que lo invierta.

# Recibe de parámetro un string y devuelve las vocales pero al revés
def imprimir_vocales(vocales):
     for i in vocales[::-1]:
          if i.lower() in 'aáeéiíoóuú':
               print(" ".join(i))     


texto = "H0l4, ¿cóm0 estás? ¡Espero que bi3n! @#&%"

imprimir_vocales(texto)