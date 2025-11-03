# 8. El kiosko de la facultad quiere automatizar un letrero que tome datos de un programa y le cobre al
# estudiante.
# Se tienen dos diccionarios, uno con un código y el producto, y otro con el código y el precio de cada
# producto.

opciones = {
   1: "hamburguesas",
   2: "milanesas",
   3: "gaseosa",
   4: "alfajor",
   5: "papas fritas",
   6: "agua"
}
valores = {
   1:1000,
   2:1500,
   3:500,
   4:300,
   5:600,
   6:350
}

def leer_menu(dicc_opcion, dicc_valor):
   print('Menú:')
   for i in dicc_opcion:
      print(f'{i}: {dicc_opcion[i]} -> ${dicc_valor[i]}')
  
def crear_ticket(dicc_opcion, dicc_valor):
   leer_menu(dicc_opcion, dicc_valor)
      
   while True:
      try:
         opcion = int(input('Elija la opción (número): '))
         if opcion not in dicc_opcion:
            print('No se encuentra en el menú.')
            continue
         break
      except ValueError:
         print('Debe ingresar un número entero.')
   
   
   while True:
      try:
         cantidad = int(input('Elija la cantidad: '))
         if cantidad <= 0:
            print('La cantidad debe ser mayor a 0')
            continue
         break
      except ValueError, IndexError:
           print('Debe ingresar un número entero.')
           
   valor_total = dicc_valor[opcion] * cantidad
   print(f'Quiere {cantidad} de {dicc_opcion[opcion]}. Total a pagar: ${valor_total}')
             
crear_ticket(opciones, valores)
