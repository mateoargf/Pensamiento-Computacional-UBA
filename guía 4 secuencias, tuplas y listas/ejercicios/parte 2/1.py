# 1. Hacer una función que reciba un string y que imprima solamente los caracteres que sean vocales.

# Recibe de parámetro un string y devuelve las vocales
def imprimir_vocales(vocales):
     for i in vocales:
          if i.lower() in 'aáeéiíoóuú':
               print(" ".join(i))     

texto = "H0l4, ¿cóm0 estás? ¡Espero que bi3n! @#&%"

imprimir_vocales(texto)