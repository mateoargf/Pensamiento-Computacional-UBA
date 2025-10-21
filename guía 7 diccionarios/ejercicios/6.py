# 6. En una fábrica, se hace un chequeo de calidad a los productos antes de cada entrega. El resultado del
# chequeo de la entrega se guarda en una lista de diccionarios, donde cada diccionario tiene la siguiente
# información de cada producto:
# ● Código del producto
# ● Fecha de vencimiento
# ● Si pasó el chequeo de calidad o no
# Se pide hacer una función que reciba esta lista de diccionarios y elimine todos los productos que no
# pasaron el chequeo de calidad. Devolver en una tupla el diccionario con los elementos eliminados y la
# cantidad de elementos que quedaron en el diccionario.
# Dado que la tupla es inmutable y nosotros no podemos ir agregando elementos a una tupla, ¿En qué
# momento deberíamos crear la tupla?

def renovar_lista(listado):
   for d in listado:
      if d['calidad'] == False:
         listado.remove(d)
         
   return tuple(listado)

productos = [
    {"codigo": "A001", "vencimiento": 2025, "calidad": True},
    {"codigo": "A002", "vencimiento": 2025, "calidad": False},
    {"codigo": "A003", "vencimiento": 2026, "calidad": True},
    {"codigo": "A004", "vencimiento": 2025, "calidad": False},
    {"codigo": "A005", "vencimiento": 2026, "calidad": True},
    {"codigo": "A006", "vencimiento": 2025, "calidad": False},
]

print(renovar_lista(productos))