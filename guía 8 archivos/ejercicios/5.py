# Se tiene un archivo csv que contiene información sobre el stock de una librería. Se guarda por cada
# línea, el nombre del producto, el código, el precio por unidad y el stock actual, es decir:
# nombre;código;precio;stock
# Un posible ejemplo de este archivo es el siguiente:
# Se pide:
# a. Leer el archivo y mostrarlo por pantalla con el siguiente formato:
# Nombre producto: lapiceras
# Código producto: 34512
# Precio por unidad: 50
# Stock: 120
# Nombre producto: cuadernos
# Código producto: 41611
# Precio por unidad: 500
# Stock: 130
# …
# b. Hacer una función que reciba un diccionario que describa una línea del archivo y lo
# agregue, es decir que si se recibe un diccionario del tipo:
# {
# “nombre”: “hojas A4”,
# “código”: 35662,
# “precio”: 600,
# “stock”: 45
# }

archivo = open('guía 8 archivos\\ejercicios\\libreria_stock.csv', 'r', encoding='utf-8')
lineas = archivo.readlines()
archivo.close()

for linea in lineas[1:]:
   nombre,codigo,precio,stock = linea.strip('\n').split(';')
   print(f'nombre producto: {nombre}')
   print(f'nombre código: {codigo}')
   print(f'precio producto: {precio}')
   print(f'stock producto: {stock}')
   print()
   
def agregar_producto(diccionario, archivo_csv='guía 8 archivos\\ejercicios\\libreria_stock.csv'):
   archivo = open(archivo_csv, 'a', encoding='utf-8')

   linea = f'{diccionario['nombre']};{diccionario['código']};{diccionario['precio']};{diccionario['stock']}\n'
   
   archivo.write(linea)
   
   archivo.close()
   
nuevo_producto = {
    "nombre": "hojas A4",
    "código": 35662,
    "precio": 600,
    "stock": 45
}

agregar_producto(nuevo_producto)
print('producto creado con éxito')