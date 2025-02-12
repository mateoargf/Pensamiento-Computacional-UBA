# 13. Se tiene un ticket de supermercado que se puede representar como una lista de tuplas (producto,
# precio).
# a. Hacer una función que reciba la lista, calcule y devuelva el total que hay que pagar.
# b. Ahora se tienen dos tickets. Juntar ambos y volver a calcular el total.

# Un ejemplo de lista puede ser: [(“Detergente”, 123), (“Jabón Líquido”, 456)] y nos tendría que devolver 579. (No copien y peguen la lista de la guía, porque hay caracteres que no los va a reconocer el editor de texto).

# Recibe de parámetro la tupla productos, calcula y devuelve el total a pagar
def calcular_pago(lista1, lista2):
     total = 0
     lista = []
     lista.extend(lista1)
     lista.extend(lista2)
     for i in lista:
          total += i[1]

     return print(f'Su total a pagar es: {total}$')

productos_1 = [("Arroz", 250), ("Leche", 320), ("Pan", 180), ("Aceite", 850), ("Azúcar", 400), ("Fideos", 275), ("Sal", 150), ("Harina", 220), ("Cereal", 600), ("Yogur", 450)]

productos_2 = [("Shampoo", 750), ("Papel Higiénico", 900), ("Queso", 1200), ("Café", 1100), ("Galletas", 500), ("Jabón en Barra", 300), ("Mayonesa", 650), ("Tomate", 350), ("Cerveza", 1300), ("Pescado", 2500)]

calcular_pago(productos_1,productos_2)
