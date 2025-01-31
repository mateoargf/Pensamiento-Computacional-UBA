# 3. Repetir pero para la expresión que permite saber si un número es par y menor a 10

# recibe un parámetro y devuevle si es par y menor a 10
def validar_num(num):
     if num < 10 and num % 2 == 0:
          return(f'su número: {num} es par y menor a 10')
     elif num > 10 and num % 2 == 0:          
          return(f'su número: {num} es par y mayor a 10')
     elif num < 10 and num % 2 != 0:
          return(f'su número: {num} es impar y menor a 10')
     elif num > 10 and num % 2 != 0:
          return(f'su número: {num} es impar y mayor a 10')  
     
     return(f'su número: {num} es par e igual a 10') 

print('Ingrese un número par y menor a 10: ')

num = int(input('Ingrese su entero: '))

respuesta = validar_num(num)

print(respuesta)