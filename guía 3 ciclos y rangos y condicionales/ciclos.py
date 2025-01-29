# print('Ingrese 5 números enteros ')
# total_mult = 0
# num = int(input('Número: '))
# if num % 3 == 0:
#      total_mult +=1
     
# num = int(input('Número: '))
# if num % 3 == 0:
#      total_mult +=1
     
# num = int(input('Número: '))
# if num % 3 == 0:
#      total_mult +=1
     
# num = int(input('Número: '))
# if num % 3 == 0:
#      total_mult +=1
     
# num = int(input('Número: '))
# if num % 3 == 0:
#      total_mult +=1
     
# print(f'Vinieron: {total_mult}, múltiplos de 3')

# Ciclo While:
# Contemos cuántos múltiplos de 3 ingresan en un lote de 5 números
print('Ingrese 5 números enteros')
total_num = 0
veces = 1
while veces <= 5:
     num = int(input(f'Número: '))
     if num % 3 == 0:
          total_num += 1
     veces += 1
print(f'Vinieron: {total_num} múltiplos de 3')

# Imprime saludo por pantalla hasta que el ususario presione X
print('Te mando un saludo hasta que me dejes')
respuesta = 'S'
while respuesta != 'X':
     print('¡Hola!')
     respuesta = input(f'¿Querés otro saludo? Ingresa X si la respuesta es no: ')
     