# 3. Se representa un ticket de supermercado como una lista de diccionarios, donde cada diccionario tiene
# la siguiente información:
# ● Nombre del producto
# ● Precio por unidad
# ● Cantidad
# Se pide hacer una función que reciba el ticket y devuelva el monto total a pagar. 
def monto(listado):
   total_producto = 0
   monto = 0
   for producto in listado:
      total_producto = producto['valor'] * producto['cantidad']
      monto += round(total_producto, 2)
      
   print(monto)
def crear_ticket(listado, nombre_producto, precio_unidad, cantidad):
   producto = {
      'tipo': nombre_producto,
      'valor': precio_unidad,
      'cantidad': cantidad
   }
   listado.append(producto)
   

ticket = []

crear_ticket(ticket, 'jabón', 7.55, 2)
crear_ticket(ticket, 'shampoo', 12.7, 3)

monto(ticket)
