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
# print('Ingrese 5 números enteros')
# total_num = 0
# veces = 1
# while veces <= 5:
#      num = int(input(f'Número: '))
#      if num % 3 == 0:
#           total_num += 1
#      veces += 1
# print(f'Vinieron: {total_num} múltiplos de 3')

# Imprime saludo por pantalla hasta que el ususario presione X
# print('Te mando un saludo hasta que me dejes')
# respuesta = 'S'
# while respuesta != 'X':
#      print('¡Hola!')
#      respuesta = input(f'¿Querés otro saludo? Ingresa X si la respuesta es no: ')
     
     
# Break
# numero = 10
# while numero <= 30:
#      if numero % 3 == 0:
#           print(f'El primer número múltiplo de 3 es: {numero}')
#           break
#      numero += 1
     
# Continue
# numero = 1
# while numero <= 10:
#      if numero % 2 == 0:
# # Si es par, suma 1 y saltar a la siguiente iteración
#           numero += 1
#           continue
#      print(numero)
#      numero += 1

# el código mal optimizado:
# numero = 0
# while numero < 3:
#      print(numero)
#      numero += 1
     
# if numero == 3:
#      print('número es tres')
# else:
#      print('número no es tres')

# Corrección del código:
# numero = 0
# while numero < 3 :
#      print(numero)
#      numero += 1
    
# print('número es tres')

# Rango:
# rango_1 = range(1,10) # valores: 1,2,3,4,5,6,7,8,9.
# rango_2 = range(6) #valores: 0,1,2,3,4,5
# rango_3 = range(0,8,2) #valores: 0,2,4,6
# rango_4 = range(15,10,-5) #valores: 15
# rango_5 = range(15,10,-1) #valores: 15,14,13,12,11

# Ciclo For:
# Contemos cuántos múltiplos de 3 ingresan en un lote de 5 números
# print('Ingrese 5 números enteros')
# total_num = 0
# for vuelta in range(5):
#      num = int(input('Número: '))
#      if num % 3 == 0:
#           total_num += 1
          
# print(f'Vinieron: {total_num} múltiplos de 3')

# Lista de números
# numeros = [11, 24, 32, 4, 15, 6, 17, 38, 94, 110]
# for numero in numeros: 
#      print(numero)

# Break
# Lista de números
# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Bucle for para encontrar el primer número divisible por 7 en la lista
# for numero in numeros:
#      if numero % 7 == 0:
#           print("El primer número divisible por 7 es:", numero)
#           break
#      print(numero)

# Continue
# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for numero in numeros:
     # Si es par, saltar a la siguiente iteración
#      if numero % 2 == 0 :
#           continue
#      print(numero)