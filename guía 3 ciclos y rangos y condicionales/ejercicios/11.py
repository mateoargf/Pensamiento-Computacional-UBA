# 11. En un almacén están buscando la forma de hacer los cobros más automáticamente. Para esto, se nos
# pide crear una función que reciba un número entero que representa lo que hay que cobrar, le pida al
# usuario ingresar un monto, y se vaya mostrando por pantalla cuánto falta para completar el pago.
# Repetir este proceso hasta que la deuda sea 0 o menor. Por ejemplo, si se recibe el monto 30:
# > El importe a pagar es de 30 pesos. Por favor, ingrese un monto.
# > 10
# > El importe a pagar es de 20 pesos. Por favor, ingrese un monto.
# > 15
# > El importe a pagar es de 5 pesos. Por favor, ingrese un monto.
# > 5

# Recibe un parámetro donde representa el cobro
def cobrar(total):
     while total > 0:
          print(f'El importe a pagar es de {total} pesos. Por favor, ingrese un monto')   
          monto = int(input('Su monto: '))
          total -= monto
     return '¡Operación exitosa!'

total = int(input('Ingrese el total a cobrar: '))

operacion = cobrar(total)          

print(operacion)