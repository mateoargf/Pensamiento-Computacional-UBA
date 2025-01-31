# 4. Crear una función que dado un número, devuelva su valor absoluto. El valor absoluto de un número es
# el mismo número sin considerar el signo.

# Recibe un parámetro y devuelve su valor absoluto
def devolver_absoluto(num):
     if num >= 0:  
          return num 
     return -num
     

print('Debe ser un número entero')

valor = int(input('Ingrese su entero: '))

res = devolver_absoluto(valor)

print(f'el valor absoluto de {valor} es: {res}')